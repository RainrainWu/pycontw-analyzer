"""
analyzer.provider.program is a unified interface which provide
more explainable programs-related data for inspecting.
"""

from analyzer.provider import lake


def get_programs_categories_with_levels():
    """
    get the mapping of category to their levels.
    """
    categories = {}
    for program in lake["programs"]:
        category = program[1]
        if category not in categories:
            categories[category] = []
        categories[category] += [program[2]]

    # for i in categories:
    #     print("{CATEGORY} {TITLES}".format(CATEGORY=i, TITLES=categories[i]))
    return categories
