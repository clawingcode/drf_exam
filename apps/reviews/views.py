from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView


from apps.reviews.serializers import ReviewSerializer
from apps.shop.models import Product
from apps.reviews.models import Review

from drf_spectacular.utils import extend_schema

tags = ["Reviews"]


class ProductReviewsView(APIView):
    serializer_class = ReviewSerializer

    @extend_schema(
        summary="Product Reviews Fetch",
        description="""
            This endpoint return all reviews for a particular product.
        """,
        tags=tags
    )

    def get(self, request, *args, **kwargs):
        product = Product.objects.get_or_none(slug=kwargs["slug"])
        if not product:
            return Response(data={"message": "Product does not exist!"}, status=HTTP_404_NOT_FOUND)
        reviews = Review.objects.select_related("user", "product").filter(product=product)
        serializer = self.serializer_class(reviews, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
