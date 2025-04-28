import streamlit as st
import pickle
import numpy as np

# Load the saved model and scaler
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

st.title("🫀 Cardiovascular Risk Prediction App")
st.write("Enter the patient's information below to predict the 10-year risk of Coronary Heart Disease (CHD).")

# Input fields for the user
age = st.number_input("Age", min_value=0, max_value=120, value=30)
education = st.selectbox("Education Level", [1, 2, 3, 4], format_func=lambda x: {
    1: "Some High School",
    2: "High School Graduate",
    3: "Some College/Vocational",
    4: "College Graduate"
}[x])
sex = st.selectbox("Sex", ["M", "F"])
is_smoking = st.selectbox("Is Smoking?", ["YES", "NO"])
cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=100, value=0)
BPMeds = st.selectbox("On BP Medication?", ["YES", "NO"])
prevalentStroke = st.selectbox("Prevalent Stroke?", ["YES", "NO"])
prevalentHyp = st.selectbox("Prevalent Hypertension?", ["YES", "NO"])
diabetes = st.selectbox("Diabetes?", ["YES", "NO"])
totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=0, max_value=700, value=200)
BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, value=25.0)
heartRate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=250, value=70)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=500, value=80)

# Feature Engineering: Create hypertension_category
# Example logic (you can modify if you have better rules)
hypertension_category = 0
if prevalentHyp == "YES":
    hypertension_category = 1
if prevalentStroke == "YES":
    hypertension_category = 2

# Convert categorical inputs to numeric
sex_numeric = 1 if sex == "M" else 0
is_smoking_numeric = 1 if is_smoking == "YES" else 0
BPMeds_numeric = 1 if BPMeds == "YES" else 0
prevalentStroke_numeric = 1 if prevalentStroke == "YES" else 0
prevalentHyp_numeric = 1 if prevalentHyp == "YES" else 0
diabetes_numeric = 1 if diabetes == "YES" else 0

# Prepare input array
input_data = np.array([
    age,
    education,
    sex_numeric,
    cigsPerDay,
    BPMeds_numeric,
    prevalentStroke_numeric,
    prevalentHyp_numeric,
    diabetes_numeric,
    totChol,
    BMI,
    heartRate,
    glucose,
    hypertension_category
]).reshape(1, -1)

# Apply scaling only on selected columns
# Scaling only specific columns (same as during training)
columns_to_scale = [0, 3, 8, 10, 12, 9, 10, 11]  # age, cigsPerDay, totChol, heartRate, hypertension_category, BMI, heartRate, glucose
scaled_part = scaler.transform(input_data[:, columns_to_scale])

# Replace original values with scaled ones
input_data[:, columns_to_scale] = scaled_part

# Predict button
if st.button("Predict Cardiovascular Risk"):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"⚠️ High Risk of Cardiovascular Disease! (Risk probability: {prediction_proba[0][1]:.2f})")
    else:
        st.success(f"✅ Low Risk of Cardiovascular Disease. (Risk probability: {prediction_proba[0][0]:.2f})")
