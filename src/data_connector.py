"""Data source connectors for the dashboard."""
import pandas as pd
from sqlalchemy import create_engine, text
import os

class DataConnector:
    def __init__(self, config):
        self.config = config
        self._cache = {}

    def load_csv(self, path):
        if not os.path.exists(path):
            return pd.DataFrame()
        df = pd.read_csv(path)
        return df

    def load_database(self, connection_string, query):
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
        engine.dispose()
        return df

    def load_source(self, source_config):
        name = source_config["name"]
        src_type = source_config["type"]
        if src_type == "csv":
            return self.load_csv(source_config["path"])
        elif src_type == "sqlite":
            return self.load_database(source_config["connection"], source_config["query"])
        else:
            raise ValueError(f"Unknown source type: {src_type}")

    def load_all(self):
        data = {}
        for source in self.config.get("data_sources", []):
            try:
                data[source["name"]] = self.load_source(source)
            except Exception as e:
                print(f"Error loading {source['name']}: {e}")
                data[source["name"]] = pd.DataFrame()
        return data
