# Puse en archivo requirements.txt openpyxl

import streamlit as st  # For creating apps in HTML
import pandas as pd     # For working with dataframes (tables)
import random           # For working with randomness

# Read the Excel file into a DataFrame
data = pd.read_excel("https://raw.githubusercontent.com/fc2gmxnet/chino/main/HPC_INCI.xlsx", engine='openpyxl')

# https://github.com/fc2gmxnet/chino/raw/main/imagenes/2-ethylhexylmyristate.png

# Page configuration
st.set_page_config(
    page_title='Google',
    page_icon=':magnifying_glass_tilted_left:',
    layout='wide'
)

st.write('INCI')


# Function to select a random row
def get_random_row():
    return data.sample(1).iloc[0]

# Initialize session state
if 'row' not in st.session_state:
    st.session_state.row = get_random_row()

# Display title (INCI)
st.title(st.session_state.row['INCI'])

# Button to reveal translations and info
if st.button('???'):
    translations = f"{st.session_state.row['EN']} | {st.session_state.row['BR']} | {st.session_state.row['ES']}"
    st.title(translations)
    st.title(st.session_state.row['Info'])
    
    # Display image
    image_url = f"https://raw.githubusercontent.com/fc2gmxnet/chino/main/imagenes/{st.session_state.row['Picture']}"
    st.image(image_url)

# Button to get a new random row
if st.button('+++'):
    st.session_state.row = get_random_row()
    st.rerun()
