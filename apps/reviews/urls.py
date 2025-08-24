from django.urls import path

from apps.reviews.views import ProductReviewsView, AddReviewView, ReviewsViewID, UserReviewsView

urlpatterns = [
    path("products/<slug:slug>", ProductReviewsView.as_view()),
    path("products/", AddReviewView.as_view()),
    path("<uuid:id>/", ReviewsViewID.as_view()),
    path("users/", UserReviewsView.as_view()), # не думаю, что это самое удачное название маршрута
]