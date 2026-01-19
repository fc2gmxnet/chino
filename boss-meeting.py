# Managing your boss
# Book by John Gabarro, Harvard Business Review
# Check-list for successful one-to-one meetings with your boss
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# Data initialization
df_dictionary = {'rule': ['pre-meeting', 'pre-meeting', 'pre-meeting', 'pre-meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'meeting', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'post-meeting execution (dependability phase)', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting', 'personal reflection (self-awareness check) right after meeting'], 'question': ['what are the key check points for a one-to-one meeting with your boss?', 'what is the medium check?', 'what is the detail check?', 'what is the priority check?', 'what are the key agenda items for a one-to-one meeting with your boss?', 'what is the manager\'s goal for the "big picture" update?', "what is the manager's goal for the expectation calibration?", 'what is the manager\'s goal for the "no surprises" brief?', "what is the manager's goal for the resource request?", "what is the manager's goal for the feedback loop?", 'what are the key point after a meeting, where credibilitiy is built or lost?', 'what is key for successful immediate follow-up after a meeting?', 'what is key to deliver on deadlines?', 'what is key to deliver consistent honesty?', 'what are the key check points for personal reflection right after a one-to-one meeting with your boss?', 'what is the reaction check?', 'what is the compliance check?', 'what is the adjustment check?'], 'answer': ['medium, detail and priority checks', 'Is your boss a Reader (send the agenda/data 24 hours early) or a Listener (be prepared to present clearly and provide the memo afterward)?', 'Does your boss want the "big picture" or are they "high-involvement" (wanting the technical specifics)?', 'What is the one thing your boss is currently under pressure to deliver to their boss? How does your update relate to that?', 'the "big picture" update, expectation calibration, the "no surprises" brief, resource request, feedback loop', 'Align your current output with their organizational goals: "To support your goal of [Project X], here is where my team stands..."', 'Ensure your "mental map" of the job matches theirs.: "I’m prioritizing A over B this week to meet the deadline. Does that align with your view?"', 'Share bad news or potential risks early.: "I wanted to flag a potential delay in [Project Y] so we can adjust before it impacts the quarter."', 'Use "blue chips" selectively for what you truly need.: "I need your influence to get the [Department] to approve this. It’s critical for our Q3 target."', 'Check for blind spots.: "What’s one thing I could do differently to make your job easier this month?"', 'Immediate follow-up, deliver on deadlines, consistent honesty', "Send a brief summary of agreed-upon expectations. This prevents misunderstandings, like where one person thinks a decision was made and the other doesn't.", "If you committed to a date during the meeting, meet it. If you can't, flag the slip immediately.", 'If the "Big Picture" changes, don\'t shade the truth to look better in the short term.', 'reaction, compliance and adjustement checks', 'Did I get defensive when challenged (Counterdependence)?', 'Did I agree to an unrealistic deadline just to please them (Overdependence)?', 'How can I adjust my "discursive" or "intuitive" style next time to better fit their "concise" or "formal" style?']}

df = pd.DataFrame(df_dictionary)

# 2. Page Configuration 
st.set_page_config(page_title="One-to-one meeting with your boss", layout="wide")
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# 2.5 Rule Selector at the Top
selected_rule = st.selectbox(
    "📌 Select a phase for a one-to-one meeting with your boss",
    options=df['rule'].unique()
)

# Filter dataframe based on selected rule
filtered_df = df[df['rule'] == selected_rule].reset_index(drop=True)

# 3. Initialize Session State
if 'current_index' not in st.session_state:
    st.session_state.current_index = random.randint(0, len(filtered_df) - 1)
if 'show_ans' not in st.session_state:
    st.session_state.show_ans = False

# 4. Functions for Logic
def next_question():
    st.session_state.current_index = random.randint(0, len(filtered_df) - 1)
    st.session_state.show_ans = False

def toggle_answer():
    st.session_state.show_ans = True

# 5. Display UI
row = filtered_df.iloc[st.session_state.current_index]

with st.container(border=True):
    st.subheader(row['rule'])
    
    st.markdown(f"<p style='font-size: 24px;'>❓ {row['question']}</p>", unsafe_allow_html=True)
    
if st.session_state.show_ans:
        # Custom CSS for a large green box
        st.markdown(
            f"""
            <div style="
                background-color: #d4edda; 
                color: #155724; 
                padding: 20px; 
                border-radius: 10px; 
                border: 1px solid #c3e6cb;
                margin-top: 20px;">
                <span style="font-size: 24px; font-weight: 500;">{row['answer']}</span>
            </div>
            """, 
            unsafe_allow_html=True
        )

# 6. Buttons
# This creates 3 columns: empty space, the buttons, and more empty space
# The middle column (ratio of 2) holds the buttons
#left_spacer, center, right_spacer = st.columns([1, 2, 1])
left_spacer, center, right_spacer = st.columns([2, 2, 2])

with center:
    col1, col2 = st.columns(2)
    with col1:
        st.button("💡 Answer", on_click=toggle_answer, use_container_width=True)
    with col2:
        st.button("➡️ Next", on_click=next_question, use_container_width=True)
