#%%

import pandas as pd
import tabula
import yaml
import requests
from data_utils import DatabaseConnector
import boto3


#%%

class DataExtractor():
    '''This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.
    '''
    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):
        table_df = pd.read_sql_table(table_name, con=engine, index_col=['index'])
        return table_df
    
    def retrieve_pdf_data(self, file_name):
        df = pd.concat(tabula.read_pdf(file_name, pages='all'))
        df.reset_index(drop=True, inplace=True)
        return df
    
    def read_api_key(self, file_path):
        with open(file_path, 'r') as file:
            api_key = yaml.safe_load(file)
        return api_key['api_key']
    
    def list_number_of_stores(self, api_key):
        # take endpoint out to pass as argument to make better
        number_of_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        response = requests.get(number_of_stores_endpoint, headers=api_key)
        number_of_stores = response.json()['number_stores']
        return number_of_stores
    
    def retrieve_stores_data(self, api_key):
        store_data_list = []
        number_of_stores = self.list_number_of_stores(api_key)
    
        # take endpoint out to pass as argument to make better

        for store_number in range(number_of_stores):
            retrieve_store_data_endpoint = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
            response = requests.get(retrieve_store_data_endpoint, headers=api_key)
            response_data = pd.json_normalize(response.json())
            store_data_list.append(response_data)

        store_data = pd.concat(store_data_list)
        return store_data
    
    def extract_from_s3(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        df = pd.read_csv(response.get("Body"), index_col='Unnamed: 0')
        return df
    
    def extract_from_s3_via_url(self, url):
        response = requests.get(url)
        table_dic = response.json()
        df = pd.DataFrame(table_dic)
        return df


#%%

