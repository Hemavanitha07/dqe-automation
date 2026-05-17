import psycopg2
import pandas as pd


class PostgresConnectorContextManager:

    def __init__(self, db_user, db_password, db_host, db_name, db_port):
        self.connection = None
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
        self.db_port = db_port

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            port=self.db_port
        )
        return self

    def get_data_sql(self, query):
        return pd.read_sql(query, self.connection)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


