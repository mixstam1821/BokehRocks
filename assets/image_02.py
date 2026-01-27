import numpy as np
import xarray as xr
import pandas as pd
from bokeh_rocks import fworld_heatmap, save_plot
from bokeh.io import show
def create_temperature_dataset(start_date='2020-01-01', periods=365, 
                                lat_range=(-90, 90), lon_range=(-180, 180),
                                lat_points=50, lon_points=50):

    # Create coordinates
    time = pd.date_range(start_date, periods=periods, freq='D')
    lat = np.linspace(lat_range[0], lat_range[1], lat_points)
    lon = np.linspace(lon_range[0], lon_range[1], lon_points)
    
    # Create meshgrid for spatial patterns
    LON, LAT = np.meshgrid(lon, lat)
    
    # Initialize temperature array
    temp = np.zeros((periods, lat_points, lon_points))
    
    for t in range(periods):
        # Base temperature: latitude gradient (warmer at equator)
        base_temp = 30 - 0.8 * np.abs(LAT)
        
        # Seasonal variation (annual cycle)
        day_of_year = time[t].dayofyear
        seasonal = 10 * np.cos(2 * np.pi * (day_of_year - 172) / 365)
        
        # Hemisphere differences (seasons opposite in N/S)
        seasonal_pattern = np.where(LAT > 0, seasonal, -seasonal)
        
        # Add spatial variability (land/ocean-like patterns)
        spatial_var = 5 * np.sin(LON * np.pi / 60) * np.cos(LAT * np.pi / 45)
        
        # Random weather noise
        noise = np.random.normal(0, 2, (lat_points, lon_points))
        
        # Combine all components
        temp[t] = base_temp + seasonal_pattern + spatial_var + noise
    
    # Create xarray Dataset
    ds = xr.Dataset(
        {
            'temperature': (['time', 'lat', 'lon'], temp, {
                'units': 'degrees Celsius',
                'long_name': 'Air Temperature at 2m',
                'standard_name': 'air_temperature'
            })
        },
        coords={
            'time': time,
            'lat': ('lat', lat, {'units': 'degrees_north', 'long_name': 'Latitude'}),
            'lon': ('lon', lon, {'units': 'degrees_east', 'long_name': 'Longitude'})
        },
        attrs={
            'title': 'Synthetic Temperature Dataset',
            'source': 'Synthetic data for demonstration',
            'creation_date': pd.Timestamp.now().isoformat()
        }
    )
    
    return ds


plot= fworld_heatmap(create_temperature_dataset().temperature.mean('time'), title="🌎 Synthetic Global Temperature (°C)", height=700, width = 1300)
show(plot)
save_plot(plot, "output/image_02")

