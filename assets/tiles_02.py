from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, Spacer
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

us_cities = {
    'name': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'lat': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 39.9526, 29.4241, 32.7157, 32.7767, 37.3382],
    'lon': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -75.1652, -98.4936, -117.1611, -96.7970, -121.8863],
    'category': ['East', 'West', 'Midwest', 'South', 'West', 'East', 'South', 'West', 'South', 'West']
}

x_us, y_us = lat_lon_to_mercator(np.array(us_cities['lat']), np.array(us_cities['lon']))

# Create separate sources for each category
colors = {'East': 'green', 'West': 'orange', 'Midwest': 'purple', 'South': 'red'}

p3 = figure(x_range=(-13500000, -12500000), y_range=(3500000, 5500000),
           x_axis_type="mercator", y_axis_type="mercator", 
           width=700, height=500, toolbar_location='below',
           title="Major US Cities by Region")
p3.add_tile(xyz.Esri.WorldImagery)

for category, color in colors.items():
    indices = [i for i, c in enumerate(us_cities['category']) if c == category]
    x_cat = x_us[indices]
    y_cat = y_us[indices]
    names_cat = [us_cities['name'][i] for i in indices]
    lat_cat = [us_cities['lat'][i] for i in indices]
    lon_cat = [us_cities['lon'][i] for i in indices]
    category_cat = [us_cities['category'][i] for i in indices]

    source_cat = ColumnDataSource(data=dict(x=x_cat, y=y_cat, name=names_cat, lat=lat_cat, lon=lon_cat, category=category_cat))
    p3.scatter('x', 'y', source=source_cat, size=20, 
              fill_color=color, fill_alpha=0.8, line_color='white', line_width=2,
              legend_label=category)

p3.legend.location = "top_right"
p3.legend.click_policy = "hide"

# THIS IS HOW YOU ENLARGE THE LEGEND LABELS!
p3.legend.label_text_font_size = "16pt"  # Change this to whatever size you want
p3.legend.glyph_width = 50               # Optional: make the legend symbols bigger
p3.legend.glyph_height = 50              # Optional: make the legend symbols taller
p3.legend.spacing = 1                   # Optional: add more space between items
# p3.legend.padding = 10                   # Optional: add padding around the legend

p3.grid.grid_line_color = 'grey'
p3.grid.grid_line_alpha = 0.5

p3.add_layout(p3.legend[0], "right")
p3.add_layout(Spacer(width=5), "right")

p3.add_tools(HoverTool(tooltips=[
    ("name", "@name"),
    ("category", "@category"),
    ("lat", "@lat"),
    ("lon", "@lon")
])) 

show(p3)
br.save_plot(p3, "output/tiles_02")