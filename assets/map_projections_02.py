import xarray as xr
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
from bokeh_rocks import contourf_map, ccrs, show, save_plot, mbpal

# Coordinates
lats = np.linspace(-90, 90, 181)
lons = np.linspace(-180, 180, 360)
times = pd.date_range('2000-01-01', periods=12, freq='MS')

# 2D lat/lon grids
lat2d, lon2d = np.meshgrid(lats, lons, indexing="ij")

# --- Large-scale climate structures ---

# Subtropical maxima (~30° N/S)
subtropics = (
    np.exp(-((lat2d - 30) / 15)**2) +
    np.exp(-((lat2d + 30) / 15)**2)
)

# ITCZ cloud belt (reduced SSR near equator)
itcz = np.exp(-(lat2d / 10)**2)

# Planetary longitudinal waves
waves = 0.5 * np.cos(np.deg2rad(lon2d * 2)) + 0.5

# Combine components
base_field = (
    180 * subtropics
    - 120 * itcz
    + 60 * waves
)

# Time dimension + smooth stochastic variability
noise = np.random.normal(0, 1, (len(times), len(lats), len(lons)))
noise = gaussian_filter(noise, sigma=(0, 7, 8))

data = base_field[None, :, :] + 305 * noise
data = np.clip(data, 0, 300)

# Xarray object
era5_ssr = xr.Dataset(
    {"ssr": (["time", "lat", "lon"], data)},
    coords={"time": times, "lat": lats, "lon": lons},
)["ssr"].mean("time")

# Plot
p2 = contourf_map(
    era5_ssr,
    title="Synthetic SSR – Banded & Wave Structure",
    levels=11,
    palette=mbpal("spring"),
    vmin=-100,
    vmax=300,
    projection=ccrs.Robinson(),
    cbar_title="SSR (W/m²)", width=1300
)

show(p2)
save_plot(p2, "output/map_projections_02")
