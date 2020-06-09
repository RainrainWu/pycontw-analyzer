"""
analyzer,visualizer.bar provides some functions to plot line chart
with sequential data.
"""

import plotly.graph_objects as go

from loguru import logger


def plot_dict(mapping):
    """
    plot line chart by mapping.
    """
    try:
        seq_x = [str(x) for x in mapping]
        seq_y = [float(x) for x in mapping.values()]
    except ValueError:
        logger.error("Unable to plot line chart with input data.")

    fig = go.Figure(data=go.Scatter(x=seq_x, y=seq_y))
    fig.show()
