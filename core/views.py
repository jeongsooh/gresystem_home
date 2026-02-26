from django.shortcuts import render

def home_view(request):
    return render(request, 'core/home.html')

def products_view(request):
    return render(request, 'core/products.html')
