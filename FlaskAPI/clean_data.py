import pandas as pd 
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')




class Data_cleaning:
    def __init__(self,data) :
        self.data=data

    def title_extraction(self,title):
        if "data"in title.lower() and "analyst" in title.lower():
            return "data analyst"
        elif "data"in title.lower() and "scientist" in title.lower():
            return "data scientist" 
        elif "data"in title.lower() and "engineer" in title.lower():
            return "data engineer"
        elif "machine"in title.lower() and "learning" in title.lower():
            return "machine learning engineer"
        else:
            return "other"
        
    def level_extraction(self,title="",description=""):
        se=title
        if se=="":
            se=description

        if 'sr' in se.lower() or "senior" in se.lower() or "lead" in se.lower() or "principal" in se.lower() or "manager" in se.lower():
            return "Senior"
        elif 'jr' in se.lower() or "junior" in se.lower() or "entry" in se.lower() or "associate" in se.lower() or "fresh" in se.lower():
            return "junior"
        else:
            return "na"

    def text_preprocess(self,text):
        text=text.lower()
        text=re.sub(r"[^a-zA-Z0-9]"," ",text)
        text=text.split(" ")
        while text.count(""):
            text.remove("")
        en_stops = set(stopwords.words('english'))
        for i in text:
            if i in en_stops:
                text.remove(i)

        return text 

    def clean_data(self):
        self.data['rating']=self.data['company_name'][-3:] if '\n' in self.data['company_name'] else 'no rating'
        self.data['company_name']=self.data['company_name'][:-4] if '\n' in self.data['company_name'] else self.data['company_name'][:-1]
        self.data['python_yn']= 1 if "python" in self.data['job_description'].lower() else 0
        self.data['spark_yn']= 1 if "spark" in self.data['job_description'].lower() else 0
        self.data['azure_yn']= 1 if "azure" in self.data['job_description'].lower() else 0
        self.data['aws_yn']= 1 if "aws" in self.data['job_description'].lower() else 0
        self.data['excel_yn']= 1 if "excel" in self.data['job_description'].lower() else 0
        self.data['machine_learning_yn']= 1 if "machine learning" in self.data['job_description'].lower() else 0
        self.data['job_simpl']=self.title_extraction(self.data['job_title'])
        self.data['seniority']=self.level_extraction(title=self.data['job_title'])
        self.data['seniority']=self.level_extraction(description=self.data['job_description']) if self.data['seniority']=='na' else self.data['seniority']
        self.data['description_len']= len(self.text_preprocess(self.data['job_description']))
        self.data['company_age']=2022-int(self.data['company_founded']) if self.data['company_founded'] != '#N/A' else '#N/A'

    def select_features(self):
        features=['company_size','company_type','company_revenue','rating','company_age','python_yn','spark_yn','azure_yn','aws_yn','excel_yn','machine_learning_yn','job_simpl','seniority','description_len']
        self.data={key:self.data[key] for key in features}
        self.df=pd.DataFrame(self.data,index=[0])
        self.df=pd.get_dummies(self.df)

    def pipeline(self):
        self.clean_data()
        self.select_features()
        return self.df


     
    




        




