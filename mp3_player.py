# MP3 Player
# Minimalistic design

import streamlit as st

# 2. Page Configuration 
st.set_page_config(page_title="One-to-one meeting with your boss", layout="wide")
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

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
    "DISC D Eagle": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/DISC_D_Eagle.mp3",
    "DISC I Parrot": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/DISC_I_Parrot.mp3",
    "DISC S Dove": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/DISC_S_Dove.mp3",
    "DISC C Owl": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/DISC_C_Owl.mp3",
    "Champion Mind": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/Champion_mind.mp3",
    "Sales Training": "https://raw.githubusercontent.com/fc2gmxnet/chino/main/mp3/sales_training.mp3",
    # Add more as needed
}

# Dropdown menu to select a song
choice = st.selectbox("▶️ Choose a track:", sorted(mp3_files.keys())) # In alphabetical order

# Play the selected MP3
st.audio(mp3_files[choice], format="audio/mp3")
#st.success(f"Playing: {choice}")
