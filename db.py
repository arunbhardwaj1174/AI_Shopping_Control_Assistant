import sqlite3
from datetime import datetime
from pathlib import Path


class Database:
    def __init__(self):
        self.db_path = Path(__file__).resolve().parent / "purchase_history.db"
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS purchase_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cost REAL NOT NULL,
            savings REAL NOT NULL,
            previous_purchase INTEGER NOT NULL,
            days_since_last_purchase INTEGER NOT NULL,
            prediction INTEGER NOT NULL,
            probability REAL NOT NULL,
            model_name TEXT NOT NULL,
            advice TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
        self.conn.execute(sql)
        self.conn.commit()

    def add_purchase(self, record):
        sql = """
        INSERT INTO purchase_history (
            cost,
            savings,
            previous_purchase,
            days_since_last_purchase,
            prediction,
            probability,
            model_name,
            advice,
            created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        values = (
            record["cost"],
            record["savings"],
            record["previous_purchase"],
            record["days_since_last_purchase"],
            int(record["prediction"]),
            float(record["probability"]),
            record["model_name"],
            record["advice"],
            datetime.utcnow().isoformat(),
        )
        self.conn.execute(sql, values)
        self.conn.commit()

    def fetch_recent(self, limit=10):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT cost, savings, previous_purchase, days_since_last_purchase, prediction, probability, model_name, advice, created_at "
            "FROM purchase_history ORDER BY id DESC LIMIT ?",
            (limit,),
        )
        rows = cursor.fetchall()
        return [dict(
            cost=row[0],
            savings=row[1],
            previous_purchase=row[2],
            days_since_last_purchase=row[3],
            prediction=bool(row[4]),
            probability=row[5],
            model_name=row[6],
            advice=row[7],
            created_at=row[8],
        ) for row in rows]

    def get_summary(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT prediction, COUNT(*) FROM purchase_history GROUP BY prediction"
        )
        counts = {0: 0, 1: 0}
        for prediction, count in cursor.fetchall():
            counts[int(prediction)] = count
        return {
            "regret": counts[1],
            "no_regret": counts[0],
        }
