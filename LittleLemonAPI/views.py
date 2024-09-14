from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
# View to handle GET (list) and POST (create) operations
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# View to handle GET (retrieve), PUT (update), and DELETE operations for a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'pk'  # Ensure this matches the primary key field (usually 'id')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def msg(request):
    return Response({"message": "This is a protected view"})