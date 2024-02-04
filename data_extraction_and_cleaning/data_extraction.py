#%%

import pandas as pd
import tabula
import yaml
import requests
from data_utils import DatabaseConnector
import boto3


#%%

class DataExtractor():
    ''' Used as a utility for extracting data from various sources such as CSV files, an API, and an S3 bucket '''
    
    def __init__(self):
        ''' Initialises the DataExtractor class '''
        pass

    def read_rds_table(self, engine, table_name):
        ''' Reads data from a table in an RDS database.

        Args:
        - engine: SQLAlchemy database engine
        - table_name (str): Name of the table to read from

        Returns:
        - table_df (pandas.DataFrame): DataFrame containing data from the specified table '''

        table_df = pd.read_sql_table(table_name, con=engine, index_col=['index'])
        return table_df
    
    def retrieve_pdf_data(self, file_name):
        ''' Retrieves data from a PDF file.

        Args:
        - file_name (str): Name of the PDF file

        Returns:
        - df (pandas.DataFrame): DataFrame containing data from the PDF '''

        df = pd.concat(tabula.read_pdf(file_name, pages='all'))
        df.reset_index(drop=True, inplace=True)
        return df
    
    def read_api_key(self, file_path):
        ''' Reads an API key from a file.

        Args:
        - file_path (str): Path to the file containing the API key

        Returns:
        - api_key (str): API key extracted from the file '''

        with open(file_path, 'r') as file:
            api_key = yaml.safe_load(file)
        return api_key['api_key']
    
    def list_number_of_stores(self, api_key):
        ''' Retrieves the number of stores using an API endpoint.

        Args:
        - api_key (dict): API key to access the endpoint

        Returns:
        - number_of_stores (int): Number of stores obtained from the API response '''

        # take endpoint out to pass as argument to make better
        number_of_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        response = requests.get(number_of_stores_endpoint, headers=api_key)
        number_of_stores = response.json()['number_stores']
        return number_of_stores
    
    def retrieve_stores_data(self, api_key):
        ''' Retrieves store data using an API.

        Args:
        - api_key (dict): API key to access the API

        Returns:
        - store_data (pandas.DataFrame): DataFrame containing store details '''

        # take endpoint out to pass as argument to make better
        store_data_list = []
        number_of_stores = self.list_number_of_stores(api_key)

        for store_number in range(number_of_stores):
            retrieve_store_data_endpoint = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
            response = requests.get(retrieve_store_data_endpoint, headers=api_key)
            response_data = pd.json_normalize(response.json())
            store_data_list.append(response_data)

        store_data = pd.concat(store_data_list)
        return store_data
    
    def extract_from_s3(self):
        ''' Extracts data from an S3 bucket.

        Returns:
        - df (pandas.DataFrame): DataFrame containing data from the S3 bucket '''

        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        df = pd.read_csv(response.get("Body"), index_col='Unnamed: 0')
        return df
    
    def extract_from_s3_via_url(self, url):
        ''' Extracts data from an S3 bucket using a URL.

        Args:
        - url (str): URL to access the S3 bucket data

        Returns:
        - df (pandas.DataFrame): DataFrame containing data retrieved from the S3 bucket via URL '''

        response = requests.get(url)
        table_dic = response.json()
        df = pd.DataFrame(table_dic)
        return df


#%%

if __name__ == '__main__':
    '''Main block for extracting various data sources and obtaining DataFrames.
    Contains lines of code which can be used for tracking successful extraction are hashed out '''

    db = DatabaseConnector()
    de = DataExtractor()

    engine = db.init_db_engine("db_creds.yaml")
    users_table = de.read_rds_table(engine, 'legacy_users')
    # users_table.info()

    card_details_table = de.retrieve_pdf_data("card_details.pdf")
    # card_details_table.info()

    api_key = de.read_api_key("api_key.yaml")
    store_details_table = de.retrieve_stores_data(api_key)
    # store_details_table.info()
    
    products_table = de.extract_from_s3()
    # products_table.info()

    orders_table = de.read_rds_table(engine, 'orders_table')
    # orders_table.info()

    url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
    date_times_table = de.extract_from_s3_via_url(url)
    # date_times_table.info()



