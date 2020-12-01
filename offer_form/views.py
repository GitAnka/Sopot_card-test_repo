from django.shortcuts import render, get_object_or_404
from .models import Category, Offers


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Offers.objects.filter(end_date=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'offer_form/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Offers, id=id, slug=slug, end_date=True)
    return render(request, 'offer_form/product/detail.html',
                  {'product': product})
