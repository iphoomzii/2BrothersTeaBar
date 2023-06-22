from flask import Flask, redirect, url_for, render_template
from datetime import timedelta

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/content")
def contentPage():
    return render_template("content.html")

@app.route("/menu")
def menuPage():
    return render_template("content-menu.html")

@app.route("/event")
def eventPage():
    return render_template("content-event.html")

@app.route("/order")
def orderPage():
    return render_template("content-order.html")

@app.route("/store")
def storePage():
    return render_template("content-store.html")