import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and scaler
with open('rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Set background image using custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20210617082812/ri/950/picture/2021/6/shutterstock_1855544260.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {
        background-color: #ffffff99;
        color: black;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🫀 Cardiovascular Risk Prediction App")
st.write("Enter the patient's information below to predict the 10-year risk of Coronary Heart Disease (CHD).")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
education = st.selectbox("Education Level", [1, 2, 3, 4], format_func=lambda x: {
    1: "Some High School", 2: "High School Graduate", 3: "Some College/Vocational", 4: "College Graduate"
}[x])
sex = st.selectbox("Sex", ["M", "F"])
is_smoking = st.selectbox("Is Smoking?", ["YES", "NO"])
cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=100, value=0)
BPMeds = st.selectbox("On BP Medication?", ["YES", "NO"])
prevalentStroke = st.selectbox("Prevalent Stroke?", ["YES", "NO"])
prevalentHyp = st.selectbox("Prevalent Hypertension?", ["YES", "NO"])
diabetes = st.selectbox("Diabetes?", ["YES", "NO"])
totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=0, max_value=700, value=200)
sysBP = st.number_input("Systolic BP (mmHg)", min_value=0, max_value=300, value=120)
diaBP = st.number_input("Diastolic BP (mmHg)", min_value=0, max_value=200, value=80)
BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, value=25.0)
heartRate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=250, value=70)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=500, value=80)

input_dict = {
    'age': age, 'education': education, 'cigsPerDay': cigsPerDay, 'totChol': totChol,
    'sysBP': sysBP, 'diaBP': diaBP, 'BMI': BMI, 'heartRate': heartRate, 'glucose': glucose,
    'sex_F': 1 if sex == 'F' else 0, 'sex_M': 1 if sex == 'M' else 0,
    'is_smoking_NO': 1 if is_smoking == 'NO' else 0, 'is_smoking_YES': 1 if is_smoking == 'YES' else 0,
    'BPMeds_0.0': 1 if BPMeds == 'NO' else 0, 'BPMeds_1.0': 1 if BPMeds == 'YES' else 0,
    'prevalentStroke_0': 1 if prevalentStroke == 'NO' else 0, 'prevalentStroke_1': 1 if prevalentStroke == 'YES' else 0,
    'prevalentHyp_0': 1 if prevalentHyp == 'NO' else 0, 'prevalentHyp_1': 1 if prevalentHyp == 'YES' else 0,
    'diabetes_0': 1 if diabetes == 'NO' else 0, 'diabetes_1': 1 if diabetes == 'YES' else 0,
}

# Reference values
reference_ranges = {
    'age': (18, 65), 'cigsPerDay': (0, 5), 'totChol': (125, 200),
    'sysBP': (90, 120), 'diaBP': (60, 80), 'BMI': (18.5, 24.9),
    'heartRate': (60, 100), 'glucose': (70, 99),
}

input_df = pd.DataFrame([input_dict])
numeric_cols = ['age', 'education','cigsPerDay', 'totChol', 'sysBP', 'diaBP', 
           'heartRate', 'BMI', 'glucose']
input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

st.subheader("📊 Risk Prediction:")
if st.button("Predict Cardiovascular Risk"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    risk_score = prediction_proba[0][1]

    if prediction[0] == 1:
        st.error(f"⚠️ High Risk of Cardiovascular Disease! (Risk probability: {risk_score:.2f})")
    else:
        st.success(f"✅ Low Risk of Cardiovascular Disease. (Risk probability: {risk_score:.2f})")

    st.subheader("🩺 Health Evaluation:")
    for feature, (low, high) in reference_ranges.items():
        value = input_dict[feature]
        if value < low:
            st.warning(f"🔽 {feature} is below normal: {value} (Normal: {low}-{high})")
        elif value > high:
            st.warning(f"🔼 {feature} is above normal: {value} (Normal: {low}-{high})")
        else:
            st.info(f"✅ {feature} is within the normal range: {value}")

    st.subheader("🍽️ Personalized Health Suggestions:")
    if input_dict['totChol'] > 200:
        st.markdown("**🧀 High Cholesterol Tips:**")
        st.markdown("- Reduce saturated fats (e.g., red meat, cheese)")
        st.markdown("- Eat more soluble fiber (e.g., oats, fruits)")
        st.markdown("- Exercise at least 30 minutes a day")

    if input_dict['BMI'] > 25:
        st.markdown("**⚖️ High BMI Tips:**")
        st.markdown("- Avoid sugary snacks and fried food")
        st.markdown("- Eat smaller, balanced meals")
        st.markdown("- Include daily walking or light exercise")

    if input_dict['glucose'] > 100:
        st.markdown("**🍬 High Glucose Tips:**")
        st.markdown("- Avoid soft drinks and refined carbs")
        st.markdown("- Eat whole grains and high-fiber foods")
        st.markdown("- Monitor blood sugar and stay hydrated")

    if input_dict['sysBP'] > 120 or input_dict['diaBP'] > 80:
        st.markdown("**💓 High Blood Pressure Tips:**")
        st.markdown("- Reduce salt and caffeine intake")
        st.markdown("- Include potassium-rich foods like bananas")
        st.markdown("- Monitor BP and manage stress")
