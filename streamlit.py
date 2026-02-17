import streamlit as st
import requests

API_URL = 'https://empterm-api-1.onrender.com/predict-termination'

st.title("Employee Termination Prediction")

st.sidebar.header("Employee Details")

emp_satisfaction = st.sidebar.slider(
    "Employee Satisfaction",
    max_value = 5,
    min_value = 1,
    value = 3,
    step = 1
)

special_project_count = st.sidebar.slider(
    "Special Project Count",
    max_value = 30,
    min_value = 1,
    value = 4,
    step = 1
)

absences = st.sidebar.slider(
    "Absences",
    max_value = 20,
    min_value = 0,
    value = 5,
    step = 1
)

if st.sidebar.button("Predict Termination or Active"):
    payload = {
        "EmpSatisfaction": emp_satisfaction,
        "SpecialProjectsCount": special_project_count,
        "Absences": absences
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            if result["Predicted Termination"] == 1:
                st.error("Employee is likely to be terminated.")
            else:
                st.success("Employee is likely to be active.")
        else:
            st.error("API ERROR!!")
    except requests.exceptions.RequestException:
        st.error("Could not connect to API. Please try again later.")