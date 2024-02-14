import pytest
import pandas as pd
import sqlite3
import os
from etl import extract, transform, load

@pytest.fixture
def setup_database():
    # Setup database and table for testing
    database_path = "test_database.db"
    conn = sqlite3.connect(database_path)
    yield database_path  # Use the database for testing
    conn.close()
    os.remove(database_path)  # Cleanup

def test_extract():
    # Test data extraction logic
    data = extract("path/to/test.csv")
    assert not data.empty

def test_transform():
    # Test data transformation logic
    data = pd.DataFrame({'column': [' Test ']})
    transformed_data = transform(data['column'])
    assert transformed_data.iloc[0] == 'test'

def test_load(setup_database):
    # Test data loading logic
    data = pd.DataFrame({'column': ['test']})
    load(data, setup_database)
    conn = sqlite3.connect(setup_database)
    loaded_data = pd.read_sql('SELECT * FROM table_name', conn)
    assert not loaded_data.empty
