from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_403_FORBIDDEN, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from apps.reviews.serializers import ReviewSerializer, AddReviewSerializer
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


class AddReviewView(APIView):

    serializer_class = ReviewSerializer

    @extend_schema(
        summary="Add Product Review",
        description="""
                This endpoint allows a user to publish review for a product.
            """,
        tags=tags,
        request=AddReviewSerializer,
        responses=AddReviewSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = AddReviewSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            data = serializer.validated_data
            product_slug = data.pop("product_slug", None)
            product = Product.objects.get_or_none(slug=product_slug)
            if not product:
                return Response(data={"message": "Product does not exist!"}, status=HTTP_404_NOT_FOUND)
            if Review.objects.get_or_none(user=user, product=product):
                return Response(data={"message": "Your review for this product has already been published!"}, status=HTTP_403_FORBIDDEN)
            data["user"] = user
            data["product"] = product
            new_review = Review.objects.create(**data)
            serializer = self.serializer_class(new_review)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ReviewsViewID(APIView):
    serializer_class = ReviewSerializer

    @extend_schema(
        summary="Review Fetch ID",
        description="""
                    This endpoint returns a user's review for the product.
                """,
        tags=tags,
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        review = Review.objects.get_or_none(user=user, id=kwargs["id"])
        if not review:
            return Response(data={"message": "Review does not exist!"}, status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(review)
        return Response(data=serializer.data)
