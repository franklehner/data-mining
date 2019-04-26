#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Word embeddings
"""


import click as _click

import lib.app.word_embeddings as _app


@_click.command()
@_click.option("--file_path", default="generated")
@_click.option("--model", default="GoogleNews-vectors-negative300.bin")
@_click.option("--keyword", default="cappucino")
def cli(file_path, model):
    url = "https://deeplearning4jblob.blob.core.windows.net/resources/wordvectors/%s.gz" % model
    _app.WordEmbeddings(url).run()


if __name__ == "__main__":
    cli()
