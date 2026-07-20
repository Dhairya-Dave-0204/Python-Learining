# Layouts
'''
# A. Columns Layout
import streamlit as st   # Importing Streamlit library

st.title("Streamlit Layout Example - Columns")   # Page title

col1, col2 = st.columns(2)   # Creating two equal-width columns side-by-side

col1.write("This is Column 1")   # Content displayed inside the first column
col2.write("This is Column 2")   # Content displayed inside the second column
'''
# B. Sidebar Layout
'''
import streamlit as st   # Importing Streamlit

st.sidebar.title("Sidebar Menu")   # Title shown in the sidebar
# The sidebar appears on the left side of the webpage

option = st.sidebar.selectbox("Select Option", ["Home", "About"])  
# A dropdown menu inside the sidebar with two choices

st.write(f"You selected: {option}")  
# Displays the selected option on the main screen
'''
# C. Tabs Layout

import streamlit as st   # Importing Streamlit

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])  
# Creating two tabs named "Tab 1" and "Tab 2"

with tab1:   # Everything inside this block will appear in Tab 1
    st.write("Content of Tab 1")   # Text displayed in Tab 1

with tab2:   # Everything inside this block will appear in Tab 2
    st.write("Content of Tab 2")   # Text displayed in Tab 2

