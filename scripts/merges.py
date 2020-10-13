#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Examples for merging in python pandas
"""


import pandas as _pd


# 1-zu-1 joins
df1 = _pd.DataFrame(
    {
        "Mitarbeiter": ["Bob", "Jake", "Lisa", "Sue"],
        "Abteilung": ["Buchhaltung", "Entwicklung", "Entwicklung", "Personal"],
    },
)

df2 = _pd.DataFrame(
    {
        "Mitarbeiter": ["Lisa", "Bob", "Jake", "Sue"],
        "MA_seit": [2004, 2008, 2012, 2014],
    },
)

print(df1)
print(df2)

df3 = _pd.merge(df1, df2)
print(df3)


# n-zu-1 joins
df4 = _pd.DataFrame(
    {
        "Abteilung": ["Buchhaltung", "Entwicklung", "Personal"],
        "Vorgesetzter": ["Carly", "Guido", "Steve"],
    },
)
print(_pd.merge(df3, df4))

# n-zu-n join
df5 = _pd.DataFrame(
    {
        "Abteilung": [
            "Buchhaltung",
            "Buchhaltung",
            "Entwicklung",
            "Entwicklung",
            "Personal",
            "Personal",
        ],
        "Faehigkeiten": [
            "Mathe",
            "Tabellenkalkulation",
            "Programmierung",
            "Linux",
            "Tabellenkalkulation",
            "Organisation",
        ],
    },
)

print(_pd.merge(df1, df5))
print(_pd.merge(df1, df2, on="Mitarbeiter"))

df3 = _pd.DataFrame(
    {
        "Name": ["Bob", "Jake", "Lisa", "Sue"],
        "Gehalt": [70000, 80000, 120000, 90000],
    },
)

print(_pd.merge(df1, df3, left_on="Mitarbeiter", right_on="Name"))
print(_pd.merge(df1, df3, left_on="Mitarbeiter", right_on="Name").drop("Name", axis=1))

df1a = df1.set_index("Mitarbeiter")
df2a = df2.set_index("Mitarbeiter")

print("df1a", df1a)
print("df2a", df2a)
print(_pd.merge(df1a, df2a, left_index=True, right_index=True))

# joins
print(df1a.join(df2a))

print(_pd.merge(df1a, df3, left_index=True, right_on="Name"))

# Mengenarithmetik bei joins
df6 = _pd.DataFrame(
    {
        "Name": ["Peter", "Paul", "Mary"],
        "Speise": ["Fisch", "Bohnen", "Brot"],
    },
    columns=["Name", "Speise"],
)

df7 = _pd.DataFrame(
    {
        "Name": ["Mary", "Joseph"],
        "Getraenk": ["Wein", "Bier"],
    },
    columns=["Name", "Getraenk"],
)

print(_pd.merge(df6, df7))
print(_pd.merge(df6, df7, how="outer"))
print(_pd.merge(df6, df7, how="left"))

# Konflikte bei Spaltennamen
df8 = _pd.DataFrame(
    {
        "Name": ["Bob", "Jake", "Lisa", "Sue"],
        "Rang": [1, 2, 3, 4],
    },
)
df9 = _pd.DataFrame(
    {
        "Name": ["Bob", "Jake", "Lisa", "Sue"],
        "Rang": [3, 1, 4, 2],
    },
)
print(_pd.merge(df8, df9, on="Name"))
print(_pd.merge(df8, df9, on="Name", suffixes=["_L", "_R"]))
