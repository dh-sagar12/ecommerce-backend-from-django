
from django.urls import  path
from stocks.views.cart_views import UserCartView
from stocks.views.order_views import OrdersStatusView, PlaceOrderView, ShowAllOrdersView
from stocks.views.stocks_views import AddStockView, get_stock_qty_of_product_item




urlpatterns  = [
        path('add-stock/', AddStockView.as_view(), name='addStock'),
        path('get-stock-qty/', get_stock_qty_of_product_item, name='getStockQty'),
        path('user-cart/', UserCartView.as_view(), name='addToCart'),
        path('place-order/', PlaceOrderView.as_view(), name = 'placeOrder'),
        path('all-order/', ShowAllOrdersView.as_view(), name = 'allOrder'),
        path('post-order-status/', OrdersStatusView.as_view(), name='postOrderStatus')
]