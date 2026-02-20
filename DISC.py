# Learn DISC to improve communication and relationship with other people
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'rule': ['Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl'], 'question': ['What is the core driver of a D style?', 'What does a D style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "S" (Steadiness) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with a D?', 'How does a D (eagle) view an I (parrot)?', 'How does a D (eagle) view an S (dove)?', 'How does a D (eagle) view a C (owl)?', 'How does a D (eagle) view others?', 'What is the core driver of an I style?', 'What does an I style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "C" (Conscientiousness) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with an I?', 'How does an I (parrot) view a D (eagle)?', 'How does an I (parrot) view an S (dove)?', 'How does an I (parrot) view a C (owl)?', 'How does an I (parrot) view others?', 'What is the core driver of an S style?', 'What does an S style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "D" (Dominance) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with an S?', 'How does an S (dove) view a D (eagle)?', 'How does an S (dove) view an I (parrot)?', 'How does an S (dove) view a C (owl)?', 'How does an S (dove) view others?', 'What is the core driver of a C style?', 'What does a C style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "I" (Influence) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with a C?', 'How does a C (owl) view a D (eagle)?', 'How does a C (owl) view an I (parrot)?', 'How does a C (owl) view an S (dove)?', 'How does a C (owl) view others?'], 'answer': ['Overcoming opposition and achieving results.', 'Power, authority, and prestige.', 'To be in control of their environment and destiny.', 'Being taken advantage of or losing control.', 'Decisiveness, goal-orientation, and high self-confidence.', 'Impatience, lack of empathy, and being overly demanding.', 'Direct, brief, and often forceful; they get straight to the point.', 'Short, bulleted, focus on action items, minimal small talk.', 'Leaning forward, intense eye contact, forceful gestures.', 'They lean into it; they see it as a way to clear the air or win.', 'Competition, winning, and new challenges.', 'Often as too slow or resistant to necessary change.', 'Fast-paced, results-oriented, rewards individual achievement.', 'By being competent, standing your ground, and delivering results.', 'Be brief, be bright, and be gone. Focus on "What."', 'As great for morale, but too talkative and lacking focus on the bottom line.', 'As loyal and supportive, but far too slow to change and lacking initiative.', 'As technically accurate, but prone to "analysis paralysis" and slowing down progress.', "The D's priority is Results and Efficiency. They view anyone who slows down the process with skepticism", 'Persuading and influencing others through social interaction.', 'Popularity, social recognition, and approval.', 'To be included and liked by the group.', 'Social rejection or being ignored.', 'Optimism, enthusiasm, and excellent communication skills.', 'Disorganization, lack of follow-through, and being overly emotional.', 'Expressive, animated, and story-driven; they talk more than listen.', 'Informal, friendly, uses emojis/exclamation points, long-winded.', 'Open gestures, frequent smiling, relaxed and approachable.', 'They try to "smooth it over" or avoid it to maintain harmony.', 'Public praise, social activities, and variety.', 'Often as cold, overly critical, or "boring."', 'Collaborative, social, and free from rigid routine.', 'Show personal interest in them and acknowledge their ideas.', 'Allow time for socializing. Focus on "Who."', 'As impressive and decisive, but often blunt, "pushy," or insensitive to feelings.', 'As wonderful and kind, but sometimes too quiet, unexciting, or overly cautious.', 'As highly intelligent, but emotionally cold, perfectionistic, and overly critical.', 'The I\'s priority is Enthusiasm and Connection. They view anyone who is too "all business" as a threat to the group dynamic.', 'Maintaining a stable and harmonious environment.', 'Sincerity, stability, and the "status quo."', 'Security and time to adjust to change.', 'Sudden change or loss of stability.', 'Reliability, active listening, and patience.', 'Indecisiveness, resistance to change, and people-pleasing.', 'Calm, steady, and gentle; they are excellent listeners.', 'Warm and appreciative; starts with personal check-ins.', 'Relaxed, non-threatening, frequent nodding in agreement.', 'They internalize it or yield to keep the peace; conflict-averse.', 'A sense of belonging, helping others, and predictable routine.', 'Often as aggressive, insensitive, or scary.', 'Calm, supportive, and predictable.', 'By being kind, consistent, and showing genuine care.', 'Don’t rush them; provide a plan for change. Focus on "How."', 'As intimidating and aggressive; they move too fast and cause unnecessary stress.', 'As fun and charming, but often exhausting, loud, and potentially unreliable.', 'As knowledgeable and professional, but far too rigid, formal, and rule-bound.', 'The S\'s priority is Stability and Cooperation. They view "fast" styles as unpredictable or even dangerous to the team\'s peace.', 'Ensuring accuracy and maintaining high standards.', 'Correctness, quality, and logic.', 'To be right and to have all the facts.', 'Criticism of their work or being wrong.', 'Precision, analytical thinking, and attention to detail.', 'Perfectionism, over-analyzing, and being emotionally detached.', 'Formal, objective, and fact-based; speak with precision.', 'Highly detailed, structured, formal, focus on data.', 'Controlled, minimal gestures, "poker face."', 'Rely on data and rules; may withdraw to gather more facts.', 'Gaining expertise, precision tasks, and high-quality results.', 'Often as superficial, disorganized, or "all talk."', 'Quiet, orderly, and rewards expertise/quality.', 'Be accurate, prepared with data, and respect their expertise.', 'Give them data and space. Focus on "Why."', 'As decisive, but reckless; they make snap judgments without enough data.', 'As charming and social, but disorganized, superficial, and "all talk."', 'As pleasant and stable, but stubborn and resistant to logical, data-backed change.', 'The C\'s priority is Logic and Quality. They view anyone who is "messy" (either emotionally or organizationally) as unprofessional.']}
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
    selected_lesson = st.selectbox("Select personality type", sorted(df.iloc[:, columna_leccion].unique()))
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
