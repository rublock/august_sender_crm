from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import OrderPosition


@require_http_methods(['GET'])
def order_positions_list(request):
    order_positions_list_status_1 = OrderPosition.objects.filter(status=1)
    order_positions_list_status_2 = OrderPosition.objects.filter(status=2)
    order_positions_list_status_3 = OrderPosition.objects.filter(status=3)
    order_positions_list_status_4 = OrderPosition.objects.filter(status=4)

    return render(request, 'home_page.html', {
        'order_positions_list_status_1': order_positions_list_status_1,
        'order_positions_list_status_2': order_positions_list_status_2,
        'order_positions_list_status_3': order_positions_list_status_3,
        'order_positions_list_status_4': order_positions_list_status_4,
        })