from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Order)