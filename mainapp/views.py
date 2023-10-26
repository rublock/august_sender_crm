from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import NewOrderForm
from django.shortcuts import redirect

from .models import OrderPosition, Order


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

    if request.method == "GET":
        order = Order.objects.create()
        order_number = order.id

    if request.method == "POST":

        form = NewOrderForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            order_position = OrderPosition.objects.create(
                order_id=Order.objects.latest('id').id,
                client=form_data['client'],
                product=form_data['product'],
                quantity=form_data['quantity'],
                status=form_data['status'],
                description= form_data['description'],
                )
            
            order_position.save()

        return redirect('mainapp:home_page')
    else:

        new_order_form = NewOrderForm()

        return render(request, "new_order.html", {
            "new_order_form": new_order_form,
            "order_number": order_number,
            })