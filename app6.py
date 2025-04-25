# Puse en archivo requirements.txt openpyxl

import streamlit as st  # For creating apps in HTML
import pandas as pd     # For working with dataframes (tables)
import random           # For working with randomness

# Read the Excel file into a DataFrame
df = pd.read_excel("https://raw.githubusercontent.com/fc2gmxnet/chino/main/HSK4-Librito.xlsx", engine='openpyxl')

# Page configuration
st.set_page_config(
    page_title='tempo - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)
# Choose language to start with
toggle = st.toggle("HSK 4:    用中文回答")

if toggle:
    columna_pregunta = 2
    columna_respuesta = 0
else:
    columna_pregunta = 0
    columna_respuesta = 2

# Initialize or update the session state to store the random row index
if "random_index" not in st.session_state:
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Function to pick a new random row
def get_new_random_row():
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Get the current random row
random_row = df.iloc[st.session_state.random_index]

# Display the value of the first column
# Pensado para mostrar con texto mayor los caracteres
if columna_pregunta == 0:
    st.title(random_row.iloc[columna_pregunta])
else:
    st.subheader(random_row.iloc[columna_pregunta])

# Button to reveal values of the second and third columns
if st.button('???'):
    st.subheader(random_row.iloc[1])
    # Pensado para mostrar con texto mayor los caracteres
    if columna_respuesta == 0:
        st.title(random_row.iloc[columna_respuesta])
    else:
        st.subheader(random_row.iloc[columna_respuesta])
   

# Button to select a new random row
if st.button(" +++ "):
    get_new_random_row()
    st.rerun()  # Refresh the app to display the new random row
