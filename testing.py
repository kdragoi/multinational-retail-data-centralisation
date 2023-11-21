import psycopg2
import pandas as pd
import numpy as np
from data_utils  import DatabaseConnector 
from data_extraction import DataExtractor 
from data_cleaning   import DataCleaning

# Things to use while cleaning to make sure not deleting important data
# .unique()
# products_data['category'].unique()
# df.isna().sum()
# print(products_data.columns.tolist())

# cleaned_orders_table.to_csv('orders.txt')
