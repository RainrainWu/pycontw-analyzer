"""
analyzer.inspector.program is a implemeentation of strategy
logic that helps to obtain proportions of each topic.
"""

import datetime

from analyzer.provider.programs import get_programs_categories_with_levels
from analyzer.provider.vacancies import get_number_of_vancacies_with_type
from analyzer.provider.proposals import (
    get_acceptance_with_title,
    get_speakers_with_year,
    get_date_with_proposals_number,
)


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


def get_speaker_with_experience(times: int = 2):
    """
    get a list of speakers that have gave talks at PyCon TW before.

    - times
      lowerbound of talk count.
    """

    speakers = get_speakers_with_year()
    target = {}
    for speaker in speakers:
        if len(speakers[speaker]) >= times:
            target[speaker] = speakers[speaker]

    return target


def get_date_with_proposals_accumulate(year: str = "2019"):
    """
    get the accumulation of proposals
    """
    submit = get_date_with_proposals_number(year)
    start = datetime.datetime.strptime(sorted(submit)[0], "%Y-%m-%d")
    end = datetime.datetime.strptime(sorted(submit)[-1], "%Y-%m-%d")
    dates = [
        (start + datetime.timedelta(days=x)).strftime("%Y-%m-%d")
        for x in range(0, (end - start).days + 1)
    ]
    accumulation = 0
    records = {}
    for date in dates:
        if date in submit:
            accumulation += submit[date]
        records[date] = accumulation

    return records
