"""
analyzer.extractor.programs comtains extractors for programs data.
"""


import csv

from analyzer.extractor import Extractor
from analyzer.config import PROGRAM_2019


class Program2019(Extractor):
    """
    Program2019 is a extractor for programs data in 2019.
    """

    topic_header = {
        "title": "title",
        "category": "category",
        "level": "python_level",
    }

    @classmethod
    def extract(cls):
        """
        extract from raw data.
        """
        with open(PROGRAM_2019, newline="") as raw:
            reader = csv.reader(raw)
            cls.hold_data = list(reader)

    @classmethod
    def transform(cls):
        """
        transform raw data to well-defined shape.
        """

        # figure out the correspounding indexes for the headers
        # describe in cls.topic_header
        topic_index = [
            cls.hold_data[0].index(x)
            if x in cls.hold_data[0]
            else -1
            for x in cls.topic_header.values()
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
