from flask import Flask, render_template, request, json
import os
import urllib.request

app = Flask(__name__)

with urllib.request.urlopen("https//apis.is/currency/arion") as url:
    data = json.loads(url.read().decode())

@app.route("/")
def home():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()