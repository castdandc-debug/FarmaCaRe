# -*- coding: utf-8 -*-
import os
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tablas creadas exitosamente.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
