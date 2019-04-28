"""
Infrastructure for wordembeddings
"""


import os as _os
import subprocess as _subprocess
import attr as _attr
import keras.utils as _utils
import gensim as _gensim


import lib.domain.entities.word_embeddings as _entity


@_attr.s
class WordEmbeddingsRepository(_entity.AbstractWordEmbeddings):
    """
    load and save pretrained models
    """

    file_path = _attr.ib()
    model_name = _attr.ib()

    def load_all(self):
        """
        load pretrained models
        """
        unzipped = _os.path.join(self.file_path, self.model_name)
        return _gensim.models.KeyedVectors.load_word2vec_format(unzipped, binary=True)

    def save(self, url):
        """
        save pretrained models
        """
        unzipped = _os.path.join(self.file_path, self.model_name)
        path = _utils.get_file(self.model_name + ".gz", url)
        with open(unzipped, "wb") as fout:
            zcat = _subprocess.Popen(
                ["zcat"],
                stdin=open(path),
                stdout=fout
            )
            zcat.wait()
