from flask import Flask, render_template
from flask import request
import pickle
import model

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('abc.html')

@app.route('/predict/', methods=['POST'])
def predict():
    global model
    Density = float(request.form["Density"])
    CO = float(request.form["Cohesion"])
    FA = float(request.form["Friction_Angle"])
    ODH = float(request.form["Overall_Dump_Height"])
    DAS = float(request.form["Dump_Angle"])
    prediction = model.predict([[Density, CO, FA, ODH, DAS]])
    FOS = round(prediction[0], 2)
    models = pickle.load(open('model.pkl', 'rb'))
    return render_template('abc.html', FOS_value=f"The FOS value generated is {FOS}")



if __name__ == '__main__':
    app.run(debug=True)
