"""
App for word_embeddings
"""


import attr as _attr


@_attr.s
class WordEmbeddings:
    """
    Main class for word embeddings
    """

    url = _attr.ib()

    def run(self):
        """
        Runner method
        """
        print(self.url)
