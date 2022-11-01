-- FUNCTION: product.get_popular_product_item(date)

-- DROP FUNCTION product.get_popular_product_item(date);

CREATE OR REPLACE FUNCTION product.get_popular_product_item(
	till_date_ date)
    RETURNS TABLE(product_id bigint, product_inventory_id bigint, product_name character varying, sku character varying, slug character varying, description character varying, category_name character varying, sub_category_name character varying, brand_name character varying, store_price numeric, discount numeric, retail_price numeric, attribute_value json, images json, store_qty numeric) 
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
    ROWS 1000
    
AS $BODY$
 	
BEGIN
	CREATE TEMP TABLE _info ON COMMIT DROP AS
    with highest_orders as (
        SELECT o.product_inventory_id,    SUM(COALESCE(o.order_qty, 0)) order_qty FROM inventory.orders o
        where ordered_date BETWEEN $1- 7 and $1 
        group by o.product_inventory_id 
        order by order_qty desc ),
	product_images as (
			select img.product_inventory_id, json_agg( '/media/' || img.file_name) images
 			from product.images  img
			group by img.product_inventory_id
		)
		select p.id product_id, ho.product_inventory_id, p.product_name,
		pi.sku, p.slug, p.description, c.category_name, sc.sub_category_name, b.brand_name, pi.store_price::numeric, 
		pi.discount::numeric , pi.retail_price::numeric, 
		(select json_object_agg(av.attribute_name, av.attribute_value) 
 		from product.get_attribute_value_by_product_item_id(ho.product_inventory_id) av )as attribut_values,
		i.images, 
		(select inventory.get_stock_qty_of_product_item(ho.product_inventory_id)) stock_qty
		from product.product_inventory pi join 
		highest_orders ho on ho.product_inventory_id = pi.id
		join product.products p on pi.product_id  =  p.id 
		join product.category c on p.category_id =  c.id
		join product.sub_category sc on p.sub_category_id =  sc.id
		join product.brands b on p.brand_id =  b.id
		join product_images i on i.product_inventory_id  =  ho.product_inventory_id;
		
		return query select * from _info;

 END
 $BODY$;

ALTER FUNCTION product.get_popular_product_item(date)
    OWNER TO postgres;
