import streamlit as st
from gradio_client import Client

def extract_resume_details(pdf_file):
    client = Client("https://sujanmidatani-resume-details-extractor.hf.space/")
    result = client.predict(pdf_file, api_name="/predict")
    with open(result, "r", encoding='utf-8') as f:
        return f.read()

def main():
    st.title("Resume Details Extractor")
    st.write("Upload a PDF file to extract resume details.")

    # File uploader
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        # Perform extraction on button click
        if st.button("Extract"):
            try:
                # Convert the uploaded file to bytes
                file_bytes = uploaded_file.read()

                # Call the extraction function
                extracted_details = extract_resume_details(file_bytes)

                # Display the extracted details
                st.text(extracted_details)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
