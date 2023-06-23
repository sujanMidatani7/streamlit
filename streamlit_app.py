from gradio_client import Client
import streamlit as st

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
    text = read_pdf(file)
    st.write(text)
