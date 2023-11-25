#%%

import psycopg2
import pandas as pd
import numpy as np
from data_utils  import DatabaseConnector 
from data_extraction import DataExtractor 
from data_cleaning   import DataCleaning

#%%

def upload_dim_users():
    '''Extracts and uploads cleaned 'legacy_users' data to 'dim_users' table in the database:
        - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
        - Initialises the database engine using credentials from 'db_creds.yaml'
        - Reads 'legacy_users' data into pandas dataframe
        - Cleans user data
        - Uploads cleaned user data to 'dim_users' table in the local database
    Function contains lines of code which can be used for checking and tracking changes are hashed out '''
    
    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    engine = db.init_db_engine('db_creds.yaml')
    # db_tables = db.list_db_tables(engine)
    # print(db_tables)
    user_table = de.read_rds_table(engine, 'legacy_users')
    # user_table.info()
    cleaned_users = user_table
    dc.clean_user_data(cleaned_users)
    # cleaned_users.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_users, 'dim_users', engine)

def upload_dim_card_details():
    ''' Extracts and uploads cleaned card details data to 'dim_card_details' table in the database:
        - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
        - Retrieves card details data from 'card_details.pdf' and stores as pandas dataframe
        - Cleans card details data
        - Uploads cleaned card details to 'dim_card_details' table in the local database
    Function contains lines of code which can be used for checking and tracking changes are hashed out'''
    
    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    card_details_table = de.retrieve_pdf_data('card_details.pdf')
    # card_details_table.info()
    cleaned_card_details = card_details_table
    dc.clean_card_data(cleaned_card_details)
    # cleaned_card_details.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_card_details, 'dim_card_details', engine)

def upload_dim_store_details():
    ''' Extracts and uploads cleaned store details data to 'dim_store_details' table in the database:
        - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
        - Reads API key from 'api_key.yaml'
        - Retrieves store details data using the API key and stores as pandas dataframe
        - Cleans store details data
        - Uploads cleaned store details to 'dim_store_details' table in the local database
    Function contains lines of code which can be used for checking and tracking changes are hashed out'''

    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    api_key = de.read_api_key('api_key.yaml')
    store_details_table = de.retrieve_stores_data(api_key)
    # store_details_table.info()
    cleaned_store_details = store_details_table
    dc.clean_store_data(cleaned_store_details)
    # cleaned_store_details.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_store_details, 'dim_store_details', engine)

def upload_dim_products():
    ''' Extracts and uploads cleaned product data to 'dim_products' table in the database:
        - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
        - Extracts product data from an S3 source and stores as pandas dataframe
        - Cleans product data
        - Uploads cleaned product data to 'dim_products' table in the local database
    Function contains lines of code which can be used for checking and tracking changes are hashed out'''
    
    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    products_data = de.extract_from_s3()
    # products_data.info()
    cleaned_products_table = products_data
    dc.clean_products_data(cleaned_products_table)
    # cleaned_products_table.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_products_table, 'dim_products', engine)

def upload_orders_table():
    '''Extracts and uploads cleaned 'orders_table' data to 'orders_table' table in the database:
            - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
            - Initialises the database engine using credentials from 'db_creds.yaml'
            - Reads 'orders_table' data into pandas dataframe
            - Cleans orders data
            - Uploads cleaned orders data to 'orders_table' table in the local database
        Function contains lines of code which can be used for checking and tracking changes are hashed out '''

    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    engine = db.init_db_engine('db_creds.yaml')
    # db_tables = db.list_db_tables(engine)
    # print(db_tables)
    orders_data = de.read_rds_table(engine, 'orders_table')
    # orders_data.info()
    cleaned_orders_table = orders_data
    dc.clean_orders_data(cleaned_orders_table)
    # cleaned_orders_table.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_orders_table, 'orders_table', engine)

def upload_dim_date_times():
    ''' Extracts and uploads cleaned date-time data to 'dim_date_times' table in the database:
        - Initialises DatabaseConnector, DataExtractor, and DataCleaning class instances
        - Extracts date-time data from an S3 source via URL and stores as pandas dataframe
        - Cleans date_time data
        - Uploads cleaned date-time data to 'dim_date_times' table in the local database
    Function contains lines of code which can be used for checking and tracking changes are hashed out'''

    db = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()
    
    url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
    date_times_data = de.extract_from_s3_via_url(url)
    # date_times_data.info()
    cleaned_date_times_table = date_times_data
    dc.clean_date_times_data(cleaned_date_times_table)
    # cleaned_date_times_table.info()

    engine = db.init_db_engine('local_db_creds.yaml')
    db.upload_to_db(cleaned_date_times_table, 'dim_date_times', engine)

#%%
