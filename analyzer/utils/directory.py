"""
analyzer.utils.directory specify the directory structure of data files.
"""

import os

from loguru import logger


def init_dir():
    """
    Create mock data directory structure.
    """
    directories = [
        "./data",
        "./data/attendee/",
        "./data/programs/",
        "./data/vacancies/",
        "./mock_data",
        "./mock_data/attendee/",
        "./mock_data/programs/",
        "./mock_data/vacancies/"
    ]
    for directory in directories:
        try:
            if not os.path.exists(directory):
                os.mkdir(directory)
        except FileExistsError:
            logger.error("Directory " + directory + " aready exists")
