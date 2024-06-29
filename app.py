'''
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import pickle

lg = pickle.load(open('placement.pkl','rb'))

# web app
img = Image.open('Job-Placement-Agency.jpg')
st.image(img,width=650)
st.title("Job Placement Prediciton Model")

input_text = st.text_input("Enter all features")
if input_text:
    input_list = input_text.split(',')
    np_df = np.asarray(input_list,dtype=float)
    prediction = lg.predict(np_df.reshape(1,-1))

    if prediction[0] == 1:
        st.write("This Person Is Placed")
    else:
        st.write("This Person is not Placed")
'''

import numpy as np
import streamlit as st
from PIL import Image
import pickle

# Load the trained model
lg = pickle.load(open('placement.pkl', 'rb'))

# Define the Streamlit app title and image
st.title("Job Placement Prediction Model")
img = Image.open('Job-Placement-Agency.jpg')

# Display the image with responsive width
st.image(img, width=650, caption='Job Placement Agency Image')

# Input box for user to enter features
input_text = st.text_input("Enter features separated by comma (e.g., feature1, feature2, ...)")

# Process input and make predictions
if input_text:
    input_list = input_text.split(',')
    try:
        np_df = np.asarray(input_list, dtype=float).reshape(1, -1)
        prediction = lg.predict(np_df)

        # Display prediction result
        if prediction[0] == 1:
            st.write("Prediction: This person is placed.")
        else:
            st.write("Prediction: This person is not placed.")
    except ValueError:
        st.write("Please enter valid numeric values separated by commas.")
