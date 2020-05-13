"""
analyzer,visualizer.pie provides some functions to plot pie chart
with structural data.
"""

import plotly.graph_objects as go


def plot_dict(mapping):
    """
    plot pie chart by dictionary.
    """
    labels = list(mapping.keys())
    values = list(mapping.values())
    fig = go.Figure(go.Pie(labels=labels, values=values))
    fig.show()
