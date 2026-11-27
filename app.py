import streamlit as st
from datetime import datetime
import pandas as pd
from pathlib import Path
from analytics import (
    calculate_average,
    calculate_summary,
    calculate_correlations
)
from storage import save_entry, load_history

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

file_path = Path("data/mood_log.csv")

if st.button("💾 Save Entry"):
    timestamp = datetime.now()

    entry = {
        "timestamp": timestamp,
        "mood": mood,
        "sleep": sleep,
        "stress": stress,
        "exercise": exercise,
        "notes": notes
    }
    df = pd.DataFrame([entry])

    save_entry(df, file_path)
    st.success("Entry saved!") 
     
st.header("Check-In History")
if file_path.exists():
    history = load_history(file_path)
    st.dataframe(history)

    st.header("Descriptive Statistics")

    average_mood = calculate_average(history, "mood")
    average_sleep = calculate_average(history, "sleep")
    average_stress = calculate_average(history, "stress")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Mood", round(average_mood, 2))
    col2.metric("Average Sleep", round(average_sleep, 2))
    col3.metric("Average Stress", round(average_stress, 2))

    st.header("Summary Statistics")

    summary = calculate_summary(history)
    st.dataframe(summary)

    st.header("Mood and Stress Over Time")

    st.line_chart(
        history,
        x="timestamp",
        y=["mood", "stress"]
    )

    st.header("Correlation Analysis")

    correlations = calculate_correlations(history)

    st.dataframe(correlations) 
    
else:
    st.info("No entries yet.")