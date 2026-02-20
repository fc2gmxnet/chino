# The dynamics of taking charge
# Book more realistic than "The first 90 days"
# Some views are somehow old-fashioned, it was written in the 1980's
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'question': ['What is the core definition of "taking charge"?', 'What are the five stages of this process?', 'How long does the full process typically take?', 'What characterizes the "Taking Hold" stage?', 'What is the primary focus during "Immersion"?', 'What happens during the "Reshaping" stage?', 'What is the purpose of the "Consolidation" stage?', 'What marks the "Refinement" stage?', 'What is the "three-wave phenomenon"?', 'Which wave of change is typically the largest?', 'Which wave is invariably the smallest?', 'Why does change activity decrease during Immersion?', 'What are the two most common causes of failure?', 'What is the "Lone Ranger Syndrome"?', 'What three tasks do successful managers handle well?', 'How does being an "industry insider" affect the transition?', 'What is a "cognitive map"?', 'What challenge do "industry outsiders" face?', 'What is "evaluative learning"?', 'Why is developing "mutual expectations" with a boss critical?', 'What role does "trust" play in the transition?', 'How do "rallying cries" help a new manager?', 'Why might a turnaround situation reduce subordinate resentment?', 'What replaces "resentment" in many turnaround situations?', 'What is the "myth of the all-purpose general manager"?', 'How does a "poorly defined going-in mandate" affect success?', 'Why do interpersonal relationships take time to develop?', 'What is "testing the limits of influence"?', 'Why is it risky to resolve differences with a subordinate prematurely?', 'What are "assimilation meetings"?', 'Why can fast-track assignments be problematic?', 'How does a manager\'s "cognitive map" change in the Immersion stage?', 'What triggers the transition to the "Reshaping" stage?', 'What tools might managers use to pave the way for Reshaping?', 'Why do the major changes occur in the "second wave"?', 'What characterizes learning in the "Consolidation" stage?', 'Why does the wave pattern diminish after 30 months?', 'What happens if a manager makes major changes based on partial diagnosis?', 'How do "people skills" impact transition success?', 'What should companies consider when assigning an "industry outsider"?', 'Can a manager\'s past experience be "too relevant"?', 'What is "symbolic behavior" in a transition?', 'Why is "decisiveness" viewed positively by subordinates?', 'What is the impact of geographic distance on relationship building?', 'How does "orientational learning" differ for an insider vs. outsider?', 'What is "reflective learning"?', 'How do managers handle "obvious competence problems"?', 'What determines the length of time in each stage?', 'Why is the taking-charge process described as "idiosyncratic"?', 'In the final analysis, who is responsible for transition success?'], 
                 'answer': ['It is a process where managers progress through predictable stages of learning and action to gain mastery over a new assignment.', '(1) Taking Hold, (2) Immersion, (3) Reshaping, (4) Consolidation, and (5) Refinement.', 'In successful cases, it generally takes between two and a half to three years.', 'It is a period of orientational learning and corrective action on the most obvious organizational problems.', 'Deeper, reflective learning to see subtleties and patterns not visible during the initial entry period.', 'The manager acts on their deeper understanding to implement major structural or organizational changes.', 'To follow through on, correct, and stabilize the changes made during the Reshaping stage.', 'Learning becomes routine and focuses on day-to-day operations; the manager is no longer considered "new."', 'The observation that organizational changes cluster into three waves corresponding to the Taking Hold, Reshaping, and Consolidation stages.', 'The second wave, which occurs during the Reshaping stage.', 'The third wave, occurring during the Consolidation stage.', 'Because the manager has already fixed obvious issues and is now focused on finer-grained learning and analysis.', 'A lack of relevant prior experience and poor working relationships with key people.', 'A failure pattern where managers try to solve problems alone rather than involving their team.', 'Diagnosing problems, building a team with shared expectations, and implementing timely changes.', 'Insiders have a better "cognitive map" and can implement major reorganizations much faster than outsiders.', 'A mental model of the organization, its key actors, and the factors affecting its performance.', 'They often feel overwhelmed by the amount of basic orientational learning, such as technical jargon.', 'Assessing key subordinates, identifying where problems lie, and determining priorities.', "Failing to do so can lead to major style conflicts and a lack of support for the manager's initiatives.", "Trust develops as managers and subordinates assess each other's judgment, integrity, and consistency over time.", 'They serve as symbols (e.g., "fixing the mechanics") to communicate and reinforce new organizational priorities.', 'The visible trouble in the organization makes subordinates more willing to accept an outsider’s leadership.', 'A sense of fear regarding job security, which the manager must counter by developing "pockets of confidence."', 'The belief that a manager can succeed in any industry or function without relevant prior experience.', 'It creates ambiguity that can stall the transition process and lead to misaligned goals.', 'They require initial orientation, assessment of limitations, and the testing/negotiating of differences.', "A process where managers and subordinates assess how much they can influence each other's decisions.", 'Managers risk losing the subordinate if their diagnosis is wrong, damaging their own credibility.', 'Facilitated meetings that allow issues and expectations to be raised quickly early in a transition.', 'They are often too short to allow a manager to progress beyond Immersion, missing the organizational payoffs of later stages.', 'It becomes fuller and more detailed, allowing for a refined concept of what truly needs to improve.', 'The development of a refined concept for organizational improvement that the manager is now ready to act upon.', 'Internal task forces, outside consultants, or both to validate their new strategy.', 'Because they are based on the deeper, more accurate diagnostic work performed during Immersion.', 'It focuses on the results of the major changes made in Reshaping and identifies where adjustments are needed.', 'Because the manager has mastered the situation and there are fewer opportunities for significant new learning.', 'The changes are often perceived as inappropriate or ineffective by both superiors and subordinates.', 'They are essential for building the effective working relationships required to implement any structural change.', 'The organization must accept a "cost" in terms of the added time the manager will need for basic learning.', 'Yes, it can lead them to make assumptions that they fail to test properly during the new Taking Hold stage.', 'Actions taken to communicate priorities, such as an early focus on finance or specific product lines.', 'It contributes to an aura of competence and leadership during a period of organizational uncertainty.', 'It can make the testing and negotiation of mutual expectations more difficult and superficial.', 'Insiders focus on unfamiliar departments, while outsiders must learn the entire business from scratch.', 'The ability to look back on early actions and see why certain problems persist or why new ones emerged.', 'Most handle these issues during the initial Taking Hold stage before moving into deeper learning.', 'The speed of learning and the specific action issues of the situation, not just a fixed schedule.', "Because it carries the manager's unique mark and depends heavily on the specific organizational context.", 'Ultimately, the success of the transition rests in the hands of the managers themselves.']}
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
