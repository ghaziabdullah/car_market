from django.urls import path
from . import views

app_name = 'carSelling'

urlpatterns = [
    path('', views.AdsListView, name='ads_list'),
    path('<int:car_id>', views.AdDetailView, name='ad_detail'),
    path('<int:ad_id>/delete', views.AdDeleteView, name='ad_delete'),
    path('new_ad', views.NewAdView, name='new_ad'),
]