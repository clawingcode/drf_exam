from django.urls import path

from apps.reviews.views import ProductReviewsView


urlpatterns = [
    path("products/<slug:slug>", ProductReviewsView.as_view()),
]