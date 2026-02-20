
# Managing your boss
# Book by John Gabarro, Harvard Business Review
# Check-list for successful one-to-one meetings with your boss
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'rule': ['pre-meeting', 'pre-meeting', 'pre-meeting', 'pre-meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting'], 'question': ['what are the key check points for a one-to-one meeting with your boss?', 'what is the medium check?', 'what is the detail check?', 'what is the priority check?', 'what are the key agenda items for a one-to-one meeting with your boss?', 'what is the manager\'s goal for the "big picture" update?', "what is the manager's goal for the expectation calibration?", 'what is the manager\'s goal for the "no surprises" brief?', "what is the manager's goal for the resource request?", "what is the manager's goal for the feedback loop?", 'what are the key point after a meeting, where credibilitiy is built or lost?', 'what is key for successful immediate follow-up after a meeting?', 'what is key to deliver on deadlines?', 'what is key to deliver consistent honesty?', 'what are the key check points for personal reflection right after a one-to-one meeting with your boss?', 'what is the reaction check?', 'what is the compliance check?', 'what is the adjustment check?'], 'answer': ['medium, detail and priority checks', 'Is your boss a Reader (send the agenda/data 24 hours early) or a Listener (be prepared to present clearly and provide the memo afterward)?', 'Does your boss want the "big picture" or are they "high-involvement" (wanting the technical specifics)?', 'What is the one thing your boss is currently under pressure to deliver to their boss? How does your update relate to that?', 'the "big picture" update, expectation calibration, the "no surprises" brief, resource request, feedback loop', 'Align your current output with their organizational goals: "To support your goal of [Project X], here is where my team stands..."', 'Ensure your "mental map" of the job matches theirs.: "I’m prioritizing A over B this week to meet the deadline. Does that align with your view?"', 'Share bad news or potential risks early.: "I wanted to flag a potential delay in [Project Y] so we can adjust before it impacts the quarter."', 'Use "blue chips" selectively for what you truly need.: "I need your influence to get the [Department] to approve this. It’s critical for our Q3 target."', 'Check for blind spots.: "What’s one thing I could do differently to make your job easier this month?"', 'Immediate follow-up, deliver on deadlines, consistent honesty', "Send a brief summary of agreed-upon expectations. This prevents misunderstandings, like where one person thinks a decision was made and the other doesn't.", "If you committed to a date during the meeting, meet it. If you can't, flag the slip immediately.", 'If the "Big Picture" changes, don\'t shade the truth to look better in the short term.', 'reaction, compliance and adjustement checks', 'Did I get defensive when challenged (Counterdependence)?', 'Did I agree to an unrealistic deadline just to please them (Overdependence)?', 'How can I adjust my "discursive" or "intuitive" style next time to better fit their "concise" or "formal" style?']}
df = pd.DataFrame(df_dictionary)

# Column indices
# If columna_leccion is not available, set it to None
columna_leccion = 0
columna_pregunta = 1
columna_respuesta = 2
# columna_imagen = 3 # Not required if there is no image

# --- Page configuration ---
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# --- UI: Dropdown on top, Toggle below ---
if columna_leccion is not None and columna_leccion < df.shape[1]:
    df.iloc[:, columna_leccion] = df.iloc[:, columna_leccion].astype(str)
    selected_lesson = st.selectbox("Select phase", sorted(df.iloc[:, columna_leccion].unique()))
    filtered_df = df[df.iloc[:, columna_leccion] == selected_lesson]
else:
    #st.info("No lesson column found. Showing all data.")
    selected_lesson = None
    filtered_df = df.copy()

toggle = st.toggle("Random question order")

# --- Session state for random index ---
if "index" not in st.session_state or st.session_state.get("last_lesson") != selected_lesson:
    st.session_state.index = 0 if not toggle else random.randint(0, len(filtered_df) - 1)
    st.session_state.last_lesson = selected_lesson

# --- Functions ---
def get_new_random_row():
    if not filtered_df.empty:
        st.session_state.index = random.randint(0, len(filtered_df) - 1)

def get_next_ordered_row():
    if not filtered_df.empty:
        st.session_state.index = (st.session_state.index + 1) % len(filtered_df)

# --- Add CSS to style the buttons ---
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        width: 350px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Display question ---
if not filtered_df.empty:
    current_row = filtered_df.iloc[st.session_state.index]
    st.subheader(current_row.iloc[columna_pregunta])

    # Reveal answer
    if st.button('?'):
        if columna_respuesta == 1:
            st.subheader(current_row.iloc[columna_respuesta])
        else:
            st.subheader(current_row.iloc[columna_respuesta])

    # Next question
    if st.button('►'):
        if toggle:
            get_new_random_row()
        else:
            get_next_ordered_row()
        st.rerun()
else:
    st.warning("No questions available.")
