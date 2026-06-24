import streamlit as st
import pandas as pd
import pickle

# Load model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page config
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Approval Predictor")
st.write("Enter applicant details and predict whether the loan will be approved.")

st.divider()

# Numerical Inputs
applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=50000
)

coapplicant_income = st.number_input(
    "Co-applicant Income",
    min_value=0,
    value=20000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=150000
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=12,
    value=360
)

# Categorical Inputs

credit_history = st.selectbox(
    "Credit History",
    ["Good", "Bad"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

employment = st.selectbox(
    "Employment Type",
    ["Employed", "Self Employed"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married", "Single"]
)

# Prediction Button

if st.button("Predict Loan Status"):

    credit_history_encoded = 1 if credit_history == "Good" else 0

    education_encoded = 1 if education == "Graduate" else 0

    employment_encoded = 1 if employment == "Employed" else 0

    dependents_1 = 1 if dependents == "1" else 0
    dependents_2 = 1 if dependents == "2" else 0
    dependents_3_plus = 1 if dependents == "3+" else 0

    property_area_semiurban = 1 if property_area == "Semiurban" else 0
    property_area_urban = 1 if property_area == "Urban" else 0

    marital_status_single = 1 if marital_status == "Single" else 0

    input_df = pd.DataFrame({
        "ApplicantIncome": [applicant_income],
        "CoapplicantIncome": [coapplicant_income],
        "LoanAmount": [loan_amount],
        "Loan_Amount_Term": [loan_term],
        "CreditHistory": [credit_history_encoded],
        "Education": [education_encoded],
        "EmploymentType": [employment_encoded],
        "Dependents_1": [dependents_1],
        "Dependents_2": [dependents_2],
        "Dependents_3+": [dependents_3_plus],
        "PropertyArea_Semiurban": [property_area_semiurban],
        "PropertyArea_Urban": [property_area_urban],
        "MaritalStatus_Single": [marital_status_single]
    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
        st.write(
            f"Approval Probability: {probability[1] * 100:.2f}%"
        )
    else:
        st.error("❌ Loan Rejected")
        st.write(
            f"Rejection Probability: {probability[0] * 100:.2f}%"
        )