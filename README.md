# Real-Time Data Dashboard

An interactive Streamlit dashboard for real-time data visualization and KPI monitoring. Supports multiple data sources (CSV, SQLite) with auto-refresh and Plotly charts.

## Architecture
```
de-realtime-data-dashboard/
├── src/
│   ├── data_connector.py   # Multi-source data loading
│   ├── metrics.py           # KPI computation engine
│   ├── charts.py            # Plotly chart builder
│   ├── app.py               # Main Streamlit application
│   └── pages/
│       ├── overview.py      # KPI cards and daily trends
│       └── sales.py         # Category and monthly analysis
├── config/config.yaml
├── tests/test_metrics.py
└── requirements.txt
```

## Features
- Multi-source data connectors (CSV, SQLite)
- Real-time KPI cards with delta indicators
- Interactive Plotly charts (line, bar, pie, heatmap, scatter)
- Multi-page navigation
- Configurable auto-refresh

## Installation
```bash
git clone https://github.com/mouachiqab/de-realtime-data-dashboard.git
cd de-realtime-data-dashboard
pip install -r requirements.txt
```

## Usage
```bash
streamlit run src/app.py
```

## Technologies
- Python 3.9+, Streamlit, Plotly, pandas, SQLAlchemy











