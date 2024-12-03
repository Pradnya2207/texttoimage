import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API Configuration
API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}  # Replace with your token

# Function to query Hugging Face API
def query_huggingface(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error {response.status_code}: {response.json()['error']}")
        return None

# Streamlit App
st.title("AI Image Generator")
st.write("Enter a prompt below to generate an image using Stable Diffusion!")

# User input for the prompt
prompt = st.text_input("Enter your prompt:", "A futuristic cityscape with flying cars at night")

# Button to generate image
if st.button("Generate Image"):
    if prompt.strip():  # Check if the prompt is not empty
        with st.spinner("Generating image..."):
            image_bytes = query_huggingface(prompt)
            if image_bytes:
                # Display the generated image
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a valid prompt.")
