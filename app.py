"""
app.py: Это основной файл вашего приложения, где вы определяете маршруты, представления и бизнес-логику. В этом файле вы создаете экземпляр приложения Flask и запускаете сервер.

/templates: Это директория, в которой хранятся все HTML-шаблоны. Flask автоматически ищет шаблоны в папке с именем templates. Примеры шаблонов могут включать hello.html, index.html, about.html и так далее.

/static: Эта папка используется для хранения статических файлов, таких как CSS-стили, JavaScript-скрипты, изображения и другие файлы, которые не изменяются в процессе работы приложения. Flask автоматически обрабатывает запросы к этим файлам.
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

app = Flask("Flask_project")


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
