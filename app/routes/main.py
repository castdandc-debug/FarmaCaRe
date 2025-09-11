from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models.usuario import Usuario
from app.extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'Administrador':
        return render_template('dashboard_admin.html')
    elif current_user.rol == 'Caja':
        return render_template('dashboard_caja.html')
    else:
        return redirect(url_for('auth.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('perfil.html', user=current_user)

@main.route('/editar_perfil', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    if current_user.rol != 'Administrador':
        flash('No tienes permiso para acceder aquí.')
        return redirect(url_for('main.profile'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        rol = request.form.get('rol')
        activo = bool(request.form.get('activo'))
        nueva_contrasena = request.form.get('nueva_contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        if not nombre or not rol:
            flash('Todos los campos son obligatorios.')
            return redirect(url_for('main.editar_perfil'))

        existente = Usuario.query.filter_by(nombre=nombre).first()
        if existente and existente.id != current_user.id:
            flash('El nombre ya está en uso por otro usuario.')
            return redirect(url_for('main.editar_perfil'))

        current_user.nombre = nombre
        current_user.rol = rol
        current_user.activo = activo

        # Cambia la contraseña solo si se llena el campo
        if nueva_contrasena or confirmar_contrasena:
            if nueva_contrasena != confirmar_contrasena:
                flash('Las contraseñas no coinciden.')
                return redirect(url_for('main.editar_perfil'))
            if nueva_contrasena:
                current_user.set_password(nueva_contrasena)

        db.session.commit()
        flash('Perfil actualizado correctamente.')
        return redirect(url_for('main.profile'))

    return render_template('editar_perfil.html', user=current_user)

@main.route('/editar_usuario', methods=['GET', 'POST'])
@login_required
def editar_usuario():
    if current_user.rol != 'Caja':
        flash('No tienes permiso para acceder aquí.')
        return redirect(url_for('main.profile'))

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        if not nombre:
            flash('El nombre de usuario es obligatorio.')
            return redirect(url_for('main.editar_usuario'))

        existente = Usuario.query.filter_by(nombre=nombre).first()
        if existente and existente.id != current_user.id:
            flash('El nombre ya está en uso por otro usuario.')
            return redirect(url_for('main.editar_usuario'))

        current_user.nombre = nombre
        db.session.commit()
        flash('Nombre actualizado correctamente.')
        return redirect(url_for('main.profile'))

    return render_template('editar_usuario.html', user=current_user)

@main.route('/cambiar_contrasena', methods=['GET', 'POST'])
@login_required
def cambiar_contrasena():
    if request.method == 'POST':
        nueva_contrasena = request.form.get('nueva_contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        if not nueva_contrasena or not confirmar_contrasena:
            flash('Debes completar ambos campos.')
            return redirect(url_for('main.cambiar_contrasena'))

        if nueva_contrasena != confirmar_contrasena:
            flash('Las contraseñas no coinciden.')
            return redirect(url_for('main.cambiar_contrasena'))

        current_user.set_password(nueva_contrasena)
        db.session.commit()
        flash('Contraseña cambiada correctamente.')
        return redirect(url_for('main.profile'))

    return render_template('cambiar_contrasena.html', user=current_user)
