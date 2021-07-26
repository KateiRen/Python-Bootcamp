from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/template")
def abcdefg():
    items = ["Apfel", "Banane", "Citrusfrucht"]
    return render_template("index.html", name = "Max Mustermann", items = items)