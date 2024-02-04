from django.urls import path
from category import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.category_list,name="category_list"),
    path('addcategory', views.addForm, name="add_Category"),
    path('category_delete/<int:id>/', views.category_delete, name='category_delete'),
]