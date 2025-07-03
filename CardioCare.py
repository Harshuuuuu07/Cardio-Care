import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import joblib


# Sidebar Navigation
with st.sidebar:
    selected = option_menu("Admin Panel", ["Dashboard",
                                           "About Us", "Dataset",
                                           "Project", "Settings"],
                           icons=['cast', 'info-circle', 'table', 'heart-pulse', 'gear'],
                           menu_icon='cast',
                           default_index=0,
                           orientation="vertical")

# Dashboard
if selected == "Dashboard":
    st.title("CardioCare: Predicting Cardiovascular Disease Risks")
    st.markdown(
        "Welcome to **CardioCare**, a machine learning-powered tool to assess the risk of cardiovascular disease (CVD) based on patient data. Navigate through the panel to explore the dataset, understand the project, and test predictions."
    )

# About Us
elif selected == "About Us":
    st.header("About CardioCare")
    st.markdown("""
    **CardioCare** is a data-driven project designed to help predict the risk of cardiovascular diseases using clinical and lifestyle parameters. 
    The goal is to assist healthcare providers and researchers by offering insights from historical health records.

    **Key Features:**
    - Easy-to-use interface
    - Real-time predictions based on patient input
    - Visual analysis of health trends

    **Data Attributes:**
    - Age (in days)
    - Gender (1 = female, 2 = male)
    - Height (in cm)
    - Weight (in kg)
    - Systolic Blood Pressure (`ap_hi`)
    - Diastolic Blood Pressure (`ap_lo`)
    - Cholesterol level (1: normal, 2: above normal, 3: well above normal)
    - Glucose level (1: normal, 2: above normal, 3: well above normal)
    - Smoke, Alcohol, Active (1: yes, 0: no)
    - Cardio (1 = presence of cardiovascular disease, 0 = none)
    """)

# Dataset Viewer
elif selected == "Dataset":
    st.header("Dataset Overview")
    try:
        df = pd.read_csv('cardio_train.csv', sep=';')
        st.success("Dataset loaded successfully!")
        st.write("Preview of the dataset:")
        st.dataframe(df.head())

        with st.expander("Show dataset info"):
            st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
            st.write("**Column Names:**")
            st.code(", ".join(df.columns))

    except FileNotFoundError:
        st.error("The dataset file `cardio_train.csv` was not found.")
    except Exception as e:
        st.error(f"Error loading dataset: {e}")

# Project: Prediction
elif selected == "Project":
    st.header("CVD Risk Prediction")
    st.info("Fill the form below to get a prediction.")

    # Collect user input
    age = st.slider("Age (in years)", 0, 100, 50)
    gender = st.radio("Gender", ["Male", "Female"])
    gender = 2 if gender == "Male" else 1  # 2 = Male, 1 = Female
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", min_value=80, max_value=200, value=120)
    ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", min_value=50, max_value=130, value=80)
    cholesterol = st.selectbox("Cholesterol Level", ["1 - Normal", "2 - Above Normal", "3 - Well Above Normal"])
    cholesterol = int(cholesterol.split(" - ")[0])
    gluc = st.selectbox("Glucose Level", ["1 - Normal", "2 - Above Normal", "3 - Well Above Normal"])
    gluc = int(gluc.split(" - ")[0])
    smoke = 1 if st.checkbox("Smoker?") else 0
    alco = 1 if st.checkbox("Consumes Alcohol?") else 0
    active = 1 if st.checkbox("Physically Active?") else 0
    model = joblib.load("cardio_model.pkl")
    # Prediction
    if st.button("Predict Risk"):
        input_data = [[
            age, gender, height, weight, ap_hi, ap_lo,
            cholesterol, gluc, smoke, alco, active
        ]]

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ High risk of cardiovascular disease.")
        else:
            st.success("✅ Low risk of cardiovascular disease.")

# Settings Page
elif selected == "Settings":
    st.header("Settings")
    st.warning("This page is under development.")

# Footer
st.markdown("---")

