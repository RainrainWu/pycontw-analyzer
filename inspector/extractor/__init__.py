import abc


class Extractor(metaclass=abc.ABCMeta):

    layer = 'extracor'
    data = None

    @classmethod
    @abc.abstractmethod
    def extract(cls):
        
        # The extract method should be implemented to extract
        # raw data for specified directories.
        raise NotImplementedError('Extractor.extract not implemented!')
        return NotImplemented

    @classmethod
    @abc.abstractmethod
    def transform(cls):

        # The transform method should be implemented to transform
        # the raw data into particular shape.
        raise NotImplementedError('Extractor.transform not implemented!')
        return NotImplemented

    @classmethod
    @abc.abstractmethod
    def peek(cls):

        # The show method should be implemented to print out
        # data schema.
        raise NotImplementedError('Extractor.peek not implemented!')
        return NotImplemented

    @classmethod
    @abc.abstractmethod
    def export(cls):

        # The output method should be implemented to obtain
        # processed data directly.
        raise NotImplementedError('Extractor.export not implemented!')
        return NotImplemented