"""KPI computation engine."""
import pandas as pd
import numpy as np
from typing import Dict, Any

class KPIEngine:
    def __init__(self):
        self.kpis = {}

    def compute_sales_kpis(self, df: pd.DataFrame) -> Dict[str, Any]:
        if df.empty:
            return {}
        self.kpis = {
            "total_revenue": float(df["amount"].sum()) if "amount" in df.columns else 0,
            "total_orders": len(df),
            "avg_order_value": float(df["amount"].mean()) if "amount" in df.columns else 0,
            "unique_customers": int(df["customer_id"].nunique()) if "customer_id" in df.columns else 0,
        }
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])
            daily = df.groupby(df["date"].dt.date)["amount"].sum()
            self.kpis["daily_avg_revenue"] = float(daily.mean())
            self.kpis["peak_day_revenue"] = float(daily.max())
        return self.kpis

    def compute_growth(self, df: pd.DataFrame, date_col="date", value_col="amount", period="M"):
        df = df.copy()
        df[date_col] = pd.to_datetime(df[date_col])
        grouped = df.groupby(df[date_col].dt.to_period(period))[value_col].sum()
        growth = grouped.pct_change() * 100
        return growth.to_dict()

    def compute_percentiles(self, series, percentiles=(25, 50, 75, 90, 99)):
        return {f"p{p}": float(np.percentile(series.dropna(), p)) for p in percentiles}
