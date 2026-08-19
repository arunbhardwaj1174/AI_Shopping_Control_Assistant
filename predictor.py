import pandas as pd
import joblib
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from .decision_rules import evaluate_decision_rules


class PredictionEngine:
    def __init__(self):
        self.root = Path(__file__).resolve().parents[3]
        self.models_dir = self.root / "models"
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.training_csv = self.root / "data" / "training_data.csv"
        self.model = self._load_model("logistic_regression_model.pkl")

    def _load_model(self, file_name):
        model_file = self.models_dir / file_name
        if model_file.exists():
            try:
                model = joblib.load(model_file)
                if not hasattr(model, "predict_proba") or not hasattr(model, "predict"):
                    raise ValueError("Loaded model is not compatible with predict or predict_proba.")
                # validate that the loaded model works with expected interface
                model.predict_proba([[0.0, 0.0, 0.0, 0.0]])
                model.predict([[0.0, 0.0, 0.0, 0.0]])
                return model
            except Exception:
                self._train_models()
        else:
            self._train_models()
        return joblib.load(model_file)

    def _train_models(self):
        df = pd.read_csv(self.training_csv)
        X = df[["cost", "savings", "previous_purchase", "days_since_last_purchase"]]
        y = df["regret"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        logistic = LogisticRegression(max_iter=1000)
        logistic.fit(X_train, y_train)
        decision_tree = DecisionTreeClassifier(max_depth=4)
        decision_tree.fit(X_train, y_train)

        joblib.dump(logistic, self.models_dir / "logistic_regression_model.pkl")
        joblib.dump(decision_tree, self.models_dir / "decision_tree_model.pkl")

    def predict(self, cost, savings, previous_purchase, days_since_last_purchase):
        features = [[cost, savings, previous_purchase, days_since_last_purchase]]
        probability = float(self.model.predict_proba(features)[0][1])
        prediction = bool(self.model.predict(features)[0])
        confidence = max(probability, 1 - probability)
        advice = evaluate_decision_rules(
            cost,
            savings,
            previous_purchase,
            days_since_last_purchase,
        )

        record = {
            "cost": cost,
            "savings": savings,
            "previous_purchase": previous_purchase,
            "days_since_last_purchase": days_since_last_purchase,
            "prediction": prediction,
            "probability": probability,
            "confidence": confidence,
            "model_name": "Logistic Regression",
            "advice": advice,
        }
        return {"record": record, **record}
