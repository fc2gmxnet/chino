# Music player
# It plays folders of MP3 files

import streamlit as st
import os
from pydub import AudioSegment

MUSIC_FOLDER = "music"

# Collect all subfolders inside "music"
subfolders = [
    f for f in os.listdir(MUSIC_FOLDER)
    if os.path.isdir(os.path.join(MUSIC_FOLDER, f))
]

# Dropdown menu to select a subfolder (album/playlist)
selected_folder = st.selectbox("📂 Choose a folder:", sorted(subfolders))

# Build the path to the chosen folder
MP3_FOLDER = os.path.join(MUSIC_FOLDER, selected_folder)

# Collect all mp3 files from the chosen folder
mp3_files = sorted([
    f for f in os.listdir(MP3_FOLDER) if f.endswith(".mp3")
])

# --- Autoplay mode: merge all tracks into one ---
playlist = AudioSegment.empty()
for track in mp3_files:
    audio = AudioSegment.from_mp3(os.path.join(MP3_FOLDER, track))
    playlist += audio

playlist.export("merged_playlist.mp3", format="mp3")

st.subheader("▶️ Autoplay all tracks")
with open("merged_playlist.mp3", "rb") as f:
    st.audio(f.read(), format="audio/mp3")

# --- Manual mode: Next/Previous buttons ---
st.subheader("⏭️ Manual track control")

if "track_index" not in st.session_state:
    st.session_state.track_index = 0

col1, col2 = st.columns([1,1])
with col1:
    if st.button("⏮️ Previous") and st.session_state.track_index > 0:
        st.session_state.track_index -= 1
with col2:
    if st.button("⏭️ Next") and st.session_state.track_index < len(mp3_files)-1:
        st.session_state.track_index += 1

current_track = mp3_files[st.session_state.track_index]
st.write(f"🎵 Now playing: {current_track}")

with open(os.path.join(MP3_FOLDER, current_track), "rb") as f:
    st.audio(f.read(), format="audio/mp3")
