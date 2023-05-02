from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} in {self.cart}"


class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.PositiveSmallIntegerField()
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.code