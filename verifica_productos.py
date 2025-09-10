from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://nueva_farmacare_db_user:8Z4GpAj7Hs0mpR8K1zMKM2hB9915F411@dpg-d2oisaogjchc73eq94cg-a.oregon-postgres.render.com/nueva_farmacare_db?sslmode=require"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT tipo, nombre, precio, codigo_barras, nombre_comercial, nombre_generico, nombre_comun, laboratorio, presentacion, grupo, stock
        FROM productos
        LIMIT 50;
    """))
    for row in result.mappings():
        print(row)
