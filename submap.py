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
my_submap = my_map.submap(roi_bottom_left, top_right=roi_top_right)

#一些点
coords = SkyCoord(Tx=300 * u.arcsec, Ty=200 * u.arcsec, frame=my_map.coordinate_frame)


fig = plt.figure()
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
my_submap = my_map.submap(roi_bottom_left, top_right=roi_top_right)

#一些点
coords = SkyCoord(Tx=300 * u.arcsec, Ty=200 * u.arcsec, frame=my_map.coordinate_frame)


fig = plt.figure()

ax = fig.add_subplot(projection=my_submap)

#绘制图像
my_submap.plot(axes=ax, cmap = 'hmimag')

ax.plot_coord(coords, 'o')
#contour1 = ax.contourf(my_submap.data, colors='white', levels=[1000, my_submap.max()], linestyles='dashed')
#contour2 = ax.contourf(my_submap.data, colors='black', levels=[-1000, -my_submap.min()], linestyles='dotted')
#plt.colorbar(contour1)
#plt.colorbar(contour2)
plt.colorbar()
plt.show()

