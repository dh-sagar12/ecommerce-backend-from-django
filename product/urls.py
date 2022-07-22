from django.urls import  path
from product.views import attribute_views, views
from product.views import category_views, product_inventory_view

urlpatterns = [
   path('get-product/', views.GetProductView.as_view(), name='getProduct'),
   path('get-product/<int:pk>', views.view_product_view, name='viewProduct'),
   path('add-product/', views.AddNewProduct.as_view(), name='addProduct'),
   path('update-product/', views.UpdateDeleteProduct.as_view(), name='updateProduct'),

   path('add-category/', category_views.AddNewCategory.as_view(), name='addCategory'),
   path('get-category/', category_views.GetCategory.as_view(), name='getCategory'),
   path('updel-category/', category_views.UpdateDeleteCategory.as_view(), name='updateDeleteCategory'),

   path('add-sub-category/', category_views.AddNewSubCategory.as_view(), name='addSubCategory'),
   path('get-sub-category/', category_views.GetSubCategory.as_view(), name='getSubCategory'),
   path('updel-sub-category/', category_views.UpdateDeleteSubCategory.as_view(), name='updateDeleteSubCategory'),

   path('add-product-inventory/', product_inventory_view.AddNewProductInventory.as_view(), name='addNewProductInventory'),
   path('get-product-inventory/', product_inventory_view.GetProductInventory.as_view(), name='getNewProductInventory'),
   path('updel-product-inventory/', product_inventory_view.UpdateDeleteProductInventory.as_view(), name='updateDeleteProductInventory'),


   path('post-attribute/', attribute_views.AttributeView.as_view(), name='attribute'),
   path('get-attribute/', attribute_views.GetAttributeView.as_view(), name='getAttribute'),



   path('get-cateogry-attribute/', attribute_views.GetCategoryAttributeView.as_view(), name='getCategoryAttribute'),
   path('cateogry-attribute/', attribute_views.CategoryAttributeView.as_view(), name='categoryAttributeView'),


   path('product-attribute/', attribute_views.ProductAttributeValueView.as_view(), name='productAttributeValue'),
   path('get-product-attribute/', attribute_views.GetProductAttributeValueView.as_view(), name='getProductAttributeValue'),


]
