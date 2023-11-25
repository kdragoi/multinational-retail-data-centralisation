-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'dim_store_details';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

SELECT MAX(LENGTH(address)) AS max_length
FROM dim_store_details;

SELECT MAX(LENGTH(store_code)) AS max_length
FROM dim_store_details;

SELECT MAX(LENGTH(country_code)) AS max_length
FROM dim_store_details;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM dim_store_details;


-- Correcting all column data types which were wrong

ALTER TABLE dim_store_details
ALTER COLUMN address TYPE varchar(255),
ALTER COLUMN longitude TYPE float,
ALTER COLUMN locality TYPE varchar(255),
ALTER COLUMN store_code TYPE varchar(20),
ALTER COLUMN staff_numbers TYPE smallint,
ALTER COLUMN opening_date TYPE date,
ALTER COLUMN store_type DROP NOT NULL,
ALTER COLUMN store_type TYPE varchar(255),
ALTER COLUMN latitude TYPE float,
ALTER COLUMN country_code TYPE varchar(5),
ALTER COLUMN continent TYPE varchar(255);

