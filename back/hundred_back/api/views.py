from rest_framework import generics, permissions

from .models import Book, CartItem, Cart, Genre
from .serializers import BookSerializer, CartItemSerializer, GenreSerializer


class BookList(generics.ListAPIView):
    # Список  книг
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetail(generics.RetrieveAPIView):
    # Детали книги по id
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookListByGenre(generics.ListAPIView):
    # Список всех книг по жанру
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        genre_id = self.request.query_params.get('genre')
        return Book.objects.filter(genre=genre_id)


class GenreList(generics.ListAPIView):
    # Список жанров
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


class GenreDetail(generics.RetrieveAPIView):
    # Детали жанра по id
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class AddToCart(generics.CreateAPIView):
    # Добавление книги в корзину пользователя
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user, ordered=False)
        serializer.save(cart=cart)


class CartItemList(generics.ListAPIView):
    # Список всех элементов корзины пользователя
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user, cart__ordered=False)
