import psycopg2
import toml
from urllib.parse import urlparse

conStr = "localhost://username:password@data_quality:5432"
p = urlparse(conStr)

with open('database_functions\config.toml') as f:
    config = toml.load(f)
    pg_connection_dict = {
    'dbname' : config['postgresql']['database'],
    'user' : config['postgresql']['username'],
    'password' : config['postgresql']['password'],
    'host' : config['postgresql']['host'],
    'port' : config['postgresql']['port']}


def connect_db():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        print("Connecting to the PostgreSQL database...")
        print("Connection string: ", pg_connection_dict)
        conn = psycopg2.connect(**pg_connection_dict)
        return conn
    except:
        print("Unable to connect to the database")
