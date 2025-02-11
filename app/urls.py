# app/urls.py
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, UserViewSet, ProfileViewSet, OrderViewSet

# Создаем роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('categories/', views.category, name='category_list'),
    path('products/', views.product, name='product_list'),
    path('users/', views.user, name='user_list'),  
    path('profiles/', views.profile, name='profile_list'), 
    path('orders/', views.order, name='order_list'),
    path('web_socket/', views.web_socket, name='web_socket'),
]
