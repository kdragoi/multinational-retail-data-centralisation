-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'dim_date_times';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

ALTER TABLE dim_date_times
ALTER COLUMN "month" TYPE varchar(225);

ALTER TABLE dim_date_times
ALTER COLUMN "year" TYPE varchar(225);

ALTER TABLE dim_date_times
ALTER COLUMN "day" TYPE varchar(225);

SELECT MAX(LENGTH("month")) AS max_length
FROM dim_date_times;

SELECT MAX(LENGTH("year")) AS max_length
FROM dim_date_times;

SELECT MAX(LENGTH("day")) AS max_length
FROM dim_date_times;

SELECT MAX(LENGTH(time_period)) AS max_length
FROM dim_date_times;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM dim_date_times;


-- Correcting all column data types which were wrong

ALTER TABLE dim_date_times
ALTER COLUMN "month" TYPE varchar(2),
ALTER COLUMN "year" TYPE varchar(4),
ALTER COLUMN "day" TYPE varchar(2),
ALTER COLUMN time_period TYPE varchar(20),
ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid;

