from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Listing model
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Booking model
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
