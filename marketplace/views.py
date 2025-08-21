from django.shortcuts import render
from products.models import Product
from blog.models import Blog
from banners.models import Banner

# def home(request):
#     products = Product.objects.all()
#     blogs = Blog.objects.all()
#     return render(request, 'basic/home.html', {'products': products, 'blogs':blogs})

def home(request):
    products = Product.objects.filter(is_approved=True, status=True).order_by('-created_at')[:6]
    banners = Banner.objects.filter(status=True)
    blogs = Blog.objects.order_by('-created_at')[:3]
    context = {
        'products': products, 
        'blogs':blogs,
        'banners': banners,
    }
    return render(request, 'home/home.html', context)


def cart(request):
    return render(request, 'cart/cart.html')





def order_complete(request):
    return render(request, 'orders/order_complete.html')

