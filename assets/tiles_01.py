from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import column, row
import xyzservices.providers as xyz
import numpy as np
import bokeh_rocks as br
# Helper function to convert lat/lon to Web Mercator
def lat_lon_to_mercator(lat, lon):
    """Convert latitude/longitude to Web Mercator coordinates"""
    r_major = 6378137.000
    x = r_major * np.radians(lon)
    scale = x / lon
    y = 180.0 / np.pi * np.log(np.tan(np.pi / 4.0 + lat * (np.pi / 180.0) / 2.0)) * scale
    return x, y

# ============================================
# Example 1: Major World Cities
# ============================================
cities = {
    'name': ['New York', 'London', 'Tokyo', 'Sydney', 'São Paulo', 'Mumbai', 'Cairo', 'Paris', 'Beijing', 'Los Angeles'],
    'lat': [40.7128, 51.5074, 35.6762, -33.8688, -23.5505, 19.0760, 30.0444, 48.8566, 39.9042, 34.0522],
    'lon': [-74.0060, -0.1278, 139.6503, 151.2093, -46.6333, 72.8777, 31.2357, 2.3522, 116.4074, -118.2437],
    'population': [8.3, 9.0, 13.9, 5.3, 12.3, 20.4, 9.5, 2.2, 21.5, 4.0]
}

# Convert to mercator
x_cities, y_cities = lat_lon_to_mercator(np.array(cities['lat']), np.array(cities['lon']))

source_cities = ColumnDataSource(data=dict(
    x=x_cities,
    y=y_cities,
    name=cities['name'],
    population=cities['population'],
    lat = cities['lat'],
    lon = cities['lon']
))

p1 = figure(x_range=(-15000000, 15000000), y_range=(-8000000, 10000000),
           x_axis_type="mercator", y_axis_type="mercator",
           width=700, height=500,
           title="Major World Cities by Population")
p1.add_tile(xyz.OpenStreetMap.Mapnik)

p1.scatter('x', 'y', source=source_cities, size='population', 
          fill_color='red', fill_alpha=0.6, line_color='darkred', line_width=2)

p1.add_tools(HoverTool(tooltips=[
    ("City", "@name"),
    ("Population", "@population"),
    ("lat", "@lat"),
    ("lon", "@lon")
])) 
show(p1)
br.save_plot(p1, "output/tiles_01")