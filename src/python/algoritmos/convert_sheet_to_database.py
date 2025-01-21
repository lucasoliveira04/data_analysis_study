import pandas as pd
from sqlalchemy import create_engine

def convert_sheet_to_database(sheet_path: str, db_url: str, table_name: str):
    sheet = pd.read_excel(sheet_path)
    engine = create_engine(db_url)
    with engine.connect() as connection:
        sheet.to_sql(table_name, con=connection, if_exists='replace', index=False)
        print(f"Dados importados com sucesso para a tabela '{table_name}' no PostgreSQL!")

sheet_path = './clientes_compras.xlsx'
db_url = 'postgresql://postgres:senha12345@localhost:5432/xlsxWithSql'
table_name = 'clientes'

convert_sheet_to_database(sheet_path, db_url, table_name)