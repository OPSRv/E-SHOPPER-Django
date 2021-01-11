from django.shortcuts import render
from django.shortcuts import get_object_or_404
from product.models import Product
from .cart import Cart
from django.conf import settings
from django.views.generic import TemplateView, ListView
from django.db.models import Q


def cart(request, product_id):
    products = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.add(products)
    product = Product.objects.filter(id__in=request.session['cart'])
    content={
        "product": product
    }
    return render (request, "pages/cart.html", content)


class SearchResultsView(ListView):
    model = Product
    template_name = "pages/search_results.html"

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')

        if query == '':
            query = 'Зелена кофта'

        object_list = Product.objects.filter(Q(tittle__icontains=query) | Q(description__icontains=query))
        return object_list
