import os

import matplotlib.pyplot as plt

import astropy.units as u

import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a

from sunkit_magex import pfss

hmi_map = sunpy.map.Map('/Users/IvanTang/Desktop/天文/大创/data/hmi.m_45s.2024.11.06_06_01_30_TAI.magnetogram.fits')

hmi_map = hmi_map.resample([360, 180] * u.pix)
nrho = 35
rss = 2.5
pfss_in = pfss.Input(hmi_map, nrho, rss)
pfss_out = pfss.pfss(pfss_in)

ss_br = pfss_out.source_surface_br
# Create the figure and axes
fig = plt.figure()
ax = plt.subplot(projection=ss_br)

# Plot the source surface map
ss_br.plot()
# Plot the polarity inversion line
ax.plot_coord(pfss_out.source_surface_pils[0])
# Plot formatting
plt.colorbar()
ax.set_title('Source surface magnetic field')

plt.show()