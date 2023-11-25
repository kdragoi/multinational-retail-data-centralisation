-- Adding primary keys in the dim tables

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

-- ALTER TABLE dim_users
-- ADD PRIMARY KEY (user_uuid);


-- To check that each table now contains a primary key

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = 'dim_card_details';

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = 'dim_date_times';

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = 'dim_products';

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = 'dim_store_details';

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = 'dim_users';


-- Adding foreign keys to the orders_table 

-- Checks that all the values in the column we want to add the foreing key constraint to is present in the primary key column
-- Where there is a mismatch of values data is then cross referenced via the raw data in python

SELECT orders_table.card_number AS missing_primary_values
FROM orders_table
LEFT JOIN dim_card_details ON orders_table.card_number = dim_card_details.card_number
WHERE dim_card_details.card_number IS NULL;
-- missing data does not exist in the raw dim_card_details table therefore must be removed from orders_table

SELECT orders_table.date_uuid AS missing_primary_values
FROM orders_table
LEFT JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
WHERE dim_date_times.date_uuid IS NULL;
-- no missing data for date_uuid

SELECT orders_table.product_code AS missing_primary_values
FROM orders_table
LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
WHERE dim_products.product_code IS NULL;
-- missing data is present in raw dim_products table but was removed during cleaning (see README improvements)
-- so for the purposes of the project the data must be removed

SELECT orders_table.store_code AS missing_primary_values
FROM orders_table
LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE dim_store_details.store_code IS NULL;
-- missing data is present in raw dim_store table but was removed during cleaning (see README improvements)
-- so for the purposes of the project the data must be removed 

SELECT orders_table.user_uuid AS missing_primary_values
FROM orders_table
LEFT JOIN dim_users ON orders_table.user_uuid = dim_users.user_uuid
WHERE dim_users.user_uuid IS NULL;
-- missing data is not present in raw dim_users table
-- mismatched data occupies all the records in the orders_table 
-- therefore it would indicate an error else where in the project
-- for this reason, the foreign key for user_uuid was not created


-- Bulk deletes the records in the dim tables which contain the missing data

DELETE FROM orders_table
WHERE card_number IN (
	SELECT orders_table.card_number AS missing_primary_values
	FROM orders_table
	LEFT JOIN dim_card_details ON orders_table.card_number = dim_card_details.card_number
	WHERE dim_card_details.card_number IS NULL);

DELETE FROM orders_table
WHERE product_code IN (
	SELECT orders_table.product_code AS missing_primary_values
	FROM orders_table
	LEFT JOIN dim_products ON orders_table.product_code = dim_products.product_code
	WHERE dim_products.product_code IS NULL);
	
DELETE FROM orders_table
WHERE store_code IN (
	SELECT orders_table.store_code AS missing_primary_values
	FROM orders_table
	LEFT JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
	WHERE dim_store_details.store_code IS NULL);

	
-- To check that the (truth) orders_table now contains all the foreign keys

SELECT COUNT(*)
FROM orders_table;

SELECT c.column_name, c.data_type
FROM information_schema.table_constraints tc 
JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
  AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
WHERE constraint_type = 'FOREIGN KEY' and tc.table_name = 'orders_table';


-- Adding foreign keys in the orders_tables

ALTER TABLE orders_table
ADD FOREIGN KEY (column_name) REFERENCES table_name(column_name);

---------------------------------------------------------------------
ALTER TABLE orders_table 
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number),
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid),
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code),
ADD FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);




