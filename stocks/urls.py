
from django.urls import  path
from stocks.views.stocks_views import AddStockView, get_stock_qty_of_product_item




urlpatterns  = [
        path('add-stock/', AddStockView.as_view(), name='addStock'),
        path('get-stock-qty/', get_stock_qty_of_product_item, name='getStockQty')
]