"""
analyzer.provider is a unified inerface which provide more
explainable data for inspecting.
"""

from loguru import logger

from analyzer.extractor.attendee import Attendee2019
from analyzer.extractor.programs import Program2019
from analyzer.utils.homogeneous import convert_company_alias

logger.info("provider start collecting data...")
lake = {"attendee": Attendee2019.export(), "programs": Program2019.export()}


def get_attendee_companies_with_times():
    """
    get the mapping of attendee company to thier number of
    discoveries.
    """
    roster = {}
    for attendee in lake["attendee"]:
        if len(attendee[2]) == 0:
            continue
        company = convert_company_alias(attendee[2])
        if company not in roster:
            roster[company] = 0
        roster[company] += 1

    # for i in roster:
    #     print('{COMPANY} {TIMES}'.format(COMPANY=i, TIMES=roster[i]))
    return roster


def get_attendee_companies_with_jobs():
    """
    get the mapping of attendee company to thier jobs.
    """
    roster = {}
    for attendee in lake["attendee"]:
        if len(attendee[2]) == 0:
            continue
        company = convert_company_alias(attendee[2])
        if company not in roster:
            roster[company] = []
        if attendee[3] not in roster[company]:
            roster[company] += [attendee[3]]

    # for i in roster:
    #     print('{COMPANY} {JOBS}'.format(COMPANY=i, JOBS=roster[i]))
    return roster


def get_session_categories_with_levels():
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
