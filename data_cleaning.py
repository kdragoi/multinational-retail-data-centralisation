#%%

import pandas as pd
import numpy as np


#%%

class DataCleaning():
    '''to clean data from each of the data sources.'''
    def __init__(self):
        pass

    def valid_name(self, df, column_name):
        regex_expression = r'^[a-zA-Z\s-]+$'
        # regex expression for any strings that consist only of alphabetical characters, spaces, and hyphens, allowing any combination of these characters
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_date(self, df, column_name):
        df[column_name] = pd.to_datetime(df[column_name], format='%Y-%m-%d', errors='ignore')
        df[column_name] = pd.to_datetime(df[column_name], format='%Y %B %d', errors='ignore') 
        df[column_name] = pd.to_datetime(df[column_name], format='%B %Y %d', errors='ignore')
        # converts dates that are in different formats into the correct format ignoring errors
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')

    def valid_number(self, df, column_name):
        regex_expression = r'^\+?[0-9\s()-]+$'
        # regex expression flexible matching of string phone numbers that contain digits, spaces, hyphens, parentheses, and an optional leading plus sign.
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_email(self, df, column_name):
        regex_expression = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        # regex expression flexible matching of emails
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_country(self, df, column_name):
        valid_countries = ['germany', 'united kingdom', 'united states']
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_countries else np.nan)

    def valid_country_code(self, df, column_name):
        valid_country_codes = ['de', 'gb', 'us']
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_country_codes else np.nan)

    def valid_card_no(self, df, column_name):
        regex_expression = r'^[0-9]+$'
        # regex exp
        # ression to ensure entire string contains only digits
        df.loc[~df[column_name].astype(str).str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_exp_date(self, df, column_name):
        regex_expression = r'^(0[1-9]|1[0-2])\/[0-9]{2}$'
        # regex expression matching expiry date in format mm/yy
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def is_float(self, df, column_name):
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        return df
    
    def valid_store_type(self, df, column_name):
        valid_types = ['web portal', 'local', 'super store', 'mall kiosk', 'outlet']
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_types else np.nan)

    def clean_continents(self, value):
        if 'Europe' in str(value):
            return 'Europe'
        elif 'America' in str(value):
            return 'America'
        else:
            return np.nan
    
    def valid_continent(self, df, column_name):
        df[column_name] = df[column_name].apply(str)
        df[column_name] = df[column_name].apply(self.clean_continents)

    def convert_product_weights(self, df, column_name):
        df[column_name] = df[column_name].apply(self.convert_to_kg)
        return df
    
    def weight_multiplication(self, value):
        if 'x' in value:
            value = value.replace(' ','')
            factors = value.split('x')
            value = float(factors[0]) * float(factors[1])
            return value
        
        else:
            return float(value)

    def convert_to_kg(self, value):
        value = str(value)
        if value.endswith('kg'):
            value = (value.replace('kg','')).strip()
            value = float(self.weight_multiplication(value))
            return value
        
        elif value.endswith('g'):
            value = (value.replace('g','')).strip()
            value = round(float(self.weight_multiplication(value))/ 1000, 2)
            return value
        
        elif value.endswith('ml'):
            value = (value.replace('ml','')).strip()
            value = round(float(self.weight_multiplication(value))/ 1000, 2)
            return value 
        
        elif value.endswith('l'):
            value = (value.replace('l','')).strip()
            value = float(self.weight_multiplication(value))
            return value
        
        elif value.endswith('oz'):
            value = (value.replace('oz','')).strip()
            value = round(float(self.weight_multiplication(value)) * 0.02835, 2)
            return value
        
        else:
            value = np.nan
            return value
    
    def valid_category(self, df, column_name):
        df[column_name] = df[column_name].apply(str)
        valid_cat = ['toys-and-games', 'sports-and-leisure', 'pets', 
                     'homeware', 'health-and-beauty', 'food-and-drink', 'diy']
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_cat else np.nan)

    def is_available(self, df, column_name):
        df[column_name] = df[column_name].apply(str)
        valid_status = ['still_avaliable', 'removed']
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_status else np.nan)

    def valid_timeperiod(self, df, column_name):
            df[column_name] = df[column_name].apply(str)
            valid_period = ['Evening', 'Morning', 'Midday', 'Late_Hours']
            df[column_name] = df[column_name].apply(lambda x: x if x in valid_period else np.nan)
    
    def valid_timestamp(self, df, column_name):
        timestamp_format = '%H:%M:%S'
        df[column_name] = pd.to_datetime(df[column_name], format=timestamp_format, errors='coerce')
        df[column_name] = df[column_name].dt.time

    def remove_null(self, df):
        df.replace('NULL', np.nan, inplace=True)
        df.dropna(how='any', inplace=True)

    def clean_user_data(self, df):
        self.valid_name(df, 'first_name')
        self.valid_name(df, 'last_name')
        self.valid_date(df, 'date_of_birth')
        self.valid_email(df, 'email_address')
        self.valid_country(df, 'country')
        self.valid_country_code(df, 'country_code')
        self.valid_number(df, 'phone_number')
        self.valid_date(df, 'join_date')
        self.remove_null(df)

    def clean_card_data(self, df):
        df.index.name = 'index'
        self.valid_card_no(df, 'card_number')
        self.valid_exp_date(df, 'expiry_date')
        self.valid_date(df, 'date_payment_confirmed')
        self.remove_null(df)

    def clean_store_data(self, df):
        df.set_index('index', inplace=True)
        df.drop(columns='lat', inplace=True)
        self.is_float(df, 'longitude')
        self.is_float(df, 'staff_numbers')
        self.valid_date(df, 'opening_date')
        self.valid_store_type(df, 'store_type')
        self.is_float(df, 'latitude')
        self.valid_country_code(df, 'country_code')
        self.valid_continent(df, 'continent')
        self.remove_null(df)
    
    def clean_products_data(self, df):
        df['product_price'] = (df['product_price'].apply(str)).str.replace('£', '')
        self.is_float(df, 'product_price')
        self.convert_product_weights(df, 'weight')
        self.valid_category(df, 'category')
        self.valid_date(df, 'date_added')
        self.is_available(df, 'removed')
        self.remove_null(df)
    
    def clean_orders_data(self, df):
        df.drop(columns='level_0', inplace=True)
        # making level_0 the index worked but then wouldn't let me rename column therefore dropping the column and naming pandas auto gen index
        df.drop(columns='first_name', inplace=True)
        df.drop(columns='last_name', inplace=True)
        df.drop(columns='1', inplace=True)
        df.index.name = 'index'
        # 'product_quantity' datatype is int therefore we can assume there is no discrepencies
        # 'card_number' datatype is int therefore we can assume there is no discrepencies
        # df.isna().sum() returns 0 for all colums remaining in df 

    def clean_date_times_data(self, df):
        df.index.name = 'index'
        self.valid_timestamp(df, 'timestamp')
        df['month'] = pd.to_numeric( df['month'], errors='coerce')
        df['year'] =  pd.to_numeric( df['year'], errors='coerce')
        df['day'] = pd.to_numeric( df['day'], errors='coerce')
        self.valid_timeperiod(df, 'time_period')
        self.remove_null(df)

    
#%%
