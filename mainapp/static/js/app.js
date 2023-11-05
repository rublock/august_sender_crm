let form = document.querySelector('.form')
form.addEventListener('htmx:afterRequest', function (event) {
  if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
    let data = JSON.parse(event.detail.xhr.responseText);
    alert(`Заказ ${data['new_order.id']} изменен`)
    window.location.href = '/';
  }
});

let orderDeleteButton = document.querySelector('.delete_order')
orderDeleteButton.addEventListener('htmx:afterRequest', function (event) {
  if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
    let data = JSON.parse(event.detail.xhr.responseText);
    alert(`Заказ ${data['deleted_order']} удален`)
    window.location.href = '/';
  }
});