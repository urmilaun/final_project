# -*- coding: utf-8 -*-



import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("dt.pkl","rb")
dt=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(duration,service,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins,logged_in):
    
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
   
    prediction=dt.predict([[duration,service,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins,logged_in]])
    print(prediction)
    if (prediction[0] == 0):
      return 'anomaly'
    else:
      return 'normal'



def main():
    st.title("Anomaly Detection in IOT Network using Machine Learning")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Anomaly Detection ML APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    duration = st.text_input("duration","Type Here")
    service = st.text_input("service","Type Here")
    src_bytes = st.text_input("src_bytes","Type Here")
    dst_bytes = st.text_input("dst_bytes","Type Here")
    land = st.text_input("land","Type Here")
    wrong_fragment = st.text_input("wrong_fragment","Type Here")
    urgent = st.text_input("urgent","Type Here")
    hot = st.text_input("hot","Type Here")
    num_failed_logins = st.text_input("num_failed_logins","Type Here")
    logged_in = st.text_input("logged_in","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(duration,service,src_bytes,dst_bytes,land,wrong_fragment,urgent,hot,num_failed_logins,logged_in)
    st.success('The Attack is {}'.format(result))


if __name__=='__main__':
    main()
    
    
    