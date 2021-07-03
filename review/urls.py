from django.urls import path
from . import views
urlpatterns = [
    path('',views.ReviewView.as_view()),
    path('thank_you',views.thank_you.as_view()),
    path('Review List',views.ReviewList.as_view(), name = 'review list'),
    path('favorite',views.AddfavoriteReview.as_view()),
    path('Detail Reviews<int:pk>',views.DetailReview.as_view(),name='Detail review')

]
