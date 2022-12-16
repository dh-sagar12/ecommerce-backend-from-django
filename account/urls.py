from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from account.views.authenticationView import GetUserData, UserLoginView

urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('current-user/', GetUserData.as_view(), name='currentUser'),
]