from flask import Flask,render_template, request
import pandas as pd


app = Flask(__name__)


@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("new.html")


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        file = request.form["upload-file"]
        data2 = pd.read_csv(file)
        return render_template("data.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
