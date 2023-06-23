import streamlit as st
from gradio_client import Client
import tempfile
import os

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
                # Create a temporary directory
                temp_dir = tempfile.mkdtemp()
                temp_file_path = os.path.join(temp_dir, "resume.pdf")

                # Save the uploaded PDF file to the temporary location
                with open(temp_file_path, "wb") as temp_file:
                    temp_file.write(uploaded_file.read())

                # Call the extraction function with the file path
                extracted_details = extract_resume_details(temp_file_path)

                # Display the extracted details
                st.text(extracted_details)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                # Clean up the temporary directory and file
                os.remove(temp_file_path)
                os.rmdir(temp_dir)

if __name__ == "__main__":
    main()
