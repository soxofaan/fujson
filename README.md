
# FuJSON: less decimals, more fuzzy JSON

FuJSON is a Python module that allows to control the 
formatting of `float`s when JSON encoding, 
typically to dial down the number of decimals.

It builds on the *standard library*'s `json.JSONEncoder`
and *monkey-patches* it to inject custom float formatting.
