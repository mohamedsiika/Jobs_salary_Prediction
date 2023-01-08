from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/display_page', methods=['POST'])
def display_page():
  url = request.form['url']
  page = requests.get(url)
  return page.text

@app.route('/display_salary', methods=['POST'])
def display_salary():
  job_url = request.form['job']
  url="http://127.0.0.1:5000/predict"

  headers={"content_type": "application/json"}
  data={"input":job_url}
  r=requests.get(url,headers=headers,json=data)
  salary = r.content
  return f'{{"salary": "{salary}"}}'


  # Look up the salary for the job using an external API or database
  

if __name__ == '__main__':
  app.run()
