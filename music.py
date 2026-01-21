# Music player
# It plays folders of MP3 files

import streamlit as st
import os

# Replace with your GitHub username and repo name
GITHUB_USER = "fc2gmxnet"
GITHUB_REPO = "chino"
BRANCH = "main"   # or "master" depending on your repo

MUSIC_FOLDER = "music"

# Collect all subfolders inside "MUSIC_FOLDER"
subfolders = [
    f for f in os.listdir(MUSIC_FOLDER)
    if os.path.isdir(os.path.join(MUSIC_FOLDER, f))
]

# Dropdown menu to select a subfolder (album/playlist)
selected_folder = st.selectbox("📂 Choose a folder:", sorted(subfolders))
MP3_FOLDER = os.path.join(MUSIC_FOLDER, selected_folder)

# Collect all mp3 files from the chosen folder
mp3_files = sorted([f for f in os.listdir(MP3_FOLDER) if f.endswith(".mp3")])

# Build raw GitHub URLs for each track
playlist_urls = [
    f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/{MUSIC_FOLDER}/{selected_folder}/{track}"
    for track in mp3_files
]

# Create HTML/JS audio player
playlist_js = f"""
<script>
let tracks = {playlist_urls};
let index = 0;
let audio = new Audio(tracks[index]);
audio.controls = true;
document.body.appendChild(audio);

audio.onended = function() {{
    index = (index + 1) % tracks.length;
    audio.src = tracks[index];
    audio.play();
}};
</script>
"""

st.components.v1.html(playlist_js, height=120)
