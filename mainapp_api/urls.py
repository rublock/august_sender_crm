from django.urls import path
from .views import OrderPositionAPI, ClientAPI

urlpatterns = [
    path("orders/", OrderPositionAPI.as_view(), name="orders"),
    path("clients/", ClientAPI.as_view(), name="clients"),
]