from django.contrib import admin

from electronet.models import Product, Company


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'launch_date')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'building', 'distributor', 'debt',
                    'creation_date')
