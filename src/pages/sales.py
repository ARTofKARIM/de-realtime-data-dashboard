"""Sales analytics page."""
import streamlit as st
import pandas as pd
from src.charts import ChartBuilder

def render(data, kpi_engine):
    st.header("Sales Analytics")
    sales_df = data.get("sales")
    if sales_df is None or sales_df.empty:
        st.warning("No data")
        return
    charts = ChartBuilder()
    col1, col2 = st.columns(2)
    if "category" in sales_df.columns:
        cat_sales = sales_df.groupby("category")["amount"].sum().reset_index()
        with col1:
            st.plotly_chart(charts.bar_chart(cat_sales, "category", "amount", "Revenue by Category"), use_container_width=True)
        with col2:
            st.plotly_chart(charts.pie_chart(cat_sales, "category", "amount", "Revenue Share"), use_container_width=True)
    if "date" in sales_df.columns:
        sales_df["date"] = pd.to_datetime(sales_df["date"])
        sales_df["month"] = sales_df["date"].dt.to_period("M").astype(str)
        monthly = sales_df.groupby("month")["amount"].agg(["sum", "count"]).reset_index()
        monthly.columns = ["month", "revenue", "orders"]
        st.plotly_chart(charts.line_chart(monthly, "month", "revenue", "Monthly Revenue"), use_container_width=True)
    st.subheader("Raw Data")
    st.dataframe(sales_df.head(100), use_container_width=True)
