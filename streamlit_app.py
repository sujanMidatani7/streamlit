import streamlit as st

from pydub import AudioSegment
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="pretrained_models/spkrec-xvect-voxceleb")
def analyze_audio(audio_file):
    # Load audio file using PyDub
   signal, fs =torchaudio.load(audio_file.name)
   embeddings_xvect1 = classifier.encode_batch(signal)
   st.write("the xvector")
   st.write(embeddings_xvect1)

# Define Streamlit app
st.title("Audio Analysis")
st.write("Analyzes the properties of an audio file using the PyDub module.")

# Create audio input component
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

# Analyze audio properties when file is uploaded
if audio_file is not None:
    analyze_audio(audio_file)
