from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('search/', views.search, name='search_form'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('login/', views.login_view, name='login_view'),

    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='product-update'),
    path('delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('detail/<int:pk>/', views.ProductDetail.as_view(), name='product_detail')
]