"""Overview dashboard page."""
import streamlit as st
from src.charts import ChartBuilder

def render(data, kpi_engine):
    st.header("Dashboard Overview")
    sales_df = data.get("sales")
    if sales_df is None or sales_df.empty:
        st.warning("No sales data available")
        return
    kpis = kpi_engine.compute_sales_kpis(sales_df)
    cols = st.columns(4)
    cols[0].metric("Total Revenue", f"${kpis.get('total_revenue', 0):,.0f}")
    cols[1].metric("Total Orders", f"{kpis.get('total_orders', 0):,}")
    cols[2].metric("Avg Order Value", f"${kpis.get('avg_order_value', 0):,.2f}")
    cols[3].metric("Unique Customers", f"{kpis.get('unique_customers', 0):,}")
    charts = ChartBuilder()
    if "date" in sales_df.columns and "amount" in sales_df.columns:
        import pandas as pd
        sales_df["date"] = pd.to_datetime(sales_df["date"])
        daily = sales_df.groupby(sales_df["date"].dt.date)["amount"].sum().reset_index()
        daily.columns = ["date", "revenue"]
        st.plotly_chart(charts.line_chart(daily, "date", "revenue", "Daily Revenue"), use_container_width=True)
