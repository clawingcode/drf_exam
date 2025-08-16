from django.db import models

from apps.common.models import IsDeletedModel
from apps.accounts.models import User
from apps.shop.models import Product


RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

class Review(IsDeletedModel):
    """
    Represents a customer's review of product.

    Attributes:
        user (ForeignKey): The user who wrote the review.
        product (ForeignKey): The product reviewed.
        rating (int): The rating of product (1-5).
        text (str): The text of review.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.TextField()
