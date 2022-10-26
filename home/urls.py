
from django.urls import  path
from home.views.banner_view import AddBannerImageView




urlpatterns  = [
        path('add-banner-image/', AddBannerImageView.as_view(), name='addbannerImage')
]