import pandas as pd
import yaml
from sqlalchemy import create_engine

# --- Data Extraction ---
def extract_data(source_type, source_path):
    """
    Extracts data from different sources such as CSV or a database.
    """
    if source_type == "csv":
        data = pd.read_csv(source_path)
    elif source_type == "postgres":
        # Connect to a PostgreSQL database
        data = pd.read_sql("SELECT * FROM table_name", con=source_path)
    elif source_type == "mysql":
        # Connect to a MySQL database
        data = pd.read_sql("SELECT * FROM table_name", con=source_path)
    else:
        raise ValueError("Unsupported data source")
    return data

# --- Data Transformation ---
def transform_data(data):
    """
    Applies data transformations for cleaning and formatting.
    """
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    # Other transformation processes as needed
    return data

# --- Data Loading ---
def load_data(data, target_type, target_config):
    """
    Loads data to a database or a file.
    """
    if target_type == "postgres":
        engine = create_engine(f"postgresql://{target_config['user']}:{target_config['password']}@{target_config['host']}:{target_config['port']}/{target_config['dbname']}")
        data.to_sql("target_table", con=engine, if_exists="replace", index=False)
    elif target_type == "mysql":
        engine = create_engine(f"mysql+pymysql://{target_config['user']}:{target_config['password']}@{target_config['host']}:{target_config['port']}/{target_config['dbname']}")
        data.to_sql("target_table", con=engine, if_exists="replace", index=False)
    else:
        raise ValueError("Unsupported target")

# --- ETL Pipeline Execution ---
if __name__ == "__main__":
    # Read connection configuration
    with open("config/db_config.yaml", 'r') as file:
        db_config = yaml.safe_load(file)

    # 1. Extraction
    data = extract_data("csv", "data/sample_data.csv")

    # 2. Transformation
    data = transform_data(data)

    # 3. Loading
    load_data(data, "postgres", db_config["postgres"])
