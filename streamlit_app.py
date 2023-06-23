from gradio_client import Client
import streamlit as st
import requests
import os
def read_pdf(file):
    # Convert the uploaded file to bytes
    # bytes_data = file.getvalue()
    # Send a post request to the API with the file as data
    client = Client("https://sujanmidatani-resume-details-extractor.hf.space/")
    result = client.predict(
		 os.path.abspath(file.name),
		api_name="/predict"
	)
        
    return result

st.title("PDF to Text")
file = st.file_uploader("Upload PDF", type=["pdf"])
if file is not None:
    text = read_pdf(file)
    st.write(text)
