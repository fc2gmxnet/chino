# Music player
# It plays folders of MP3 files

import streamlit as st
import os

MP3_FOLDER = "mp3"

# Collect all mp3 files from the folder
mp3_files = sorted([
    f for f in os.listdir(MP3_FOLDER) if f.endswith(".mp3")
])

# Use session state to remember which track is playing
if "track_index" not in st.session_state:
    st.session_state.track_index = 0

# Buttons to move through playlist
col1, col2 = st.columns([1,1])
with col1:
    if st.button("⏮️ Previous") and st.session_state.track_index > 0:
        st.session_state.track_index -= 1
with col2:
    if st.button("⏭️ Next") and st.session_state.track_index < len(mp3_files)-1:
        st.session_state.track_index += 1

# Current track
current_track = mp3_files[st.session_state.track_index]
st.write(f"🎵 Now playing: {current_track}")

# Play audio
with open(os.path.join(MP3_FOLDER, current_track), "rb") as f:
    st.audio(f.read(), format="audio/mp3")
