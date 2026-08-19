import pandas as pd
from pathlib import Path
from datetime import datetime


class ReportGenerator:
    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.reports_dir = self.root / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def generate_prediction_summary(self):
        """Generate a summary of all predictions from saved_predictions.csv"""
        try:
            predictions_path = self.root / "data" / "saved_predictions.csv"
            if not predictions_path.exists():
                return {"status": "No predictions saved yet", "count": 0}
            
            df = pd.read_csv(predictions_path)
            summary = {
                "total_predictions": len(df),
                "regret_predictions": int(df["prediction"].sum()),
                "no_regret_predictions": len(df) - int(df["prediction"].sum()),
                "average_probability": float(df["probability"].mean()),
                "highest_probability": float(df["probability"].max()),
                "lowest_probability": float(df["probability"].min()),
            }
            return summary
        except Exception as e:
            return {"error": str(e)}

    def generate_user_report(self, user_id, num_recent=10):
        """Generate a report for a specific user's recent predictions"""
        try:
            from src.gui.database.db import Database
            db = Database()
            recent = db.fetch_recent(num_recent)
            
            report = {
                "user_id": user_id,
                "generated_at": datetime.utcnow().isoformat(),
                "total_recent": len(recent),
                "predictions": recent,
            }
            
            if recent:
                predictions_list = [p["prediction"] for p in recent]
                report["regret_count"] = sum(predictions_list)
                report["no_regret_count"] = len(predictions_list) - sum(predictions_list)
            
            return report
        except Exception as e:
            return {"error": str(e)}

    def export_report_to_csv(self, report_data, filename):
        """Export report data to CSV"""
        try:
            df = pd.DataFrame([report_data] if isinstance(report_data, dict) else report_data)
            output_path = self.reports_dir / filename
            df.to_csv(output_path, index=False)
            return {"status": "success", "path": str(output_path)}
        except Exception as e:
            return {"error": str(e)}


if __name__ == "__main__":
    gen = ReportGenerator()
    print("Prediction Summary:", gen.generate_prediction_summary())
    print("User Report:", gen.generate_user_report(user_id="user_001", num_recent=5))
