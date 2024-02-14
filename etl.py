import pandas as pd
import sqlite3

def extract(file_path):
    return pd.read_csv(file_path)

def transform(dataframe):
    dataframe = dataframe.strip().lower()
    return dataframe

def load(dataframe, database_path):
    conn = sqlite3.connect(database_path)
    dataframe.to_sql('table_name', conn, if_exists='append', index=False)
    conn.close()
