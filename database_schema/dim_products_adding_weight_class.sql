-- Add column weight_class column to table dim_products

ALTER TABLE dim_products
ADD COLUMN weight_class varchar(20)


-- Filling weight_class column with the appropriate corrosponding class depending on the kg weight in weight column

UPDATE dim_products
SET weight_class = 
    CASE 
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END;
