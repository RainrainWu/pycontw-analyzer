"""
analyzer.inspector.program is a implemeentation of strategy
logic that helps to obtain proportions of each topic.
"""

from analyzer.provider.programs import get_programs_categories_with_levels
from analyzer.provider.vacancies import get_number_of_vancacies_with_type
from analyzer.provider.proposals import get_acceptance_with_title


def get_proportion_of_categories():
    """
    get proportion of each categories.
    """
    proportions = {}
    categories = get_programs_categories_with_levels()
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
    categories = get_programs_categories_with_levels()
    for category in categories:
        breakdown = {}
        for level in levels:
            breakdown[level] = categories[category].count(level)
        proportions[category] = breakdown

    return proportions


def get_proportion_of_vacancies():
    """
    get proportion of each vacancy type.
    """
    vacancies = get_number_of_vancacies_with_type()
    total = sum(vacancies.values())
    proportion = {}
    for i in vacancies:
        proportion[i] = round(vacancies[i] / total, 2)

    return proportion


def get_trend_of_accept_rate():
    """
    get historical trend of proposal accept rate.
    """
    acceptance = get_acceptance_with_title()
    years = ["2016", "2017", "2018", "2019"]
    accept_rate = {}

    for year in years:
        accept_num = len(acceptance[year]["accept"])
        unaccept_num = len(acceptance[year]["unaccept"])
        accept_rate[year] = round(accept_num / (accept_num + unaccept_num), 2)

    return accept_rate
