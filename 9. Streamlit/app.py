import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
model = pickle.load(open("Multiple_LinearRegression_Model.pkl", "rb"))

# Optional dataset
try:
    df = pd.read_csv("house_price.csv")
except:
    df = None

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction App")
st.write("Choose a version below to explore different UI styles.")


# Tabs
tab1, tab2, tab3 = st.tabs([
    "1. Basic Clean Version",
    "2. Professional Version",
    "3. Smart Dropdown + Manual Version"
])


# --------------------------------------------------------------------
# 🔹 TAB 1 — BASIC CLEAN
# --------------------------------------------------------------------
with tab1:
    st.header("Basic Version")

    area = st.number_input("Area (sq ft)", 100, 10000, 1500, 50)
    bedrooms = st.number_input("Bedrooms", 1, 10, 3, 1)
    age = st.number_input("House Age (years)", 0, 100, 5, 1)

    if st.button("Predict (Basic Version)"):
        input_data = np.array([[area, bedrooms, age]])
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Price: {prediction:,.2f}")



# --------------------------------------------------------------------
# 🔹 TAB 2 — PROFESSIONAL VERSION
# --------------------------------------------------------------------
with tab2:
    st.header("Professional Version")

    col1, col2 = st.columns(2)

    with col1:
        area2 = st.number_input("Area (sq ft)", 100, 10000, 1800, 50)
        bedrooms2 = st.slider("Bedrooms", 1, 10, 3)
        age2 = st.slider("House Age (years)", 0, 100, 10)
        btn_prof = st.button("Predict (Professional Version)")

    with col2:
        st.subheader("Prediction Output")
        if btn_prof:
            input_data = np.array([[area2, bedrooms2, age2]])
            prediction = model.predict(input_data)[0]
            st.metric("Predicted House Price", f"{prediction:,.2f}")
        else:
            st.info("Provide values and click predict.")

    st.subheader("Dataset Preview")
    if df is not None:
        st.dataframe(df.head())
    else:
        st.warning("Dataset not found.")



# --------------------------------------------------------------------
# 🔹 TAB 3 — SMART DROPDOWN + MANUAL INPUT VERSION (BEST UX)
# --------------------------------------------------------------------
with tab3:
    st.header("Smart Dropdown + Manual Input Version")

    st.write(
        """
        This version automatically **hides the dropdown** when you start typing manually.  
        Manual input always has priority.  
        """
    )

    st.markdown("### 🔸 Area Input (Auto Smart Mode)")

    # Manual Area Input
    manual_area = st.text_input(
        "Type Custom Area (sq ft):",
        placeholder="Example: 1450    (Leave empty to use dropdown)"
    )

    # Float conversion helper
    def safe_float(value):
        try:
            return float(value)
        except:
            return None

    st.markdown("---")

    # If manual input is given → hide dropdown
    if manual_area.strip() == "":
        st.markdown("#### Or Select Area from Dropdown")
        area_options = [500, 800, 1000, 1200, 1500, 1800, 2200, 3000, 3500, 4000]
        area_final = st.selectbox("Select Area (sq ft)", area_options)
    else:
        # Try converting manual value
        manual_value = safe_float(manual_area)

        if manual_value is None or manual_value <= 0:
            st.error("❌ Please enter a valid positive number for manual area.")
            area_final = None
        else:
            st.success(f"Using manual area: **{manual_value} sq ft**")
            area_final = manual_value

    st.markdown("### 🔸 Other Inputs")

    bedrooms3 = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5, 6])
    age3 = st.selectbox("House Age (years)", list(range(0, 51)))

    # Predict Button
    if st.button("Predict (Smart Version)"):
        if area_final is not None:
            input_data = np.array([[area_final, bedrooms3, age3]])
            prediction = model.predict(input_data)[0]

            st.success(f"Predicted House Price: {prediction:,.2f}")
        else:
            st.error("Please fix area input before predicting.")
