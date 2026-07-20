# File Upload in Streamlit

# A. Basic CSV Upload + Show Data

import streamlit as st   # Importing Streamlit
import pandas as pd      # Importing pandas to work with CSV data

st.title("File Upload Example - CSV Viewer")   # Title of the app

st.write("Upload a CSV file to view its contents.")   # Short instruction for user

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])  
# File uploader widget that accepts only CSV files

if uploaded_file is not None:   # This block runs only if a file is uploaded
    df = pd.read_csv(uploaded_file)   # Reading the uploaded CSV into a pandas DataFrame
    
    st.subheader("Preview of Data")   # Subheader for data preview
    st.write(df.head())   # Showing the first 5 rows of the DataFrame
    
    st.subheader("DataFrame Shape")   # Subheader for shape info
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")   
    # Displaying number of rows and columns
    
    st.subheader("Basic Statistics")   # Subheader for statistics
    st.write(df.describe())   # Showing basic statistics for numeric columns
else:
    st.info("No file uploaded yet. Please upload a CSV file.")  
    # Message shown when no file is uploaded

# B. Little Cleaner Version with Success Message

import streamlit as st   # Import Streamlit
import pandas as pd      # Import pandas

st.title("CSV Upload and Analysis")   # App title

uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])  
# Asking user to upload CSV

if uploaded_file is not None:   # Check if file is uploaded
    st.success("File uploaded successfully!")   # Green success message
    
    df = pd.read_csv(uploaded_file)   # Read CSV into DataFrame
    
    st.subheader("Top 10 Rows")   # Subheader for top 10 rows
    st.dataframe(df.head(10))   # Display first 10 rows in scrollable table
    
    st.subheader("Column Names")   # Subheader for columns
    st.write(list(df.columns))   # Show all column names as list
    
    st.subheader("Summary Statistics")   # Subheader for stats
    st.write(df.describe())   # Basic statistics of numeric columns
else:
    st.warning("Please upload a CSV file to continue.")  
    # Yellow warning message if no file is uploaded

