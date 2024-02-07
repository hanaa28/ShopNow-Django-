from django.urls import path
from .views import *

urlpatterns=[
    path('allproducts/',allProducts,name='allproducts'),
    path('getProduct/<int:id>/', getProduct, name='getProduct'),
    path('getProduct/<str:name>/', getProductName, name='getProduct'),
    path('addProduct/',addProduct, name='addProduct'),
    path('update/<int:id>/', updateProduct, name='updateProduct'),
    path('delete/<int:id>/', deleteProduct, name='eleteProduct'),
]