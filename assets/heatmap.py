import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, LinearColorMapper
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256
from bokeh.io import export_png

x = np.arange(10)
y = np.arange(10)
xx, yy = np.meshgrid(x, y)

source = ColumnDataSource(dict(
    x=xx.flatten(),
    y=yy.flatten(),
    v=np.random.rand(100)
))

hover_cb = CustomJS(code="""
console.log("Hovered cell:", cb_data.index['1d'].indices);
""")

mapper = LinearColorMapper(palette=Viridis256, low=0, high=1)

p = figure(
    title="Heatmap",
    x_range=(-0.5, 9.5),
    y_range=(-0.5, 9.5),
    tools="pan,wheel_zoom,reset"
)

rects = p.rect(
    "x", "y", 1, 1,
    source=source,
    fill_color=linear_cmap("v", Viridis256, 0, 1),
    line_color=None
)

p.add_tools(HoverTool(
    tooltips=[("x", "@x"), ("y", "@y"), ("value", "@v{0.000}")],
    callback=hover_cb,
    renderers=[rects]
))

output_file("heatmap.html")
save(p)
export_png(p, filename="heatmap.png")

