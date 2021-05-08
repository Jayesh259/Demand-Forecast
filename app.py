# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import pandas as pd
import requests
import pickle 
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest.pkl','rb'))
@app.route('/',methods = ['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict",methods=['POST'])
def predict():
  
    if request.method == 'POST':
        P = str(request.form['Product'])
        if P == 'Milk':
            P=1
        elif P == 'Bread':
            P=2
        elif P == 'Soda':
            P=3
        elif P == 'Cereal':
            P=4
        elif P == 'Rice':
            P=5
        elif P == 'Yogurt':
            P=6
        elif P == 'Cheese':
            P=7
        elif P == 'Popcorn':
            P=8
        elif P == 'Keto Coffee':
            P=9
        elif P == 'Peanut Butter':
            P=10
        elif P == 'Jelly Sandwich':
            P=11
        elif P == 'Banana':
            P=12
        elif P == 'Olive Oil':
            P=13
        elif P == 'Premia Sugar':
            P=14
        elif P == 'Jaggery':
            P=15
        elif P == 'Salt':
            P=16
        elif P == 'Dry Fruits':
            P=17
        elif P == 'Cookies':
            P=18
        else:
            P=19
            
        
        S =  int(request.form['Store'])
        
        
        X=pd.read_csv('X.csv')
        X['item']=P
        X['store']=S
            
        prediction = model.predict(X[['store', 'item','year','month','dayofweek','weekofyear','is_weekend']])
        A = [int(a) for a in prediction]
        s=sum(A)
        avg = int(s/len(A))
        A = [str(a) + ' qty' for a in A]
        j=[]
        for i in range(1,32):
            j.append(i)
        j = [str(i) for i in j]
        j = ['Day '+i for i in j]
        res = {}
        res = dict(zip(j, A))
        
       ## return redirect(url_for("index"), res = res , prediction_text2 = 'Total Sales Forecast for next month : {}'.format(s) , prediction_text3 = 'Average Sale per Day: {} '.format(avg))
      
    return render_template('index.html',prediction_text1= res , prediction_text2 = 'Total Sales Forecast for next month : {}'.format(s) , prediction_text3 = 'Average Sale per Day: {} '.format(avg))
   
            
if __name__=='__main__':
    app.run(debug=True)
            