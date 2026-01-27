# main.py
import numpy as np
import geopandas as gpd
import requests
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.palettes import Category20, Turbo256
from bokeh.layouts import column, row
from bokeh_rocks import save_plot, hovfun
# ───────────────────────────────────────────────
# 🌐 Helper: Load GADM GeoJSON for any country
# ───────────────────────────────────────────────
def load_gadm(country_code_or_name="GRC", level=2):
    """
    Load GADM level-2 boundaries for a given country code or name.
    Example: "GRC", "ITA", "ESP", "DEU".
    """
    base = "https://geodata.ucdavis.edu/gadm/gadm4.1/json"
    country_code_or_name = country_code_or_name.upper()
    url = f"{base}/gadm41_{country_code_or_name}_{level}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        gdf = gpd.GeoDataFrame.from_features(response.json()["features"])
        gdf = gdf[gdf[f"NAME_{level}"].notna()]
        gdf["region"] = gdf[f"NAME_{level}"]
        return gdf
    except Exception as e:
        print(f"❌ Could not load {url}")
        raise e



# ───────────────────────────────────────────────
# 🗺️ High-Level Map Function
# ───────────────────────────────────────────────
def plot_country_regions(country_code="GRC", level=2):
    """
    Plot all administrative regions of a given country using GADM JSON.
    """
    # Load data
    gdf = load_gadm(country_code, level)

    # Simulate synthetic data (e.g., population, GDP)
    gdf["value"] = np.random.randint(100, 5000, len(gdf))
    gdf["population"] = np.random.randint(10_000, 2_000_000, len(gdf))

    # Set CRS to Web Mercator
    gdf.set_crs(epsg=4326, inplace=True)
    gdf = gdf.to_crs(epsg=3857)

    # Assign colors
    palette = Turbo256 if len(gdf) > 20 else Category20[len(gdf) if len(gdf) <= 20 else 20]
    gdf["color"] = [palette[i % len(palette)] for i in range(len(gdf))]

    # Build GeoJSON source
    geo_source = GeoJSONDataSource(geojson=gdf.to_json())

    # Create map figure
    p = figure(
        title=f"🗺️ {country_code} — Level-{level} Regions (CartoDB Dark Matter)",
        width=600,
        height=350,
        tools="pan,wheel_zoom,reset,save",
        x_axis_type="mercator",
        y_axis_type="mercator",
    )
    p.add_tile("CartoDB Dark Matter", retina=True)
    p.patches(
        "xs", "ys", source=geo_source,
        fill_color="color", line_color="white",
        line_width=0.4, alpha=0.7
    )

    # Hover tool
    hover = HoverTool(tooltips=hovfun("""
        <b>@region</b><br>
        Synthetic Value: @value{0,0}<br>
        Population: @population{0,0}
    """), point_policy='follow_mouse')
    p.add_tools(hover)
    p.grid.visible = False
    p.title.text_color = "deepskyblue"
    p.title.text_font = "Helvetica"
    p.title.text_font_size = "20pt"

    return p


# ───────────────────────────────────────────────
# 🌍 Multiple Countries Example
# ───────────────────────────────────────────────
countries = ["GRC", "ITA", "ESP", "DEU"]  # Greece, Italy, Spain, Germany

maps = [plot_country_regions(c) for c in countries]

layout = column(row(maps[0], maps[1]), row(maps[2], maps[3]))   
show(layout)
save_plot(layout, "output/tiles_06")