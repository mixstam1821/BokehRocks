
import xarray as xr
import pandas as pd
import numpy as np
from bokeh_rocks import contourf_map,ccrs, show, save_plot
# Simple coordinates
lats = np.linspace(-90, 90, 181)
lons = np.linspace(-180, 180, 360)
times = pd.date_range('2000-01-01', periods=12, freq='MS')
# Base latitudinal pattern (more radiation near equator)
lat_factor = np.cos(np.deg2rad(lats))  # shape (lat,)
lat_factor = lat_factor / lat_factor.max()

# Expand to 3D
lat_3d = lat_factor[None, :, None]

# Smooth random variability
noise = np.random.normal(loc=0, scale=20, size=(len(times), len(lats), len(lons)))

data = 250 * lat_3d + noise
data = np.clip(data, 0, 300)

from scipy.ndimage import gaussian_filter

noise = np.random.normal(0, 1, (len(times), len(lats), len(lons)))
noise = gaussian_filter(noise, sigma=(0, 3, 6))  # smooth in lat/lon

data = 220 * lat_3d + 40 * noise
data = np.clip(data, 0, 300)
# Create xarray
era5_ssr = xr.Dataset(
    {'ssr': (['time', 'lat', 'lon'], data)},
    coords={'time': times, 'lat': lats, 'lon': lons}
)['ssr'].mean('time')

# Plot with contourf style
p2 = contourf_map(
    era5_ssr,
    title="ERA5 SSR - Mollweide",
    levels=10,
    palette='Plasma256',
    vmin=0,
    vmax=300, 
    projection=ccrs.Orthographic(central_latitude=30),
    cbar_title="ERA5 SSR (W/m²)", width=900, height=800
)

show(p2)
save_plot(p2, "output/map_projections_01")