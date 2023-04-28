from flask import Flask, jsonify, request
from joblib import load
import numpy as np

model = load('model/model.joblib')

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.json
    features = np.array([[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]])
    prediction = model.predict(features)
    prediction_str = str(prediction[0])
    return jsonify({'prediction':prediction_str})

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = 5000)