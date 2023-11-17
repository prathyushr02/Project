from django.urls import path
from . import views

app_name = 'cart'
app_name = 'cartapp'
urlpatterns = [
    path('add/<int:product_id>/', views.addcart, name='add_cart'),
    path('remove/<int:product_id>/', views.removecart, name='remove_cart'),
    path('delete/<int:product_id>/', views.deletecart, name='delete_cart'),
    path('', views.cart_detail, name='cart_detail'),
]