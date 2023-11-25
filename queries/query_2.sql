-- Query 2
-- Which locations currently have the most stores?

SELECT locality, COUNT (*) 
FROM dim_store_details 
GROUP BY locality	
ORDER BY COUNT(*) DESC;