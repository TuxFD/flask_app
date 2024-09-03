"""
app.py: Это основной файл вашего приложения, где вы определяете маршруты, представления и бизнес-логику. В этом файле вы создаете экземпляр приложения Flask и запускаете сервер.

/templates: Это директория, в которой хранятся все HTML-шаблоны. Flask автоматически ищет шаблоны в папке с именем templates. Примеры шаблонов могут включать hello.html, index.html, about.html и так далее.

/static: Эта папка используется для хранения статических файлов, таких как CSS-стили, JavaScript-скрипты, изображения и другие файлы, которые не изменяются в процессе работы приложения. Flask автоматически обрабатывает запросы к этим файлам.
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from mysrc.config import db_name

# ================================================================
"""
Интеграция с базами данных

Flask поддерживает SQL и NoSQL. Для простых приложений популярным выбором является SQLite из-за его легкости и неприхотливости в настройке.
SQLAlchemy - это ORM (Object-Relational Mapping) библиотека для Python, которая облегчает работу с базами данных SQL. В Flask ее можно использовать для упрощения операций с базой данных.
Пример подключения к базе данных с использованием SQLAlchemy:
"""

app = Flask("Flask_project")
# local DB connect
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///[{db_name}]"
db = SQLAlchemy(app)

"""
Создание БД моделей

Модели в SQLAlchemy представляют таблицы баз данных. Они позволяют взаимодействовать с данными на более высоком уровне абстракции.
Пример создания модели:
"""


class User(db.Model):
    """TODO: вынести этот блок как в MVC?"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


"""
Операции CRUD

CRUD означает Создание (Create), Чтение (Read), Обновление (Update), Удаление (Delete). SQLAlchemy упрощает выполнение этих операций.
Пример создания нового пользователя:
"""
# line 59 -- RuntimeError: Working outside of application context.
# TODO: SQLAlchemy app без Flask
# new_user = User(username="Tester", email="test@test.to")
# db.session.add(new_user)
# db.session.commit()

"""
Пример чтения пользователя:
"""
# line 65 -- RuntimeError: Working outside of application context.
# User.query.filter_by(username="newuser").first()

"""
Миграции

Для управления изменениями в структуре базы данных можно использовать расширение Flask-Migrate. Оно облегчает процесс создания и применения миграций.
"""


# ================================================================


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about")
def about():
    return "This is the about page"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"Hello, user {username}"


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


"""
Работа с данными в Flask

Flask обеспечивает простой способ обработки входящих запросов, будь то GET или POST запросы. Это делается через маршрутизацию и функции представлений.
Пример обработки GET запроса:
"""


@app.route("/greet/<name>", methods=["GET"])
def greet(name):
    return f"Hello, {name}!"


"""
В этом примере, Flask обрабатывает запрос к URL /greet/<name> и возвращает приветствие с именем пользователя.
Пример обработки POST запроса:
"""


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return f"Hello, {name}"


"""
Работа с формами

Для работы с формами в Flask часто используется объект request, который позволяет получить доступ к данным, отправленным пользователем.
Пример HTML-формы:

Эта форма отправляет данные на маршрут /submit, который мы обрабатываем в нашем Flask приложении.
"""


@app.route("/form")
def form():
    return render_template("form.html")
    # return f"Hello, {name}"


"""
Отправка данных

Flask позволяет не только принимать данные, но и отправлять их обратно пользователю. Это может быть в виде HTML, JSON, XML и других форматов.
Пример отправки JSON:
"""


@app.route("/data")
def data():
    return jsonify({"key": "value"})


if __name__ == "__main__":
    app.run(debug=True)
