# app.py
import streamlit as st

st.set_page_config(page_title="Quick Links", page_icon="🔗", layout="centered")

# --- App title and description ---
st.title("🔗 Quick Links")
st.write("Choose an option below to open the corresponding web page in a new tab.")

# --- Define options and URLs ---
LINKS = {
    "HSK 2": "https://hsk2url.streamlit.app/",
    "HSK 3": "https://hsk3url.streamlit.app/",
    "Sales Training: "https://sales-training.streamlit.app/",
    "Job Interview Training": "https://job-interview-psychology.streamlit.app/",
    "INCI": "https://inci2learn.streamlit.app/",
    "HPC-INCI": "https://hpc-inci.streamlit.app/"
}

# --- Dropdown selection ---
selected = st.selectbox("Select a destination:", list(LINKS.keys()))

# --- Open selected link in a new tab ---
# Streamlit's native link_button opens in the same tab; to open in a new tab,
# we render a custom HTML anchor with target="_blank".
if st.button("Open selected link"):
    url = LINKS[selected]
    st.markdown(
        f'<a href="{url}" target="_blank">Click here if the link didn\'t open automatically.</a>',
        unsafe_allow_html=True,
    )
    # Trigger a small JS snippet to open the link immediately in a new tab
    st.write(
        f"""
        <script>
        window.open("{url}", "_blank");
        </script>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# --- Quick access buttons ---
st.subheader("Quick access")
cols = st.columns(3)
items = list(LINKS.items())

for i, (label, url) in enumerate(items):
    with cols[i % 3]:
        # Render as HTML to ensure new-tab behavior
        st.markdown(
            f"""
            <a href="{url}" target="_blank">
                <button style="padding:8px 12px; margin-top:8px; cursor:pointer;">{label}</button>
            </a>
            """,
            unsafe_allow_html=True,
        )

# --- Footer ---
st.caption("Tip: You can customize the options and URLs in the LINKS dictionary.")
