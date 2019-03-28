from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdList.as_view(), name='ad_list'),
]