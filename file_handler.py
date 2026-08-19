import csv
from pathlib import Path


def append_prediction_csv(record):
    root = Path(__file__).resolve().parents[3]
    file_path = root / "data" / "saved_predictions.csv"
    headers = [
        "cost",
        "savings",
        "previous_purchase",
        "days_since_last_purchase",
        "prediction",
        "probability",
        "model_name",
        "advice",
    ]

    file_exists = file_path.exists()
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "cost": record["cost"],
                "savings": record["savings"],
                "previous_purchase": record["previous_purchase"],
                "days_since_last_purchase": record["days_since_last_purchase"],
                "prediction": int(record["prediction"]),
                "probability": record["probability"],
                "model_name": record["model_name"],
                "advice": record["advice"],
            }
        )
