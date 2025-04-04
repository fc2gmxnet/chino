import streamlit as st  # Para crear apps en HTML
import pandas as pd     # Para trabajar con dataframes (tablas)
import random           # Para trabajar con aleatoriedades

df=pd.read_excel('https://github.com/fc2gmxnet/chino/HSK2.xlsx')

st.write('HSK 2')

#st.dataframe(df.sample(3))

# Initialize or update the session state to store the random row index
if "random_index" not in st.session_state:
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Function to pick a new random row
def get_new_random_row():
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Get the current random row
random_row = df.iloc[st.session_state.random_index]

# Display the value of the first column
#st.title("?")
st.title(random_row.iloc[0])

# Button to reveal values of the second and third columns
if st.button("?"):
    #st.write(' ')
    #st.write("### Value from Column 2:")
    st.subheader(random_row.iloc[1])
    #st.write(' ')
    #st.write("### Value from Column 3:")
    st.subheader(random_row.iloc[2])

# Button to select a new random row
if st.button("+++"):
    get_new_random_row()
    st.rerun()  # Refresh the app to display the new random row

