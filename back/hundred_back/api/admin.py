from django.contrib import admin

from .models import Book, Genre, Cart, Discount, CartItem

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Cart)
admin.site.register(Discount)
admin.site.register(CartItem)