"""
import subprocess
import sys

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure the openpyxl package is installed
try:
    import openpyxl
except ImportError:
    install_package("openpyxl")
    import openpyxl
"""
# Puse en archivo requirements.txt openpyxl

import streamlit as st  # For creating apps in HTML
import pandas as pd     # For working with dataframes (tables)
import random           # For working with randomness

# Read the Excel file into a DataFrame
df = pd.read_excel("https://raw.githubusercontent.com/fc2gmxnet/chino/main/HSK3.xlsx", engine='openpyxl')

# Page configuration
st.set_page_config(
    page_title='Google',
    page_icon=':magnifying_glass_tilted_left:',
    layout='wide'
)

st.write('HSK 3')

# Initialize or update the session state to store the random row index
if "random_index" not in st.session_state:
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Function to pick a new random row
def get_new_random_row():
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Get the current random row
random_row = df.iloc[st.session_state.random_index]

# Display the value of the first column
st.title(random_row.iloc[0])

# Button to reveal values of the second and third columns
if st.button('???'):
    st.title(random_row.iloc[1])
    #st.subheader(random_row.iloc[2])

# Button to select a new random row
if st.button(" +++ "):
    get_new_random_row()
    st.rerun()  # Refresh the app to display the new random row
