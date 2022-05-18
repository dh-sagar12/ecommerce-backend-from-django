from django.urls import  path
from product.views import views

urlpatterns = [
   path('get-product/', views.GetProductView.as_view(), name='getProduct'),
   path('get-product/<int:pk>', views.view_product_view, name='viewProduct'),
   path('add-product/', views.AddNewProduct.as_view(), name='addProduct'),
   path('update-product/', views.UpdateDeleteProduct.as_view(), name='updateProduct'),
]
