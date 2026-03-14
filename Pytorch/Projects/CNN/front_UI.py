import streamlit as st
import requests
from PIL import Image

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image to detect plant diseases using CNN.")

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict Disease"):

        with st.spinner("Analyzing leaf..."):

            files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
            }

            response = requests.post(API_URL, files=files)

            if response.status_code == 200:

                prediction = response.json()["prediction"]

                st.success(f"Prediction: {prediction}")

            else:

                st.error("Error communicating with prediction API")