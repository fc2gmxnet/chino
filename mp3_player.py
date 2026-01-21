# MP3 Player

import streamlit as st

st.title("🎶 MP3 Player")

# Dictionary of MP3 files stored in your GitHub repo
mp3_files = {
    "Get the truth": "https://raw.githubusercontent.com/<username>/<repo>/main/music/song1.mp3",
    "Taking charge": "https://raw.githubusercontent.com/<username>/<repo>/main/music/song2.mp3",
    "Sales management": "https://raw.githubusercontent.com/<username>/<repo>/main/music/song3.mp3",
    "Boss management": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Boss-Management-UK.mp3",
    # Add more as needed
}

# Dropdown menu to select a song
choice = st.selectbox("Choose a track:", sorted(mp3_files.keys())) # In alphabetical order

# Play the selected MP3
st.audio(mp3_files[choice], format="audio/mp3")
st.success(f"Now playing: {choice}")
