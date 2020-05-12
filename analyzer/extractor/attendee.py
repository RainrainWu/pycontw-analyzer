"""
analyzer.extractor.attendee comtains extractors for attendee data.
"""


import csv

from analyzer.extractor import Extractor
from analyzer.config import (
    ATTENDEE_STANDARD,
    ATTENDEE_RESERVED,
    ATTENDEE_DISCOUNT
)


class Attendee2019(Extractor):
    """
    Attendee_2019 is a extractor for attendee data in 2019.
    """
    group_data = {}
    topic_header = {
        'seniority': 'Years of Using Python / 使用 Python 多久',
        'interest': 'Area of Interest / 興趣領域',
        'company': 'Company  / 服務單位 (For students or teachers, fill in the School + Department Name)',
        'job': 'Job Title / 職稱 (If you are a student, fill in "student")',
        'region': 'Come From / 國家或地區',
    }
    export_data = {}

    @classmethod
    def extract(cls):
        """
        extract from raw data.
        """
        group_file = {
            'standard': ATTENDEE_STANDARD,
            'reserved': ATTENDEE_RESERVED,
            'discount': ATTENDEE_DISCOUNT,
        }
        for group in group_file:
            with open(group_file[group], newline='') as raw:
                reader = csv.reader(raw)
                cls.group_data[group] = list(reader)

    @classmethod
    def transform(cls):
        """
        transform raw data to well-defined shape.
        """

        # figure out the correspounding indexes for the headers
        # describe in cls.topic_header
        topic_index = {
            'standard': [
                cls.group_data['standard'][0].index(x)
                if x in cls.group_data['standard'][0] else -1
                for x in cls.topic_header.values()
            ],
            'reserved': [
                cls.group_data['reserved'][0].index(x)
                if x in cls.group_data['reserved'][0] else -1
                for x in cls.topic_header.values()
            ],
            'discount': [
                cls.group_data['discount'][0].index(x)
                if x in cls.group_data['discount'][0] else -1
                for x in cls.topic_header.values()
            ],
        }

        # collect data with specified index and reform them
        topic_data = {
            'standard': (
                [row[x] if x != -1 else '' for x in topic_index['standard']]
                for row in cls.group_data['standard'][1:]
            ),
            'reserved': (
                [row[x] if x != -1 else '' for x in topic_index['reserved']]
                for row in cls.group_data['reserved'][1:]
            ),
            'discount': (
                [row[x] if x != -1 else '' for x in topic_index['discount']]
                for row in cls.group_data['discount'][1:]
            ),
        }

        # concat all types of attendee data
        cls.export_data = list(topic_data['standard']) + list(topic_data['reserved']) + list(topic_data['discount'])

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

Attendee2019.extract()
Attendee2019.transform()
