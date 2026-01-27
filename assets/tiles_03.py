from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool,Spacer
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

np.random.seed(42)
n_points = 100
base_lat, base_lon = 40.7128, -74.0060
lat_rand = base_lat + np.random.randn(n_points) * 0.5
lon_rand = base_lon + np.random.randn(n_points) * 0.5
values = np.random.uniform(0, 100, n_points)

x_rand, y_rand = lat_lon_to_mercator(lat_rand, lon_rand)

source_rand = ColumnDataSource(data=dict(
    x=x_rand,
    y=y_rand,
    values=values,
    lat = lat_rand,
    lon = lon_rand
))

from bokeh.transform import linear_cmap
from bokeh.models import ColorBar, LinearColorMapper

mapper = LinearColorMapper(palette="Viridis256", low=0, high=100)

p4 = figure(x_range=(-8300000, -8100000), y_range=(4900000, 5000000),
           x_axis_type="mercator", y_axis_type="mercator", 
           width=700, height=500,
           title="Simulated Sensor Data (New York Area)")
p4.add_tile(xyz.CartoDB.DarkMatter)

scatter = p4.scatter('x', 'y', source=source_rand, size=12, 
          fill_color={'field': 'values', 'transform': mapper},
          fill_alpha=0.8, line_color='white', line_width=1)

color_bar = ColorBar(color_mapper=mapper, width=8, location=(0,0))
p4.add_layout(color_bar, 'right')


p4.grid.grid_line_color = 'grey'
p4.grid.grid_line_alpha = 0.2

p4.add_tools(HoverTool(tooltips=[

    ("lat", "@lat"),
    ("lon", "@lon"),
    ("value", "@values"),
])) 

show(p4)
br.save_plot(p4, "output/tiles_03")