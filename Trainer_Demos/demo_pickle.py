#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO PRESERVE ONE PYTHON object
# (data + structure) to a file using the pickle module.
"""
    Docstring:
"""
import pickle
import pprint

movies = { 'joe': ['lotr', 'rocky', 'interstellar'],
           'merrick': ['matrix', 'godfather', 'godfather II'],
           'niteen': ['godfather', '3idiots', 'benjamin button'],
           'brad': ['jaws', 'star wars', 'rocky'],
           'mahendran': ['top gun', 'terminator', 'rambo']
}

# Open PICKLE file for WRITING in BINARY mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.p", mode="wb") as fh_out:
    pickle.dump(movies, fh_out)

# Open PICKLE file for READING in BINARY mode.
with open(r"c:\labs\projects\Python3_labs\Trainer_Demos\movies.p", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)