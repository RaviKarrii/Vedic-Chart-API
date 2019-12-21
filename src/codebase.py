import swisseph as swe
from __future__ import division
from math import floor, ceil
from collections import namedtuple as struct

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE
}
ASPECT_SYMBOLS = {
    "Conjunction": "\u260C",
    "Semi-Sextile": "\u26BA",
    "Semi-Square": "\u2220",
    "Sextile": "\u26B9",
    "Quintile": "Q",
    "Square": "\u25A1",
    "Trine": "\u25B3",
    "Sesquiquadrate": "\u26BC",
    "BiQuintile": "bQ",
    "Quincunx": "\u26BB",
    "Opposite": "\u260D",
}