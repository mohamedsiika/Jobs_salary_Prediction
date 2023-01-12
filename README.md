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
