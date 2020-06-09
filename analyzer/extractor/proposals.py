"""
analyzer.extractor.proposal contains extractors for proposals data.
"""


import re

from loguru import logger

from analyzer.extractor import Extractor

SQL_FILE = "data/proposals/sql_dump/public.proposals_talkproposal.sql"
proposal_hash_pattern = re.compile("[0-9]+")
target_index = [1, 2, 3, 6, 12, 13, 15, 16, 17]


class Proposal2019(Extractor):
    """
    Proposal2019 is a extractor for proposal data in 2019.
    """

    hold_data = []
    export_data = []

    @classmethod
    def extract(cls):
        """
        extract from postgresql dump.
        """
        conf_tag = "pycontw-2019"
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        with open(SQL_FILE, "r") as read_file:
            lines = read_file.readlines()
            for line in lines:

                # match line with hash id and corresponding conference
                line = line.split("\t")
                if proposal_hash_pattern.match(line[0]) and (line[17] == conf_tag):
                    cls.hold_data += [line]

    @classmethod
    def transform(cls):
        """
        transform raw data to well-define shape.
        """
        for proposal in cls.hold_data:
            cls.export_data += [[proposal[x] for x in target_index]]


class Proposal2018(Extractor):
    """
    Proposal2018 is a extractor for proposal data in 2018.
    """

    hold_data = []
    export_data = []

    @classmethod
    def extract(cls):
        """
        extract from postgresql dump.
        """
        conf_tag = "pycontw-2018"
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        with open(SQL_FILE, "r") as read_file:
            lines = read_file.readlines()
            for line in lines:

                # match line with hash id and corresponding conference
                line = line.split("\t")
                if proposal_hash_pattern.match(line[0]) and (line[17] == conf_tag):
                    cls.hold_data += [line]

    @classmethod
    def transform(cls):
        """
        transform raw data to well-define shape.
        """
        for proposal in cls.hold_data:
            cls.export_data += [[proposal[x] for x in target_index]]


class Proposal2017(Extractor):
    """
    Proposal2017 is a extractor for proposal data in 2017.
    """

    hold_data = []
    export_data = []

    @classmethod
    def extract(cls):
        """
        extract from postgresql dump.
        """
        conf_tag = "pycontw-2017"
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        with open(SQL_FILE, "r") as read_file:
            lines = read_file.readlines()
            for line in lines:

                # match line with hash id and corresponding conference
                line = line.split("\t")
                if proposal_hash_pattern.match(line[0]) and (line[17] == conf_tag):
                    cls.hold_data += [line]

    @classmethod
    def transform(cls):
        """
        transform raw data to well-define shape.
        """
        for proposal in cls.hold_data:
            cls.export_data += [[proposal[x] for x in target_index]]


class Proposal2016(Extractor):
    """
    Proposal2016 is a extractor for proposal data in 2016.
    """

    hold_data = []
    export_data = []

    @classmethod
    def extract(cls):
        """
        extract from postgresql dump.
        """
        conf_tag = "pycontw-2016"
        logger.info(cls.extract_log_tpl.format(NAME=cls.__name__))
        with open(SQL_FILE, "r") as read_file:
            lines = read_file.readlines()
            for line in lines:

                # match line with hash id and corresponding conference
                line = line.split("\t")
                if proposal_hash_pattern.match(line[0]) and (line[17] == conf_tag):
                    cls.hold_data += [line]

    @classmethod
    def transform(cls):
        """
        transform raw data to well-define shape.
        """
        for proposal in cls.hold_data:
            cls.export_data += [[proposal[x] for x in target_index]]


Proposal2016.extract()
Proposal2016.transform()

Proposal2017.extract()
Proposal2017.transform()

Proposal2018.extract()
Proposal2018.transform()

Proposal2019.extract()
Proposal2019.transform()
