import streamlit as st
from datetime import datetime
import pandas as pd
from pathlib import Path
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

timestamp = datetime.now()
st.write(timestamp)

entry = {
    'timestamp': timestamp,
    'mood': mood,
    'sleep': sleep,
    'stress': stress,
    'exercise': exercise,
    'notes': notes
}

st.write(entry)
df = pd.DataFrame([entry])
st.dataframe(df)

file_path = Path("data/mood_log.csv")
file_path.parent.mkdir(parents=True, exist_ok=True)

if st.button("💾 Save Entry"):
    df.to_csv(
        file_path,
        mode="a",
        index=False,
        header=not file_path.exists()
    )
st.success("Entry saved!")

st.header("Check-In History")
if file_path.exists():
    history = pd.read_csv(file_path)
    history["timestamp"] = pd.to_datetime(history["timestamp"])
    st.dataframe(history)

    st.header("Descriptive Statistics")

    average_mood = history["mood"].mean()
    average_sleep = history["sleep"].mean()
    average_stress = history["stress"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Mood", round(average_mood, 2))
    col2.metric("Average Sleep", round(average_sleep, 2))
    col3.metric("Average Stress", round(average_stress, 2))

    st.header("Summary Statistics")

    summary = history[["mood", "sleep", "stress"]].describe()
    st.dataframe(summary)

    st.header("Mood and Stress Over Time")

    st.line_chart(
        history,
        x="timestamp",
        y=["mood", "stress"]
    )

    st.header("Correlation Analysis")

    correlations = history[["mood", "sleep", "stress"]].corr()

    st.dataframe(correlations) 
    
else:
    st.info("No entries yet.")