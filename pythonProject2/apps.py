from flask import Flask,render_template, request, redirect , url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

def create_app():
    app = Flask(__name__)
    @app.route("/upload", methods= ['GET','POST'])

    def upload():
        if request.method =='POST':
            return render_template("index.html")


@app.route("/home")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
