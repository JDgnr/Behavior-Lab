import streamlit as st
st.title("🧠 BehaviorLab")
st.header("Daily Check-In")
mood = st.slider("How are you feeling today?",
                 min_value=1,
                 max_value=10,
                 value=5
                 )
sleep = st.number_input(
    "Hours of sleep",
    min_value=0.0,
    max_value=24.0,
    value=8.0,
    step=0.5
)
stress = st.slider(
    "Stress level",
    min_value=1,
    max_value=10,
    value=5
)
exercise = st.checkbox("Did you exercise today?")
notes = st.text_area("Anything you want to remember?")
if st.button("💾 Save Entry"):
    st.success("Entry saved!")
    

