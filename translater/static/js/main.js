var btn_add = document.querySelector(".add_new_word");
var btn_add2 = document.querySelector(".add");

var main_window = document.querySelector("#main_window");
var additional_window = document.querySelector("#additional_window");

// Задержка ответа
setTimeout(function () {
    var answer_from_DB = document.querySelector(".answer_from_DB").innerHTML = "";
}, 2000);

additional_window.style.display = "none";

// Кнопка добавить новое слово
btn_add.onclick = function () {
    main_window.style.display = "none";
    additional_window.style.display = "block";
};

// Доп. Окно добавить
btn_add2.onclick = function () {
    main_window.style.display = "block";
    additional_window.style.display = "none";
};