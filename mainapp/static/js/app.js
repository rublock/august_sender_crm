console.log('welcome to august_sender_crm')

var url = window.location.href;
var id = url.split("/").reverse()[0];

let form = document.querySelector('.form')

form.addEventListener('submit', function (e) {
    e.preventDefault();

    let formData = new FormData(form);
    let xhr = new XMLHttpRequest();

    if (form.classList[1] == 'new_order') {
        xhr.open('POST', 'http://127.0.0.1:8000/new_order/', true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                let response = JSON.parse(xhr.responseText);
                alert(`Заказ #${response["order.id"]} создан`);
                window.location.href = "/";
            } else {
                console.log('Ошибка: ' + xhr.status);
            }
        };

        xhr.onerror = function () {
            console.log('Произошла ошибка сети');
        };

        xhr.send(formData);

    } else if (form.classList[1] == 'new_client') {
        xhr.open('POST', 'http://127.0.0.1:8000/new_client/', true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                let response = JSON.parse(xhr.responseText);
                alert(`${response["client.name"]} создан`);
                window.location.href = "/";
            } else {
                console.log('Ошибка: ' + xhr.status);
            }
        };
       xhr.onerror = function () {
            console.log('Произошла ошибка сети');
       };

       xhr.send(formData);

    } else if (form.classList[1] == 'edit_client') {
        xhr.open('POST', 'http://127.0.0.1:8000/client/' + id, true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                let response = JSON.parse(xhr.responseText);
                alert(`${response["new_client.name"]} изменен`);
                window.location.href = "/clients/";
            } else {
                console.log('Ошибка: ' + xhr.status);
            }
        };
       xhr.onerror = function () {
            console.log('Произошла ошибка сети');
       };

       xhr.send(formData);

    } else if (form.classList[1] == 'edit_order') {
        xhr.open('POST', 'http://127.0.0.1:8000/order/' + id, true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                let response = JSON.parse(xhr.responseText);
                alert(`Заказ ${response["new_order.id"]} изменен`);
                window.location.href = "/";
            } else {
                console.log('Ошибка: ' + xhr.status);
            }
        };
       xhr.onerror = function () {
            console.log('Произошла ошибка сети');
       };

       xhr.send(formData);

    }

});
