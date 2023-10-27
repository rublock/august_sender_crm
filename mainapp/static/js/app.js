console.log('welcome to august_sender_crm')

document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('new_order_form');

    form.addEventListener('submit', function (e) {
        e.preventDefault();  // Предотвращаем стандартное действие формы

        // Собираем данные из формы
        var formData = new FormData(form);

        // Создаем и настраиваем объект для AJAX-запроса
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://127.0.0.1:8000/order/', true);

        // Определяем обработчик успешного ответа
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                // Обработка успешного ответа от сервера
                var response = JSON.parse(xhr.responseText);
                alert(`Заказ #${response["order.id"]} создан`);
                window.location.href = "/";
            } else {
                // Обработка ошибки
                console.log('Ошибка: ' + xhr.status);
            }
        };

        // Определяем обработчик ошибки
        xhr.onerror = function () {
            console.log('Произошла ошибка сети');
        };

        // Отправляем данные на сервер
        xhr.send(formData);
    });
});