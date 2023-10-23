from rest_framework import generics
from mainapp.models import OrderPosition, Client
from .serializers import OrderPositionSerializer, ClientPositionSerializer

class OrderPositionAPI(generics.ListAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer

class ClientPositionAPI(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientPositionSerializer
