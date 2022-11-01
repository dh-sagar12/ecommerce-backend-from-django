-- FUNCTION: inventory.get_stock_qty_of_product_item(bigint)

-- DROP FUNCTION inventory.get_stock_qty_of_product_item(bigint);

CREATE OR REPLACE FUNCTION inventory.get_stock_qty_of_product_item(
	product_inventory_id_ bigint)
    RETURNS TABLE(stock_qty numeric) 
    LANGUAGE 'plpgsql'

    COST 100
    STABLE 
    ROWS 1000
    
AS $BODY$
 	DECLARE stock_qty numeric =  0;
	 DECLARE order_qty numeric =  0;

 BEGIN
		SELECT SUM(COALESCE(s.stock_qty, 0)) into stock_qty  FROM inventory.stocks s
		WHERE s.product_inventory_id =  product_inventory_id_
		GROUP BY s.product_inventory_id ;
		
		SELECT SUM(COALESCE(o.order_qty, 0)) into order_qty  FROM inventory.orders o
		WHERE o.product_inventory_id =  product_inventory_id_
		GROUP BY o.product_inventory_id ;
		
		RETURN  QUERY select COALESCE(stock_qty, 0) -COALESCE(order_qty, 0) stock_qty;
		
 END
 $BODY$;

ALTER FUNCTION inventory.get_stock_qty_of_product_item(bigint)
    OWNER TO postgres;
	
	
