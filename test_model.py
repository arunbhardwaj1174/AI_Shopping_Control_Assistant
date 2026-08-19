import unittest
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.gui.ml.predictor import PredictionEngine
from src.gui.ml.decision_rules import evaluate_decision_rules


class TestPredictionEngine(unittest.TestCase):
    
    def setUp(self):
        """Initialize the prediction engine before each test"""
        self.engine = PredictionEngine()
    
    def test_engine_initialization(self):
        """Test that the engine initializes correctly"""
        self.assertIsNotNone(self.engine.model)
        self.assertTrue(self.engine.models_dir.exists())
    
    def test_predict_low_regret(self):
        """Test prediction for low regret scenario"""
        result = self.engine.predict(
            cost=100.0,
            savings=5000.0,
            previous_purchase=1,
            days_since_last_purchase=30
        )
        self.assertIn("prediction", result)
        self.assertIn("probability", result)
        self.assertIn("confidence", result)
        self.assertIn("advice", result)
        self.assertIsInstance(result["prediction"], bool)
        self.assertGreater(result["probability"], 0)
        self.assertLess(result["probability"], 1)
    
    def test_predict_high_regret(self):
        """Test prediction for high regret scenario"""
        result = self.engine.predict(
            cost=5000.0,
            savings=1000.0,
            previous_purchase=5,
            days_since_last_purchase=2
        )
        self.assertIn("prediction", result)
        self.assertTrue(result["prediction"])  # Should predict regret
    
    def test_record_structure(self):
        """Test that the returned record has all required fields"""
        result = self.engine.predict(
            cost=250.0,
            savings=1000.0,
            previous_purchase=2,
            days_since_last_purchase=15
        )
        record = result["record"]
        required_fields = [
            "cost", "savings", "previous_purchase", "days_since_last_purchase",
            "prediction", "probability", "confidence", "model_name", "advice"
        ]
        for field in required_fields:
            self.assertIn(field, record)


class TestDecisionRules(unittest.TestCase):
    
    def test_high_risk_scenario(self):
        """Test decision rules for high risk purchase"""
        advice = evaluate_decision_rules(
            cost=6000.0,
            savings=1000.0,
            previous_purchase=5,
            days_since_last_purchase=2
        )
        self.assertIn("risk factors", advice.lower())
    
    def test_mild_risk_scenario(self):
        """Test decision rules for mild risk purchase"""
        advice = evaluate_decision_rules(
            cost=600.0,
            savings=1000.0,
            previous_purchase=2,
            days_since_last_purchase=25
        )
        self.assertIn("mild risk", advice.lower())
    
    def test_low_risk_scenario(self):
        """Test decision rules for low risk purchase"""
        advice = evaluate_decision_rules(
            cost=100.0,
            savings=5000.0,
            previous_purchase=1,
            days_since_last_purchase=30
        )
        self.assertIn("reasonable", advice.lower())


if __name__ == "__main__":
    unittest.main()
