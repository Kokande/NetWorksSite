from flask import Flask, render_template, redirect

"""
from flask_ngrok import run_with_ngrok

run_with_ngrok(app)
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'notsosecretkey'


@app.route("/", methods=['GET'])
def index():
    return render_template("main.html", title="Welcome! | NetWorks")


@app.route("/model1", methods=['GET'])
def model1():
    return render_template("model1.html", title="Wider Model | NetWorks")


@app.route("/model2", methods=['GET'])
def model2():
    return render_template("model2.html", title="Model 2 | NetWorks")


@app.route("/model3", methods=['GET'])
def model3():
    return render_template("model3.html", title="Model 3 | NetWorks")


@app.route("/main_model", methods=['GET'])
def main_model():
    return render_template("main_model.html", title="Main Model | NetWorks")


@app.route("/models", methods=['GET'])
def models():
    return render_template("main.html", title="Models | NetWorks")


@app.route("/contacts", methods=['GET'])
def contacts():
    return render_template("contacts.html", title="Contacts | NetWorks")


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html", title="About | NetWorks")


if __name__ == '__main__':
    app.run()
