-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'orders_table';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

ALTER TABLE orders_table
ALTER COLUMN card_number TYPE varchar(225);

SELECT MAX(LENGTH(card_number)) AS max_length
FROM orders_table;

SELECT MAX(LENGTH(store_code)) AS max_length
FROM orders_table;

SELECT MAX(LENGTH(product_code)) AS max_length
FROM orders_table;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM orders_table;


-- Correcting all column data types which were wrong

ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid,
ALTER COLUMN user_uuid TYPE uuid USING date_uuid::uuid,
ALTER COLUMN card_number TYPE varchar(20),
ALTER COLUMN store_code TYPE varchar(20),
ALTER COLUMN product_code TYPE varchar(20),
ALTER COLUMN product_quantity TYPE smallint;

