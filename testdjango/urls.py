"""
URL configuration for testdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homepage_view, contact_view, home_view
from products.views import products_detail_view, products_create_view, render_intiial_data, dynamic_lookup_view, product_delete_view, product_list
# from pages.views import contact_view
urlpatterns = [
    path('home/', homepage_view, name="homepage"),
    path('', home_view, name="homepage2"),
    path('contact/', contact_view, name="contact"),
    path('create/', products_create_view, name="create"),
    path('product/', products_detail_view, name="product"),
    path('products/<int:id>/delete/', product_delete_view, name="delete"),
    path('products/<int:id>/', dynamic_lookup_view, name="product-detail"),
    path('products/', product_list, name="product-list"),
    path('admin/', admin.site.urls),
]

