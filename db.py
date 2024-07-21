# db.py
import pyodbc
from config import DATABASE_CONFIG

def get_db_connection():
    connection_string = f"DRIVER={DATABASE_CONFIG['driver']};SERVER={DATABASE_CONFIG['server']};DATABASE={DATABASE_CONFIG['database']};Trusted_Connection={DATABASE_CONFIG['trusted_connection']}"
    conn = pyodbc.connect(connection_string)
    return conn
