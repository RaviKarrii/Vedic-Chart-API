import swisseph as swe
#from __future__ import division
from math import floor, ceil
from collections import namedtuple as struct
from timezonefinder import TimezoneFinder
import datetime
import pytz
import json

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

def getTZ_old(Lat,Lon):
    from tzwhere import tzwhere
    tzwhere = tzwhere.tzwhere()
    timezone_str = tzwhere.tzNameAt(float(Lat), float(Lon)) # Seville coordinates
    return timezone_str

def getTZ(Lat,Lon):
    tf = TimezoneFinder()
    latitude, longitude = float(Lat), float(Lon)
    return tf.timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'

out = {}
Ascendant_output = {}
out_maker = {}

def process(Json_payload):
    #return Json_payload
    Lat,Lon = Json_payload["Lat"],Json_payload["Lon"]
    DY,DMon,DD,DH,DMin,DS = Json_payload["Year"],Json_payload["Month"],Json_payload["Day"],Json_payload["Hour"],Json_payload["Min"],"00"
    naive = datetime.datetime.strptime (DY+"-"+DMon+"-"+DD+" "+DH+":"+DMin+":"+DS, "%Y-%m-%d %H:%M:%S")
    try:
        local = pytz.timezone(getTZ(float(Lat),float(Lon)))
    except Exception as e:
        print(e)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    utc_dt = utc_dt.strftime ("%Y:%m:%d:%H:%M:%S")
    DY,DMon,DD,DH,DMin,DS = utc_dt.split(":")
    kkd = Place(float(Lat),float(Lon))
    dtR = swe.utc_to_jd(int(DY),int(DMon),int(DD),int(DH),int(DMin),int(DS),1)
    swe.set_ephe_path('files')
    #swe.set_topo(12.9667, 77.5667, 0);
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    for key in PLANETS:
    
        output = swe.calc_ut(dtR[0], PLANETS[key], flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED)
        ActualDegrees = decdeg2dms((output[0]))
        out_maker = {}
        out_maker["ActualDegrees"] = str(ActualDegrees[0])
        out_maker["ConvertedDegrees"] = str(convert_angle(ActualDegrees[0])[0])
        out_maker["ConvertedMin"] = str(ActualDegrees[1])
        out_maker["ConvertedSec"] = str(ActualDegrees[2])
        out_maker["Zodiad"] = str(convert_angle(ActualDegrees[0])[1])
        out[key] =  out_maker

    ascDeg = swe.houses_ex(dtR[0], kkd[0], kkd[1], str.encode('A'), flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED)
    DeG = decdeg2dms(convert_angle(ascDeg[0][0])[0])
    out["Ascendant"] = str(ascDeg[0][0]) + " " +str(DeG[0])+ " " + str(DeG[1]) + " " + str(DeG[2]) + " " + str(convert_angle(ascDeg[0][0])[1])
    return out
    

