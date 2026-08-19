import unittest
import tempfile
from pathlib import Path
import sys
import sqlite3

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.gui.database.db import Database


class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        """Create a test database before each test"""
        self.db = Database()
    
    def test_database_initialization(self):
        """Test that database initializes and creates table"""
        self.assertTrue(self.db.db_path.exists())
        
        # Verify table exists
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='purchase_history';"
        )
        result = cursor.fetchone()
        self.assertIsNotNone(result)
    
    def test_add_purchase(self):
        """Test adding a purchase record to database"""
        record = {
            "cost": 500.0,
            "savings": 2000.0,
            "previous_purchase": 2,
            "days_since_last_purchase": 10,
            "prediction": False,
            "probability": 0.25,
            "model_name": "TestModel",
            "advice": "Test advice message",
        }
        
        self.db.add_purchase(record)
        
        # Verify record was added
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM purchase_history;")
        count = cursor.fetchone()[0]
        self.assertGreater(count, 0)
    
    def test_fetch_recent(self):
        """Test fetching recent purchase records"""
        record1 = {
            "cost": 100.0,
            "savings": 1000.0,
            "previous_purchase": 0,
            "days_since_last_purchase": 30,
            "prediction": False,
            "probability": 0.15,
            "model_name": "TestModel",
            "advice": "First test",
        }
        
        record2 = {
            "cost": 500.0,
            "savings": 2000.0,
            "previous_purchase": 2,
            "days_since_last_purchase": 10,
            "prediction": True,
            "probability": 0.75,
            "model_name": "TestModel",
            "advice": "Second test",
        }
        
        self.db.add_purchase(record1)
        self.db.add_purchase(record2)
        
        recent = self.db.fetch_recent(limit=2)
        self.assertEqual(len(recent), 2)
        self.assertTrue(recent[0]["prediction"])  # Most recent should be record2
    
    def test_get_summary(self):
        """Test getting prediction summary"""
        # Add multiple records
        for i in range(3):
            record = {
                "cost": 100.0 + (i * 100),
                "savings": 1000.0,
                "previous_purchase": i,
                "days_since_last_purchase": 20,
                "prediction": i % 2 == 0,  # Alternate between True and False
                "probability": 0.1 + (i * 0.1),
                "model_name": "TestModel",
                "advice": f"Test {i}",
            }
            self.db.add_purchase(record)
        
        summary = self.db.get_summary()
        self.assertIn("regret", summary)
        self.assertIn("no_regret", summary)
        self.assertGreater(summary["regret"] + summary["no_regret"], 0)
    
    def test_record_structure(self):
        """Test that fetched records have correct structure"""
        record = {
            "cost": 250.0,
            "savings": 1500.0,
            "previous_purchase": 1,
            "days_since_last_purchase": 15,
            "prediction": False,
            "probability": 0.3,
            "model_name": "TestModel",
            "advice": "Structure test",
        }
        
        self.db.add_purchase(record)
        recent = self.db.fetch_recent(limit=1)
        
        self.assertEqual(len(recent), 1)
        fetched = recent[0]
        
        self.assertEqual(fetched["cost"], 250.0)
        self.assertEqual(fetched["savings"], 1500.0)
        self.assertEqual(fetched["previous_purchase"], 1)
        self.assertEqual(fetched["days_since_last_purchase"], 15)
        self.assertEqual(fetched["prediction"], False)
        self.assertAlmostEqual(fetched["probability"], 0.3, places=2)
        self.assertEqual(fetched["model_name"], "TestModel")


if __name__ == "__main__":
    unittest.main()
