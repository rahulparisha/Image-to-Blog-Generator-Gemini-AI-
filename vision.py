from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image_data):
    model = genai.GenerativeModel('gemini-1.5-flash')
    contents = [
        input_prompt,
        image_data
    ]
    response = model.generate_content(contents)
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_part = {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
        return image_part
    else:
        return None

st.set_page_config(page_title="IMG TO BLOG GENERATION")
st.header("Give an image to generate your own blog")
input_prompt = st.text_input("Input prompt: ", key="input", value="Generate a blog post about the content of this image:")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_data = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image.", use_container_width=True)
    image_data = input_image_setup(uploaded_file)

submit = st.button("Generate a blog")

if submit:
    if image_data:
        response = get_gemini_response(input_prompt, image_data)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please upload an image before generating the blog.")