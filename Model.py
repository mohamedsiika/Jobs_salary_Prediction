import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import get_scorer_names,mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import pickle as pkl


df=pd.read_csv("eda.csv")
df.drop(["Unnamed: 0.1","Unnamed: 0"],inplace=True,axis=1)

features=df[['company_size','company_type','company_revenue','rating','company_age','python_yn','spark_yn','azure_yn','aws_yn','excel_yn','machine_learning_yn','job_simpl','seniority','description_len']]

features['company_size'].fillna(features['company_size'].mode()[0],inplace=True)
features['company_type'].fillna(features['company_type'].mode()[0],inplace=True)
features['company_revenue'].fillna(features['company_revenue'].mode()[0],inplace=True)
features['rating'].fillna(features['rating'].mean(),inplace=True)
features['company_age'].fillna(features['company_age'].mean(),inplace=True)

features_dum=pd.get_dummies(features)
target=df['salary estimate']

x_train,x_test,y_train,y_test=train_test_split(features_dum,target,train_size=0.8,random_state=40)

rf=RandomForestRegressor()

Params={'n_estimators':range(50,200,10),'max_features':('auto','sqrt','log2')}
gs=GridSearchCV(rf,Params,scoring='neg_mean_absolute_error')
gs.fit(x_train,y_train)

y_pred=gs.predict(x_test)
print(mean_absolute_error(y_test,y_pred))
print(gs.best_estimator_)

pkl.dump(gs.best_estimator_,open("FlaskAPI/models/Model_file.p","wb"))

