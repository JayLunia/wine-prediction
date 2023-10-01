from flask import Flask , render_template,request , jsonify
import numpy as np
import pickle
app = Flask(__name__)

cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
model= pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html',title='House Price Predictor', cols = cols)

@app.route("/pred",methods=['POST'])
def pred():
    if request.method == 'POST':
        input = []
        for i in cols:
            input.append(request.form.get(i))
        input = np.array(input).reshape(1,-1)
        output=model.predict(input)
        return jsonify(str(output[0]))


if __name__=="__main__":
    app.run()