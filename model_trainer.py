import pandas as pd
import joblib
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def train_models():
    root = Path(__file__).resolve().parents[1]
    data_path = root / "data" / "training_data.csv"
    models_dir = root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)
    X = df[["cost", "savings", "previous_purchase", "days_since_last_purchase"]]
    y = df["regret"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)

    dt = DecisionTreeClassifier(max_depth=4)
    dt.fit(X_train, y_train)

    joblib.dump(lr, models_dir / "logistic_regression_model.pkl")
    joblib.dump(dt, models_dir / "decision_tree_model.pkl")

    print("Models trained successfully.")


if __name__ == "__main__":
    train_models()
