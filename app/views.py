from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib import messages

from app.forms import UserForm
from .models import Category, Product, User, Profile, Order
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, ProfileSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def index(request):
    return render(request, "index.html")

def category(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def user(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def profile(request):
    profiles = Profile.objects.all()
    return render(request, "profiles.html", {"profiles": profiles})

def order(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})


def web_socket(request):
    return render(request, "web_socket.html")