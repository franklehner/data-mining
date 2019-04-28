# pylint: disable=no-member
"""
App for word_embeddings
"""


import os as _os
import attr as _attr

import lib.domain.usecases.word_embeddings as _usecase


@_attr.s
class WordEmbeddings:
    """
    Main class for word embeddings
    """

    file_path = _attr.ib()
    model_name = _attr.ib()
    term = _attr.ib()

    def run(self):
        """
        Runner method
        """
        self.get_model()
        usecase = _usecase.WordEmbeddings(self.file_path, self.model_name)
        model = usecase.load_all()
        world = usecase.get_world()
        terms = self.term.split(",")
        for term in terms:
            usecase.map_term(model, world, term)

    def check_file(self):
        """
        Check if model is already on hdd
        """
        return _os.path.isfile(
            _os.path.join(self.file_path, self.model_name)
        )

    def get_model(self):
        """
        Get the official model
        """
        url = "https://deeplearning4jblob.blob.core.windows.net/resources/wordvectors/%s.gz"
        url = url % self.model_name
        if not self.check_file():
            _usecase.WordEmbeddings(self.file_path, self.model_name, self.term).save(url)
