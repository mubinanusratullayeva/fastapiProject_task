from django.shortcuts import render
from django.views import View
from .models import Product, Order


# Create your views here.
class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'product': products
        }

        return render(request, 'products.html', context)