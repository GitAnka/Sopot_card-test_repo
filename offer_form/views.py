from django.shortcuts import render, get_object_or_404
from .models import Category, Offers


def offer_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Offers.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'offer_form/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def offer_detail(request, id, slug):
    product = get_object_or_404(Offers, id=id, slug=slug)
    return render(request, 'offer_form/product/detail.html',
                  {'product': product})
