document.addEventListener('htmx:afterSettle', function (event) {
  if (event.detail.xhr.status >= 200 && event.detail.xhr.status < 300) {
    let data = JSON.parse(event.detail.xhr.responseText);
    alert(`Заказ ${data['new_order.id']} изменен`)
    window.location.href = '/';
  }
});