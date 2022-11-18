from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("yadd.db")
cursor = connection.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/art.html")
def art():
    return render_template("art.html")


@app.route("/history.html")
def history():
    return render_template("history.html")


@app.route("/albums.html")
def albums():
    return render_template("albums.html")


@app.route("/yadd.html")
def yadd():
    return render_template("yadd.html")


if __name__ == '__main__':  # Runs on execution
    app.run()  # Creates site
