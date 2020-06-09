"""
analyzer,visualizer.sunburst provides some functions to plot sunburst
chart with structural data.
"""

from plotly import graph_objects as go


def plot_two_levels_dict(title, hierarchy):
    """
    plot sunburst with hierarchical dictionary.
    """
    inner_ids = list(hierarchy.keys())
    outer_ids = [x + "_" + y for x in hierarchy for y in hierarchy[x]]
    ids = inner_ids + outer_ids

    # set program labels
    inner_labels = list(hierarchy.keys())
    outer_labels = list(list(hierarchy.values())[0].keys()) * len(inner_labels)
    labels = inner_labels + outer_labels

    # set label's parents
    inner_parents = [""] * len(inner_labels)
    outer_parents = [x for x in inner_labels for _ in hierarchy[inner_labels[0]]]
    parents = inner_parents + outer_parents

    # set label's values
    outer_values = [x for y in hierarchy.values() for x in list(y.values())]
    inner_values = [sum(outer_values[x * 3 : x * 3 + 3]) for x in range(len(hierarchy))]
    values = inner_values + outer_values

    # plot figure
    fig = go.Figure(
        go.Sunburst(
            ids=ids, labels=labels, parents=parents, values=values, branchvalues="total"
        )
    )
    fig.update_layout(title=title, margin=dict(t=0, l=0, r=0, b=0))
    fig.show()
