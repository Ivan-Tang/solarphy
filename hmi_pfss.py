import os

import matplotlib.pyplot as plt

import astropy.units as u

import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a

from sunkit_magex import pfss

series = a.jsoc.Series('hmi.synoptic_mr_polfil_720s')
crot = a.jsoc.PrimeKey('CAR_ROT', 2210)

result = Fido.search(series, crot, a.jsoc.Notify(os.environ["JSOC_EMAIL"]))
files = Fido.fetch(result)