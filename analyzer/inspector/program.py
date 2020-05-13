"""
analyzer.inspector.program is a implemeentation of strategy
logic that helps to obtain proportions of each topic.
"""

from analyzer import provider


def get_proportion_of_categories():
    """
    get proportion of each categories.
    """
    proportions = {}
    categories = provider.get_session_categories_with_levels()
    total = sum([len(categories[category]) for category in categories])
    for category in categories:
        proportions[category] = round(len(categories[category]) / total, 2)

    return proportions


def get_number_of_categories_and_levels():
    """
    get proportion of each categories and devided by levels
    """
    levels = ["NOVICE", "INTERMEDIATE", "EXPERIENCED"]
    proportions = {}
    categories = provider.get_session_categories_with_levels()
    for category in categories:
        breakdown = {}
        for level in levels:
            breakdown[level] = categories[category].count(level)
        proportions[category] = breakdown

    return proportions
