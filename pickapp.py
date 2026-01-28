# My colection of apps
import streamlit as st

st.set_page_config(page_title="Quick Links", page_icon="🔗", layout="centered")

# --- Define options and URLs ---
LINKS = {
    "HSK 2": "https://hsk2url.streamlit.app/",
    "HSK 3": "https://hsk3url.streamlit.app/",
    "HSK 4": "https://hsk4url.streamlit.app/",
    "Sales": "https://sales-training.streamlit.app/",  # Sales Training
    "Job Interview": "https://job-interview-psychology.streamlit.app/",  # Job Interview Training
    "INCI": "https://inci2learn.streamlit.app/",
    "HPC-INCI": "https://hpc-inci.streamlit.app/",
    "Taking Charge": "https://taking-charge.streamlit.app/",  # How to understand and prepare for a new managerial role
    "DISC": "https://disc-tutorial.streamlit.app/",
    "Boss mgmt": "https://boss-management.streamlit.app/", # How to manage the relationship with your boss
    "Boss meeting": "https://boss-meeting.streamlit.app/", # How to prepare a one-to-one meeting with your boss
    "PP": "https://pp-training.streamlit.app/",  # PP training on main applications
    "PE": "https://pe-training.streamlit.app/",  # PE training on main applications
    "Bus": "https://olhovivo.sptrans.com.br/",  # Bus in Sao Paulo
    "Truth": "https://get-the-truth.streamlit.app/",  # Elicitation training
    "MP3": "https://mp3-player.streamlit.app/", # MP3 Player
    "Champion": "https://champion-mind.streamlit.app/", # Develop a Champion's mind
}

# --- Dropdown selection (sorted alphabetically) ---
sorted_labels = sorted(LINKS.keys())
selected = st.selectbox("Choose to open the web page in a new tab:", sorted_labels)

# --- Open selected link in a new tab ---
if st.button("Open selected link"):
    url = LINKS[selected]
    st.markdown(
        f'<a href="{url}" target="_blank">Click here if the link didn\'t open automatically.</a>',
        unsafe_allow_html=True,
    )
    st.write(
        f"""
        <script>
        window.open("{url}", "_blank");
        </script>
        """,
        unsafe_allow_html=True,
    )

# --- Quick access buttons (sorted alphabetically) ---

# Sort items by label (dictionary key)
items = sorted(LINKS.items(), key=lambda x: x[0])

# Create one row with as many columns as items
cols = st.columns(len(items))

# Place each item in its own column
for i, (label, url) in enumerate(items):
    with cols[i]:
        st.markdown(
            f"""
            <a href="{url}" target="_blank">
                <button style="padding:8px 12px; margin-top:8px; cursor:pointer;">{label}</button>
            </a>
            """,
            unsafe_allow_html=True,
        )

