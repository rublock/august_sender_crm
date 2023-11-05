from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import NewOrderForm, NewClientForm, ChangeClientForm, ChangeOrderForm

from .models import OrderPosition, Order, Client


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

        form = NewOrderForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            order = Order.objects.create()

            order_position = OrderPosition.objects.create(
                order_id=order.id,
                client=form_data['client'],
                product=form_data['product'],
                quantity=form_data['quantity'],
                status=form_data['status'],
                description=form_data['description'],
            )

            order_position.save()

            return JsonResponse({'order.id': order.id})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        new_order_form = NewOrderForm()

        return render(request, "new_order.html", {
            "new_order_form": new_order_form,
        })


def edit_order(request, id):
    if request.method == "POST":
        order = OrderPosition.objects.get(id__iexact=id)
        order_change_form = ChangeOrderForm(request.POST, instance=order)

        if order_change_form.is_valid():
            new_order = order_change_form.save()
            return JsonResponse({'new_order.id': new_order.id})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        order = OrderPosition.objects.get(id__iexact=id)
        order_change_form = ChangeOrderForm(instance=order)

        return render(request, "order.html", {
            'order_change_form': order_change_form,
            'deleted_order': order.id,
        })


def delete_order(request, id):
    if request.method == "DELETE":
        order = get_object_or_404(OrderPosition, id__iexact=id)
        deleted_order = order.id
        order.delete()
        return JsonResponse({'deleted_order': deleted_order})

def new_client(request):
    if request.method == "POST":

        form = NewClientForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            client = Client.objects.create(
                name=form_data['name'],
                contact=form_data['contact'],
                where_from=form_data['where_from'],
                oder_details=form_data['oder_details'],
                address=form_data['address'],
                notes=form_data['notes'],
            )

            client.save()

            return JsonResponse({'client.name': client.name})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        new_client_form = NewClientForm()

        return render(request, "new_client.html", {
            "new_client_form": new_client_form,
        })


def client_list(request):
    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list
    })


def edit_client(request, id):
    if request.method == "POST":
        client = Client.objects.get(id__iexact=id)
        client_change_form = ChangeClientForm(request.POST, instance=client)

        if client_change_form.is_valid():
            new_client = client_change_form.save()
            return JsonResponse({'new_client.name': new_client.name})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        client = Client.objects.get(id__iexact=id)
        client_change_form = ChangeClientForm(instance=client)

        return render(request, "client.html", {
            "client_change_form": client_change_form,
        })
