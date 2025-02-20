import sunpy.map
import sunpy.data.sample  
import matplotlib.colors
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord


my_map = sunpy.map.Map('./data/hmi.m_45s.2024.11.06_06_01_30_TAI.magnetogram.fits')  

print(my_map.data.shape, my_map.date, my_map.exposure_time, my_map.dimensions, my_map.dtype) 

#一个区域  
roi_bottom_left = SkyCoord(Tx=0*u.arcsec, Ty=0*u.arcsec, frame=my_map.coordinate_frame)
roi_top_right = SkyCoord(Tx=500*u.arcsec, Ty=500*u.arcsec, frame=my_map.coordinate_frame)

#一些点
coords = SkyCoord(Tx=300 * u.arcsec, Ty=200 * u.arcsec, frame=my_map.coordinate_frame)


fig = plt.figure()

ax = fig.add_subplot(projection=my_map)

#绘制图像
my_map.plot(axes=ax, cmap = 'hmimag')

#绘制区域
my_map.draw_quadrangle(roi_bottom_left, top_right=roi_top_right, axes=ax, color='C0')

#绘制边缘
my_map.draw_limb(axes=ax, color='C0')


#绘制点
ax.plot_coord(coords, 'o')
ax.plot_coord(my_map.center, 'X')



plt.colorbar()
plt.show()