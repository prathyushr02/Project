from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name='shopapp'
urlpatterns = [
    path('', views.AllProductCat, name='AllProductCat'),
    path('<slug:c_slug>/',views.AllProductCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.pdetail, name='productCatdetail'),

]
