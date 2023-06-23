from gradio_client import Client
import streamlit as st
import base64
def read_pdf(file):
	client = Client("https://sujanmidatani-resume-details-extractor.hf.space/")
	result = client.predict(
					file.name,
					api_name="/predict"
	)
        
	return result
st.title("PDF to Text")
file = st.file_uploader("Upload PDF", type=["pdf"])
if file is not None:
    encoded_pdf = base64.b64encode(file.read()).decode('utf-8')
    # Send the encoded pdf file to the API
    text = read_pdf(encoded_pdf)
    st.write(text)
