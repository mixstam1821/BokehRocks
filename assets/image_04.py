import numpy as np
import xarray as xr
import pandas as pd
from bokeh_rocks import fworld_heatmap, save_plot, mbpal
from bokeh.io import show
def create_rain_dataset(start_date='2020-01-01', periods=365,
                        lat_range=(-90, 90), lon_range=(-180, 180),
                        lat_points=90, lon_points=90):

    
    # Create coordinates
    time = pd.date_range(start_date, periods=periods, freq='D')
    lat = np.linspace(lat_range[0], lat_range[1], lat_points)
    lon = np.linspace(lon_range[0], lon_range[1], lon_points)
    
    # Create meshgrid
    LON, LAT = np.meshgrid(lon, lat)
    
    # Initialize precipitation array
    precip = np.zeros((periods, lat_points, lon_points))
    
    for t in range(periods):
        # Day of year for seasonal patterns
        day_of_year = time[t].dayofyear
        
        # Tropical rain belt (ITCZ) - follows the sun
        itcz_position = 10 * np.sin(2 * np.pi * (day_of_year - 81) / 365)
        tropical_rain = 15 * np.exp(-((LAT - itcz_position)**2 / 100))
        
        # Mid-latitude storm tracks
        midlat_rain_north = 8 * np.exp(-((LAT - 45)**2 / 150))
        midlat_rain_south = 8 * np.exp(-((LAT + 45)**2 / 150))
        midlat_rain = midlat_rain_north + midlat_rain_south
        
        # Monsoon-like patterns (seasonal, location-specific)
        monsoon_season = 0.5 * (1 + np.cos(2 * np.pi * (day_of_year - 172) / 365))
        monsoon = 10 * monsoon_season * np.exp(-((LAT - 20)**2 / 200)) * \
                  np.maximum(0, np.sin(LON * np.pi / 180))
        
        # Desert regions (low precipitation)
        desert_factor = 1 - 0.7 * np.exp(-((LAT - 25)**2 / 300))
        
        # Base precipitation pattern
        base_precip = (tropical_rain + midlat_rain + monsoon) * desert_factor
        
        # Random precipitation events (30% chance of rain)
        rain_events = np.random.random((lat_points, lon_points)) < 0.3
        
        # Rain intensity (gamma distribution for realistic variability)
        rain_intensity = np.random.gamma(2, 2, (lat_points, lon_points))
        
        # Combine: base pattern + random events
        precip[t] = base_precip * rain_events * rain_intensity
        precip[t] = np.maximum(precip[t], 0)  # Ensure non-negative
    
    # Create xarray Dataset
    ds = xr.Dataset(
        {
            'precipitation': (['time', 'lat', 'lon'], precip, {
                'units': 'mm day-1',
                'long_name': 'Daily Precipitation',
                'standard_name': 'precipitation_amount'
            })
        },
        coords={
            'time': time,
            'lat': ('lat', lat, {'units': 'degrees_north', 'long_name': 'Latitude'}),
            'lon': ('lon', lon, {'units': 'degrees_east', 'long_name': 'Longitude'})
        },
        attrs={
            'title': 'Synthetic Precipitation Dataset',
            'source': 'Synthetic data for demonstration',
            'creation_date': pd.Timestamp.now().isoformat()
        }
    )
    
    return ds

Greys = mbpal("Greys")
plot= fworld_heatmap(create_rain_dataset().precipitation.mean('time'), palette=Greys,coast_color="red", title="🌎 Synthetic Global SSR")
show(plot)
save_plot(plot, "output/image_04")
