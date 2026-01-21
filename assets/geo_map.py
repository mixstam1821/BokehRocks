import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256
from bokeh.io import export_png

source = ColumnDataSource(dict(
    x=np.random.randint(0, 10, 50),
    y=np.random.randint(0, 10, 50),
    v=np.random.rand(50)
))

hover_cb = CustomJS(code="""
console.log("Hovered tile:", cb_data.index['1d'].indices);
""")

p = figure(title="Tile Plot", tools="pan,wheel_zoom,reset")
tiles = p.rect(
    "x", "y", 0.9, 0.9,
    source=source,
    fill_color=linear_cmap("v", Viridis256, 0, 1),
    line_color="white"
)

p.add_tools(HoverTool(
    tooltips=[("x", "@x"), ("y", "@y"), ("value", "@v{0.00}")],
    callback=hover_cb,
    renderers=[tiles]
))

output_file("tile_plot.html")
save(p)
export_png(p, filename="tile_plot.png")

