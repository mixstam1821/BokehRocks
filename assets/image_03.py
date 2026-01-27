import numpy as np
import xarray as xr
import pandas as pd
from bokeh_rocks import fworld_heatmap, save_plot, mbpal
from bokeh.io import show
def create_ssr_dataset(start_date='2020-01-01', periods=365,
                       lat_range=(-90, 90), lon_range=(-180, 180),
                       lat_points=90, lon_points=90):
    """
    Create synthetic Surface Solar Radiation (SSR) dataset.
    
    Parameters:
    -----------
    start_date : str
        Start date for time series
    periods : int
        Number of time steps (days)
    lat_range, lon_range : tuple
        (min, max) for latitude and longitude
    lat_points, lon_points : int
        Number of grid points
        
    Returns:
    --------
    xarray.Dataset with SSR data
    """
    
    # Create coordinates
    time = pd.date_range(start_date, periods=periods, freq='D')
    lat = np.linspace(lat_range[0], lat_range[1], lat_points)
    lon = np.linspace(lon_range[0], lon_range[1], lon_points)
    
    # Create meshgrid
    LON, LAT = np.meshgrid(lon, lat)
    
    # Initialize SSR array
    ssr = np.zeros((periods, lat_points, lon_points))
    
    for t in range(periods):
        # Day of year for seasonal calculation
        day_of_year = time[t].dayofyear
        
        # Solar declination angle (simplified)
        declination = 23.45 * np.sin(2 * np.pi * (day_of_year - 81) / 365)
        
        # Solar elevation factor (latitude and season dependent)
        solar_factor = np.cos(np.radians(LAT - declination))
        solar_factor = np.maximum(solar_factor, 0)  # No negative radiation
        
        # Base SSR (W/m²)
        base_ssr = 300 * solar_factor
        
        # Cloud cover effect (random spatial patterns)
        cloud_reduction = np.random.uniform(0.7, 1.0, (lat_points, lon_points))
        
        # Spatial patterns (desert regions have less clouds)
        desert_boost = 1 + 0.2 * np.exp(-((LAT - 25)**2 / 400))
        
        # Add daily variation noise
        noise = np.random.normal(1.0, 0.1, (lat_points, lon_points))
        
        # Combine all components
        ssr[t] = base_ssr * cloud_reduction * desert_boost * noise
        ssr[t] = np.maximum(ssr[t], 0)  # Ensure non-negative
    
    # Create xarray Dataset
    ds = xr.Dataset(
        {
            'ssr': (['time', 'lat', 'lon'], ssr, {
                'units': 'W m-2',
                'long_name': 'Surface Solar Radiation',
                'standard_name': 'surface_downwelling_shortwave_flux'
            })
        },
        coords={
            'time': time,
            'lat': ('lat', lat, {'units': 'degrees_north', 'long_name': 'Latitude'}),
            'lon': ('lon', lon, {'units': 'degrees_east', 'long_name': 'Longitude'})
        },
        attrs={
            'title': 'Synthetic Surface Solar Radiation Dataset',
            'source': 'Synthetic data for demonstration',
            'creation_date': pd.Timestamp.now().isoformat()
        }
    )
    
    return ds

COOL = mbpal("cool")
plot= fworld_heatmap(create_ssr_dataset().ssr.mean('time'), palette=COOL, title="🌎 Synthetic Global SSR")
show(plot)
save_plot(plot, "output/image_03")
