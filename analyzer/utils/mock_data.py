"""
analyzer.utils.mockdata provides a convenient way to generate mock data.
"""

import os
import csv
import random

from loguru import logger

from analyzer.config import (
    ATTENDEE_COLUMNS,
    MOCK_ATTENDEE_STANDARD,
    MOCK_ATTENDEE_RESERVED,
    MOCK_ATTENDEE_DISCOUNT,
    MOCK_ATTENDEE_NUMBER,
    MOCK_ATTENDEE_AREAS,
    MOCK_ATTENDEE_COMPANIES,
    MOCK_ATTENDEE_JOBS,
    MOCK_ATTENDEE_COUNTRIES,
    PROGRAMS_COLUMNS,
    MOCK_PROGRAMS_2019,
    MOCK_PROGRAMS_NUMBER,
    MOCK_PROGRAMS_CATEGORIES,
    MOCK_PROGRAMS_LEVELS,
)


def random_mask(items):
    """
    mask off some elements in a list randomly.
    """
    mask = [random.random() > 0.5 for _ in items]
    result = []
    for i in items:
        if mask[items.index(i)]:
            result += [i]
    return result


def create_dir():
    """
    Create mock data directory structure.
    """
    directories = ["./mock_data", "./mock_data/attendee/", "./mock_data/programs/"]
    for directory in directories:
        try:
            if not os.path.exists(directory):
                os.mkdir(directory)
        except FileExistsError:
            logger.error("Directory " + directory + " aready exists")


def mock_data_attendee():
    """
    generate mock attendee data.
    """
    for file in [
        MOCK_ATTENDEE_STANDARD,
        MOCK_ATTENDEE_RESERVED,
        MOCK_ATTENDEE_DISCOUNT,
    ]:
        years = [round(random.random() * 20) for _ in range(MOCK_ATTENDEE_NUMBER)]
        areas = [
            ", ".join(random_mask(MOCK_ATTENDEE_AREAS))
            for _ in range(MOCK_ATTENDEE_NUMBER)
        ]
        companies = [
            random.choice(MOCK_ATTENDEE_COMPANIES) for _ in range(MOCK_ATTENDEE_NUMBER)
        ]
        jobs = [random.choice(MOCK_ATTENDEE_JOBS) for _ in range(MOCK_ATTENDEE_NUMBER)]
        countries = [
            random.choice(MOCK_ATTENDEE_COUNTRIES) for _ in range(MOCK_ATTENDEE_NUMBER)
        ]

        with open(file, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            writer.writerow(ATTENDEE_COLUMNS)
            for i in range(MOCK_ATTENDEE_NUMBER):
                writer.writerow(
                    [years[i], areas[i], companies[i], jobs[i], countries[i]]
                )


def mock_data_programs():
    """
    generate mock program data.
    """
    for file in [MOCK_PROGRAMS_2019]:
        titles = ["" for _ in range(MOCK_PROGRAMS_NUMBER)]
        categories = [
            random.choice(MOCK_PROGRAMS_CATEGORIES) for _ in range(MOCK_PROGRAMS_NUMBER)
        ]
        levels = [
            random.choice(MOCK_PROGRAMS_LEVELS) for _ in range(MOCK_PROGRAMS_NUMBER)
        ]
        names = ["" for _ in range(MOCK_PROGRAMS_NUMBER)]

        with open(file, "w", newline="") as write_file:
            writer = csv.writer(write_file)
            writer.writerow(PROGRAMS_COLUMNS)
            for i in range(MOCK_PROGRAMS_NUMBER):
                writer.writerow([titles[i], categories[i], levels[i], names[i]])


create_dir()
mock_data_attendee()
mock_data_programs()
