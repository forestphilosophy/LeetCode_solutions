WITH new_id_CTE (id,even_or_odd)  
AS  
-- Define the CTE query.  
(  
    SELECT TOP 1 id, id%2 AS even_or_odd
    FROM seat 
    ORDER BY id DESC  
)  

SELECT 
CASE
    WHEN (SELECT even_or_odd FROM new_id_CTE) = 0 THEN IIF(id%2 = 0 ,id-1, id+1)
    ELSE 
        CASE
            WHEN id = (SELECT id FROM new_id_CTE)  THEN id 
            ELSE IIF(id%2 = 0 ,id-1, id+1)
        END
END AS id,    
student

FROM seat
ORDER BY id
