from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.order_positions_list, name="home_page"),
    path("order/", views.new_order, name="new_order"),
]