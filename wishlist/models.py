from django.db import models

from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class WishList(models.Model):
    user = models.OneToOneField(User, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class WishlistProduct(models.Model):
    wishlist = models.ForeignKey(WishList, related_name='wishlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wishlist.user.email}'
