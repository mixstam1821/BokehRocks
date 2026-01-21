import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.io import export_png

source = ColumnDataSource(dict(
    x=np.random.rand(100),
    y=np.random.rand(100),
    size=np.random.randint(6, 14, 100)
))

hover_cb = CustomJS(code="""
console.log("Hovered scatter:", cb_data.index['1d'].indices);
""")

p = figure(title="Scatter Plot", tools="pan,wheel_zoom,reset")
glyph = p.circle("x", "y", size="size", alpha=0.6, source=source)

p.add_tools(HoverTool(
    tooltips=[("x", "@x{0.000}"), ("y", "@y{0.000}")],
    callback=hover_cb,
    renderers=[glyph]
))

output_file("scatter_plot.html")
save(p)
export_png(p, filename="scatter_plot.png")

