import streamlit as st
import pandas as pd
import random
import os

# --- FILE CONFIGURATION ---
CSV_FILE = 'hsk2.csv'

def load_data():
    """Loads the CSV or creates it from the initial dictionary if missing."""
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        # Initializing with your provided data
        data = {
            'Column1': ['爷爷常常让我给他读报纸', '这个消息是我从报纸上看到的', '考试的时候不可以使用铅笔', '妈妈给我买了一块新手表', '她用手机给我拍了一些照片'],
            'Column2': ['Yéye chángcháng ràng wǒ gěi tā dú bàozhǐ', 'zhè ge xiāoxi shì wǒ cóng bàozhǐ shang kàn dào de', 'kǎoshì de shíhou bù kěyǐ shǐyòng qiānbǐ', 'māma gěi wǒ mǎi le yī kuài xīn shǒubiǎo', 'tā yòng shǒujī gěi wǒ pāi le yī xiē zhàopiàn'],
            'Column3': ['My grandfather often lets me read the newspaper for him', 'I saw this news in the newspaper', 'Pencil is not allowed during the exam', 'Mother bought a new watch for me', 'She took photos with her phone'],
            'level': ['normal'] * 5  # Adds the level column automatically
        }
        df_new = pd.DataFrame(data)
        df_new.to_csv(CSV_FILE, index=False, encoding='utf-8-sig') # utf-8-sig ensures Chinese characters display correctly in Excel
        return df_new

def update_csv_level(index, new_level):
    """Saves the difficulty level back to the CSV file."""
    df_current = pd.read_csv(CSV_FILE)
    df_current.at[index, 'level'] = new_level
    df_current.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')

# --- APP CONFIG ---
st.set_page_config(page_title='HSK 2 Flashcards', layout='wide')

df = load_data()

# --- SIDEBAR / SETTINGS ---
with st.sidebar:
    st.header("Settings")
    toggle = st.toggle("Answer in Chinese (用中文回答)")
    col_q = 'Column3' if toggle else 'Column1'
    col_a = 'Column1' if toggle else 'Column3'
    
    st.divider()
    st.write("### Progress Stats")
    st.write(df['level'].value_counts())

# --- SESSION STATE ---
if "random_index" not in st.session_state:
    st.session_state.random_index = random.randint(0, len(df) - 1)
if "revealed" not in st.session_state:
    st.session_state.revealed = False

# --- MAIN INTERFACE ---
row = df.iloc[st.session_state.random_index]

# Display the Question
st.markdown("### Question:")
if col_q == 'Column1':
    st.title(row['Column1'])
else:
    st.subheader(row['Column3'])

# Level Selector
level_options = ["easy", "normal", "difficult"]
current_val = row['level'] if row['level'] in level_options else "normal"
new_choice = st.selectbox("Set Level:", level_options, index=level_options.index(current_val))

# Save level logic
if st.button("💾 Save Difficulty"):
    update_csv_level(st.session_state.random_index, new_choice)
    st.toast(f"Updated to {new_choice}!")

st.divider()

# Reveal and Navigation Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button('??? Reveal Answer', use_container_width=True):
        st.session_state.revealed = True

with col2:
    if st.button("+++ Next Card", use_container_width=True, type="primary"):
        st.session_state.random_index = random.randint(0, len(df) - 1)
        st.session_state.revealed = False
        st.rerun()

# Reveal Logic
if st.session_state.revealed:
    st.info(f"**Pinyin:** {row['Column2']}")
    if col_a == 'Column1':
        st.title(row['Column1'])
    else:
        st.success(f"**English:** {row['Column3']}")
