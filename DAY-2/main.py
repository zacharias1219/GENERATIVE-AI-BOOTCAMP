import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🖼️ Image Caption Generator")

uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    if st.button("Generate Caption"):
        response = model.generate_content(["Describe this image in one sentence.", image])
        st.subheader("Generated Caption:")
        st.write(response.text)
