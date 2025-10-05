from django.shortcuts import render
# booking/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Movie, Show, Booking
from .serializers import UserSerializer, MovieSerializer, ShowSerializer, BookingSerializer

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(User, username=username)
        if not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class ShowsByMovieView(generics.ListAPIView):
    serializer_class = ShowSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Show.objects.filter(movie_id=movie_id)

class BookSeatView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, show_id):
        user = request.user
        show = get_object_or_404(Show, id=show_id)
        seat_number = request.data.get('seat_number')
        if seat_number is None:
            return Response({'detail': 'seat_number is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            seat_number = int(seat_number)
        except ValueError:
            return Response({'detail': 'seat_number must be an integer'}, status=status.HTTP_400_BAD_REQUEST)
        if seat_number < 1 or seat_number > show.total_seats:
            return Response({'detail': 'seat_number out of range'}, status=status.HTTP_400_BAD_REQUEST)
        booked_seats_count = Booking.objects.filter(show=show, status='booked').count()
        if booked_seats_count >= show.total_seats:
            return Response({'detail': 'Show is fully booked'}, status=status.HTTP_400_BAD_REQUEST)
        existing_booking = Booking.objects.filter(show=show, seat_number=seat_number, status='booked').first()
        if existing_booking:
            return Response({'detail': 'This seat is already booked'}, status=status.HTTP_400_BAD_REQUEST)
        booking = Booking.objects.create(user=user, show=show, seat_number=seat_number, status='booked')
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user != request.user:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        if booking.status == 'cancelled':
            return Response({'detail': 'Booking already cancelled'}, status=status.HTTP_400_BAD_REQUEST)
        booking.status = 'cancelled'
        booking.save()
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# Create your views here.
