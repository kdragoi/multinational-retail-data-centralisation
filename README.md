# Multinational Retail Data Centralisation Poject 

## Overview
The Multinational Retail Data Centralisation project aims to centralise and consolidate retail-related data from multiple sources into a single database for efficient management and analysis. This repository contains the scripts and utilities to extract, clean, and upload data from various retail-related sources into a database.

## Installation

### 1. Clone the repository:
```
git clone https://github.com/kdragoi/multinational-retail-data-centralisation.git
```
### 2. Install the required Python packages:
```
pip install -r environment_requirements.txt
```
Required packages can be accessed via the environment_requirements.txt document located in the repository.

## File structure

This root of this repository contains python files:
- data_utils.py
- data_extraction.py
- data_cleaning.py
- main.py

These files are responsible for connecting to an AWS Relational Database, extracing and cleaning the data before uploading it to a local database server.

The folder **database_schema** contains all the nesseccary SQL code scripts to create the star based schema of the database.

Finally, the folder **queries** contains all the SQL scripts nessecary to execute the tasks within milestone 4.

## Usage Workflow

1. Set up the necessary database credentials by creating the **db_creds.yaml** and **local_db_creds.yaml** files.

2. Execute the **data_utils.py**, **data_extraction.py**, **data_cleaning.py** and **main.py** scripts according to your data extraction and cleaning needs:
    - **upload_dim_users()**: Extracts, cleans, and uploads user data to the database
    - **upload_dim_card_details()**: Extracts, cleans, and uploads card details data to the database
    - **upload_dim_store_details()**: Extracts, cleans, and uploads store information data to the database
    - **upload_dim_products()**: Extracts, cleans, and uploads product data to the database
    - **upload_orders_table()**: Extracts, cleans, and uploads orders data to the database
    - **upload_dim_date_times()**: Extracts, cleans, and uploads date/time details data to the database

3. Execute the scripts in the **database_schema** folder in order:
    1. **dim_users_datatype_correction.sql**
    1. **dim__card_details_datatype_correction.sql**
    1. **dim_store_details_datatype_correction.sql**
    1. **dim_products_adding_weight_class.sql**
    1. **dim_products_datatype_correction.sql**
    1. **dim_date_times_datatype_correction.sql**
    1. **orders_table_datatype_correction.sql**
    1. **sales_db_relationships.sql**

    to create correct the datatypes of each column in each table and then create the starbased schemas seen below:

    ![database_schema](/database_schema/database_schema.PNG)

4. Execute the scripts in the **queries** according to the query you would like to see


## Limitations and Improvements

Since completing the project there are are a few limitations and improvements which I believe would mitiage some problems I had in the later stages as well as improve the overall performace. 

When adding the foreign key constraints to the orders_table, I came across missing data in the dim tables. I therefore went back to the raw data and checked if the data ever existed in the raw tables before determining wether to delete them or not in order for the foreign key assignment to work. Where the data still existed in the raw data tables, I believe that either my data cleaning was too thorough and therefore resulted in significant data loss and/or when validating certain data, there was an unforseen error in the program leading to losing data which was infact valid.

In order to reduce this data loss, I believe that it would be more beneficial to link the tables in a different way in order to allow for this mismatching.

One issue that I could not resolve was when checking the mismatching data prior to creating the foreign keys, all of the user_uuids in the orders_table were mismatched and I also did not find that they existed in the raw data table. Therefore, as none of the query tasks relied on the user data, I refrained from adding the user_uuid foreign key to the users_table.


