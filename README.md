# ❤️ Cardiovascular Risk Prediction

> **Using Machine Learning to Detect Heart Disease Risk and Save Lives**

---

## 📚 Project Overview

Despite advances in medical technology, coronary heart disease (CHD) remains a leading cause of death worldwide. Early detection of CHD risk is crucial to preventing and mitigating its devastating impact.

This project leverages machine learning techniques to **classify patients' 10-year risk of developing CHD** based on health, lifestyle, and demographic data, using insights from the famous **Framingham Heart Study** dataset.

By accurately predicting patient risk, healthcare providers can implement timely interventions, ultimately saving lives.

---

## 🛠 Project Type

- **Type**: Supervised Machine Learning (Classification Problem)
- **Approach**: Multimodel comparison and optimization

---

## 👨‍💻 Team Contribution

- **Team Size**: 3
- **Members**:
  - Dileep Singh
  - Vishal Singh ([GitHub](https://github.com/vish1007/Cardiovascular-Risk-Prediction-))
  - Mohammad Irfan

---

## 🎯 Problem Statement

With over 4,000 patient records and 15 health attributes, manually identifying individuals at high risk for coronary heart disease is challenging.

This project aims to develop an **automated predictive model** that:
- Accurately classifies patients based on their risk
- Enhances early detection
- Reduces CHD impact on patients and healthcare systems

---

## 🏥 Dataset Overview

- **Source**: Cardiovascular Study on Framingham, Massachusetts Residents
- **Size**: ~4,000 records
- **Key Features**:
  - **Demographics**: Age, Sex
  - **Behavioral**: Smoking habits, Alcohol use
  - **Medical History**: Hypertension, Diabetes, Stroke
  - **Current Health Metrics**: Blood Pressure, BMI, Heart Rate, Glucose
  - **Target Variable**: 10-year risk of CHD (Binary: 1 = Risk, 0 = No Risk)

---

## 🧠 Workflow

### 🔹 Data Preprocessing:
- Import libraries and datasets
- Handle missing data
- Data wrangling and cleaning

### 🔹 Exploratory Data Analysis (EDA):
- Pie Charts, Histograms, and Bar Plots
- Multivariate Visualizations (e.g., Smoking vs CHD by Gender)
- Correlation Analysis and Pairplots
- Hypothesis Testing:
  - **T-Test**
  - **Chi-Square Test**

### 🔹 Feature Engineering:
- Categorical encoding
- Null value treatment
- Feature scaling

### 🔹 Machine Learning Models:
- Logistic Regression
- Random Forest Classifier
- SVM Classifier
- KNN Classifier
- Decision Tree Classifier
- XGBoost Classifier

---

## 📈 Insights & Findings

- **Heart Attack Cases**: 511 positive cases vs 2879 negative
- **Education Level**: Lower education correlates with higher heart attack risk
- **Smoking Habits**: Male smokers have significantly higher heart disease risk
- **Blood Pressure Meds**: Only 100 people on BP meds; small subset prone to heart attack
- **Diabetes Impact**: 37.9% of diabetic patients are at high CHD risk
- **Hypertension**: 23.9% of hypertensive patients show elevated CHD risk
- **Cholesterol**: Higher cholesterol levels (>240) associate with a ~6% increased CHD risk
- **BMI Analysis**: 
  - Underweight and Overweight patients face higher risks compared to Normal BMI group
- **Heart Rate**: Higher heart rates correlate with greater heart disease risk
- **Stroke History**: Strongly increases probability of CHD
- **Age**: Older individuals show an increased probability of CHD

---

## 🏆 Results

- **Best Model**: ✅ Random Forest Classifier
- **Accuracy**: **90%**
- **F1-Score**: **0.91**
- **Conclusion**: Random Forest provides the most accurate and reliable classification for CHD risk prediction.

---

## 📂 How to Run

1. Clone the Repository:
   ```bash
   git clone https://github.com/vish1007/Cardiovascular-Risk-Prediction-
   ```
2. Navigate to Project Directory:
   ```bash
   cd Cardiovascular-Risk-Prediction
   ```
3. Install Required Libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the Notebook:
   ```bash
   jupyter notebook Cardiovascular_Risk_Prediction.ipynb
   ```

---

## 📊 Visuals Included

- Correlation Heatmap
- Feature Importance Charts
- ROC-AUC Curves
- Bivariate and Multivariate Explorations
- Hypothesis Testing Visuals

---

## 🚀 Future Scope

- Deploying the model with a Flask/Django API
- Integrating real-time patient health monitoring
- Expanding to multi-class prediction (severity levels)

---

## 🤝 Let's Connect

If you're looking for passionate, results-driven data scientists — let's connect!

📧 Contact: [singhvishdata10@gmail.com]  
💼 LinkedIn: [https://www.linkedin.com/in/vishal-singh-983821218/]

---

# ❤️ Empowering Healthcare with AI | Early Detection Saves Lives!

---
