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
from flask import render_template

app = Flask("Flask project")

# ===============================================================

@app.route("/")
def page():
    return render_template("index.html")

# ===============================================================

if __name__ == "__main__":
    app.run(debug=True)
