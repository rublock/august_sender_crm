console.log('welcome to august_sender_crm')

let xhr = new XMLHttpRequest();

xhr.open('GET', 'http://127.0.0.1:8000/api/', true);

xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 300) {
        let responseData = JSON.parse(xhr.responseText);
        console.log(responseData);
    } else {
        console.error(xhr.statusText);
    }
};

xhr.onerror = function() {
    console.error('Произошла сетевая ошибка');
};

xhr.send();

