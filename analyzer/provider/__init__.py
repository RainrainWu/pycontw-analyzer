"""
analyzer.provider is a unified inerface which provide more
explainable data for inspecting.
"""

from loguru import logger

from analyzer.extractor.attendee import Attendee2019
from analyzer.extractor.programs import Program2019
from analyzer.extractor.vacancies import VacancyLinkedIn, VacancyCakeResume
from analyzer.extractor.proposals import (
    Proposal2016,
    Proposal2017,
    Proposal2018,
    Proposal2019,
)

logger.info("provider start collecting data...")
lake = {
    "attendee": Attendee2019.export(),
    "programs": Program2019.export(),
    "proposals": {
        "2016": Proposal2016.export(),
        "2017": Proposal2017.export(),
        "2018": Proposal2018.export(),
        "2019": Proposal2019.export(),
    },
    "vacancies": {
        "linked_in": VacancyLinkedIn.export(),
        "cake_resume": VacancyCakeResume.export(),
    },
}
