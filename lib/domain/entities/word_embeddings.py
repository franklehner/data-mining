"""
Abstract Base class for infrastructure
"""


import abc as _abc


class AbstractWordEmbeddings:
    """
    Abstract class for wordembeddings
    """
    __metaclass__ = _abc.ABCMeta

    @_abc.abstractmethod
    def load_all(self):
        """
        Load model from hdd
        """
        raise NotImplementedError

    @_abc.abstractmethod
    def save(self, url):
        """
        Save model to hdd
        """
        raise NotImplementedError
