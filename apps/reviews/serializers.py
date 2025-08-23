from rest_framework import serializers

from apps.profiles.serializers import ProfileSerializer
from apps.reviews.models import Review
from apps.shop.serializers import ProductSerializer


class ReviewSerializer(serializers.Serializer):
    user = ProfileSerializer()
    product = ProductSerializer()
    rating = serializers.IntegerField()
    text = serializers.CharField()


def rating_validator(value):
    if not 1 <= value <= 5:
        raise serializers.ValidationError("Rating must be in the range from 1 to 5!")
    return value


class AddReviewSerializer(serializers.Serializer):
    product_slug = serializers.SlugField()
    rating = serializers.IntegerField(validators=[rating_validator])
    text = serializers.CharField()