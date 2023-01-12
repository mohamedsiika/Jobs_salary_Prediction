# Jobs_salary_Prediction
A web application that predicts the average salary for a job based on the job's url from Glassdoor.

## resources
- https://github.com/rohan-benjamin/Glassdoor-Scraper-Final/blob/main/glassdoor_scraper.ipynb
- https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
- https://youtu.be/MpF9HENQjDo

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python 3.6 or higher
Flask
pandas
numpy
joblib
requests
bs4
re
Selenium

#### Install the required packages:

```
pip install -r requirements.txt
```
#### Run the app:
```
python wsgi.py
```

## Project Structure
- **FlaskAPI**: contains the server-side code for the web application, including the app.py file that runs the application and the wsgi.py file that helps to serve the application using a WSGI server.
- **FlaskAPI/models**: contains the Random Regressor and One Hot Encoder models that are used to make predictions.
- **FlaskAPI/templates**: contains the HTML template files that are used to render the web page that the user interacts with.

- **Scraped_Data**: contains the 4 CSV files that were scraped from Glassdoor using Selenium and used to train the model.
- **Notebooks**: contains 4 Jupyter notebooks glassdoor_scraper.ipynb, Data_cleaning.ipynb, EDA.ipynb, Model.ipynb

### app.py 
This is the main file that runs the web application. It uses the Flask library to create a web application and define routes for handling HTTP requests. When the user submits a job url through the form on the web page, the application uses the `scrape_job.py` file to scrape job details from the web, and the `clean_data.py` file to clean the data and create the features that are used as input to the model. Then it loads the model using the `load_models()` function and makes a prediction of the average salary for the job. Finally, it renders the `result.html` template and returns the result of the prediction to the user.

### glassdoor_scraper.ipynb
This notebook is used to scrape job data from Glassdoor.com using Selenium and save it to the `Scraped_Data` directory.
### Data_cleaning.ipynb
This notebook is used to clean and preprocess the data from the `Scraped_Data` directory, and save it in `sala_data_cleaned.csv`.
### eda.ipynp
This notebook is used to explore and analyze the data, and gain insights into the data that can be used to inform the modeling process.during analysis I cleaned the data once more and saved it in `eda.csv`

