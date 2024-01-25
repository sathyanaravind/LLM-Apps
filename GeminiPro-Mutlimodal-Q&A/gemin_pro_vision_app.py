from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load gemini pro
model = genai.GenerativeModel('gemini-pro-vision')
def get_response(text,image):
    if input != "":
        response = model.generate_content([text,image])
    else:
        response =  model.generate_content(image)
    return response.text


# streamlit app
st.set_page_config(page_title = "Gemini Vision Demo")
st.header("Google Gemini Pro Vision App")

input = st.text_input("Input", key = "input")

uploaded_file = st.file_uploader("Choose an image", type=["jpp", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "uploaded file", use_column_width = True)

submit = st.button("Ask the question about the image")

if submit:
    response = get_response(input, image)
    st.subheader("The Response is ")
    st.write(response)
