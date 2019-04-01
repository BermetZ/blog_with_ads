from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.AdList.as_view(), name='ad_list'),
    path('ad/<int:pk>', views.ad_detail, name='ad_detail'),
    path('ad/new/', views.AdCreate.as_view(), name='ad_new'),
    path('ad/<int:pk>/edit/', views.AdEdit.as_view(), name='ad_edit'),
    path('company/<int:pk>', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('company/new/', views.CompanyCreate.as_view(), name='company_new'),
    path('company/<int:pk>/edit/', views.CompanyEdit.as_view(), name='company_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)