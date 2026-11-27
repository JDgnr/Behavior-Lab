import pandas as pd
from pathlib import Path

def save_entry(data, file_path):
    file_path.parent.mkdir(parents= True, exist_ok=True)

    data.to_csv(
        file_path,
        mode = 'a',
        index = False,
        header = not file_path.exists()
    )

def load_history(file_path):
    history = pd.read_csv(file_path)
    history["timestamp"] = pd.to_datetime(history["timestamp"])
    return history