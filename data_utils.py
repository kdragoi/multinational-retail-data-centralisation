#%%

import psycopg2
import pandas as pd
import yaml
import sqlalchemy
from sqlalchemy import create_engine, inspect

#%%

class DatabaseConnector():
    '''use to connect with and upload data to the database.'''
    def __init__(self):
         pass
        
    def read_db_creds(self, file_name):      
        with open(file_name, 'r') as file:
                credentials = yaml.safe_load(file)
                return credentials
    
    def init_db_engine(self, file_name):
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
         '''gets list of tables'''
         inspector = inspect(engine)
         table_names = inspector.get_table_names()
         return table_names
    
    def upload_to_db(self, df, table_name, engine):
        df.to_sql(table_name, engine, if_exists='replace')

#%%

if __name__ == '__main__':
    db = DatabaseConnector()
    engine = db.init_db_engine("db_creds.yaml")
    # Create the database engine
    db_tables = db.list_db_tables(engine)
    print(db_tables)
    # table_df = pd.read_sql_table('legacy_users', con=engine)
    # table_df.info()
    # table_df.head()

#%%
