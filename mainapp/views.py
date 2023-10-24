from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import OrderPosition


@require_http_methods(['GET'])
def order_positions_list(request):
    order_positions_list = OrderPosition.objects.all()
    return render(request, 'home_page.html', {'order_positions_list': order_positions_list})