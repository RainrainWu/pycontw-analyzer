"""
analyzer,visualizer.bar provides some functions to plot bar chart
with structural data.
"""

import plotly.graph_objects as go


def plot_dict(mapping):
    """
    plot bar chart by dictionary.
    """
    items = list(mapping.keys())
    values = list(mapping.values())
    fig = go.Figure(go.Bar(x=items, y=values))
    fig.show()
