# Learn fundamentals of job interview psychology
# My admiration to the teachings from:
# https://youtu.be/m4U4iDuZaDk?si=wfMF7KEkQ_4uXD6Y
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# Data initialization
df_dictionary = {'rule': ['Psychology in job interviews', 'Psychology in job interviews', '1: Cognitive Ease (being the "easy" choice', '1: Cognitive Ease (being the "easy" choice', '1: Cognitive Ease (being the "easy" choice', '2: Halo Effect (a first impression that creates an overall positive bias)', '2: Halo Effect (a first impression that creates an overall positive bias)', '2: Halo Effect (a first impression that creates an overall positive bias)', '3: Likability (affinity bias)', '3: Likability (affinity bias)', '3: Likability (affinity bias)', '4: Authority Bias (perceived over actual expertise)', '4: Authority Bias (perceived over actual expertise)', '4: Authority Bias (perceived over actual expertise)', '5: Confirmation Bias (winning in the first 90 seconds)', '5: Confirmation Bias (winning in the first 90 seconds)', '5: Confirmation Bias (winning in the first 90 seconds)', '6: Commitment Principle (locking an up-front contract)', '6: Commitment Principle (locking an up-front contract)', '6: Commitment Principle (locking an up-front contract)'], 'question': ['Why do "average" candidates sometimes get offers over more qualified ones?', 'How quickly do hiring managers make a judgment about a candidate?', 'What does "Cognitive Ease" mean in the context of a job search?', 'How can I sabotage my "Cognitive Ease" during an interview?', 'What is the best "underrated" tactic for applying this principle?', 'How does the Halo Effect help me in an interview?', 'Can I trigger the Halo Effect before the interview even starts?', 'Why is the "impression" more important than the skills?', 'Is the hiring process truly objective and fair?', "What is a common mistake that kills a candidate's likability?", 'Does being likable mean I have to be "overly friendly"?', 'What is Authority Bias?', 'How do I demonstrate authority during an interview answer?', 'What is the "EBC Method" for building authority?', 'How does Confirmation Bias work during an interview?', 'Why do some interviews feel like a struggle to "get through"?', 'How can I ensure I use this principle to my advantage?', 'What is the Commitment Principle?', 'What is the "Commitment Lock" technique?', 'What specific script should I use for the "Commitment Lock"?'], 'answer': ['Hiring is often emotional and instinctive rather than purely logical. If a candidate understands human psychology, they can make the interviewer feel confident and comfortable, which often outweighs technical skills.', 'Unconscious judgments happen fast—often within the first 3 minutes, and sometimes the fundamental "yes" or "no" decision is made within the first 60 to 90 seconds.', 'Humans naturally gravitate toward what feels easy. If your resume is clear, your LinkedIn is easy to read, and your interview answers get straight to the point, you create "ease" for the recruiter.', 'By "waffling" or letting your answers drag on too long. When you don\'t get to the point, the interviewer mentally checks out. Getting defensive or bad-mouthing past employers also creates friction.', "Simply being likable and easy to deal with. Matching the interviewer's energy and focusing on their needs makes you the path of least resistance for the hire.", 'If an interviewer likes one specific thing about you (e.g., clear communication), they subconsciously assume you are good at everything else (e.g., competence and organization).', 'Yes. By building a strong online presence or personal brand, recruiters will often assume you already know your craft and treat you with more respect during the initial meeting.', 'Because hiring is emotional before it is logical. If you create a powerful first impression, the interviewer will spend the rest of the time looking for reasons to believe you are the right fit.', 'No. Despite HR efforts, unconscious bias always creeps in. Humans hire humans, and people ultimately hire those they would actually enjoy working with every day.', 'Complaining about the job market, recruiters, or a previous manager early in the conversation. This makes the interviewer worry that you will be a source of drama in the future.', 'No. It’s about matching the interviewer’s energy, respecting their time, and showing that you can get things done without unnecessary drama.', 'We are wired to trust people who appear to be experts. In hiring, the person who looks and sounds like an authority often gets fast-tracked over those who lack a professional presence.', 'Use the STAR format for structure, answer with clarity, and showcase ownership. Speak in terms of what you delivered specifically, rather than just what the team did.', 'Entertaining content builds an audience, Valuable content builds trust, and Credible content builds authority. This mix establishes your perceived value before you walk in the door.', 'People look for evidence to support the opinion they already have. If you start strong, the interviewer’s brain will scan for reasons to "confirm" you are the right choice.', 'If you start weak, the interviewer’s brain looks for reasons to back that negative belief. You end up spending the whole interview trying to dig yourself out of a hole.', 'Start the interview strong with confidence, clarify questions before responding, and align your answers with the specific impression you want to leave behind.', 'People are much more likely to follow through on an action if they have verbally committed to it. You can use this to turn an interview into a firm next step or offer.', 'At the end of the interview, you verbally lock in three things: the next steps, the exact timeframe for an update, and permission to follow up if that timeframe is missed.', '"Before I go, could you walk me through the next steps and when I should expect an update? ... Perfect, and if I don\'t hear anything by then, is it okay to give you a polite nudge?"']}

df = pd.DataFrame(df_dictionary)

# 2. Page Configuration 
st.set_page_config(page_title="Sales Training", layout="wide")
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# 3. Initialize Session State
if 'current_index' not in st.session_state:
    st.session_state.current_index = random.randint(0, len(df) - 1)
if 'show_ans' not in st.session_state:
    st.session_state.show_ans = False

# 4. Functions for Logic
def next_question():
    st.session_state.current_index = random.randint(0, len(df) - 1)
    st.session_state.show_ans = False

def toggle_answer():
    st.session_state.show_ans = True

# 5. Display UI
row = df.iloc[st.session_state.current_index]

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
