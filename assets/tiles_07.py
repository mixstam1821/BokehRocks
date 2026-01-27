# main.py
import numpy as np
import geopandas as gpd
import requests
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.palettes import Turbo256, Category20
from bokeh.layouts import column
from bokeh_rocks import save_plot, hovfun

# ───────────────────────────────────────────────
# 🌐 Load all countries (GADM Level 0)
# ───────────────────────────────────────────────
def load_world():
    """
    Load all world countries from GADM (Level 0 = national boundaries).
    """
    url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    print("🌍 Loading GADM Level 0 world boundaries...")
    response = requests.get(url)
    response.raise_for_status()
    gdf = gpd.GeoDataFrame.from_features(response.json()["features"])
    # gdf = gdf[gdf["Feature"].notna()]
    # gdf["properties"] = gdf["name"]
    return gdf



# ───────────────────────────────────────────────
# 🗺️ Build the Global Map
# ───────────────────────────────────────────────
def plot_world_map():
    # Load data
    gdf = load_world()

    # 🔢 Simulate synthetic data (e.g., population, GDP, CO₂)
    gdf["population"] = np.random.randint(1_000_000, 200_000_000, len(gdf))
    gdf["gdp"] = np.random.randint(5_000, 100_000, len(gdf))
    gdf["index"] = np.random.uniform(0, 1, len(gdf))

    # Set CRS
    gdf.set_crs(epsg=4326, inplace=True)
    gdf = gdf.to_crs(epsg=3857)

    # 🎨 Color palette
    palette = Turbo256 if len(gdf) > 20 else Category20[len(gdf)]
    gdf["color"] = [palette[i % len(palette)] for i in range(len(gdf))]

    # GeoJSON data source
    geo_source = GeoJSONDataSource(geojson=gdf.to_json())

    # 🗺️ Create figure
    p = figure(
        title="🌍 World Countries (GADM Level 0)",
        width=1000, height=600,
        tools="pan,wheel_zoom,reset,save",
        x_axis_type="mercator", y_axis_type="mercator",
        x_range=(-10_000_000, 10_000_000),
        y_range=(-18_000_000, 18_000_000),
    )
    p.add_tile("CartoDB Dark Matter", retina=True)

    # 🖌️ Draw country polygons
    p.patches(
        "xs", "ys", source=geo_source,
        fill_color="color",
        line_color="white",
        line_width=0.3,
        alpha=0.7
    )

    # 🪶 Hover Tool
    hover = HoverTool(tooltips=hovfun("""
        <b>@name</b><br>
        Population: @population{0,0}<br>
        GDP (USD): @gdp{0,0}<br>
        Index: @index{0.00}
    """), point_policy='follow_mouse')
    p.add_tools(hover)

    # ✨ Styling
    p.grid.visible = False
    p.title.text_color = "deepskyblue"
    p.title.text_font = "Helvetica"
    p.title.text_font_size = "22pt"

    return p


# ───────────────────────────────────────────────
# 🚀 Run
# ───────────────────────────────────────────────
p_world = plot_world_map()
show(column(p_world))
save_plot(p_world, "output/tiles_07")