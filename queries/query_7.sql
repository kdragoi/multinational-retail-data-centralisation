-- Query 7
-- What is our staff headcount?

SELECT SUM(dim_store_details.staff_numbers) AS total_staff_numbers, dim_store_details.country_code
FROM dim_store_details
GROUP BY dim_store_details.country_code
ORDER BY total_staff_numbers DESC;