# -*- coding: utf-8 -*-
import os
from app import create_app
from app.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Render asigna el puerto a través de la variable de entorno PORT
    port = int(os.environ.get('PORT', 5000))
    
    # ¡Importante! Escuchar en 0.0.0.0, no en 127.0.0.1
    app.run(host='0.0.0.0', port=port, debug=False)
