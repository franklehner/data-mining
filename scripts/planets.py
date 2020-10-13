#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Statistics over planets
"""


import seaborn as _sns


planets = _sns.load_dataset("planets")

print(planets.shape)
print(planets.head())
print(planets.describe())
print(planets.dropna().describe())
print(planets.groupby("method"))
print(planets.groupby("method")["orbital_period"])
print(planets.groupby("method")["orbital_period"].median())

for method, group in planets.groupby("method"):
    print("{0:30} shape={1}".format(method, group.shape))

print(planets.groupby("method")["year"].describe())
