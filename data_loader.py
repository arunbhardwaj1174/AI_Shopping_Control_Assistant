import pandas as pd
from pathlib import Path


def load_training_data():
    root = Path(__file__).resolve().parents[3]
    training_path = root / "data" / "training_data.csv"
    return pd.read_csv(training_path)


def load_saved_predictions():
    root = Path(__file__).resolve().parents[3]
    saved_path = root / "data" / "saved_predictions.csv"
    return pd.read_csv(saved_path) if saved_path.exists() else pd.DataFrame()
