## [Junior-] Задание 1.<br/>

# 1. Написать скрипт на Python, который создаст (прямые запросы на SQL или ORM) таблицы и установит связи между ними для базы данных «Библиотека».
# **Требование: в задаче следует работать с СУБД PostgreSQL, а не с SQLite.**
# Структура таблиц:
# Таблица authors (Авторы). Хранит информацию о писателях.
#     id: INTEGER, первичный ключ (PRIMARY KEY), автоинкремент.
#     name: VARCHAR(255), имя автора, обязательно для заполнения (NOT NULL).
#     biography: TEXT, краткое описание.
#
# CREATE TABLE authors (
#     id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     biography TEXT
# )
# Таблица books (Книги). Хранит данные о книгах и ссылается на автора.
#     id: INTEGER, первичный ключ, автоинкремент.
#     title: VARCHAR(255), название книги (NOT NULL).
#     author_id: INTEGER, внешний ключ (FOREIGN KEY), указывает на authors(id).
#     published_year: INTEGER, год издания.
#     isbn: VARCHAR(13), уникальный международный номер (UNIQUE).
#
# CREATE TABLE books (
#     id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     author_id INTEGER REFERENCES authors(id) NOT NULL,
#     published_year INTEGER,
#     isbn VARCHAR(13) UNIQUE
# )
# Таблица users (Читатели). Хранит данные пользователей библиотеки.
#     id: INTEGER, первичный ключ, автоинкремент.
#     full_name: VARCHAR(255), ФИО (NOT NULL).
#     email: VARCHAR(254), электронная почта (UNIQUE).
#
# CREATE TABLE users (
#     id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     full_name VARCHAR(255) NOT NULL,
#     email VARCHAR(254) UNIQUE
# )
# Таблица loans (Выдача книг). Связующая таблица для фиксации того, кто и какую книгу взял.
#     book_id: INTEGER, внешний ключ к books(id), входит в состав первичного ключа loans.
#     user_id: INTEGER, внешний ключ к users(id), входит в состав первичного ключа loans.
#     loan_date: DATE, дата выдачи (по умолчанию текущая), входит в состав первичного ключа loans.
#     return_date: DATE, дата возврата (может быть пустой, если книга ещё у читателя).
#
# CREATE TABLE loans (
#     book_id INTEGER REFERENCES books(id),
#     user_id INTEGER REFERENCES users(id),
#     loan_date DATE, ???(по умолчанию текущая)
#     return_date DATE,
#     CONSTRAINT loans PRIMARY KEY (book_id, user_id, loan_date)
# )
# 2. Написать (или дополнить существующий) скрипт на Python для получения данных из БД «Библиотека»:
# Вывести названия всех книг, изданных после 2010 года.
# <li>Вывести список всех книг вместе с именами их авторов.</li>
# <li>Найти всех пользователей, чья электронная почта заканчивается на @gmail.com.</li>
# <li>Посчитать общее количество книг у каждого автора в базе.</li>
# <li>Вывести имена читателей и названия книг, которые они взяли, но еще не вернули.</li>
