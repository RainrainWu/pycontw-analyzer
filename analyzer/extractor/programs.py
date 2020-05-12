"""
analyzer.extractor.programs comtains extractors for programs data.
"""


import csv
from typing import List

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
    program_data = []  # type: List
    export_data = []  # type: List

    @classmethod
    def extract(cls):
        """
        extract from raw data.
        """
        with open(PROGRAM_2019, newline="") as raw:
            reader = csv.reader(raw)
            cls.program_data = list(reader)

    @classmethod
    def transform(cls):
        """
        transform raw data to well-defined shape.
        """

        # figure out the correspounding indexes for the headers
        # describe in cls.topic_header
        topic_index = [
            cls.program_data[0].index(x)
            if x in cls.program_data[0]
            else -1
            for x in cls.topic_header.values()
        ]

        # collect data with specified index and reform them
        topic_data = (
            [row[x] if x != -1 else "" for x in topic_index]
            for row in cls.program_data[1:]
        )

        # concat all types of attendee data
        cls.export_data = list(topic_data)

    @classmethod
    def peek(cls):
        """
        peek holding data.
        """
        for i in range(5):
            print(cls.export_data[i])

    @classmethod
    def export(cls):
        """
        export processed data.
        """
        return cls.export_data


Program2019.extract()
Program2019.transform()
