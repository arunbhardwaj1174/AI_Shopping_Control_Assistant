import pandas as pd
from pathlib import Path
from datetime import datetime


class UserReportManager:
    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.reports_dir = self.root / "reports"
        self.user_reports_dir = self.reports_dir / "user_reports"
        
        # Remove existing file if it exists and create directory
        if self.user_reports_dir.exists() and self.user_reports_dir.is_file():
            self.user_reports_dir.unlink()
        
        self.user_reports_dir.mkdir(parents=True, exist_ok=True)

    def save_user_report(self, user_id, prediction_data):
        """Save individual user prediction to a report file"""
        try:
            filename = f"user_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            filepath = self.user_reports_dir / filename
            
            with open(filepath, "w") as f:
                f.write(f"User Report for {user_id}\n")
                f.write(f"Generated: {datetime.utcnow().isoformat()}\n")
                f.write("=" * 50 + "\n\n")
                
                for key, value in prediction_data.items():
                    f.write(f"{key}: {value}\n")
            
            return {"status": "saved", "path": str(filepath)}
        except Exception as e:
            return {"error": str(e)}

    def list_user_reports(self, user_id=None):
        """List all user reports, optionally filtered by user_id"""
        try:
            reports = list(self.user_reports_dir.glob("*.txt"))
            if user_id:
                reports = [r for r in reports if user_id in r.name]
            return [str(r) for r in sorted(reports, reverse=True)]
        except Exception as e:
            return {"error": str(e)}

    def get_report_summary(self):
        """Get summary of all saved user reports"""
        try:
            reports = list(self.user_reports_dir.glob("*.txt"))
            return {
                "total_reports": len(reports),
                "reports_dir": str(self.user_reports_dir),
                "reports": [r.name for r in reports[-10:]]  # Last 10
            }
        except Exception as e:
            return {"error": str(e)}


if __name__ == "__main__":
    manager = UserReportManager()
    
    sample_prediction = {
        "cost": 250.0,
        "savings": 1000.0,
        "previous_purchase": 1,
        "days_since_last_purchase": 20,
        "prediction": "Low Regret",
        "probability": 0.12,
        "advice": "This purchase is safe.",
    }
    
    result = manager.save_user_report("user_001", sample_prediction)
    print("Save result:", result)
    print("Summary:", manager.get_report_summary())
    print("User reports list:", manager.list_user_reports())
