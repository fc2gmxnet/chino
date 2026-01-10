import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df = pd.DataFrame(df_dictionary)
df['Lesson'] = df['Lesson'].astype(str)  # Ensure lessons are strings

# --- Page configuration ---
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# --- UI: Toggle and Dropdown side by side ---
col1, col2 = st.columns([2, 1])
with col1:
    toggle = st.toggle("HSK 4:    用中文回答")
with col2:
    selected_lesson = st.selectbox("Lesson", sorted(df['Lesson'].unique()))

# --- Language columns ---
if toggle:
    columna_pregunta = 2
    columna_respuesta = 1
else:
    columna_pregunta = 1
    columna_respuesta = 2

# --- Filter by selected lesson ---
filtered_df = df[df['Lesson'] == selected_lesson]

# --- Session state for random index ---
if "random_index" not in st.session_state or st.session_state.get("last_lesson") != selected_lesson:
    st.session_state.random_index = random.randint(0, len(filtered_df) - 1) if not filtered_df.empty else None
    st.session_state.last_lesson = selected_lesson

# --- Function to pick a new random row ---
def get_new_random_row():
    if not filtered_df.empty:
        st.session_state.random_index = random.randint(0, len(filtered_df) - 1)

# --- Display question ---
if st.session_state.random_index is not None:
    random_row = filtered_df.iloc[st.session_state.random_index]
    st.subheader(random_row.iloc[columna_pregunta])

    # Reveal answer
    if st.button('???'):
        st.subheader(random_row.iloc[3])
        if columna_respuesta == 1:
            st.title(random_row.iloc[columna_respuesta])
        else:
            st.subheader(random_row.iloc[columna_respuesta])

    # Next question
    if st.button("+++"):
        get_new_random_row()
        st.rerun()
else:
    st.warning("No questions available for this lesson.")
