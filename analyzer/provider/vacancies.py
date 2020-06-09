"""
analyzer.provider.vacancies is a unified interface which provide
more explainable vacancies-related data for inspecting.
"""

from analyzer.provider import lake
from analyzer.utils.homogeneous import convert_vacancy_alias


def get_number_of_vancacies_with_type():
    """
    get the mapping of vacancy to their type.
    """
    vacancies_pre = [x[1] for x in lake["vacancies"]["linked_in"][1:]]
    vacancies_pre += [x[1] for x in lake["vacancies"]["cake_resume"][1:]]
    vacancies_post = [convert_vacancy_alias(x) for x in vacancies_pre]
    vacancies = {}
    for vacancy in vacancies_post:
        if vacancy not in vacancies:
            vacancies[vacancy] = 0
        vacancies[vacancy] += 1

    # for i in vacancies:
    #     print("{VACANCY} {NUMBER}".format(VACANCY=i, NUMBER=vacancies[i]))
    return vacancies
