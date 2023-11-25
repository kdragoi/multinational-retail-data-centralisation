#%%

import pandas as pd
import numpy as np


#%%

class DataCleaning():
    ''' Used to clean data from various data sources '''

    def __init__(self):
        ''' Initialises the DataCleaning class '''
        pass

    def valid_name(self, df, column_name):
        ''' Validates and cleans the given column in the DataFrame to contain only valid names.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        regex_expression = r'^[a-zA-Z\s-]+$'
        # Regex expression for any strings that consist only of alphabetical characters, spaces, and hyphens, allowing any combination of these characters
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_date(self, df, column_name):
        ''' Validates and cleans date formats in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        df[column_name] = pd.to_datetime(df[column_name], format='%Y-%m-%d', errors='ignore')
        df[column_name] = pd.to_datetime(df[column_name], format='%Y %B %d', errors='ignore') 
        df[column_name] = pd.to_datetime(df[column_name], format='%B %Y %d', errors='ignore')
        # Converts dates that are in different formats into the correct format ignoring errors
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')

    def valid_number(self, df, column_name):
        ''' Validates and cleans phone number formats in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''

        regex_expression = r'^\+?[0-9\s()-]+$'
        # Regex expression flexible matching of string phone numbers that contain digits, spaces, hyphens, parentheses, and an optional leading plus sign.
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_email(self, df, column_name):
        ''' Validates and cleans email addresses in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''

        regex_expression = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        # Regex expression flexible matching of emails
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_country(self, df, column_name):
        ''' Validates and cleans country names in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        valid_countries = ['germany', 'united kingdom', 'united states']
        # List containing valid countries in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_countries else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match

    def valid_country_code(self, df, column_name):
        ''' Validates and cleans country codes in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        valid_country_codes = ['de', 'gb', 'us']
        # List containing valid country codes in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_country_codes else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match

    def valid_card_no(self, df, column_name):
        ''' Validates and cleans card numbers in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''

        regex_expression = r'^[0-9]+$'
        # regex expression to ensure entire string contains only digits
        df.loc[~df[column_name].astype(str).str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def valid_exp_date(self, df, column_name):
        ''' Validates and cleans card expiry dates in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''
        
        regex_expression = r'^(0[1-9]|1[0-2])\/[0-9]{2}$'
        # regex expression matching expiry date in format mm/yy
        df.loc[~df[column_name].str.match(regex_expression), column_name] = np.nan 
        # For every row  where the Phone column does not match our regular expression, replace the value with NaN

    def is_float(self, df, column_name):
        ''' Converts the values in the specified column of the DataFrame to float type.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be converted to float

        Returns:
        - pandas.DataFrame: DataFrame with the specified column converted to float type '''

        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        return df
    
    def valid_store_type(self, df, column_name):
        ''' Validates and cleans store types in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        valid_types = ['web portal', 'local', 'super store', 'mall kiosk', 'outlet']
        # List containing valid store types in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_types else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match

    def clean_continents(self, value):
        ''' Cleans continent values.

        Args:
        - value: Value to be cleaned into valid continents

        Returns:
        - str or NaN: Cleaned continent or NaN if the value does not match specified conditions '''

        if 'Europe' in str(value):
            return 'Europe'
        elif 'America' in str(value):
            return 'America'
        else:
            return np.nan
    
    def valid_continent(self, df, column_name):
        ''' Validates and cleans continents in the specified column in the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''

        df[column_name] = df[column_name].apply(str)
        df[column_name] = df[column_name].apply(self.clean_continents)

    def convert_product_weights(self, df, column_name):
        ''' Converts product weight values in the specified column of the DataFrame to kilograms.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned

        Returns:
        - pandas.DataFrame: DataFrame with the specified column converted to kilograms '''

        df[column_name] = df[column_name].apply(self.convert_to_kg)
        return df
    
    def weight_multiplication(self, value):
        ''' Performs multiplication of weight factors if the input value contains 'x'

        Args:
        - value: Value possibly containing 'x' as a separator for weight factors

        Returns:
        - float: Result of multiplication if 'x' is present, otherwise the input value converted to float '''
        
        if 'x' in value:
            value = value.replace(' ','')
            factors = value.split('x')
            value = float(factors[0]) * float(factors[1])
            return value
        
        else:
            return float(value)

    def convert_to_kg(self, value):
        ''' Converts various weight units to kilograms based on the input value.

        Args:
        - value: Value representing different weight units

        Returns:
        - float or NaN: Value converted to kilograms or NaN if unable to convert '''
        
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
        ''' Validates and cleans product categories in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        df[column_name] = df[column_name].apply(str)
        valid_cat = ['toys-and-games', 'sports-and-leisure', 'pets', 
                     'homeware', 'health-and-beauty', 'food-and-drink', 'diy']
        # List containing valid categories in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_cat else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match

    def is_available(self, df, column_name):
        ''' Validates and cleans availability status in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        df[column_name] = df[column_name].apply(str)
        valid_status = ['still_avaliable', 'removed']
        # List containing valid status in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x.lower() in valid_status else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match

    def valid_timeperiod(self, df, column_name):
        ''' Validates and cleans time periods in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data 
        - column_name (str): Name of the column to be cleaned '''

        df[column_name] = df[column_name].apply(str)
        valid_period = ['Evening', 'Morning', 'Midday', 'Late_Hours']
        # List containing valid time period in lower case for comparison
        df[column_name] = df[column_name].apply(lambda x: x if x in valid_period else np.nan)
        # Lambda function which takes the value, converts it to lower case and compares it to the values in the list, changing value to nan where there is no match
  
    def valid_timestamp(self, df, column_name):
        ''' Validates the timestamp values in the specified column of the DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data
        - column_name (str): Name of the column to be cleaned '''

        timestamp_format = '%H:%M:%S'
        df[column_name] = pd.to_datetime(df[column_name], format=timestamp_format, errors='coerce')
        # Converting timestamp to format '%H:%M:%S', coercing errors as nan
        df[column_name] = df[column_name].dt.time
        # Extracting time element of datetime value

    def remove_null(self, df):
        ''' Removes null values from the a specified DataFrame.

        Args:
        - df (pandas.DataFrame): DataFrame containing the data '''
        
        df.replace('NULL', np.nan, inplace=True)
        # Replaces occurrences of 'NULL' strings with NaN for consistent null representation
        df.dropna(how='any', inplace=True)
        # Drops rows with any NaN value

    def clean_user_data(self, df):
        ''' Cleans user-related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing user data
        
        Methods Applied:
        - valid_name: Validates 'first_name' and 'last_name' columns
        - valid_date: Validates 'date_of_birth' and 'join_date' columns as dates
        - valid_email: Validates 'email_address' column as email addresses
        - valid_country: Validates 'country' column as valid countries
        - valid_country_code: Validates 'country_code' column as valid country codes
        - valid_number: Validates 'phone_number' column as phone numbers
        - remove_null: Removes rows with NULL values '''

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
        ''' Cleans card-related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing card-related data
        
        Methods Applied:
        - valid_card_no: Validates 'card_number' column as card numbers
        - valid_exp_date: Validates 'expiry_date' column as expiry dates
        - valid_date: Validates 'date_payment_confirmed' column as dates
        - remove_null: Removes rows with NULL values '''

        df.index.name = 'index'
        self.valid_card_no(df, 'card_number')
        self.valid_exp_date(df, 'expiry_date')
        self.valid_date(df, 'date_payment_confirmed')
        self.remove_null(df)

    def clean_store_data(self, df):
        ''' Cleans store-related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing store-related data
        
        Methods Applied:
        - is_float: Converts 'longitude' and 'staff_numbers' columns to float type
        - valid_date: Validates 'opening_date' column as dates
        - valid_store_type: Validates 'store_type' column as valid store types
        - valid_country_code: Validates 'country_code' column as valid country codes
        - valid_continent: Validates 'continent' column as valid continents
        - remove_null: Removes rows with NULL values'''
        
        # In this method, nans had to be dropped for individual columns as web store only contain valid data for some of the columns and therefore we need to account for that
        df.set_index('index', inplace=True)
        df.drop(columns='lat', inplace=True)
        self.is_float(df, 'longitude')
        self.is_float(df, 'staff_numbers')
        df.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        self.valid_date(df, 'opening_date')
        df.dropna(subset = ['opening_date'],how='any',inplace= True)
        self.valid_store_type(df, 'store_type')
        df.dropna(subset = ['store_type'],how='any',inplace= True)
        self.is_float(df, 'latitude')
        self.valid_country_code(df, 'country_code')
        df.dropna(subset = ['country_code'],how='any',inplace= True)
        self.valid_continent(df, 'continent')
        df.dropna(subset = ['continent'],how='any',inplace= True)
    
    def clean_products_data(self, df):
        ''' Cleans product-related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing product-related data
        
        Methods Applied:
        - is_float: Converts 'product_price' column to float type
        - convert_product_weights: Converts 'weight' column values to kilograms
        - valid_category: Validates 'category' column as valid categories
        - valid_date: Validates 'date_added' column as dates
        - is_available: Validates 'removed' column as available or removed products
        - remove_null: Removes rows with NULL values ''' 
        
        df['product_price'] = (df['product_price'].apply(str)).str.replace('£', '')
        self.is_float(df, 'product_price')
        self.convert_product_weights(df, 'weight')
        self.valid_category(df, 'category')
        self.valid_date(df, 'date_added')
        self.is_available(df, 'removed')
        self.remove_null(df)
    
    def clean_orders_data(self, df):
        ''' Cleans order-related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing order-related data
        
        Methods Applied:
        - remove columns: Drops irrelevant columns ('level_0', 'first_name', 'last_name', '1')
        - remove_null: Removes rows with NULL values '''
        
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
        ''' Cleans date-time related data in the DataFrame.
        
        Parameters:
        - df: DataFrame containing date-time related data
        
        Methods Applied:
        - valid_timestamp: Validates 'timestamp' column as valid timestamps
        - pd.to_numeric: Converts 'month', 'year', and 'day' columns to numeric format
        - valid_timeperiod: Validates 'time_period' column as valid time periods
        - remove_null: Removes rows with NULL values '''
        
        df.index.name = 'index'
        self.valid_timestamp(df, 'timestamp')
        df['month'] = pd.to_numeric( df['month'], errors='coerce')
        df['year'] =  pd.to_numeric( df['year'], errors='coerce')
        df['day'] = pd.to_numeric( df['day'], errors='coerce')
        self.valid_timeperiod(df, 'time_period')
        self.remove_null(df)

    
#%%
