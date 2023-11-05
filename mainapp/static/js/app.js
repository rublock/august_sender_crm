var url = window.location.href;
var id = url.split("/").reverse()[0];

let form = document.querySelector('.form')
let del = document.querySelector('.delete');

del.addEventListener('click', function (e) {
    console.log('del')
    var csrftoken = getCookie('csrftoken');
    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:8000/order/' + id, true);
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.send('del')


    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length === 2) {
          return parts.pop().split(";").shift();
        }
    }
})


form.addEventListener('submit', function (e) {
    e.preventDefault();

    let formData = new FormData(form);
    let xhr = new XMLHttpRequest();

    xhr.open("POST", 'http://127.0.0.1:8000/order/' + id, true);
    xhr.send(formData)

    xhr.onreadystatechange = function () {
       if (this.readyState == 4 && this.status == 200) {
          console.log(this.responseText);
       }
    }
})



//console.log('welcome to august_sender_crm')
//
//var url = window.location.href;
//var id = url.split("/").reverse()[0];
//
//let form = document.querySelector('.form')
//
//form.addEventListener('submit', function (e) {
//    e.preventDefault();
//
//    let formData = new FormData(form);
//    let xhr = new XMLHttpRequest();
//
//    if (form.classList[1] == 'new_order') {
//        xhr.open('POST', 'http://127.0.0.1:8000/new_order/', true);
//
//        xhr.onload = function () {
//            if (xhr.status >= 200 && xhr.status < 300) {
//                let response = JSON.parse(xhr.responseText);
//                alert(`Заказ #${response["order.id"]} создан`);
//                window.location.href = "/";
//            } else {
//                console.log('Ошибка: ' + xhr.status);
//            }
//        };
//
//        xhr.onerror = function () {
//            console.log('Произошла ошибка сети');
//        };
//
//        xhr.send(formData);
//
//    } else if (form.classList[1] == 'new_client') {
//        xhr.open('POST', 'http://127.0.0.1:8000/new_client/', true);
//
//        xhr.onload = function () {
//            if (xhr.status >= 200 && xhr.status < 300) {
//                let response = JSON.parse(xhr.responseText);
//                alert(`${response["client.name"]} создан`);
//                window.location.href = "/";
//            } else {
//                console.log('Ошибка: ' + xhr.status);
//            }
//        };
//       xhr.onerror = function () {
//            console.log('Произошла ошибка сети');
//       };
//
//       xhr.send(formData);
//
//    } else if (form.classList[1] == 'edit_client') {
//        xhr.open('POST', 'http://127.0.0.1:8000/client/' + id, true);
//
//        xhr.onload = function () {
//            if (xhr.status >= 200 && xhr.status < 300) {
//                let response = JSON.parse(xhr.responseText);
//                alert(`${response["new_client.name"]} изменен`);
//                window.location.href = "/clients/";
//            } else {
//                console.log('Ошибка: ' + xhr.status);
//            }
//        };
//       xhr.onerror = function () {
//            console.log('Произошла ошибка сети');
//       };
//
//       xhr.send(formData);
//
//    } else if (form.classList[1] == 'edit_order') {
//        xhr.open('POST', 'http://127.0.0.1:8000/order/' + id, true);
//
//        xhr.onload = function () {
//            if (xhr.status >= 200 && xhr.status < 300) {
//                let response = JSON.parse(xhr.responseText);
//                alert(`Заказ ${response["new_order.id"]} изменен`);
//                window.location.href = "/";
//            } else {
//                console.log('Ошибка: ' + xhr.status);
//            }
//        };
//       xhr.onerror = function () {
//            console.log('Произошла ошибка сети');
//       };
//
//       xhr.send(formData);
//
//    }
//
//});
