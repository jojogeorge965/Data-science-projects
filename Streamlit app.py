import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt


from PIL import Image



pickle_in = open("heartRad.pkl","rb")
classifier=pickle.load(pickle_in)


data=pd.read_csv("data/dataset.csv")
data["sex"]=data["sex"].map({0:"M",1:"F"})




#def welcome():
#    return "Welcome All"


def predict_note_authentication(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal):
    
    age=float(age)
    sex=float(sex)
    cp=float(cp)
    trestbps=float(trestbps)
    chol=float(chol)
    fbs=float(fbs)
    restecg=float(restecg)
    thalach=float(thalach)
    exang=float(exang)
    oldpeak=float(oldpeak)
    slope=float(slope)
    ca=float(ca)
    thal=float(thal)
    
  
  
   
    prediction=classifier.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal]])
    #print(classifier.predict([[2,3,4,1,2,3,4,1,2,3,4,1,4]]))
    print(prediction)
    return prediction



def main():
    st.title("Heart Disease Prediction")
    st.write("Using Machine Learning to Find Heart disease for you")
    
    
#    html_temp = """
#    <div style="background-color:tomato;padding:10px">
#    <h2 style="color:white;text-align:center;">Streamlit HEART DISEASE PREDICTION ML App </h2>
#    </div>
#    """
    
#IMAGE LOAFING
    image = Image.open('front_img.jpg')
    st.image(image, use_column_width=True)

#LOADING HTML
    
#    st.markdown(html_temp,unsafe_allow_html=True)   
    
    
# ENTERING INPUTS
    
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    cp = st.text_input("cp","Type Here")
    trestbps = st.text_input("trestbps","Type Here")
    chol = st.text_input("chol","Type Here")
    fbs = st.text_input("fbs","Type Here")
    restecg = st.text_input("restecg","Type Here")
    thalach = st.text_input("thalach","Type Here")
    exang = st.text_input("exang","Type Here")
    oldpeak = st.text_input("oldpeak","Type Here")
    slope = st.text_input("slope","Type Here")
    ca = st.text_input("ca","Type Here")
    thal = st.text_input("thal","Type Here")  
    
#SLIDEBAR SELECTBOX
    
    gender = st.sidebar.selectbox('What is GENDER?', ["Male","Female"])
    st.write("your selected gender",gender)
    
#SLIDEBAR
    
    age=st.slider("SELECT AGE",0,120)
    st.write("your selected age",age)
    
 #BUTTON AND PLOTTING
    
    if st.button('DISTRIBUTION OF CP'):
        st.bar_chart(data["cp"])
        
    if st.button('LINE CHART OF DATA'):
        st.line_chart(data)
    
    
    
    

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal)        
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("JOJO")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    