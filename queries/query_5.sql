-- Query 5
-- What percentage of sales come through each type of store?

SELECT dim_store_details.store_type,
	ROUND(SUM(orders_table.product_quantity*dim_products.product_price)) AS total_sales_revenue,
	ROUND(SUM(100.0*orders_table.product_quantity*dim_products.product_price)/
		  (SELECT SUM(orders_table.product_quantity * dim_products.product_price)
           FROM orders_table
           JOIN dim_products ON orders_table.product_code = dim_products.product_code)) AS percentage_total																		   
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY dim_store_details.store_type
ORDER BY percentage_total DESC;