from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# Helper functions to get tables from database.
def get_albums():
    conn = sqlite3.connect("yadd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM albums")
    results = cursor.fetchall()
    conn.close()
    return results


def get_songs():
    conn = sqlite3.connect("yadd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs")
    results = cursor.fetchall()
    conn.close()
    return results


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
    std_albums = get_albums()
    songs = get_songs()
    print(std_albums, songs)
    return render_template("yadd.html", albums=std_albums, songs=songs)


if __name__ == '__main__':  # Runs on execution
    app.run()  # Creates site

