import xarray as xr
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter
from bokeh_rocks import contourf_map, ccrs, show, save_plot, mbpal

terrain = mbpal("terrain")
# Coordinates
lats = np.linspace(-90, 90, 181)
lons = np.linspace(-180, 180, 360)
times = pd.date_range("2000-01-01", periods=12, freq="MS")

# Base smooth random field (no explicit lat function)
base = np.random.normal(0, 1, (len(times), len(lats), len(lons)))

# Strong spatial smoothing → large coherent structures
base = gaussian_filter(base, sigma=(0, 6, 12))

# Gentle latitude damping (not a cosine, just decay)
lat_damp = 1 - 0.6 * (np.abs(lats) / 90)
lat_damp = np.clip(lat_damp, 0.4, 1.0)

data = 180 + 80 * base * lat_damp[None, :, None]

# Physical bounds
data = np.clip(data, 0, 300)

# Xarray
era5_ssr = xr.Dataset(
    {"ssr": (["time", "lat", "lon"], data)},
    coords={"time": times, "lat": lats, "lon": lons},
)["ssr"].mean("time")

# Plot
p2 = contourf_map(
    era5_ssr,
    title="Synthetic SSR – Smooth Geophysical Field",
    levels=10,
    palette=terrain,
    vmin=178,
    vmax=183,
    projection=ccrs.Mollweide(),
    cbar_title="SSR (W/m²)",
)

show(p2)
save_plot(p2, "output/map_projections_03")
