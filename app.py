import streamlit as st
from PIL import Image

st.title(':blue[Beauty Score]')

# Upload file
uploaded_file = st.file_uploader("Choose a photo ...", type="jpg")

# If upload success
if uploaded_file is not None:

    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([3, 1])

    with col1:
        st.image(image, width=500)

    with col2:
        st.metric("Score", "86%")
