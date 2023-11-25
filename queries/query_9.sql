-- Query 9
-- How quickly is the company making sales?

-- Adding column to dim_date_times to store complete timestamps
ALTER TABLE dim_date_times
ADD COLUMN complete_timestamp TIMESTAMP;

-- Updating dim_date_times table to populate the new column by concating each of the separate timestamp elements and converting to timestamp
UPDATE dim_date_times
SET complete_timestamp = 
    TO_TIMESTAMP(CONCAT(dim_date_times.year, '-', LPAD(dim_date_times.month::text, 2, '0'), '-', LPAD(dim_date_times.day::text, 2, '0'), ' ', dim_date_times.timestamp), 'YYYY-MM-DD HH24:MI:SS');

-- Query to select the average time difference between orders, grouped by year
-- Sub query used in order to separate the AVG aggregate function from LEAD as they cannot work together
SELECT year,
    AVG(time_diff) / 3600.0 AS avg_time_taken_in_hours
FROM (
    SELECT EXTRACT(YEAR FROM complete_timestamp) AS year,
        EXTRACT(EPOCH FROM (LEAD(complete_timestamp) OVER (ORDER BY complete_timestamp) - complete_timestamp)) AS time_diff
    FROM dim_date_times) AS subquery
GROUP BY year
ORDER BY avg_time_taken_in_hours;
	