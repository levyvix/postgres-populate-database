import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Get the values from environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Create the database connection URL
db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the engine
engine = create_engine(db_url)


def load_data(engine=engine, csv_files=[]):

    for csv_file in csv_files:
        table_name = os.path.basename(csv_file).split(".")[0].split("PdM_")[1]
        pd.read_csv(csv_file).to_sql(table_name, engine, schema="kaggle", if_exists="replace", index=False)


if __name__ == "__main__":
    db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(db_url)

    csv_files = [
        os.path.join(
            "C:", os.sep, "Users", "levyv", "Desktop", "Banco de Dados I - Pasta Geral", "dados", "PdM_machines.csv"
        ),
        os.path.join(
            "C:", os.sep, "Users", "levyv", "Desktop", "Banco de Dados I - Pasta Geral", "dados", "PdM_maint.csv"
        ),
        os.path.join(
            "C:", os.sep, "Users", "levyv", "Desktop", "Banco de Dados I - Pasta Geral", "dados", "PdM_telemetry.csv"
        ),
        os.path.join(
            "C:", os.sep, "Users", "levyv", "Desktop", "Banco de Dados I - Pasta Geral", "dados", "PdM_errors.csv"
        ),
        os.path.join(
            "C:", os.sep, "Users", "levyv", "Desktop", "Banco de Dados I - Pasta Geral", "dados", "PdM_failures.csv"
        ),
    ]

    load_data(engine, csv_files)
