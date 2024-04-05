# -*- coding: utf-8 -*-


from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("dt.pkl","rb")
dt=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Anomaly detection web app.
    ---
    parameters:  
      - name: duration
        in: query
        type: number
        required: true
      - name: service
        in: query
        type: number
        required: true
      - name: src_bytes
        in: query
        type: number
        required: true
      - name: dst_bytes
        in: query
        type: number
        required: true
      - name: wrong_fragment
        in: query
        type: number
        required: true
      - name: urgent
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    duration=request.args.get("duration")
    service=request.args.get("service")
    src_bytes=request.args.get("src_bytes")
    dst_bytes=request.args.get("dst_bytes")
    land=request.args.get("land")
    wrong_fragment=request.args.get("wrong_fragment")
    urgent=request.args.get("urgent")
    hot=request.args.get("hot")
    num_failed_logins=request.args.get("num_failed_logins")
    logged_in=request.args.get("logged_in")

    prediction=dt.predict([[duration,service,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins,logged_in]])
    print(prediction)
    return "The Attack is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("Test_data"))
    print(df_test.head())
    prediction=dt.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    