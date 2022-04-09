from itertools import product
from unicodedata import category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from api.models import Product
from api.models import Category

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_item(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    return JsonResponse(product.to_json(), status=200, safe=False)

#####################################################################

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_element(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    return JsonResponse(category.to_json(), status=200, safe=False)

def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=404)
    category_json = category.to_json()


    products = Product.objects.all()
    products_json = [product.to_json() for product in products]

    result_products = []
    for product in products_json:
        if product['category'] == category_json['name']:
            result_products.append(product)
    
    return JsonResponse(result_products, safe=False)
    