from django.contrib import admin

# Register your models here.
from .models import WishList, WishlistProduct

admin.site.register(WishList)
admin.site.register(WishlistProduct)