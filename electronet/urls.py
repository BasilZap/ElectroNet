from django.urls import path
from electronet.apps import ElectronetConfig
from electronet.views import CompanyListAPIView, CompanyUpdateAPIView, CompanyRetrieveAPIView, CompanyDestroyAPIView, \
    CompanyCreateAPIView

app_name = ElectronetConfig.name

urlpatterns = [
    path('', CompanyListAPIView.as_view(), name='list'),
    path('update/<int:pk>/', CompanyUpdateAPIView.as_view(), name='update'),
    path('view/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='view'),
    path('delete/<int:pk>/', CompanyDestroyAPIView.as_view(), name='delete'),
    path('create/', CompanyCreateAPIView.as_view(), name='create'),
]
