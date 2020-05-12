"""
analyzer.provider is a unified inerface which provide more
explainable data for inspecting.
"""

from analyzer.extractor.attendee import Attendee2019
from analyzer.utils.homogeneous import convert_company_alias


lake = {
    'attendee': Attendee2019.export()
}


def get_attendee_companies_with_times():
    """
    get the mapping of attendee company to thier number of
    discoveries.
    """
    roster = {}
    for attendee in lake['attendee']:
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
    for attendee in lake['attendee']:
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
