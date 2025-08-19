from django.urls import path
from . import views

urlpatterns = [
    # User Pages
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'), # Login Page
    path('logout/', views.user_logout, name='user_logout'), 
    path('dashboard/', views.user_dashboard, name='user_dashboard'), # Dashboard Page
    path('edit-profile/', views.edit_profile, name='edit-profile'), #Edit Profile
    path('my-products/', views.my_products, name='my_products'), # MY Products
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('add-product/', views.add_product, name='add_product'),
    path('change-password/', views.change_password, name='change_password'), # Change Password page
    path('my-orders/', views.my_orders, name='my_orders'),
    path('my-requests-sent/', views.my_requests_sent, name='my_request_sent'),
    path('my-requests-received/', views.my_requests_received, name='my_requests_received'),
    path('fulfill/<int:pk>/', views.mark_request_fulfilled, name='mark_request_fulfilled'),
    path('reopen/<int:pk>/', views.reopen_request, name='reopen_request'),
]