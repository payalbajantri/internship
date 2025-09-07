import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")
st.divider()
st.write("with this app, you can get estimations of salaries of the company employess")
years = st.number_input("enter years" , value=1 , step= 1 , min_value= 0)
jobrate = st.number_input("enter jobrate" , value=3.5, step = 0.5 , min_value= 0.0)
x = [years,jobrate] 
model = joblib.load("linearmodel.pkl")
st.divider()
predict = st.button("press the button for prediction")
st.divider()
if predict:
    st.balloons()
    x1 = np.array([x])
    prediction = model.predict(x1)
    st.write(f"Salary prediction is {prediction}")





else:
    "press button for app to make prediction"