# etl_pipeline.py

import pandas as pd
import yaml
from sqlalchemy import create_engine

# --- Extracción de Datos ---
def extract_data(source_type, source_path):
    """
    Extrae datos desde diferentes fuentes como CSV o una base de datos.
    """
    if source_type == "csv":
        data = pd.read_csv(source_path)
    elif source_type == "postgres":
        # Conectar a una base de datos PostgreSQL
        data = pd.read_sql("SELECT * FROM tabla", con=source_path)
    elif source_type == "mysql":
        # Conectar a una base de datos MySQL
        data = pd.read_sql("SELECT * FROM tabla", con=source_path)
    else:
        raise ValueError("Fuente de datos no soportada")
    return data

# --- Transformación de Datos ---
def transform_data(data):
    """
    Aplica transformaciones en los datos para limpieza y formateo.
    """
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    # Otros procesos de transformación según necesidad
    return data

# --- Carga de Datos ---
def load_data(data, target_type, target_config):
    """
    Carga los datos a una base de datos o un archivo.
    """
    if target_type == "postgres":
        engine = create_engine(f"postgresql://{target_config['user']}:{target_config['password']}@{target_config['host']}:{target_config['port']}/{target_config['dbname']}")
        data.to_sql("tabla_destino", con=engine, if_exists="replace", index=False)
    elif target_type == "mysql":
        engine = create_engine(f"mysql+pymysql://{target_config['user']}:{target_config['password']}@{target_config['host']}:{target_config['port']}/{target_config['dbname']}")
        data.to_sql("tabla_destino", con=engine, if_exists="replace", index=False)
    else:
        raise ValueError("Destino no soportado")

# --- Ejecución del Pipeline ETL ---
if __name__ == "__main__":
    # Leer configuración de conexión
    with open("config/db_config.yaml", 'r') as file:
        db_config = yaml.safe_load(file)

    # 1. Extracción
    data = extract_data("csv", "data/sample_data.csv")

    # 2. Transformación
    data = transform_data(data)

    # 3. Carga
    load_data(data, "postgres", db_config["postgres"])