from django.contrib import admin

# Register your models here.
from .models import CustomUser, Item, Branch, Order

admin.site.register((CustomUser, Item, Branch, Order))
