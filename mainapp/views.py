from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import NewOrderForm
from django.http import HttpResponse

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


def new_order(request):
    if request.method == "POST":
        client = request.POST.get("client")
        product = request.POST.get("product")
        quantity = request.POST.get("quantity")
        description = request.POST.get("description")
        status = request.POST.get("status")
        new_order_form = NewOrderForm()
        print(client, product, quantity, description, status)
        return render(request, "new_order.html", {"new_order_form": new_order_form})
    else:
        new_order_form = NewOrderForm()
        return render(request, "new_order.html", {"new_order_form": new_order_form})