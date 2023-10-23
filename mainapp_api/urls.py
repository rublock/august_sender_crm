from django.urls import path
from .views import OrderPositionAPI, ClientPositionAPI

urlpatterns = [
    path("orders/", OrderPositionAPI.as_view(), name="orders"),
    path("clients/", ClientPositionAPI.as_view(), name="clients"),
]