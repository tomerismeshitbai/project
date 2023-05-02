from django.urls import path

from .views import GenreDetail, GenreList, BookList, BookDetail, CartItemList

urlpatterns = [
    path('api/genres/', GenreList.as_view(), name='genre_list'),
    path('api/genres/<int:pk>/', GenreDetail.as_view(), name='genre_detail'),
    path('api/books/', BookList.as_view(), name='book_list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('api/carts/', CartItemList.as_view(), name='cart_list'),
]