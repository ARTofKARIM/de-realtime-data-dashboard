"""Main Streamlit dashboard application."""
import streamlit as st
import yaml
from src.data_connector import DataConnector
from src.metrics import KPIEngine
from src.pages import overview, sales

def load_config(path="config/config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    st.set_page_config(page_title=config["app"]["title"], layout="wide")
    st.title(config["app"]["title"])
    connector = DataConnector(config)
    data = connector.load_all()
    kpi_engine = KPIEngine()
    page = st.sidebar.selectbox("Navigation", config["dashboard"]["pages"])
    if page == "Overview":
        overview.render(data, kpi_engine)
    elif page == "Sales Analytics":
        sales.render(data, kpi_engine)
    elif page == "Performance Metrics":
        st.header("Performance Metrics")
        st.info("Connect a metrics data source to view performance data.")
    st.sidebar.markdown("---")
    st.sidebar.text(f"Auto-refresh: {config['app']['refresh_interval']}s")

if __name__ == "__main__":
    main()
