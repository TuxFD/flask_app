"""
App:
    app.py
    /templates
        *.html
    /static
        *.css
        *.js
        *.img
        *.other
    /mysrc
        config.py

"""

from flask import Flask

app = Flask("Flask project")


if __name__ == "__main__":
    app.run(debug=True)
