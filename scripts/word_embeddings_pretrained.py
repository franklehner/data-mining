#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-value-for-parameter
"""
Word embeddings
"""


import click as _click

import lib.app.word_embeddings as _app


@_click.command()
@_click.option("--file_path", default="generated")
@_click.option("--model_name", default="GoogleNews-vectors-negative300.bin")
@_click.option("--term", default="cappucino")
def cli(file_path, model_name, term):
    """
    Client for plotting word embeddings based map
    """
    _app.WordEmbeddings(file_path, model_name, term).run()


if __name__ == "__main__":
    cli()
