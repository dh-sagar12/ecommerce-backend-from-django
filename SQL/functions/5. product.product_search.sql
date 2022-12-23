-- FUNCTION: product.product_search(bigint, character varying)

-- DROP FUNCTION product.product_search(bigint, character varying);

CREATE OR REPLACE FUNCTION product.product_search(
	product_id_ bigint,
	product_name_ character varying)
    RETURNS TABLE(id bigint, product_name character varying, description character varying, category character varying) 
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
    ROWS 1000
    
AS $BODY$
BEGIN
		Return query(
				select p.id, p.product_name, p.description, c.category_name as category from product.products p
			join product.category c on p.category_id  =  c.id 
			where (p.product_name ilike '%'||product_name_||'%' OR product_name_ = '')
			and (p.id =  product_id_ or product_id_  =  0 )
		);
END
$BODY$;

ALTER FUNCTION product.product_search(bigint, character varying)
    OWNER TO postgres;
