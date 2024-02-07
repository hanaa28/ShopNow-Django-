from django.urls import path
from category import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path
from .views import categoryCreate

urlpatterns = [
    path('', views.category_list, name="category_list"),
    # path('addcategory/', views.addForm, name="add_Category"),
    # path('category_delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category_update/<pk>', views.category_update.as_view(), name='category_update'),
    path('category_Create/', categoryCreate.as_view(), name='category_Create'),
    path('categorydeleted/<pk>', views.categorydeleted.as_view(), name='categorydeleted'),

]
