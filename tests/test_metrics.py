"""Tests for KPI engine."""
import unittest
import pandas as pd
from src.metrics import KPIEngine

class TestKPIEngine(unittest.TestCase):
    def setUp(self):
        self.engine = KPIEngine()
        self.df = pd.DataFrame({
            "amount": [100, 200, 150, 300],
            "customer_id": [1, 2, 1, 3],
            "date": ["2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03"],
        })

    def test_total_revenue(self):
        kpis = self.engine.compute_sales_kpis(self.df)
        self.assertEqual(kpis["total_revenue"], 750)

    def test_unique_customers(self):
        kpis = self.engine.compute_sales_kpis(self.df)
        self.assertEqual(kpis["unique_customers"], 3)

    def test_empty_df(self):
        kpis = self.engine.compute_sales_kpis(pd.DataFrame())
        self.assertEqual(kpis, {})

if __name__ == "__main__":
    unittest.main()
