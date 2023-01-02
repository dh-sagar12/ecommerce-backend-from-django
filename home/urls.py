
from django.urls import  path
from home.views.banner_view import AddBannerImageView, GetAllBannerImagesView, UpdateBannerImages
from home.views.country_views import CountryView



urlpatterns  = [
        path('add-banner-image/', AddBannerImageView.as_view(), name='addBannerImage'),
        path('get-banner-image/', GetAllBannerImagesView.as_view(), name='getBannerImage'),
        path('update-banner-image/', UpdateBannerImages.as_view(), name='updateBannerImage'),
        path('countries/', CountryView.as_view(), name='countries'),
]