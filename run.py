# run.py
# ... resto del código ...

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Crear usuario admin si no existe
        from app.models import Usuario
        if not Usuario.query.filter_by(nombre='admin').first():
            admin = Usuario(nombre='admin', rol='Administrador')
            admin.set_password('123456')
            db.session.add(admin)
            db.session.commit()
            print("✅ Usuario admin creado al iniciar.")
        else:
            print("👤 Usuario admin ya existe.")
    
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
