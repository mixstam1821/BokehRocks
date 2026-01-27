import xarray as xr
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
from bokeh_rocks import contourf_map, ccrs, show, save_plot

# Coordinates
lats = np.linspace(-90, 90, 181)
lons = np.linspace(-180, 180, 360)
times = pd.date_range("2000-01-01", periods=12, freq="MS")

lat2d, lon2d = np.meshgrid(lats, lons, indexing="ij")

# Very smooth background gradient (no randomness)
background = 160 + 80 * np.exp(-(lat2d / 55)**2)*np.cos(np.deg2rad(lon2d * 1))

# Extremely low-amplitude, heavily smoothed noise
noise = np.random.normal(0, 1, (len(times), len(lats), len(lons)))
noise = gaussian_filter(noise, sigma=(0, 12, 24))

data = background[None, :, :] + 6 * noise
data = np.clip(data, 0, 300)

# Xarray
era5_ssr = xr.Dataset(
    {"ssr": (["time", "lat", "lon"], data)},
    coords={"time": times, "lat": lats, "lon": lons},
)["ssr"].mean("time")

# Plot
p2 = contourf_map(
    era5_ssr,
    title="Synthetic SSR – Ultra-Smooth Climatology",
    levels=10,
    palette="Cividis256",
    vmin=0,
    vmax=300,
    projection=ccrs.Sinusoidal(),
    cbar_title="SSR (W/m²)",
)

show(p2)
save_plot(p2, "output/map_projections_05")
