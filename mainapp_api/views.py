from rest_framework import generics
from mainapp.models import OrderPosition
from .serializers import OrderPositionSerializer

class OrderPositionList(generics.ListAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer
