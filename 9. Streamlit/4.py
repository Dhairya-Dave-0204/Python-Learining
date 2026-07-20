# Charts & Images

# A. Showing a Simple Line Chart

import streamlit as st   # Importing Streamlit library
import pandas as pd      # Importing pandas for data handling
import numpy as np       # Importing numpy to generate random numbers

st.title("Charts Example")   # Page title shown at the top of the app

data = pd.DataFrame({        # Creating a DataFrame (table) with random numbers
    "numbers": np.random.randn(50)   # 50 random numbers generated
})

st.write("Below is a simple line chart:")   # Text before the chart

st.line_chart(data)  # Streamlit automatically draws a line chart using DataFrame

# B. Bar Chart

import streamlit as st   # Import Streamlit
import pandas as pd      # Import pandas
import numpy as np       # Import numpy

st.title("Bar Chart Example")   # Title for this section

data = pd.DataFrame({           # Creating a table with 3 columns
    "A": np.random.randint(1, 50, 5),   # 5 random integers for column A
    "B": np.random.randint(1, 50, 5),   # 5 random integers for column B
    "C": np.random.randint(1, 50, 5)    # 5 random integers for column C
})

st.write("This is a bar chart:")   # Label before the chart

st.bar_chart(data)  # Streamlit automatically creates a bar chart

# C. Displaying an Image

import streamlit as st   # Import Streamlit

st.title("Image Example")   # Title for the image section

st.write("Below is an image displayed using Streamlit:")   # Text before the image

st.image("Messi.jpg")  # Displaying an image from your project folder
# Make sure the image file is in the same folder as your py file

# D. Display an Image with Caption + Width

import streamlit as st   # Import Streamlit

st.title("Image with Caption")   # Section title

st.image("Messi.jpg", caption="This is an example image", width=300)
# caption: small text shown below image
# width: resize the image to 300 pixels width