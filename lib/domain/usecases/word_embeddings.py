"""
Usecase for wordembeddings
"""


import csv as _csv
import attr as _attr
import numpy as _np
import geopandas as _gpd
import matplotlib.pyplot as _plt


import lib.infra.stream.word_embeddings as _infra


@_attr.s
class WordEmbeddings:
    """
    Word embeddings
    """

    file_path = _attr.ib()
    model_name = _attr.ib()

    def load_all(self):
        """
        Load model from hdd or web
        """
        return _infra.WordEmbeddingsRepository(self.file_path, self.model_name).load_all()

    def save(self, url):
        """
        Save model to hdd
        """
        _infra.WordEmbeddingsRepository(self.file_path, self.model_name).save(url)

    @classmethod
    def get_countries(cls):
        """
        Read csv file with all countries from data directory
        """
        return list(_csv.DictReader(open("data/countries.csv")))

    @classmethod
    def get_country_vecs(cls, model, countries):
        """
        Write countries into an array
        """
        return _np.asarray([model[country["name"]] for country in countries])

    def rank_countries(self, model, term, topn=10, field="name"):
        """
        Bring countrie-vectors in the right order with ther distance
        """
        countries = self.get_countries()
        country_vecs = self.get_country_vecs(model, countries)
        if not term in model:
            return []

        vec = model[term]
        dists = _np.dot(country_vecs, vec)
        return [
            (countries[idx][field], float(dists[idx]))
            for idx in reversed(_np.argsort(dists)[-topn:])
        ]

    def map_term(self, model, world, term):
        """
        Plot the map
        """
        data = {
            key.upper(): value
            for key, value in self.rank_countries(model, term, topn=0, field="cc3")
        }
        world[term] = world["iso_a3"].map(data)
        world[term] /= world[term].max()
        world.dropna().plot(term, cmap="OrRd")
        _plt.show()

    @classmethod
    def get_world(cls):
        """
        Get geometrical world data from geopandas
        """
        world = _gpd.read_file(_gpd.datasets.get_path("naturalearth_lowres"))
        return world
