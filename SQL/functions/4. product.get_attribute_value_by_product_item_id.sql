-- FUNCTION: product.get_attribute_value_by_product_item_id(bigint)

-- DROP FUNCTION product.get_attribute_value_by_product_item_id(bigint);

CREATE OR REPLACE FUNCTION product.get_attribute_value_by_product_item_id(
	product_item_id_ bigint)
    RETURNS TABLE(id bigint, attribute_id bigint, attribute_name character varying, attribute_value character varying) 
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
    ROWS 1000
    
AS $BODY$
BEGIN
		Return query(
			select av.id, a.id attribute_id, a.attribute_name, av.attribute_value
				from product.product_attribute_values  av
				join product.attributes a on av.attribute_id =  a.id
				where av.product_inv_id
				 = product_item_id_
		);
END
$BODY$;

ALTER FUNCTION product.get_attribute_value_by_product_item_id(bigint)
    OWNER TO postgres;
