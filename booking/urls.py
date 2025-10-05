# booking/urls.py
from django.urls import path
from .views import SignupView, LoginView, MovieListView, ShowsByMovieView, BookSeatView, CancelBookingView, MyBookingsView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:movie_id>/shows/', ShowsByMovieView.as_view()),
    path('shows/<int:show_id>/book/', BookSeatView.as_view()),
    path('bookings/<int:booking_id>/cancel/', CancelBookingView.as_view()),
    path('my-bookings/', MyBookingsView.as_view()),
]
