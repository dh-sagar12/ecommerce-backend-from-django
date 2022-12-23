
from django.urls import  path
from stocks.views.cart_views import UserCartView
from stocks.views.stocks_views import AddStockView, get_stock_qty_of_product_item




urlpatterns  = [
        path('add-stock/', AddStockView.as_view(), name='addStock'),
        path('get-stock-qty/', get_stock_qty_of_product_item, name='getStockQty'),
        path('user-cart/', UserCartView.as_view(), name='addToCart')
]