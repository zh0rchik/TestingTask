from django.contrib import admin
from django.urls import path

from shops.views import CityViewSet, CityDetail, ShopDetail

urlpatterns = [
    path('city/', CityViewSet.as_view({'get': 'list'})),
    path('city/<int:pk>/', CityDetail.as_view()),
    path('shop/', ShopDetail.as_view()),
]