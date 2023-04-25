import streamlit as st

from pydub import AudioSegment
import torchaudio

def analyze_audio(audio_file):
    # Load audio file using PyDub
    st.write(audio_file)
    audio,sr = torchaudio.load(audio_file.name)

    # Analyze audio properties
    channels = audio.channels
    sample_width = audio.sample_width
    frame_rate = audio.frame_rate
    duration = audio.duration_seconds

    # Display results
    st.write("Channels:", channels)
    st.write("Sample Width:", sample_width)
    st.write("Frame Rate:", frame_rate)
    st.write("Duration:", duration)


# Define Streamlit app
st.title("Audio Analysis")
st.write("Analyzes the properties of an audio file using the PyDub module.")

# Create audio input component
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

# Analyze audio properties when file is uploaded
if audio_file is not None:
    analyze_audio(audio_file)
