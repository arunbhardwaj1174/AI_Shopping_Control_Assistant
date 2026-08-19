import unittest
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.gui.utils.validation import parse_float, parse_int
from src.gui.utils.data_loader import load_training_data, load_saved_predictions
from src.gui.utils.charts import build_summary_figure


class TestValidation(unittest.TestCase):
    
    def test_parse_float_valid(self):
        """Test parsing valid float values"""
        self.assertEqual(parse_float("123.45", "test"), 123.45)
        self.assertEqual(parse_float("0", "test"), 0.0)
        self.assertEqual(parse_float("999.99", "test"), 999.99)
    
    def test_parse_float_invalid(self):
        """Test parsing invalid float values raises error"""
        with self.assertRaises(ValueError):
            parse_float("abc", "field")
        
        with self.assertRaises(ValueError):
            parse_float("", "field")
        
        with self.assertRaises(ValueError):
            parse_float("-100", "field")
    
    def test_parse_int_valid(self):
        """Test parsing valid integer values"""
        self.assertEqual(parse_int("123", "test"), 123)
        self.assertEqual(parse_int("0", "test"), 0)
        self.assertEqual(parse_int("5.9", "test"), 5)  # Truncates float
    
    def test_parse_int_invalid(self):
        """Test parsing invalid integer values raises error"""
        with self.assertRaises(ValueError):
            parse_int("abc", "field")
        
        with self.assertRaises(ValueError):
            parse_int("", "field")
        
        with self.assertRaises(ValueError):
            parse_int("-50", "field")


class TestDataLoader(unittest.TestCase):
    
    def test_load_training_data(self):
        """Test loading training data"""
        df = load_training_data()
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)
        
        # Check expected columns
        expected_cols = ["cost", "savings", "previous_purchase", "days_since_last_purchase", "regret"]
        for col in expected_cols:
            self.assertIn(col, df.columns)
    
    def test_load_saved_predictions(self):
        """Test loading saved predictions"""
        df = load_saved_predictions()
        self.assertIsNotNone(df)
        # Might be empty initially, but should be a DataFrame
        self.assertTrue(hasattr(df, 'shape'))


class TestCharts(unittest.TestCase):
    
    def test_build_summary_figure(self):
        """Test building a summary chart"""
        summary = {"regret": 5, "no_regret": 10}
        fig = build_summary_figure(summary)
        
        self.assertIsNotNone(fig)
        self.assertTrue(hasattr(fig, 'add_subplot'))
    
    def test_build_summary_figure_empty(self):
        """Test building a chart with no data"""
        summary = {"regret": 0, "no_regret": 0}
        fig = build_summary_figure(summary)
        
        self.assertIsNotNone(fig)
    
    def test_build_summary_figure_only_regret(self):
        """Test building a chart with only regret data"""
        summary = {"regret": 15, "no_regret": 0}
        fig = build_summary_figure(summary)
        
        self.assertIsNotNone(fig)


class TestInputValidation(unittest.TestCase):
    """Test the input validation flow"""
    
    def test_valid_purchase_inputs(self):
        """Test validation of realistic purchase inputs"""
        # These should all be valid
        cost = parse_float("250.50", "cost")
        savings = parse_float("1000", "savings")
        prev_purchase = parse_int("2", "previous_purchase")
        days = parse_int("15", "days_since_last_purchase")
        
        self.assertEqual(cost, 250.50)
        self.assertEqual(savings, 1000.0)
        self.assertEqual(prev_purchase, 2)
        self.assertEqual(days, 15)
    
    def test_invalid_purchase_inputs(self):
        """Test validation rejects invalid inputs"""
        invalid_inputs = [
            ("abc", "cost"),
            ("-100", "savings"),
            ("", "previous_purchase"),
            ("12.5.5", "days"),
        ]
        
        for value, field in invalid_inputs:
            with self.assertRaises(ValueError):
                parse_float(value, field)


if __name__ == "__main__":
    unittest.main()
