import requests
from data_input import data_in

url="http://127.0.0.1:5000/predict"
headers={"content_type": "application/json"}
data={"input":data_in}

r=requests.get(url,headers=headers,json=data)
print(r.content)

