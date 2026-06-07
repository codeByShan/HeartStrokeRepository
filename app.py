import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

model = joblib.load("LogisticRegression_heart.pkl")
scaler = joblib.load("scalar.pkl")
expected_columns = joblib.load("columns.pkl")
 
st.title("Heart Stroke Prediction by Zeeshan")
st.markdown('Provide the following details')

age = st.slider('Age', 18,100,40)
sex = st.selectbox("Sex",['Male', 'Female'])
chest_pain = st.selectbox("Chest Pain", ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input("Resting BP (mm)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/DL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 (mg/DL)", [0,1])
resting_ecg = st.selectbox("Resting ECG", ['RestingECG Normal', 'RestingECG ST', 'RestingECG LVH'])
max_hr = st.slider('Max Heart Rate', 60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ['Y', "N"])
old_peak = st.slider('Oldpeak (ST Depression)', 0.0,6.0,1.0)
st_slope = st.selectbox('ST Slope', ['Up', 'Flat', 'Down'])


if st.button('Predict') : 
    raw_input = {
        'Age' : age,
        'RestingBP' : resting_bp,
        'Cholesterol' : cholesterol, 
        'Fasting BS' : fasting_bs,
        'MaxHR' : max_hr,
        'Oldpeak' : old_peak,
        'Sex_' + sex : 1,
        'ChestPainType_' + chest_pain : 1,
        'RestingECG_' + resting_ecg : 1,
        'ExerciseAngina' + exercise_angina : 1, 
        'ST_Slope_' + st_slope : 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns : 
        if col not in input_df : 
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1 : 
        st.error('🛑 High risk of Heart Disease')
    else : 
        st.success('🫂 Low risk of Heart Disease')