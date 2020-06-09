"""
analyzer.provider.program is a unified interface which provide
more explainable proposals-related data for inspecting.
"""

from analyzer.provider import lake
from analyzer.config import YEAR_TAGS


def get_acceptance_with_title():
    """
    get the mapping of acceptance to the titles.
    """
    acceptance = {}

    for year in YEAR_TAGS:
        acceptance[year] = {}
        acceptance[year]["accept"] = [
            x[0] for x in lake["proposals"][year] if (x[6] == "f" and x[7] == "t")
        ]
        acceptance[year]["unaccept"] = [
            x[0] for x in lake["proposals"][year] if (x[6] != "f" or x[7] != "t")
        ]

    return acceptance


def get_speakers_with_year():
    """
    get the mapping of speaker and the years they gave a talk.
    """
    speakers = {}

    for year in YEAR_TAGS:
        for proposal in lake["proposals"][year]:
            if proposal[6] != "f" or proposal[7] != "t":
                continue
            if proposal[4] not in speakers:
                speakers[proposal[4]] = []
            if year not in speakers[proposal[4]]:
                speakers[proposal[4]] += [year]

    return speakers


def get_date_with_proposals_number(year: str = "2019"):
    """
    get the accumulation of proposals
    """

    submit = {}
    for proposal in lake["proposals"][year]:
        date = proposal[5].split(" ")[0]
        if date not in submit:
            submit[date] = 0
        submit[date] += 1

    return submit
