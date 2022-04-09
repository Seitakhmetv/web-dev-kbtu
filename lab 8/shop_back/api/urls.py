from django.urls import path
from api.views import product_list, product_item, category_list, category_element, category_products

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', product_item),
    path('categories/', category_list),
    path('categories/<int:id>/', category_element),
    path('categories/<int:id>/products', category_products),
]
