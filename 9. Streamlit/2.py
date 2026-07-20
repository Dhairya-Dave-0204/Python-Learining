# Add Basic UI Elements

import streamlit as st   # Importing the Streamlit library

st.title("Basic Streamlit Components")   # Main title of the webpage

st.header("1. Text Elements")   # A big header to separate sections
st.write("This is normal text.")   # Normal text shown on the page
st.subheader("Subheader example")   # A smaller header below main header
st.caption("This is a caption")   # Light, small text below elements

st.header("2. User Input Elements")   # Section header for input elements

name = st.text_input("Enter your name:")   # Text box for user to type their name
age = st.number_input("Enter your age:", min_value=1, max_value=100)  
# A number input box with minimum and maximum allowed values

if st.button("Submit"):   # Code runs only when user clicks "Submit"
    st.success(f"Hello {name}, your age is {age}")  
    # Displays a green success message using user's input