from django.shortcuts import render
from django.db.models import Func, F, Value
from django.db.models.functions import Concat
from .models import Product

def fetch_product(request):
    # item = Product.objects.order_by('title')
    # items = Product.objects.earliest('title')

    # writing sql function to add the full_name row to the product table, with a value of the concatination of the first_name and last_name
    # query_set = Product.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # does the same thing as the previous line of code only difference is the use of Concat instead of the Func and F methods
    # query_set = Product.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))


    return render(request, 'index.html', {'name': 'Emmanuel'})


