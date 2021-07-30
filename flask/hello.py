from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    args = request.args
    name = args.get("name")
    age = args.get("age")
    return render_template("test.html", name = name, age = age)

@app.route("/template")
def abcdefg():
    items = ["Apfel", "Banane", "Citrusfrucht"]
    return render_template("index.html", name = "Max Mustermann", items = items)