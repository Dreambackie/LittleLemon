from django.shortcuts import render
from rest_framework import generics, viewsets 
from .models import Menu, Booking
from .serializers import Menuserializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer    

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 