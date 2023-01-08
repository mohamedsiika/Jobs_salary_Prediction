import flask
from flask import Flask, jsonify, request
import pickle as pkl
from scrape_job import scraping
import numpy as np
import json

def load_models():
    file_name="FlaskAPI/models/Model_file.p"
    with open(file_name,'rb') as pickled:
        model=pkl.load(pickled)
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    request_json=request.get_json()
    x=request_json['input']
    scraping_obj=scraping(x)
    job_detail=scraping.scrape_one_job()
    

    #import model
    model = load_models()
    prediction=model.predict(x_in)[0]
    response=json.dumps({"response":prediction})
    return (response,200)

if __name__ == '__main__':
    app.run(debug=True)