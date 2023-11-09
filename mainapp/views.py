from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import NewOrderForm, NewClientForm, ChangeClientForm, ChangeOrderForm

from .models import OrderPosition, Order, Client


@login_required
def order_positions_list(request):
    if request.method == "GET":
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


@login_required
def new_order(request):
    if request.method == "POST":

        form = NewOrderForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            order = Order.objects.create()

            client_name = form_data['client']
            try:
                existing_client = Client.objects.get(name=client_name)

                if existing_client.name == client_name:
                    order_position = OrderPosition.objects.create(
                        order_id=order.id,
                        client=existing_client,
                        product=form_data['product'],
                        quantity=form_data['quantity'],
                        status=form_data['status'],
                        description=form_data['description'],
                    )

                    order_position.save()

                    return JsonResponse({'new_order_id': order.id})

            except Exception:

                new_client = Client.objects.create(
                    name=form_data['client']
                )

                order_position = OrderPosition.objects.create(
                    order_id=order.id,
                    client=new_client,
                    product=form_data['product'],
                    quantity=form_data['quantity'],
                    status=form_data['status'],
                    description=form_data['description'],
                )

                order_position.save()

                return JsonResponse({'new_order_id': order.id})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        new_order_form = NewOrderForm()
        client_list = Client.objects.all()

        return render(request, "new_order.html", {
            'new_order_form': new_order_form,
            'client_list': client_list
        })


@login_required
def edit_order(request, id):
    if request.method == "POST":
        order = OrderPosition.objects.get(id__iexact=id)
        order_change_form = ChangeOrderForm(request.POST, instance=order)

        if order_change_form.is_valid():
            new_order = order_change_form.save()
            return JsonResponse({'new_order_id': new_order.id})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        order = OrderPosition.objects.get(id__iexact=id)
        edit_order_form = ChangeOrderForm(instance=order)

        return render(request, "order.html", {
            'edit_order_form': edit_order_form,
            'edit_order_id': order.id,
        })


@login_required
def delete_order(request, id):
    if request.method == "DELETE":
        order = get_object_or_404(OrderPosition, id__iexact=id)
        deleted_order_id = order.id
        order.delete()
        return JsonResponse({'deleted_order_id': deleted_order_id})


@login_required
def new_client(request):
    if request.method == "POST":
        form = NewClientForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            client_name = form_data['name']
            try:
                existing_client = Client.objects.get(name=client_name)

                if existing_client.name == client_name:
                    return HttpResponse('<div style="color: red">Такой клиент уже существует</div>')

            except Exception:

                client = Client.objects.create(
                    name=form_data['name'],
                    contact=form_data['contact'],
                    where_from=form_data['where_from'],
                    oder_details=form_data['oder_details'],
                    address=form_data['address'],
                    notes=form_data['notes'],
                )

                client.save()

                return JsonResponse({'new_client_name': client.name})

        else:
            return JsonResponse({'error': 'Server error'}, status=400)

    else:
        new_client_form = NewClientForm()

        return render(request, "new_client.html", {
            "new_client_form": new_client_form,
        })


@login_required
def client_list(request):
    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list
    })


@login_required
def edit_client(request, id):
    if request.method == "POST":
        client = Client.objects.get(id__iexact=id)
        client_change_form = ChangeClientForm(request.POST, instance=client)

        if client_change_form.is_valid():
            edited_client = client_change_form.save()
            return JsonResponse({'edited_client_name': edited_client.name})
        else:
            return JsonResponse({'error': 'Server error'}, status=400)
    else:
        client = Client.objects.get(id__iexact=id)
        edit_client_form = ChangeClientForm(instance=client)

        return render(request, "client.html", {
            "edit_client_form": edit_client_form,
            'edited_client_id': client.id,
            'edited_client_name': client.name,
        })


@login_required
def delete_client(request, id):
    if request.method == "DELETE":
        client = get_object_or_404(Client, id__iexact=id)
        deleted_client_id = client.id
        deleted_client_name = client.name
        client.delete()
        return JsonResponse({
            'deleted_client_name': deleted_client_name,
            'deleted_client_id': deleted_client_id,
        })


def check_username(request):
    client_name = request.POST.get('name')
    if Client.objects.filter(name=client_name).exists():
        return HttpResponse('<div style="color: red">такой пользователь уже есть</div>')
    else:
        return HttpResponse('<div style="color: green">имя свободно</div>')
