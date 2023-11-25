
-- Checking current column data types

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'dim_products';


-- Checking maximum character length of columns to become varchar to set appropriate char limit

SELECT MAX(LENGTH(product_code)) AS max_length
FROM dim_products;

SELECT MAX(LENGTH(weight_class)) AS max_length
FROM dim_products;


-- Check data count before and after altering column data types to make sure no data loss

SELECT COUNT(*) FROM dim_products;


-- Correcting all column data types which were wrong
-- weight_class not included because correct type was already specified when creating column

ALTER TABLE dim_products
ALTER COLUMN product_name TYPE varchar(255),
ALTER COLUMN product_price TYPE float,
ALTER COLUMN weight TYPE float,
ALTER COLUMN category TYPE varchar(255),
ALTER COLUMN "EAN" TYPE varchar(255),
ALTER COLUMN date_added TYPE date,
ALTER COLUMN "uuid" TYPE uuid USING "uuid"::uuid,
ALTER COLUMN product_code TYPE varchar(20),
ALTER COLUMN removed SET DATA TYPE BOOLEAN
  USING CASE WHEN removed = 'Removed' THEN TRUE ELSE FALSE END;

