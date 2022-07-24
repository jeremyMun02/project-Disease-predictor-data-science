# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:12:10 2022

@author: USER
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/USER/Desktop/disease predictor/work models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/USER/Desktop/disease predictor/work models/hearted_model.sav', 'rb'))
breast_model = pickle.load(open('C:/Users/USER/Desktop/disease predictor/work models/breast_model.sav', 'rb'))


#sidebar navigation

with st.sidebar:
    
     selected = option_menu ('Disease Prediction System', 
                            ['Diabetes prediction',
                         'Heart and stroke prediction',
                         'Breast Cancer prediction'], 
                            icons = ['activity', 'heart', 'x-diamond'],
                            
                            default_index = 0)
    
    #Diabetes prediction page

if (selected == 'Diabetes prediction'):
        
    #page title
    st.title ('Prediction for Diabetes')
    
    # getting the input data from the user
    # columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
                        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col2:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
   
    
    # code for prediction
    
    di_diagnosis = ''
    
    # creating button for results
    
    if st.button('Results'):
       dia_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
       if (dia_prediction[0] == 1):
           di_diagnosis = 'The person is diabetic'
        
       else:
           di_diagnosis = 'The person is not diabetic'
        
    st.success(di_diagnosis)
            
         
       
if (selected == 'Heart and stroke prediction'):
         
     #page title
    st.title ('Prediction for Heart failure')
     
    col1, col2, col3 = st.columns(3)
    with col1:
         age = st.text_input('Age')
         with col2:
              anaemia = st.text_input('anaemia')
              with col3:
                   creatinine_phosphokinase = st.text_input('Creatinine')
                   with col1:
                        diabetes  = st.text_input('diabetes ')
                        with col2:
                             ejection_fraction  = st.text_input('ejection')
                             with col3:
                                  high_blood_pressure = st.text_input('blood pressure')
                                  with col1:
                                      platelets  = st.text_input('platelets')
                                      with col2:
                                           serum_creatinine  = st.text_input('serum_creatinine')
                                           with col3:
                                                 serum_sodium = st.text_input('serum_sodium')
                                                 with col1:
                                                      sex  = st.text_input('sex')
                                                      with col2:
                                                          smoking  = st.text_input('smoking')
                                                          with col3:
                                                               time  = st.text_input('time')
                                                 
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        
        heart_prediction = heart_model.predict([[age, anaemia, creatinine_phosphokinase, diabetes,ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person has heart failure'
         
        else:
            heart_diagnosis = 'The person does not have heart failure'
         
    st.success(heart_diagnosis)
        
    
if(selected == 'Breast Cancer prediction'):
        
    #page title
    st.title ('Prediction for Breast Cancer')
    
    col1, col2, col3 = st.columns(3)
    with col1:
           mean_radius = st.text_input('radius of the breast')
    
    with col2:
            mean_texture = st.text_input('texture of the breast')
        
    with col3:
              mean_perimeter = st.text_input('perimeter of breast ')
        
    with col1:
            mean_area = st.text_input('area of the breast')
        
    with col2:
          mean_smoothness = st.text_input('smoothness of the breast')
        
       
        
        
        # code for Prediction
    br_diagnosis = ''
        
        # creating a button for Prediction
    if st.button('Cancer Test Result'):
            br_prediction = breast_model.predict([[ mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])
            
            if (br_prediction[0] == 1):
              br_diagnosis = 'The person has cancer'
            
            else:
              br_diagnosis = 'The person does not have Cancer'
            
    st.success(br_diagnosis)




    