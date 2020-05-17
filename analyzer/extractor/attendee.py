"""
analyzer.extractor.attendee comtains extractors for attendee data.
"""


import csv
from typing import Dict

from loguru import logger

from analyzer.extractor import Extractor
from analyzer.config import (
    ATTENDEE_STANDARD,
    ATTENDEE_RESERVED,
    ATTENDEE_DISCOUNT,
    ATTENDEE_COLUMNS
)


class Attendee2019(Extractor):
    """
    Attendee2019 is a extractor for attendee data in 2019.
    """
    hold_data = {}  # type: Dict[str, list]

    @classmethod
    def extract(cls):
        """
        extract from raw data.
        """
        group_file = {
            "standard": ATTENDEE_STANDARD,
            "reserved": ATTENDEE_RESERVED,
            "discount": ATTENDEE_DISCOUNT,
        }
        logger.info(cls.extract_log_tpl.format(
            NAME=cls.__name__
        ))
        for group in group_file:
            try:
                with open(group_file[group], newline="") as raw:
                    reader = csv.reader(raw)
                    cls.hold_data[group] = list(reader)
            except FileNotFoundError:
                logger.error(group_file[group] + "raw data file not found")

    @classmethod
    def transform(cls):
        """
        transform raw data to well-defined shape.
        """

        # figure out the correspounding indexes for the headers
        # describe in ATTENDEE_COLUMNS
        topic_index = {
            "standard": [
                cls.hold_data["standard"][0].index(x)
                if x in cls.hold_data["standard"][0]
                else -1
                for x in ATTENDEE_COLUMNS
            ],
            "reserved": [
                cls.hold_data["reserved"][0].index(x)
                if x in cls.hold_data["reserved"][0]
                else -1
                for x in ATTENDEE_COLUMNS
            ],
            "discount": [
                cls.hold_data["discount"][0].index(x)
                if x in cls.hold_data["discount"][0]
                else -1
                for x in ATTENDEE_COLUMNS
            ],
        }

        # collect data with specified index and reform them
        topic_data = {
            "standard": (
                [row[x] if x != -1 else "" for x in topic_index["standard"]]
                for row in cls.hold_data["standard"][1:]
            ),
            "reserved": (
                [row[x] if x != -1 else "" for x in topic_index["reserved"]]
                for row in cls.hold_data["reserved"][1:]
            ),
            "discount": (
                [row[x] if x != -1 else "" for x in topic_index["discount"]]
                for row in cls.hold_data["discount"][1:]
            ),
        }

        # concat all types of attendee data
        cls.export_data = (
            list(topic_data["standard"])
            + list(topic_data["reserved"])
            + list(topic_data["discount"])
        )


Attendee2019.extract()
Attendee2019.transform()
