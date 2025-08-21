from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Product, Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q

def store(request, category_slug=None):
    products = None
    categories = None

    # Using slug to find the category, if found filter according to the slug
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, status=True)
    
    # If no slug is passed, redirect to the normal store page
    else:
        products = Product.objects.all().filter(status=True).order_by('id')
    
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }  

    return render(request, 'products/products.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)

        if not product.is_approved and not (request.user.is_staff or request.user == getattr(product, 'owner', None)):
            raise Http404("Product not found")
        
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except Product.DoesNotExist:
        raise Http404("Product_not_found")
    
    context = {
        'product': product,
        'in_cart': in_cart,
    }

    return render(request, 'products/details.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword', '').strip()
        products = Product.objects.none()
        if keyword:
            products = Product.objects.order_by('-created_at').filter(
                Q(description__icontains=keyword) |Q(name__icontains=keyword)
            )
    
    context = {
        'products': products,
        'product_count': products.count(),
    }

    return render(request, 'products/products.html', context)

