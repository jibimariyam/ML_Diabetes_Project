import streamlit as st
import pandas as pd
import joblib

# Configure the Streamlit page
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# Load the trained machine learning model
model = joblib.load("models/diabetes_model.pkl")

# Application title
st.title("Diabetes Prediction System")

st.write(
    "An educational machine learning application "
    "for diabetes status classification."
)

st.info(
    "This application is for educational purposes only "
    "and is not a medical diagnostic tool."
)

st.header("1. Demographic Information")

col1, col2 = st.columns(2)

with col1:
    age_group = st.selectbox(
        "Age Group",
        ['18-30', '31-40', '41-50', '51-60', '61-70', '71-90']
    )

    gender = st.selectbox(
        "Gender",
        ['Male', 'Female', 'Non-Bi']
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

    waist_circumference_cm = st.number_input(
        "Waist Circumference (cm)",
        min_value=0.0,
        value=80.0
    )

with col2:
    family_history_diabetes = st.selectbox(
        "Family History of Diabetes",
        ['No', 'Yes']
    )

    family_history_obesity = st.selectbox(
        "Family History of Obesity",
        ['No', 'Yes']
    )

    family_history_hypertension = st.selectbox(
        "Family History of Hypertension",
        ['No', 'Yes']
    )

    st.header("2. Lifestyle Information")

col1, col2 = st.columns(2)

with col1:
    physical_activity_level = st.selectbox(
        "Physical Activity Level",
        ['Sedentary', 'Lightly Active',
         'Moderately Active', 'Very Active',
         'Extremely Active']
    )

    exercise_days_per_week = st.number_input(
        "Exercise Days per Week",
        min_value=0,
        max_value=7,
        value=3
    )

    sedentary_hours_per_day = st.number_input(
        "Sedentary Hours per Day",
        min_value=0.0,
        max_value=24.0,
        value=6.0
    )

with col2:
    smoking_status = st.selectbox(
        "Smoking Status",
        ['Never', 'Former', 'Current']
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0
    )

    stress_level = st.selectbox(
        "Stress Level",
        ['Low', 'Moderate', 'High', 'Very High']
    )

    st.header("3. Diet and Health Information")

col1, col2 = st.columns(2)

with col1:
    diet_quality_score = st.number_input(
        "Diet Quality Score",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    added_sugar_grams_per_day = st.number_input(
        "Added Sugar (grams per day)",
        min_value=0.0,
        value=50.0
    )

    fiber_grams_per_day = st.number_input(
        "Fiber (grams per day)",
        min_value=0.0,
        value=20.0
    )

    fruit_servings_per_day = st.number_input(
        "Fruit Servings per Day",
        min_value=0.0,
        value=2.0
    )

with col2:
    systolic_bp = st.number_input(
        "Systolic Blood Pressure",
        min_value=0.0,
        value=120.0
    )

    diastolic_bp = st.number_input(
        "Diastolic Blood Pressure",
        min_value=0.0,
        value=80.0
    )

    triglycerides_mg_dl = st.number_input(
        "Triglycerides (mg/dL)",
        min_value=0.0,
        value=150.0
    )

    st.divider()

if st.button("Predict Diabetes Status", type="primary", use_container_width=True):

    input_data = pd.DataFrame([{
        'age_group': age_group,
        'gender': gender,
        'bmi': bmi,
        'waist_circumference_cm': waist_circumference_cm,
        'family_history_diabetes': family_history_diabetes,
        'family_history_obesity': family_history_obesity,
        'family_history_hypertension': family_history_hypertension,
        'physical_activity_level': physical_activity_level,
        'exercise_days_per_week': exercise_days_per_week,
        'sedentary_hours_per_day': sedentary_hours_per_day,
        'smoking_status': smoking_status,
        'sleep_hours': sleep_hours,
        'stress_level': stress_level,
        'diet_quality_score': diet_quality_score,
        'added_sugar_grams_per_day': added_sugar_grams_per_day,
        'fiber_grams_per_day': fiber_grams_per_day,
        'fruit_servings_per_day': fruit_servings_per_day,
        'systolic_bp': systolic_bp,
        'diastolic_bp': diastolic_bp,
        'triglycerides_mg_dl': triglycerides_mg_dl
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.warning("The model classified this input as Diabetes (Class 1).")
    else:
        st.success("The model classified this input as No Diabetes (Class 0).")

    st.caption(
        "Educational demonstration only. This prediction is not a medical diagnosis."
    )