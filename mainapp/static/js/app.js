console.log('welcome to august_sender_crm')

let form = document.querySelector('.form')

form.addEventListener('submit', function (e) {
    e.preventDefault();

    let formData = new FormData(form);
    let xhr = new XMLHttpRequest();

    if (form.classList[1] == 'order') {
        xhr.open('POST', 'http://127.0.0.1:8000/order/', true);

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

    } else if (form.classList[1] == 'client') {
        xhr.open('POST', 'http://127.0.0.1:8000/client/', true);

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                let response = JSON.parse(xhr.responseText);
                alert(`${response["name"]} создан`);
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
