from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view  # 👈 add this



urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),

    # ✅ Only this is needed here for custom register view
    path('register/', views.register, name='register'),
    path('checkout/', views.checkout, name='checkout'),
    path('accounts/logout/', logout_view, name='logout'),



]
