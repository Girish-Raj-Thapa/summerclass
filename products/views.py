from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from . models import Product, Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from . forms import ContactSellerForm

def store(request, category_slug=None):
    products = None
    categories = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        # Filter by category + approved + active
        products = Product.objects.filter(category=categories, is_approved=True, status=True)
    else:
        # All approved and active products
        products = Product.objects.filter(is_approved=True, status=True).order_by('id')

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
        keyword = request.GET.get ('keyword', '').strip()
        products = Product.objects.none ()

        if keyword:
            # Search in multiple fields: description or product_name
            products = Product.objects.order_by('-created_at'). filter(
                 Q(description__icontains=keyword) | 
                Q (name__icontains=keyword)
            )
           

    context = {
    'products': products,
    'product_count': products. count()
    }

    return render (request, 'products/products.html', context)


User = get_user_model()

def seller_profile(request, user_id):
    seller = get_object_or_404(User, pk=user_id)

    qs = Product.objects.filter(owner=seller, status=True, is_approved=True).order_by('-id')
    product_count = qs.count()

    # Optional pagination (12 per page)
    paginator = Paginator(qs, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        "seller": seller,
        "products": products,
        "product_count": product_count,
        # If your empty-state text references {{ keyword }}, keep it defined
        "keyword": "",
    }
    return render(request, "accounts/seller/seller_profile.html",context)


def _display_name(user):
    name = f"{getattr(user, 'first_name', '')} {getattr(user, 'last_name', '')}".strip()
    return name or getattr(user, 'email', 'User')
