-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'dim_card_details';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

SELECT MAX(LENGTH(card_number)) AS max_length
FROM dim_card_details;

SELECT MAX(LENGTH(expiry_date)) AS max_length
FROM dim_card_details;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM dim_card_details;


-- Correcting all column data types which were wrong

ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE varchar(20),
ALTER COLUMN expiry_date TYPE varchar(5),
ALTER COLUMN card_provider TYPE varchar(255),
ALTER COLUMN date_payment_confirmed TYPE date;

