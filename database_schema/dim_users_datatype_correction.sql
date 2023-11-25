-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'dim_users';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

SELECT MAX(LENGTH(country_code)) AS max_length
FROM dim_users;

SELECT MAX(LENGTH(country)) AS max_length
FROM dim_users;

SELECT MAX(LENGTH(phone_number)) AS max_length
FROM dim_users;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM dim_users;


-- Correcting column data types

ALTER TABLE dim_users
ALTER COLUMN first_name TYPE varchar(255),
ALTER COLUMN last_name TYPE varchar(255),
ALTER COLUMN date_of_birth TYPE DATE,
ALTER COLUMN company TYPE varchar(255),
ALTER COLUMN email_address TYPE varchar(255),
ALTER COLUMN address TYPE varchar(255),
ALTER COLUMN country TYPE varchar(100),
ALTER COLUMN country_code TYPE varchar(5),
ALTER COLUMN phone_number TYPE varchar(20),
ALTER COLUMN join_date TYPE DATE,
ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid;


