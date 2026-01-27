# main.py
import numpy as np
import json
from bokeh.io import curdoc
from bokeh.models import (
    GeoJSONDataSource, HoverTool,
    ColorBar, LinearColorMapper, BasicTicker, PrintfTickFormatter
)
from bokeh.plotting import figure
from bokeh.sampledata.us_states import data as states
from bokeh.layouts import column
from bokeh.palettes import Viridis256
from bokeh_rocks import save_plot, show
# 🧩 Clean up states
states = {code: state for code, state in states.items() if state["name"] not in ["Hawaii", "Alaska"]}

# 🎲 Random value for each state
for state in states.values():
    state["value"] = np.random.randint(10, 100)

# ✅ GeoJSON with MultiPolygon support + NaN fix
def states_to_geojson(states_dict):
    features = []
    for code, state in states_dict.items():
        coords = []
        current_poly = []
        for lon, lat in zip(state["lons"], state["lats"]):
            if np.isnan(lon) or np.isnan(lat):
                if current_poly:
                    coords.append(current_poly)
                    current_poly = []
            else:
                current_poly.append((lon, lat))
        if current_poly:
            coords.append(current_poly)
        features.append({
            "type": "Feature",
            "id": code,
            "properties": {
                "name": state["name"],
                "value": state["value"]
            },
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [[[pt for pt in poly]] for poly in coords]
            }
        })
    return json.dumps({
        "type": "FeatureCollection",
        "features": features
    })

# 🧠 SVG Generator w/ Y-axis + dark theme
def bar_svg(values, years=None, width=180, height=100):
    if years is None:
        years = [str(2020 + i) for i in range(len(values))]
    max_val = max(values)
    y_ticks = np.linspace(0, max_val, 4).astype(int)
    bar_width = (width - 40) // len(values)  # reserve 40px for y-axis
    svg_bars = ""
    svg_labels = ""
    svg_grid = ""
    svg_y_ticks = ""

    for tick in y_ticks:
        y = height - 20 - int((tick / max_val) * (height - 40))
        svg_grid += f'<line x1="35" y1="{y}" x2="{width}" y2="{y}" stroke="#444" stroke-dasharray="2"/>'
        svg_y_ticks += f'<text x="30" y="{y + 4}" font-size="8" fill="#ccc" text-anchor="end">{tick}</text>'

    for i, (val, label) in enumerate(zip(values, years)):
        bar_height = int((val / max_val) * (height - 40))
        x = 40 + i * bar_width
        y = height - 20 - bar_height
        svg_bars += f'<rect x="{x}" y="{y}" width="{bar_width - 4}" height="{bar_height}" fill="#00bfff" />'
        svg_labels += f'<text x="{x + bar_width//2}" y="{height - 5}" font-size="8" fill="#ccc" text-anchor="middle">{label}</text>'

    return f"""
    <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
        <rect width="{width}" height="{height}" fill="black" />
        {svg_grid}
        {svg_y_ticks}
        {svg_bars}
        {svg_labels}
    </svg>
    """.replace('\n', '')

# 🔄 Embed SVGs into GeoJSON
geojson_obj = json.loads(states_to_geojson(states))
for feature in geojson_obj["features"]:
    values = np.random.randint(10, 100, size=5)
    years = [str(y) for y in range(2019, 2024)]
    svg = bar_svg(values, years)
    feature["properties"]["bar_svg"] = svg

# 📡 Data source
geo_source = GeoJSONDataSource(geojson=json.dumps(geojson_obj))

# 🎨 Color mapping
color_mapper = LinearColorMapper(palette=Viridis256, low=10, high=100)

# 🗺️ Choropleth map figure
p = figure(
    title="US Choropleth Map with Dark-Themed Bar Chart Tooltips",
    toolbar_location="left",
    x_axis_location=None,
    y_axis_location=None,
    width=1000,
    height=600
)
p.grid.grid_line_color = None

# 🧱 Draw states
p.patches("xs", "ys", source=geo_source,
          fill_color={'field': 'value', 'transform': color_mapper},
          line_color="white", line_width=1)

# 🧠 Tooltip with dark SVG
hover = HoverTool(
    tooltips="""
    <div>
        <div><strong>@name</strong></div>
        <div>@bar_svg{safe}</div>
    </div>
    """
)
p.add_tools(hover)

# 🎨 Add color bar (legend)
color_bar = ColorBar(color_mapper=color_mapper, 
                     ticker=BasicTicker(desired_num_ticks=10),
                     formatter=PrintfTickFormatter(format="%d"),
                     label_standoff=12,
                     border_line_color=None,
                     location=(0, 0))
p.add_layout(color_bar, 'right')


show(p)
save_plot(p, 'output/custom_plots_14')