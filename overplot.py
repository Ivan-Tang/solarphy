import matplotlib.pyplot as plt
import numpy as np

import astropy.units as u
from astropy.coordinates import SkyCoord

import sunpy.map
from sunpy.data.sample import AIA_193_IMAGE, HMI_LOS_IMAGE

aia, hmi = sunpy.map.Map(AIA_193_IMAGE, HMI_LOS_IMAGE)

bottom_left = SkyCoord(30 * u.deg, -40 * u.deg, frame='heliographic_stonyhurst')
top_right = SkyCoord(70 * u.deg, 0 * u.deg, frame='heliographic_stonyhurst')

sub_aia = aia.submap(bottom_left, top_right=top_right)
sub_hmi = hmi.submap(bottom_left, top_right=top_right)

fig = plt.figure(figsize=(11, 5))

ax1 = fig.add_subplot(121, projection=sub_aia)
sub_aia.plot(axes=ax1, clip_interval=(1, 99.99)*u.percent)

ax2 = fig.add_subplot(122, projection=sub_hmi)
sub_hmi.plot(axes=ax2)

fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(projection=sub_aia)
sub_aia.plot(axes=ax, clip_interval=(1, 99.99)*u.percent)
sub_aia.draw_grid(axes=ax)

ax.set_title("AIA 193 with HMI magnetic field strength contours", y=1.1)

levels = [50, 100, 150, 300, 500, 1000] * u.Gauss
bounds = ax.axis()
cset = sub_hmi.draw_contours(levels, axes=ax, cmap='seismic', alpha=0.5)
ax.axis(bounds)
plt.colorbar(cset,
             label=f"Magnetic Field Strength [{sub_hmi.unit}]",
             ticks=list(levels.value) + [0],
             shrink=0.8,
             pad=0.17)

plt.show()