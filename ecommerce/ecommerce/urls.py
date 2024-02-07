"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from productlist import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from productlist import views as productlist_views
from django.urls import path,include
from category import views

urlpatterns = [
    path('', productlist_views.product_list,name="product_list"),
    path('product_detail/<int:id>/', productlist_views.product_detail, name='product_detail'),
    path('addproduct', productlist_views.product_add, name='addproduct'),
    path('product_delete/<int:id>/', productlist_views.product_delete, name='product_delete'),
    path('product_update/<int:id>/', productlist_views.product_update, name='product_update'),
    path('AddProductFrom', productlist_views.addForm, name='addForm'),
    path('category/',include('category.urls')),
    path('accounts/',include('accounts.urls')),
    path('product/API/',include('productlist.api.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)