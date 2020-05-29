"""
analyzer.extractor is the raw data extractor specification,
the abstract class template is provided below, each extractor
class instance needs to inherit it and implement all abstract
method in order to communicate with analyzer.provider.
"""

import abc
from typing import Any

from loguru import logger

from analyzer.config import PEEK_MAXIMUM


class Extractor(abc.ABC):
    """
    Extractor is the abstract class template for extractor instances,
    the class attributes hold_data and export_data could be overwritten
    by some data type that iterable (e.g. dict, set).

    The hold_data is act as a buffer that stores temporary data
    during your operations, you can check it via peek_hold_data which
    can make your debugging more convenient.

    But the export_data is for final data only, it means no artifacts
    should be put into the field to avoid unexpected errors while
    anlayzer.provider try to collect data from extractors.

    The mechanism of extractor decribed above could be overwrote as
    you want, but just needs to meets the communication required
    with analyzer.provider.
    """

    layer = "extracor"
    peek_tpl = "\n===[ {NAME} current {FIELD} ]===\n{SUM} records in total"
    extract_log_tpl = "extractor {NAME} start extracting raw data..."
    hold_data = []  # type: Any
    export_data = []  # type: Any

    @classmethod
    @abc.abstractmethod
    def extract(cls):
        """
        The extract method should be implemented to extract
        raw data for specified directories.
        """
        raise NotImplementedError("Extractor.extract not implemented!")

    @classmethod
    @abc.abstractmethod
    def transform(cls):
        """
        The transform method should be implemented to transform
        the raw data into particular shape.
        """
        raise NotImplementedError("Extractor.transform not implemented!")

    @classmethod
    def peek_hold_data(cls):
        """
        The peek_hold_data method was implemented to print out
        current hold_data within the extractor.
        """
        # peek hold data
        print(cls.peek_tpl.format(NAME=cls.__name__, FIELD="hold_data", SUM=len(cls.hold_data)))
        try:
            for i in range(min(len(cls.hold_data), PEEK_MAXIMUM)):
                print(cls.export_data[i])
        except TypeError:
            logger.error("current hold_data is not iterable")

        print("")

    @classmethod
    def peek_export_data(cls):
        """
        The peek_export_data method was implemented to print out
        current export_data within the extractor.
        """
        # peek export data
        print(cls.peek_tpl.format(NAME=cls.__name__, FIELD="export_data", SUM=len(cls.export_data)))
        try:
            for i in range(min(len(cls.export_data), PEEK_MAXIMUM)):
                print(cls.export_data[i])
        except TypeError:
            logger.error("current export_data is not iterable")

        print("")

    @classmethod
    def export(cls):
        """
        The output method should be implemented to obtain
        processed data directly.
        """
        return cls.export_data
