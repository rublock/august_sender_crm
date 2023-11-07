from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from mainapp.models import OrderPosition, Client
from .serializers import OrderPositionSerializer, ClientSerializer


class OrderPositionAPI(generics.ListAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer

    permission_classes = [IsAuthenticated]


class ClientAPI(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated]
