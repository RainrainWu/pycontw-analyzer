"""
analyzer.provider.program is a unified interface which provide
more explainable proposals-related data for inspecting.
"""


from analyzer.provider import lake


def get_acceptance_with_title():
    """
    get the mapping of acceptance to the titles.
    """
    years = ["2016", "2017", "2018", "2019"]
    acceptance = {}

    for year in years:
        acceptance[year] = {}
        acceptance[year]["accept"] = [
            x[0] for x in lake["proposals"][year] if (x[6] == "f" and x[7] == "t")
        ]
        acceptance[year]["unaccept"] = [
            x[0] for x in lake["proposals"][year] if (x[6] != "f" or x[7] != "t")
        ]
    return acceptance
