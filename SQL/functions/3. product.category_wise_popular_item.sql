-- FUNCTION: product.category_wise_popular_item(date)

-- DROP FUNCTION product.category_wise_popular_item(date);

CREATE OR REPLACE FUNCTION product.category_wise_popular_item(
	till_date_ date)
    RETURNS TABLE(category_id bigint, category_title character varying, category_url character varying, products json) 
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
    ROWS 1000
    
AS $BODY$
 	
BEGIN
	RETURN QUERY SELECT c.id, ('Popular On '|| c.category_name || '')::character varying category_title, c.slug category_url, json_agg(p.*) products
from product.get_popular_product_item(till_date_) p join product.category c 
on p.category_name  =  c.category_name
group by c.id, c.category_name, c.slug ;
	

 END
 $BODY$;

ALTER FUNCTION product.category_wise_popular_item(date)
    OWNER TO postgres;
