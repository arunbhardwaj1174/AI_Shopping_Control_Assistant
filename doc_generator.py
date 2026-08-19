import json
from pathlib import Path
from datetime import datetime


class DocumentationGenerator:
    def __init__(self):
        self.root = Path(__file__).resolve().parent.parent
        self.docs_dir = self.root / "docs"
        self.docs_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_project_summary(self):
        """Generate a project summary document"""
        summary = {
            "project_name": "AI Shopping Control Assistant",
            "description": "A desktop application for predicting purchase regret using machine learning",
            "version": "1.0.0",
            "generated_at": datetime.utcnow().isoformat(),
            "components": {
                "GUI": ["main_window.py", "input_frame.py", "result_frame.py", "dashboard.py"],
                "ML": ["predictor.py", "decision_rules.py", "regret_classifier.py"],
                "Database": ["db.py"],
                "Utils": ["data_loader.py", "file_handler.py", "validation.py", "charts.py"],
                "Reports": ["report_generator.py", "user_report_manager.py"],
            },
            "technologies": [
                "Python 3.14+",
                "customtkinter",
                "scikit-learn",
                "pandas",
                "numpy",
                "matplotlib",
                "SQLite3",
            ],
            "dependencies": {
                "pandas": ">=1.0.0",
                "numpy": ">=1.0.0",
                "scikit-learn": ">=0.24.0",
                "joblib": ">=1.0.0",
                "customtkinter": ">=5.0.0",
                "matplotlib": ">=3.0.0",
            },
        }
        return summary
    
    def generate_api_documentation(self):
        """Generate API documentation"""
        api_docs = {
            "PredictionEngine": {
                "module": "src.gui.ml.predictor",
                "methods": {
                    "predict": {
                        "params": {
                            "cost": "float",
                            "savings": "float",
                            "previous_purchase": "int",
                            "days_since_last_purchase": "int",
                        },
                        "returns": "dict with prediction details",
                    },
                    "_load_model": {
                        "params": {"file_name": "str"},
                        "returns": "Trained ML model",
                    },
                },
            },
            "Database": {
                "module": "src.gui.database.db",
                "methods": {
                    "add_purchase": {
                        "params": {"record": "dict"},
                        "returns": "None",
                    },
                    "fetch_recent": {
                        "params": {"limit": "int"},
                        "returns": "list of dict",
                    },
                    "get_summary": {
                        "params": {},
                        "returns": "dict with regret/no_regret counts",
                    },
                },
            },
            "ValidationUtils": {
                "module": "src.gui.utils.validation",
                "methods": {
                    "parse_float": {
                        "params": {
                            "value": "str",
                            "field_name": "str",
                        },
                        "returns": "float",
                        "raises": "ValueError",
                    },
                    "parse_int": {
                        "params": {
                            "value": "str",
                            "field_name": "str",
                        },
                        "returns": "int",
                        "raises": "ValueError",
                    },
                },
            },
        }
        return api_docs
    
    def generate_setup_guide(self):
        """Generate setup and installation guide"""
        guide = {
            "title": "Setup & Installation Guide",
            "generated_at": datetime.utcnow().isoformat(),
            "steps": [
                {
                    "step": 1,
                    "title": "Clone/Download Project",
                    "instructions": [
                        "Download or clone the AI_Shopping_Control_Assistant project",
                        "Navigate to the project directory",
                    ],
                },
                {
                    "step": 2,
                    "title": "Create Virtual Environment",
                    "instructions": [
                        "PowerShell: python -m venv .venv",
                        ".venv\\Scripts\\Activate.ps1",
                        "Command Prompt: python -m venv .venv",
                        ".venv\\Scripts\\activate.bat",
                    ],
                },
                {
                    "step": 3,
                    "title": "Install Dependencies",
                    "instructions": [
                        "pip install -r requirements.txt",
                    ],
                },
                {
                    "step": 4,
                    "title": "Train Models",
                    "instructions": [
                        "python models/model_trainer.py",
                    ],
                },
                {
                    "step": 5,
                    "title": "Run Application",
                    "instructions": [
                        "python app.py",
                    ],
                },
                {
                    "step": 6,
                    "title": "Run Tests",
                    "instructions": [
                        "python tests/test_model.py -v",
                        "python tests/test_database.py -v",
                        "python tests/test_gui.py -v",
                    ],
                },
            ],
        }
        return guide
    
    def export_json(self, data, filename):
        """Export data as JSON"""
        output_path = self.docs_dir / filename
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
        return {"status": "success", "path": str(output_path)}


if __name__ == "__main__":
    gen = DocumentationGenerator()
    
    summary = gen.generate_project_summary()
    print("Project Summary:")
    print(json.dumps(summary, indent=2))
    
    print("\n" + "="*60 + "\n")
    
    api_docs = gen.generate_api_documentation()
    print("API Documentation:")
    print(json.dumps(api_docs, indent=2))
    
    print("\n" + "="*60 + "\n")
    
    setup_guide = gen.generate_setup_guide()
    print("Setup Guide:")
    print(json.dumps(setup_guide, indent=2))
    
    # Export to JSON files
    gen.export_json(summary, "project_summary.json")
    gen.export_json(api_docs, "api_documentation.json")
    gen.export_json(setup_guide, "setup_guide.json")
    print("\nDocumentation exported to docs/ folder.")
