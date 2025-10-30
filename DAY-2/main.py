import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# Configure API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# System prompt for image analysis
system_prompt = "You are a helpful AI assistant that analyzes images. You provide clear, detailed, and accurate descriptions of what you see in images. Be specific about objects, people, settings, colors, and activities. Always be friendly and helpful in your descriptions."
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash"))

# App Title
st.title("🖼️ AI Image Caption Generator")
st.markdown("Upload an image and AI will describe what it sees!")

# Simple upload section
uploaded_file = st.file_uploader(
    "Choose an image", 
    type=["jpg", "png", "jpeg"],
    help="Upload a JPG, PNG, or JPEG image"
)

# Show image and generate caption
if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Image", use_container_width=True)
    
    # Generate caption button
    if st.button("🔍 Generate Caption", type="primary"):
        # Generate caption
        with st.spinner("AI is looking at your image..."):
            try:
                # Combine system prompt with user request
                full_prompt = f"{system_prompt}\n\nPlease describe this image in detail."
                response = model.generate_content([full_prompt, image])
                
                if response.text:
                    st.success("✨ AI's Description:")
                    st.write(response.text)
                else:
                    st.error("Couldn't generate a description. Try a different image!")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")

else:
    # Show examples when no image is uploaded
    st.info("👆 Upload an image above to get started!")
    
    st.markdown("### 💡 Try these examples:")
    st.markdown("- Upload a photo of your pet")
    st.markdown("- Upload a landscape photo") 
    st.markdown("- Upload a photo of food")
    st.markdown("- Upload a selfie")
