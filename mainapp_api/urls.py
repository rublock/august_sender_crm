from django.urls import path
from .views import OrderPositionList

urlpatterns = [
    path("", OrderPositionList.as_view(), name="order_list"),
]