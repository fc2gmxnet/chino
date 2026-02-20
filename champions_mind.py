# The Champion's Mind
# Book by Jim Afremow
# Minimalistic layout (ideal for mobile phones)

import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'question': ['What is the "Gold Level" for the psychological game?', 'What does "Think It, Then Ink It" mean?', 'What should be the primary focus of your goals?', 'Why focus on the process over the result?', 'How should you break down a "Dream Goal"?', 'What is the purpose of tracking your progress?', 'What is "Visualization to Actualize"?', 'Why is "polysensory" imagery important?', 'What is "Internal Imagery"?', 'What is "External Imagery"?', 'How can imagery help during injury?', 'What are "ANTs"?', 'How do you "Feed the Good Wolf"?', 'Why should you avoid "Don\'t" phrases?', 'What is the power of "Power Phrases"?', 'How do you use "Performance Cues"?', 'Where does unshakeable belief come from?', 'How do you "Flex your Confidence Muscle"?', 'Can you have "too much" confidence?', 'How do you use "Confidence Cards"?', 'How should you view your past triumphs?', 'What is "Futurizing"?', 'How do you stay in the "Now"?', 'How do you handle external distractions?', 'What is the "Zone"?', 'Why is breathing called a "remote control"?', 'What is a simple calming breathing rhythm?', 'How does breath help with "Rushing"?', 'What is the true definition of Mental Toughness?', 'Does toughness mean "trying harder"?', 'How do you build "Mental Calluses"?', 'How should you view a setback?', 'Is anxiety always bad?', 'How do you reframe "Nerves"?', 'What is the role of a Pre-Performance Routine?', 'Why is "Enjoyment" a mental skill?', 'Can you be afraid and grateful at the same time?', 'What motivates a "Mastery-Driven" athlete?', 'How do "Expansive Postures" affect you?', 'What does "Acting the Part" do?', 'What is the "Animal Predator" mindset?', 'How do you "Train like you are No. 2"?', 'What are the 3 key questions for a debrief?', 'What is the "24-Hour Rule"?', 'How do you handle a mistake mid-game?', 'How do you handle social pressure?', 'Why seek professional mental support?', 'What is the ultimate goal of mental skills?', 'What are the 3 big mental errors athletes often make?', 'What is the mental correction agains overemphasizing the outcome?', 'What is the mental correction agains trying too much?', 'What is the mental correction agains tracking the negative?', 'How to keep your sanity over success, regarding your own mind?', 'How to keep your sanity over success, regarding worrying?', 'How to keep your sanity over success, regarding apathy and inactivity?', 'How to keep your sanity over success, regarding conflicts of interest?', 'How to keep your sanity over success, regarding need for help and support?', 'How to keep your sanity over success, regarding stress and fatigue?', 'How to keep your sanity over success, regarding tense situations?', 'How to become a champion?', 'How to organize your life?'], 'answer': ['Committing to a world-class mindset where you focus on daily acts of excellence.', 'You must write your goals down on paper to make them concrete and commit to them.', 'Focus on "process goals" (actions you control) rather than just "outcome goals" (winning).', 'Because process goals reduce anxiety and keep you focused on what you can control in the moment.', 'Use small, achievable steps to build momentum and avoid feeling overwhelmed.', 'To celebrate small wins and adjust your approach as needed to maintain motivation.', 'The process of using all your senses to vividly imagine successful performances and perfect execution.', 'Involving sight, sound, smell, and touch makes the mental rehearsal more realistic for the brain.', 'Visualizing through your own eyes, as if you are actually performing the movement.', 'Seeing yourself on a mental "movie screen" to analyze form and technique.', 'It allows you to mentally practice skills and visualize healing, preventing "mental rust".', '"Automatic Negative Thoughts" that eat away at your performance and create tension.', 'By intentionally choosing positive, empowering phrases to replace negative internal dialogue.', 'The brain struggles to process negatives (e.g., "Don\'t miss"); use affirmative cues like "Stay on target".', 'Using short, present-tense phrases like "I bring it every day" to trigger motivation.', 'Use one-word commands (e.g., "Smooth") to avoid overthinking during high-pressure moments.', 'It stems from thorough preparation and a solid track record of past successes.', 'By continually working hard in training and maintaining an undying will to win.', 'Only if it leads to complacency; true confidence requires constant effort to remain elite.', 'Carry a card listing your best performances to refer to when confidence feels low.', 'Hold onto memories of triumphs long-term and let go of losses quickly.', 'Worrying about possible results or future consequences instead of the current task.', 'Direct 100% of your attention to the immediate experience and the present moment.', 'Anchor your attention back to your process or your breath whenever it wanders.', 'A state of total immersion where you are focused on the process and acting instinctively.', 'Intentional, deep breaths calm both the mental state and physical responses under stress.', 'Inhaling for five seconds through the nose and exhaling for eight seconds out the mouth.', 'It slows down your heart rate and thoughts, preventing careless mistakes made in haste.', 'The ability to remain positive and proactive in the most adverse circumstances.', "No; it's not about clenching teeth or straining, but staying disciplined and focused.", "By doing the hard things over and over again, especially when you don't feel like it.", 'As an "opportunity for an epic comeback" or a lesson to adapt and improve.', 'No; moderate anxiety can sharpen your focus and shape your performance.', 'View them as "excitement" or positive energy that shows you are ready to perform.', 'To provide familiarity and center yourself before a high-pressure event.', 'It combats the fear of failure and eliminates physical tension in the body.', 'No; an "Attitude of Gratitude" makes it impossible to remain in a state of fear.', 'The love of the sport and the desire to improve, rather than external accolades.', 'They can elevate feelings of power and tolerance for risk.', "Projecting a champion's posture signals to your brain that you are in control and ready.", 'Choosing an animal personality (like a shark) to emulate to reach the required intensity.', 'Work tirelessly and prepare as if you have just come up short of winning.', '1) What did I do that was good? 2) What needs to get better? 3) How will I do it?', 'Allow yourself one day to process a win or loss, then move on to the next task.', 'Shift your focus immediately to the "Next Play" and remain proactive.', 'Identify the source (fans, family) and return your focus to your personal "Why".', 'Champions are not afraid to use every resource available to gain a mental edge.', 'To become the "best version of yourself" in the game of life.', 'Three big mental errors athletes often make at major events are 1) overemphasizing the outcome, 2) trying too much, and 3) tracking the negative', 'Against overemphasizing the outcome, stop stressing yourself out about winning or losing, just focus on the process and concentrate on doing your job, the outcome can wait, do not chase the win, let the win find you', 'Against trying too much, just do your normal excellent job and battle to the best of your abilities, nothing else is needed', 'Against tracking the negative, just follow the positive track, remember that there is always some margin for error, therefore put an immediate stop to any negative commentary running in your head, refuse to get sucked into frustration, panic or pessimism, let go of the negative events and move on, this will help you stay cool and confident', 'In regards to whatever is on your mind right now, realize that this too shall pass.', 'Focus your energy on problem solving in the present rather than excessive worrying about the future.', 'Take positive-action steps instead of succumbing to apathy and inactivity.', 'Be assertive by supporting your rights and needs, such as taking the necessary time for your training and regeneration. Sometimes this requires placing concern with your interests above the interests of others. That is, learn when to say no to others and hold to it in order to reduce stress or stick to your priorities.', 'Talk with friends and family or a specialist for help and support rather than becoming or staying isolated.', 'Continue to be brilliant with self-care basics and relaxation techniques for tension release.', 'Maintain a boundless sense of humor—find the funny side or silver lining in your situation.', 'Champions aren’t made in the gyms. Champions are made from something they have deep inside them—a desire, a dream, a vision.', 'Organize your life around your dreams—and watch them come true.']}
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
    st.info("No lesson column found. Showing all data.")
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
            st.title(current_row.iloc[columna_respuesta])
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
