let form = document.querySelector('.form')
let deleteButton = document.querySelector('.delete')

form.addEventListener('htmx:afterRequest', function (event) {
    if (form.classList[1] == 'new_order') {
        if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
            let data = JSON.parse(event.detail.xhr.responseText);
            alert(`Заказ ${data['new_order_id']} создан`)
            window.location.href = '/';
        }
    } else if (form.classList[1] == 'edit_order') {
        if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
            let data = JSON.parse(event.detail.xhr.responseText);
            alert(`Заказ ${data['new_order_id']} изменен`)
            window.location.href = '/';
        }
    } else if (form.classList[1] == 'new_client') {
        if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
            let data = JSON.parse(event.detail.xhr.responseText);
            alert(`Клиент ${data['new_client_name']} создан`)
            window.location.href = '/clients/';
        }
    } else if (form.classList[1] == 'edit_client') {
        if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
            let data = JSON.parse(event.detail.xhr.responseText);
            alert(`Клиент ${data['edited_client_name']} изменен`)
            window.location.href = '/clients/';
        }
    }
});

deleteButton.addEventListener('htmx:afterRequest', function (event) {
    if (deleteButton.classList[3] == 'order_delete') {
      if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
        let data = JSON.parse(event.detail.xhr.responseText);
        alert(`Заказ ${data['deleted_order_id']} удален`)
        window.location.href = '/';
      }
    } else if (deleteButton.classList[3] == 'client_delete') {
      if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
        let data = JSON.parse(event.detail.xhr.responseText);
        alert(`Клиент ${data['deleted_client_name']} удален`)
        window.location.href = '/';
      }
    }
});