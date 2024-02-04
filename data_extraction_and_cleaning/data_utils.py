#%%

import psycopg2
import pandas as pd
import yaml
import sqlalchemy
from sqlalchemy import create_engine, inspect

#%%

class DatabaseConnector():
    '''Used to connect with and upload data to the database.'''

    def __init__(self):
        '''Initialises DatabaseConnector class '''
        pass
        
    def read_db_creds(self, file_name):
        ''' Reads database credentials from a YAML file.
        Args: file_name (str): Name of the YAML file containing credentials
        Returns: credentials (dict): Dictionary containing database credentials '''

        with open(file_name, 'r') as file:
                credentials = yaml.safe_load(file)
                return credentials
    
    def init_db_engine(self, file_name):
        ''' Initialises the database engine for establishing a connection.
        Args: file_name (str): Name of the YAML file containing credentials
        Returns: engine (sqlalchemy.engine.Engine): SQLAlchemy database engine '''

        credentials = self.read_db_creds(file_name)
        db_username = credentials.get('RDS_USER')
        db_password = credentials.get('RDS_PASSWORD')
        db_host = credentials.get('RDS_HOST')
        db_port = credentials.get('RDS_PORT')
        db_name = credentials.get('RDS_DATABASE')
        
        db_url = f"{'postgresql'}+{'psycopg2'}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(db_url)
        return engine

    def list_db_tables(self, engine):
        '''' Retrieves a list of tables in the database.
        Args: engine (sqlalchemy.engine.Engine): SQLAlchemy database engine
        Returns: table_names (list): List of table names in the database '''

        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names
    
    def upload_to_db(self, df, table_name, engine):
        ''' Uploads a DataFrame to the specified table in the database.
        Args:
        - df (pandas.DataFrame): DataFrame to upload
        - table_name (str): Name of the table in the database
        - engine (sqlalchemy.engine.Engine): SQLAlchemy database engine '''

        df.to_sql(table_name, engine, if_exists='replace')

#%%

if __name__ == '__main__':
    '''Main execution block for initialising the DatabaseConnector, connecting to the database, and listing the tables '''

    db = DatabaseConnector()
    engine = db.init_db_engine("db_creds.yaml")
    db_tables = db.list_db_tables(engine)
    print(db_tables)

#%%
