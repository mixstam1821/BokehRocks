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

# --- Patch centers ---
n_centers = 25
centers_lat = np.random.uniform(-60, 60, n_centers)
centers_lon = np.random.uniform(-180, 180, n_centers)
centers_amp = np.random.uniform(80, 160, n_centers)
centers_scale = np.random.uniform(8, 18, n_centers)

field = np.zeros((len(lats), len(lons)))

for clat, clon, amp, scale in zip(
    centers_lat, centers_lon, centers_amp, centers_scale
):
    dist2 = (lat2d - clat)**2 + ((lon2d - clon) * np.cos(np.deg2rad(clat)))**2
    field += amp * np.exp(-dist2 / (2 * scale**2))

# Normalize + add background
field = field / field.max()
field = 120 + 160 * field

# Time dimension + mild noise
noise = np.random.normal(0, 1, (len(times), len(lats), len(lons)))
noise = gaussian_filter(noise, sigma=(0, 2, 4))

data = field[None, :, :] + 25 * noise
data = np.clip(data, 0, 300)

# Xarray
era5_ssr = xr.Dataset(
    {"ssr": (["time", "lat", "lon"], data)},
    coords={"time": times, "lat": lats, "lon": lons},
)["ssr"].mean("time")

# Plot
p2 = contourf_map(
    era5_ssr,
    title="Synthetic SSR – Patchy Observational Field",
    levels=10,
    palette="Viridis256",
    vmin=0,
    vmax=300,
    projection=ccrs.PlateCarree(),
    cbar_title="SSR (W/m²)",
)

show(p2)
save_plot(p2, "map_projections_04")
