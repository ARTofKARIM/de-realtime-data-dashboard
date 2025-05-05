"""Chart generation with Plotly."""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class ChartBuilder:
    def __init__(self, theme="plotly_dark"):
        self.theme = theme

    def line_chart(self, df, x, y, title="", color=None):
        fig = px.line(df, x=x, y=y, title=title, color=color, template=self.theme)
        fig.update_layout(height=400)
        return fig

    def bar_chart(self, df, x, y, title="", color=None):
        fig = px.bar(df, x=x, y=y, title=title, color=color, template=self.theme)
        fig.update_layout(height=400)
        return fig

    def pie_chart(self, df, names, values, title=""):
        fig = px.pie(df, names=names, values=values, title=title, template=self.theme)
        return fig

    def kpi_card(self, value, label, delta=None):
        fig = go.Figure(go.Indicator(
            mode="number+delta" if delta else "number",
            value=value, title={"text": label},
            delta={"reference": value - delta} if delta else None,
        ))
        fig.update_layout(height=200, template=self.theme)
        return fig

    def heatmap(self, df, title=""):
        fig = px.imshow(df, text_auto=True, title=title, template=self.theme, color_continuous_scale="Blues")
        return fig

    def scatter(self, df, x, y, size=None, color=None, title=""):
        fig = px.scatter(df, x=x, y=y, size=size, color=color, title=title, template=self.theme)
        return fig
