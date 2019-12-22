import swisseph as swe
#from __future__ import division
from math import floor, ceil
from collections import namedtuple as struct
import datetime
import pytz
from tzwhere import tzwhere

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
def convert_angle(angle):
    if 0 < angle < 30:
        return angle, "Aries"
    elif 30 <= angle < 60:
        return angle - 30, "Taurus"
    elif 60 <= angle < 90:
        return angle - 60, "Gemini"
    elif 90 <= angle < 120:
        return angle - 90, "Cancer"
    elif 120 <= angle < 150:
        return angle - 120, "Leo"
    elif 150 <= angle < 180:
        return angle - 150, "Virgo"
    elif 180 <= angle < 210:
        return angle - 180, "Libra"
    elif 210 <= angle < 240:
        return angle - 210, "Scorpio"
    elif 240 <= angle < 270:
        return angle - 240, "Sagittarius"
    elif 270 <= angle < 300:
        return angle - 270, "Capricorn"
    elif 300 <= angle < 330:
        return angle - 300, "Aquarius"
    elif 330 <= angle < 360:
        return angle - 330, "Pisces"
def decdeg2dms(deg):
    d = int(deg)
    mins = (deg - d) * 60
    m = int(mins)
    s = int(round((mins - m) * 60))
    return [d, m, s]
Date = struct('Date', ['year', 'month', 'day', 'hour','greg'])
Place = struct('Location', ['latitude', 'longitude'])
def getTZ(Lat,Lon):
    from tzwhere import tzwhere
    tzwhere = tzwhere.tzwhere()
    timezone_str = tzwhere.tzNameAt(float(Lat), float(Lon)) # Seville coordinates
    return timezone_str

    
def process_return(planet_path_dictionary):
    return ""