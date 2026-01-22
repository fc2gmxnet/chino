# MP3 Player
# Minimalistic design

import streamlit as st

#st.title("▶️ MP3 Player")

# Dictionary of MP3 files stored in your GitHub repo
mp3_files = {
    "Get the truth": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/get_the_truth.mp3",
    "Taking charge": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/taking_charge.mp3",
    "Sales management": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/sales_management.mp3",
    "Boss management": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Boss-Management-UK.mp3",
    "Six Sigma Pricing": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Six_Sigma_Pricing.mp3",
    "Music Jazz French": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Music_Space_Jazz_Afternoon_French.mp3",
    "Music Jazz Nature 1": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Music_Space_Jazz_Nature_1.mp3",
    "Music Jazz Nature 2": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Music_Space_Jazz_Nature_2.mp3",
    "Music Jazz Nature 3": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Music_Space_Jazz_Nature_3.mp3",
    "Music Jazz Dreamy": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Music_Space_Jazz_Dreamy.mp3",
    # Add more as needed
}

# Dropdown menu to select a song
choice = st.selectbox("▶️ Choose a track:", sorted(mp3_files.keys())) # In alphabetical order

# Play the selected MP3
st.audio(mp3_files[choice], format="audio/mp3")
#st.success(f"Playing: {choice}")
