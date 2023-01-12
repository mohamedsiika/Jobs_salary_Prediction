import flask
from flask import Flask, jsonify, request,render_template
import pickle as pkl
from scrape_job import scraping
from clean_data import Data_cleaning
import json

def load_models():
    file_name="FlaskAPI/models/Model_file.p"
    with open(file_name,'rb') as pickled:
        model=pkl.load(pickled)
    return model

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['job']
    
    scraping_obj=scraping(url)
    job_detail=scraping_obj.scrape_one_job()

    pipeline_obj=Data_cleaning(job_detail)
    features=pipeline_obj.pipeline()
    
    #import model
    model = load_models()
    prediction=model.predict(features)[0]
    response=json.dumps({"response":prediction})
    return render_template('result.html', salary=prediction)

if __name__ == '__main__':
    app.run(debug=True)