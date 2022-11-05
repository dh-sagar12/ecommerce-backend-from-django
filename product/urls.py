
from django.urls import  path
from product.views import attribute_views, views
from product.views import category_views, product_inventory_view, images_views

urlpatterns = [
   path('get-product/', views.GetOnlyProductView.as_view(), name = 'getOnlyProduct' ),
   path('product-search/', views.product_search,  name = 'productSearch' ),
   path('get-product/<int:pk>', views.GetOneSingleProductView.as_view(), name = 'getOneSingleProductView' ),
   path('get-full-product/', views.GetFullProductView.as_view(), name='getFullProduct'),
   path('get-full-product/<int:pk>', views.view_product_view, name='viewProduct'),
   path('add-product/', views.AddNewProduct.as_view(), name='addProduct'),
   path('add-full-product/', views.AddFullProduct.as_view(), name='addFullProduct'),


   path('update-product/', views.UpdateDeleteProduct.as_view(), name='updateProduct'),

   path('add-category/', category_views.AddNewCategory.as_view(), name='addCategory'),
   path('get-category/', category_views.GetCategory.as_view(), name='getCategory'),
   path('updel-category/', category_views.UpdateDeleteCategory.as_view(), name='updateDeleteCategory'),

   path('add-sub-category/', category_views.AddNewSubCategory.as_view(), name='addSubCategory'),
   path('get-sub-category/', category_views.GetSubCategory.as_view(), name='getSubCategory'),
   path('updel-sub-category/', category_views.UpdateDeleteSubCategory.as_view(), name='updateDeleteSubCategory'),

   path('add-product-inventory/', product_inventory_view.AddNewProductInventory.as_view(), name='addNewProductInventory'),
   path('get-product-inventory/', product_inventory_view.GetProductInventory.as_view(), name='getNewProductInventory'),
   path('get-product-inventory/<int:pk>', product_inventory_view.view_product_items_view, name='ViewSingleProductItem'),

   path('updel-product-inventory/', product_inventory_view.UpdateDeleteProductInventory.as_view(), name='updateDeleteProductInventory'),


   path('post-attribute/', attribute_views.AttributeView.as_view(), name='attribute'),
   path('get-attribute/', attribute_views.GetAttributeView.as_view(), name='getAttribute'),



   path('get-cateogry-attribute/', attribute_views.GetCategoryAttributeView.as_view(), name='getCategoryAttribute'),
   path('cateogry-attribute/', attribute_views.CategoryAttributeView.as_view(), name='categoryAttributeView'),


   path('product-attribute/', attribute_views.ProductAttributeValueView.as_view(), name='productAttributeValue'),
   path('get-product-attribute/', attribute_views.GetProductAttributeValueView.as_view(), name='getProductAttributeValue'),
   path('get-item-attribute-value/', attribute_views.get_attribute_value_with_item_id, name='getAttributeValue'),



   path('upload-image/', images_views.AddImages.as_view(), name  =  'addImage' ),

   path('get-brands/', views.GetBrandsView.as_view(), name= 'GetBrands'),


   # functional urls 
   # /api/get-popular-items/
   path('get-popular-items/', product_inventory_view.PopularProductItems.as_view(), name= 'getPopularItems'),
   path('categorywise-popular-items/', product_inventory_view.CategoryWisePopularItems.as_view(), name= 'categoryWisePopularItems')


]
