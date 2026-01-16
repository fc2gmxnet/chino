# The dynamics of taking charge
# Book more realistic than "The first 90 days"
# Some views are somehow old-fashioned, it was written in the 1980's
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# Data initialization
df_dictionary = {'question': ['What is the core definition of "taking charge"?', 'What are the five stages of this process?', 'How long does the full process typically take?', 'What characterizes the "Taking Hold" stage?', 'What is the primary focus during "Immersion"?', 'What happens during the "Reshaping" stage?', 'What is the purpose of the "Consolidation" stage?', 'What marks the "Refinement" stage?', 'What is the "three-wave phenomenon"?', 'Which wave of change is typically the largest?', 'Which wave is invariably the smallest?', 'Why does change activity decrease during Immersion?', 'What are the two most common causes of failure?', 'What is the "Lone Ranger Syndrome"?', 'What three tasks do successful managers handle well?', 'How does being an "industry insider" affect the transition?', 'What is a "cognitive map"?', 'What challenge do "industry outsiders" face?', 'What is "evaluative learning"?', 'Why is developing "mutual expectations" with a boss critical?', 'What role does "trust" play in the transition?', 'How do "rallying cries" help a new manager?', 'Why might a turnaround situation reduce subordinate resentment?', 'What replaces "resentment" in many turnaround situations?', 'What is the "myth of the all-purpose general manager"?', 'How does a "poorly defined going-in mandate" affect success?', 'Why do interpersonal relationships take time to develop?', 'What is "testing the limits of influence"?', 'Why is it risky to resolve differences with a subordinate prematurely?', 'What are "assimilation meetings"?', 'Why can fast-track assignments be problematic?', 'How does a manager\'s "cognitive map" change in the Immersion stage?', 'What triggers the transition to the "Reshaping" stage?', 'What tools might managers use to pave the way for Reshaping?', 'Why do the major changes occur in the "second wave"?', 'What characterizes learning in the "Consolidation" stage?', 'Why does the wave pattern diminish after 30 months?', 'What happens if a manager makes major changes based on partial diagnosis?', 'How do "people skills" impact transition success?', 'What should companies consider when assigning an "industry outsider"?', 'Can a manager\'s past experience be "too relevant"?', 'What is "symbolic behavior" in a transition?', 'Why is "decisiveness" viewed positively by subordinates?', 'What is the impact of geographic distance on relationship building?', 'How does "orientational learning" differ for an insider vs. outsider?', 'What is "reflective learning"?', 'How do managers handle "obvious competence problems"?', 'What determines the length of time in each stage?', 'Why is the taking-charge process described as "idiosyncratic"?', 'In the final analysis, who is responsible for transition success?'], 
                 'answer': ['It is a process where managers progress through predictable stages of learning and action to gain mastery over a new assignment.', '(1) Taking Hold, (2) Immersion, (3) Reshaping, (4) Consolidation, and (5) Refinement.', 'In successful cases, it generally takes between two and a half to three years.', 'It is a period of orientational learning and corrective action on the most obvious organizational problems.', 'Deeper, reflective learning to see subtleties and patterns not visible during the initial entry period.', 'The manager acts on their deeper understanding to implement major structural or organizational changes.', 'To follow through on, correct, and stabilize the changes made during the Reshaping stage.', 'Learning becomes routine and focuses on day-to-day operations; the manager is no longer considered "new."', 'The observation that organizational changes cluster into three waves corresponding to the Taking Hold, Reshaping, and Consolidation stages.', 'The second wave, which occurs during the Reshaping stage.', 'The third wave, occurring during the Consolidation stage.', 'Because the manager has already fixed obvious issues and is now focused on finer-grained learning and analysis.', 'A lack of relevant prior experience and poor working relationships with key people.', 'A failure pattern where managers try to solve problems alone rather than involving their team.', 'Diagnosing problems, building a team with shared expectations, and implementing timely changes.', 'Insiders have a better "cognitive map" and can implement major reorganizations much faster than outsiders.', 'A mental model of the organization, its key actors, and the factors affecting its performance.', 'They often feel overwhelmed by the amount of basic orientational learning, such as technical jargon.', 'Assessing key subordinates, identifying where problems lie, and determining priorities.', "Failing to do so can lead to major style conflicts and a lack of support for the manager's initiatives.", "Trust develops as managers and subordinates assess each other's judgment, integrity, and consistency over time.", 'They serve as symbols (e.g., "fixing the mechanics") to communicate and reinforce new organizational priorities.', 'The visible trouble in the organization makes subordinates more willing to accept an outsider’s leadership.', 'A sense of fear regarding job security, which the manager must counter by developing "pockets of confidence."', 'The belief that a manager can succeed in any industry or function without relevant prior experience.', 'It creates ambiguity that can stall the transition process and lead to misaligned goals.', 'They require initial orientation, assessment of limitations, and the testing/negotiating of differences.', "A process where managers and subordinates assess how much they can influence each other's decisions.", 'Managers risk losing the subordinate if their diagnosis is wrong, damaging their own credibility.', 'Facilitated meetings that allow issues and expectations to be raised quickly early in a transition.', 'They are often too short to allow a manager to progress beyond Immersion, missing the organizational payoffs of later stages.', 'It becomes fuller and more detailed, allowing for a refined concept of what truly needs to improve.', 'The development of a refined concept for organizational improvement that the manager is now ready to act upon.', 'Internal task forces, outside consultants, or both to validate their new strategy.', 'Because they are based on the deeper, more accurate diagnostic work performed during Immersion.', 'It focuses on the results of the major changes made in Reshaping and identifies where adjustments are needed.', 'Because the manager has mastered the situation and there are fewer opportunities for significant new learning.', 'The changes are often perceived as inappropriate or ineffective by both superiors and subordinates.', 'They are essential for building the effective working relationships required to implement any structural change.', 'The organization must accept a "cost" in terms of the added time the manager will need for basic learning.', 'Yes, it can lead them to make assumptions that they fail to test properly during the new Taking Hold stage.', 'Actions taken to communicate priorities, such as an early focus on finance or specific product lines.', 'It contributes to an aura of competence and leadership during a period of organizational uncertainty.', 'It can make the testing and negotiation of mutual expectations more difficult and superficial.', 'Insiders focus on unfamiliar departments, while outsiders must learn the entire business from scratch.', 'The ability to look back on early actions and see why certain problems persist or why new ones emerged.', 'Most handle these issues during the initial Taking Hold stage before moving into deeper learning.', 'The speed of learning and the specific action issues of the situation, not just a fixed schedule.', "Because it carries the manager's unique mark and depends heavily on the specific organizational context.", 'Ultimately, the success of the transition rests in the hands of the managers themselves.']}
df = pd.DataFrame(df_dictionary)

# 2. Page Configuration 
st.set_page_config(page_title="Taking Charge Training", layout="wide")
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# 3. Initialize Session State
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0   # start at the first row
    #st.session_state.current_index = random.randint(0, len(df) - 1) # start at a random row
if 'show_ans' not in st.session_state:
    st.session_state.show_ans = False

# 4. Functions for Logic
def next_question():
    # move to the next row in order
    st.session_state.current_index += 1
    if st.session_state.current_index >= len(df):
        st.session_state.current_index = 0   # loop back to start if at the end
    #st.session_state.current_index = random.randint(0, len(df) - 1) # Original code, to pick questions randomly
    st.session_state.show_ans = False

def toggle_answer():
    st.session_state.show_ans = True

# 5. Display UI
row = df.iloc[st.session_state.current_index]

with st.container(border=True):
    st.subheader('The dynamics of taking charge')
    
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
