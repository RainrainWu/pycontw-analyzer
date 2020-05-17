"""
analyzer.extractor.programs comtains extractors for programs data.
"""


import csv

from loguru import logger

from analyzer.extractor import Extractor
from analyzer.config import PROGRAMS_2019, PROGRAMS_COLUMNS


class Program2019(Extractor):
    """
    Program2019 is a extractor for programs data in 2019.
    """

    @classmethod
    def extract(cls):
        """
        extract from raw data.
        """
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        try:
            with open(PROGRAMS_2019, newline="") as raw:
                reader = csv.reader(raw)
                cls.hold_data = list(reader)
        except FileNotFoundError:
            logger.error(PROGRAMS_2019 + "raw data file not found")

    @classmethod
    def transform(cls):
        """
        transform raw data to well-defined shape.
        """

        # figure out the correspounding indexes for the headers
        # describe in PROGRAM_COLUMNS
        topic_index = [
            cls.hold_data[0].index(x) if x in cls.hold_data[0] else -1
            for x in PROGRAMS_COLUMNS
        ]

        # collect data with specified index and reform them
        topic_data = (
            [row[x] if x != -1 else "" for x in topic_index]
            for row in cls.hold_data[1:]
        )

        # concat all types of attendee data
        cls.export_data = list(topic_data)


Program2019.extract()
Program2019.transform()
