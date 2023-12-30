# Homework_1

## Task_1

* Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
* Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
* Данные о новостях должны быть переданы в шаблон через
контекст.

Решение: ***[>> Код <<](homework/h_1/task_01.py)*** ***[>> HTML <<](homework/1/templates/task_01.html)***

## Task_2

* Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние 
шаблоны для страниц категорий товаров и отдельных товаров. 
* Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

Решение: 
* ***[>> Код <<](homework/h_1/task_02.py)*** 
* ***[>> HTML шаблон<<](homework/h_1/templates/task_02_index.html)***
* ***[>> HTML одежда<<](homework/h_1/templates/task_02_cloth.html)***
* ***[>> HTML обувь<<](homework/h_1/templates/task_02_shoes.html)***
* ***[>> HTML куртка<<](homework/h_1/templates/task_02_jacket.html)***

# Homework_2

## Task_6

* Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
* При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на страницу с 
ошибкой в случае некорректного возраста

Решение: 
* ***[>> Код <<](homework/h_2/task_06.py)*** 
* ***[>> HTML форма запроса<<](homework/h_2/templates/task_06_form.html)***
* ***[>> HTML возраст > 18<<](homework/h_2/templates/age_big.html)***
* ***[>> HTML возраст < 18<<](homework/h_2/templates/age_small.html)***

## Task_7

* Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
* При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число 
и его квадрат.

Решение: 
* ***[>> Код <<](homework/h_2/task_07.py)*** 
* ***[>> HTML форма запроса<<](homework/h_2/templates/task_07_form.html)***
* ***[>> HTML результат<<](homework/h_2/templates/task_07_result.html)***

# Homework_3

## Task_3

* Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
* База данных должна содержать две таблицы: "Студенты" и "Оценки".
* В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
* В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
* Необходимо создать связь между таблицами "Студенты" и "Оценки".
* Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

Решение: 
* ***[>> Код <<](homework/h_3/task_3.py)*** 
* ***[>> Модуль <<](homework/h_3/models_3.py)***
* ***[>> HTML <<](homework/h_3/templates/task_3_index.html)***

# Homework_4

## Task_7

* Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.

        Пример массива: 
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]   

* Массив должен быть заполнен случайными целыми числами от 1 до 100.   
* При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.   
* В каждом решении нужно вывести время выполнения вычислений.

Решение: 
* ***[>> Код <<](homework/h_4/task_7.py)*** 