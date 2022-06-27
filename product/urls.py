from django.urls import  path
from product.views import views
from product.views import category_views

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
]
