from rest_framework import serializers
from .models import Book, Genre, Cart, CartItem, Discount


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'price', 'genre')


class CartItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'book', 'quantity')


# class CartSerializer(serializers.ModelSerializer):
#     books = CartItemSerializer(many=True)
#
#     class Meta:
#         model = Cart
#         fields = ('id', 'user', 'books', 'created_at')


class DiscountSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Discount
        fields = ('id', 'code', 'discount_percent', 'books')


class AddToCartSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
