from rest_framework import generics, viewsets

from electronet.models import Product, Company
from electronet.serializers import ProductSerializer, CompanySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели "Продукт"
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания поставщика
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для изменения поставщика
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для просмотра поставщика
    """
    queryset = Company.objects.select_related('distributor')
    serializer_class = CompanySerializer


class CompanyListAPIView(generics.ListAPIView):
    """
    Представление для просмотра списка поставщиков
    """
    queryset = Company.objects.select_related('distributor')
    serializer_class = CompanySerializer


class CompanyDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления поставщика
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
