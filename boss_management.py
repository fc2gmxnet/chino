# Managing your boss
# Book by John Gabarro (Harvard Business Review)
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'question': ['What is the core definition of "managing your boss"?', 'Is managing upward just "apple polishing" or "politics"?', 'Why do many talented managers ignore this aspect of their job?', 'What is the risk of a "passively reactive" stance toward a boss?', 'What was the fundamental error of the manager in the book?', 'How does "mutual dependence" work in this context?', 'Why shouldn\'t a manager see themselves as "self-sufficient"?', 'What is the "dangerous expectation" regarding a boss’s help?', 'What are the two pillars of managing a healthy relationship?', 'What context must you understand about your boss?', 'How do "blind spots" affect the relationship?', 'Why is it a mistake to take information from a boss at "face value"?', 'How do you identify a boss\'s "work style"?', 'What is a "Reader" boss?', 'What is a "Listener" boss?', 'How do you manage a "high-involvement" boss?', 'How do you manage a boss who prefers to delegate?', 'Why is self-awareness critical for a manager?', 'What is "counterdependent" behavior?', 'What is "overdependent" behavior?', 'How does a manager handle frustrations with a boss?', 'How can you get a vague boss to express expectations?', 'Why is it important to communicate your own expectations?', 'How should you handle a boss who dislikes "bad news"?', 'Why is "dependability" more important than "peak success"?', 'What is the most "troubling trait" a subordinate can have?', "How should a manager use their boss's time?", 'What should you do if your boss has a different personality?', 'What role does a manager play in their boss’s weaknesses?', 'What is the ultimate responsibility of a manager?', 'How do you audit your own style?'], 'answer': ['It is the process of consciously working with your superior to obtain the best possible results for you, the boss, and the company.', 'No. It is not about manipulation; it is about managing a relationship of mutual dependence between two fallible human beings.', 'They often view management only as a top-down activity or assume they should be self-sufficient and reactive toward their own bosses.', 'It leads to misunderstandings, missed goals, and can ultimately lead to the manager being fired, as seen in the Bonnevie/Gibbons case.', 'He assumed his boss would magically know what information he needed and failed to realize he was responsible for managing the relationship.', 'The boss needs your cooperation and honesty to succeed, and you need the boss’s resources and information to do your job well.', 'Because the boss is the critical link to the rest of the organization, securing resources and ensuring your priorities align with company needs.', 'The belief that a boss will instinctively provide all the help you need. Effective managers assume responsibility for seeking out what they need.', '1) Understanding the other person and yourself, and 2) Using that info to develop a compatible work style and mutual expectations.', 'Their goals/objectives, the pressures they face from their own superiors, and their personal strengths and weaknesses.', 'Every boss has them; if you don’t identify where your boss is weak, you can’t provide the support or information necessary to protect the team.', 'Bosses are under pressure and may have conflicting priorities. You must actively clarify their objectives rather than making assumptions.', 'By observing how they prefer to receive information (memos vs. meetings), how they handle conflict, and their level of desired involvement.', 'A boss who prefers to receive information in report form first so they can study it before discussing it.', 'A boss who prefers an in-person briefing where they can ask questions, followed by a summary memo.', 'Satisfy their need for control by touching base on an ad hoc basis and including them in decisions at your initiative.', 'Keep them informed of major changes or problems, but handle the day-to-day independently as they expect.', "You cannot change your personality or your boss's, but you can control your reactions to make the relationship more effective.", 'An instinctive rebellion against authority where the manager sees the boss as an enemy or an obstacle to be circumvented.', 'Seeing the boss as an all-wise parent and complying with every decision, even when you know a decision is poor or ill-informed.', 'By reflecting on their own predisposition toward authority and adjusting their behavior to be more objective and less impulsive.', 'Draft a detailed memo of what you think the expectations are and schedule a face-to-face meeting to review and refine them.', 'To ensure your standards are realistic and to influence the boss to value the goals that are most important to your department.', 'Find indirect ways to feed them data (like reports) or ensure that potential problems are flagged immediately to avoid "surprises."', 'A boss needs to rely on a consistent output; repeated missed deadlines or "surprises" destroy the trust needed for delegation.', 'Dishonesty. Even "shading the truth" undermines credibility and forces the boss to check every decision you make.', 'Selectively. Do not waste "blue chips" (influence/time) on trivial issues; save those resources for major goals.', 'Focus on work style compatibility rather than personality change. Adjust your delivery (e.g., be conciser if the boss is impatient).', 'An effective manager helps compensate for the boss’s weaknesses (e.g., monitoring staff issues if the boss is poor at it).', 'To be responsible for what they achieve, which requires managing every relationship they depend on—especially the one with their boss.', 'Ask yourself if you tend to be "counterdependent" (rebelling) or "overdependent" (blindly following). Awareness is 90% of the cure.']}
df = pd.DataFrame(df_dictionary)

# Column indices
# If columna_leccion is not available, set it to None
columna_leccion = None
columna_pregunta = 0
columna_respuesta = 1
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
    selected_lesson = st.selectbox("Select Chapter", sorted(df.iloc[:, columna_leccion].unique()))
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
