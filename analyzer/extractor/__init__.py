"""
analyzer.extractor is the raw data extractor specification,
the abstract class template is provided below, each extractor
class instance needs to inherit it and implement all abstract
method in order to communicate with analyzer.provider.
"""

import abc


class Extractor(metaclass=abc.ABCMeta):
    """
    Extractor is the abstract class template for extractor instances.
    """
    layer = 'extracor'
    data = None

    @classmethod
    @abc.abstractmethod
    def extract(cls):
        """
        The extract method should be implemented to extract
        raw data for specified directories.
        """
        raise NotImplementedError('Extractor.extract not implemented!')

    @classmethod
    @abc.abstractmethod
    def transform(cls):
        """
        The transform method should be implemented to transform
        the raw data into particular shape.
        """
        raise NotImplementedError('Extractor.transform not implemented!')

    @classmethod
    @abc.abstractmethod
    def peek(cls):
        """
        The show method should be implemented to print out
        data schema.
        """
        raise NotImplementedError('Extractor.peek not implemented!')

    @classmethod
    @abc.abstractmethod
    def export(cls):
        """
        The output method should be implemented to obtain
        processed data directly.
        """
        raise NotImplementedError('Extractor.export not implemented!')
