from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Ticket Booking API",
        default_version='v1',
        description="API documentation for Movie Ticket Booking System",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('booking.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),  # <--- name='swagger'
    path('', lambda request: redirect('swagger')),  # redirect root to swagger by name
]
