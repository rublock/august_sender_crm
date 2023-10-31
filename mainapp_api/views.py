from rest_framework import generics
from mainapp.models import OrderPosition, Client
from .serializers import OrderPositionSerializer, ClientSerializer

class OrderPositionAPI(generics.ListAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer

class ClientAPI(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
