from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.order_positions_list, name="home_page"),
    path("new_order/", views.new_order, name="new_order"),
    path("send/", views.send_orders, name="send_orders"),
    path("new_client/", views.new_client, name="new_client"),
    path("clients/", views.client_list, name="client_list"),
    path("client/<int:id>", views.edit_client, name="edit_client"),
    path("order/<int:id>", views.edit_order, name="edit_order"),
    path("delete_order/<int:id>", views.delete_order, name="delete_order"),
    path("delete_client/<int:id>", views.delete_client, name="delete_client"),
]

htmx_urlpatterns = [
    path("check_username/", views.check_username, name="check_username"),
]

urlpatterns += htmx_urlpatterns
