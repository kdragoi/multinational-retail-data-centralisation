-- Query 1 
-- How many stores does the business have and in which countries?

SELECT country_code, COUNT (*) 
FROM dim_store_details 
GROUP BY country_code;