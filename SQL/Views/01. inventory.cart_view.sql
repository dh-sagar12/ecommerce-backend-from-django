-- View: inventory.cart_view

-- DROP VIEW inventory.cart_view;

CREATE OR REPLACE VIEW inventory.cart_view
 AS
 SELECT c.id,
    c.user_id,
    c.product_id,
    p.product_name,
    p.description,
    c.product_inventory_id,
    pi.retail_price,
    pi.discount,
    pi.store_price,
    pi.sku,
    array_agg(i.file_name) AS images,
    ( SELECT json_object_agg(get_attribute_value_by_product_item_id.attribute_name, get_attribute_value_by_product_item_id.attribute_value) AS json_object_agg
           FROM product.get_attribute_value_by_product_item_id(c.product_inventory_id) get_attribute_value_by_product_item_id(id, attribute_id, attribute_name, attribute_value)) AS product_attributes,
    c.cart_qty,
    c.status
   FROM inventory.cart c
     JOIN product.products p ON c.product_id = p.id
     JOIN product.product_inventory pi ON c.product_inventory_id = pi.id
     JOIN product.images i ON c.product_inventory_id = i.product_inventory_id
  GROUP BY c.id, c.user_id, c.product_id, p.product_name, p.description, pi.retail_price, pi.discount, pi.store_price, pi.sku;

ALTER TABLE inventory.cart_view
    OWNER TO postgres;

