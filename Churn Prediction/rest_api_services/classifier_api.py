from flask import Flask, request
import pickle
import os
import numpy as np

# path = "C:/Users/duong/Desktop/MLOps Capstone Project/Churn Prediction/models/"
# os.startfile(path)

classifier = pickle.load(open('classifier.pickle', 'rb'))
scaler = pickle.load(open('sc.pickle', 'rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def prediction():
    request_data = request.get_json(force=True)
    total_visits = request_data['total_visits']
    average_time_spent = request_data['average_time_spent']

    prediction = classifier.predict(scaler.transform(np.array([[total_visits, average_time_spent]])))

    return "The prediction from GCP API is {}".format(prediction)

if __name__ == "__main__":
    app.run(port=8005, debug=True)
