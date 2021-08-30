import numpy as np
import pickle
import pandas as pd
import streamlit as st 


from PIL import Image



pickle_in = open("heartRad.pkl","rb")
classifier=pickle.load(pickle_in)




def welcome():
    return "Welcome All"


def predict_note_authentication(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal):
 
   
    prediction=classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal]])
    print(prediction)
    return prediction



def main():
    html_temp = """

    <div style="background-color:#2980B9;padding:10px">
    <h2 style="color:white;text-align:center;"> HEART DISEASE PREDICTION</h2>
    </div>

    """
    st.markdown(html_temp,unsafe_allow_html=True)  
    
    image = Image.open('img.jpg')
    st.image(image, use_column_width=True)
    
    age = st.text_input("Age","Type Here")
    sex = st.text_input("Sex","Type Here")
    cp = st.text_input("Cp","Type Here")
    trestbps = st.text_input("Trestbps","Type Here")
    chol = st.text_input("Chol","Type Here")
    fbs = st.text_input("Fbs","Type Here")
    restecg = st.text_input("Restecg","Type Here")
    thalach = st.text_input("Thalach","Type Here")
    exang = st.text_input("Exang","Type Here")
    oldpeak = st.text_input("Oldpeak","Type Here")
    slope = st.text_input("Slope","Type Here")
    ca = st.text_input("CA","Type Here")
    thal = st.text_input("Thal","Type Here")  
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal)        
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("JOJO GEORGE")


if __name__=='__main__':
    main()
    
