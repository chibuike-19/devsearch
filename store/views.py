from django.shortcuts import render
from models import Product


def fetch_product(request):


    return render(request, 'index.html', {'name': 'Emmanuel'})


