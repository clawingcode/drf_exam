from django.urls import path

from apps.reviews.views import ProductReviewsView, AddReviewView, ReviewsViewID

urlpatterns = [
    path("products/<slug:slug>", ProductReviewsView.as_view()),
    path("products/", AddReviewView.as_view()),
    path("<uuid:id>/", ReviewsViewID.as_view()),
]