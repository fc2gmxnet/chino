# Learn fundamentals of sales
# It is a sales training
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# Data initialization
df_dictionary = {'rule': ['Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Dominance (D): Eagle', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Influence (I): Parrot', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Steadiness (S): Dove', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl', 'Conscientiousness (C): Owl'], 'question': ['What is the core driver of a D style?', 'What does a D style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "S" (Steadiness) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with a D?', 'How does a D (eagle) view an I (parrot)?', 'How does a D (eagle) view an S (dove)?', 'How does a D (eagle) view a C (owl)?', 'How does a D (eagle) view others?', 'What is the core driver of an I style?', 'What does an I style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "C" (Conscientiousness) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with an I?', 'How does an I (parrot) view a D (eagle)?', 'How does an I (parrot) view an S (dove)?', 'How does an I (parrot) view a C (owl)?', 'How does an I (parrot) view others?', 'What is the core driver of an S style?', 'What does an S style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "D" (Dominance) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with an S?', 'How does an S (dove) view a D (eagle)?', 'How does an S (dove) view an I (parrot)?', 'How does an S (dove) view a C (owl)?', 'How does an S (dove) view others?', 'What is the core driver of a C style?', 'What does a C style want most?', 'What is their primary psychological need?', 'What is their greatest fear?', 'What are their primary strengths?', 'What are their common weaknesses?', 'How do they communicate verbally?', 'What is their writing style (email)?', 'What is their typical body language?', 'How do they handle conflict?', 'What motivates them?', 'How do they view "I" (Influence) types?', 'What is their ideal environment?', 'How do you gain their respect?', 'What is the #1 recommendation for dealing with a C?', 'How does a C (owl) view a D (eagle)?', 'How does a C (owl) view an I (parrot)?', 'How does a C (owl) view an S (dove)?', 'How does a C (owl) view others?'], 'answer': ['Overcoming opposition and achieving results.', 'Power, authority, and prestige.', 'To be in control of their environment and destiny.', 'Being taken advantage of or losing control.', 'Decisiveness, goal-orientation, and high self-confidence.', 'Impatience, lack of empathy, and being overly demanding.', 'Direct, brief, and often forceful; they get straight to the point.', 'Short, bulleted, focus on action items, minimal small talk.', 'Leaning forward, intense eye contact, forceful gestures.', 'They lean into it; they see it as a way to clear the air or win.', 'Competition, winning, and new challenges.', 'Often as too slow or resistant to necessary change.', 'Fast-paced, results-oriented, rewards individual achievement.', 'By being competent, standing your ground, and delivering results.', 'Be brief, be bright, and be gone. Focus on "What."', 'As great for morale, but too talkative and lacking focus on the bottom line.', 'As loyal and supportive, but far too slow to change and lacking initiative.', 'As technically accurate, but prone to "analysis paralysis" and slowing down progress.', "The D's priority is Results and Efficiency. They view anyone who slows down the process with skepticism", 'Persuading and influencing others through social interaction.', 'Popularity, social recognition, and approval.', 'To be included and liked by the group.', 'Social rejection or being ignored.', 'Optimism, enthusiasm, and excellent communication skills.', 'Disorganization, lack of follow-through, and being overly emotional.', 'Expressive, animated, and story-driven; they talk more than listen.', 'Informal, friendly, uses emojis/exclamation points, long-winded.', 'Open gestures, frequent smiling, relaxed and approachable.', 'They try to "smooth it over" or avoid it to maintain harmony.', 'Public praise, social activities, and variety.', 'Often as cold, overly critical, or "boring."', 'Collaborative, social, and free from rigid routine.', 'Show personal interest in them and acknowledge their ideas.', 'Allow time for socializing. Focus on "Who."', 'As impressive and decisive, but often blunt, "pushy," or insensitive to feelings.', 'As wonderful and kind, but sometimes too quiet, unexciting, or overly cautious.', 'As highly intelligent, but emotionally cold, perfectionistic, and overly critical.', 'The I\'s priority is Enthusiasm and Connection. They view anyone who is too "all business" as a threat to the group dynamic.', 'Maintaining a stable and harmonious environment.', 'Sincerity, stability, and the "status quo."', 'Security and time to adjust to change.', 'Sudden change or loss of stability.', 'Reliability, active listening, and patience.', 'Indecisiveness, resistance to change, and people-pleasing.', 'Calm, steady, and gentle; they are excellent listeners.', 'Warm and appreciative; starts with personal check-ins.', 'Relaxed, non-threatening, frequent nodding in agreement.', 'They internalize it or yield to keep the peace; conflict-averse.', 'A sense of belonging, helping others, and predictable routine.', 'Often as aggressive, insensitive, or scary.', 'Calm, supportive, and predictable.', 'By being kind, consistent, and showing genuine care.', 'Don’t rush them; provide a plan for change. Focus on "How."', 'As intimidating and aggressive; they move too fast and cause unnecessary stress.', 'As fun and charming, but often exhausting, loud, and potentially unreliable.', 'As knowledgeable and professional, but far too rigid, formal, and rule-bound.', 'The S\'s priority is Stability and Cooperation. They view "fast" styles as unpredictable or even dangerous to the team\'s peace.', 'Ensuring accuracy and maintaining high standards.', 'Correctness, quality, and logic.', 'To be right and to have all the facts.', 'Criticism of their work or being wrong.', 'Precision, analytical thinking, and attention to detail.', 'Perfectionism, over-analyzing, and being emotionally detached.', 'Formal, objective, and fact-based; speak with precision.', 'Highly detailed, structured, formal, focus on data.', 'Controlled, minimal gestures, "poker face."', 'Rely on data and rules; may withdraw to gather more facts.', 'Gaining expertise, precision tasks, and high-quality results.', 'Often as superficial, disorganized, or "all talk."', 'Quiet, orderly, and rewards expertise/quality.', 'Be accurate, prepared with data, and respect their expertise.', 'Give them data and space. Focus on "Why."', 'As decisive, but reckless; they make snap judgments without enough data.', 'As charming and social, but disorganized, superficial, and "all talk."', 'As pleasant and stable, but stubborn and resistant to logical, data-backed change.', 'The C\'s priority is Logic and Quality. They view anyone who is "messy" (either emotionally or organizationally) as unprofessional.']}

df = pd.DataFrame(df_dictionary)

# 2. Page Configuration 
st.set_page_config(page_title="Sales Training", layout="wide")
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# 2.5 Rule Selector at the Top
selected_rule = st.selectbox(
    "📌 Select a Rule",
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
