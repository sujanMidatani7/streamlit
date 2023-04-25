import streamlit as st
import torch
import torchaudio
from speechbrain.pretrained import EncoderClassifier

# Load the encoder classifier model
classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="pretrained_models/spkrec-xvect-voxceleb")


def load_audio(file):
    # Load audio file using Torchaudio
    
        waveform, sample_rate = torchaudio.load(file)
        return waveform, sample_rate
    

def analyze_audio(file):
    waveform, sample_rate = load_audio(file)
    if waveform is None:
        return

    # Encode the audio signal using the x-vector model
    embeddings_xvect = classifier.encode_batch(waveform)

    # Display the embeddings
    st.write("The x-vector embeddings are:")
    st.write(embeddings_xvect)

# Define Streamlit app
st.title("Audio Analysis")
st.write("Analyzes the properties of an audio file using the PyDub module.")

# Create audio input component
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "flac"])

# Analyze audio properties when file is uploaded
if audio_file is not None:
    analyze_audio(audio_file)
