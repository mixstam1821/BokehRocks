# # main.py
# https://www.statistics.gr/en/statistics/pop
import numpy as np
import geopandas as gpd
import requests
from bokeh.io import show
from bokeh.layouts import row, column
from bokeh.models import (
    GeoJSONDataSource, HoverTool, ColumnDataSource, Div
)
from bokeh.plotting import figure
from bokeh.palettes import Category20
from bokeh_rocks import save_plot, hovfun
# https://geodata.ucdavis.edu/gadm/gadm4.1/json/
# 🌍 Load Greece GADM Level 2
url = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_GRC_2.json"
gdf = gpd.GeoDataFrame.from_features(requests.get(url).json()["features"])
gdf = gdf[gdf["NAME_2"].notna()]
gdf["region"] = gdf["NAME_2"]

# 🧠 Simulate 40 years of data
years = list(range(1985, 2025))
region_births = {}
region_deaths = {}
for region in gdf["region"]:
    region_births[region] = np.random.poisson(lam=600, size=len(years))
    region_deaths[region] = np.random.poisson(lam=350, size=len(years))
    gdf.loc[gdf["region"] == region, "total_births"] = region_births[region].sum()

# 🔥 CRS
gdf.set_crs(epsg=4326, inplace=True)
gdf = gdf.to_crs(epsg=3857)

# 🎨 Colors
palette = Category20[20]
gdf["color"] = [palette[i % len(palette)] for i in range(len(gdf))]

# 📦 Data sources
geo_source = GeoJSONDataSource(geojson=gdf.to_json())

# 🗺️ Map
p_map = figure(
    title="🗺️ Greece Regions (CartoDB Dark Matter)",
    width=700,
    height=600,
    tools="pan,wheel_zoom,reset,tap",
    x_axis_type="mercator",
    y_axis_type="mercator",
)
p_map.add_tile("CartoDB Dark Matter", retina=True)
p_map.patches("xs", "ys", source=geo_source,
              fill_color="color", line_color="white", line_width=0.5, alpha=0.6)
hover = HoverTool(tooltips=hovfun("""
<b>@region</b><br>
Total Births: @total_births{0,0}
"""), point_policy='follow_mouse')
p_map.add_tools(hover)
p_map.grid.visible = False

# 🚀 Layout
layout = column(
    p_map
)

show(layout)
save_plot(layout, "output/tiles_05")