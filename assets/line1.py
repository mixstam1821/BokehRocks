import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.io import export_png

x = np.arange(20)
y = np.cumsum(np.random.randn(20))

source = ColumnDataSource(dict(x=x, y=y))

hover_cb = CustomJS(code="""
console.log("Hovered point:", cb_data.index['1d'].indices);
""")

p = figure(title="Line Chart", tools="pan,wheel_zoom,reset")
line = p.line("x", "y", source=source, line_width=2)
pts = p.circle("x", "y", size=8, source=source)

p.add_tools(HoverTool(
    tooltips=[("x", "@x"), ("y", "@y{0.00}")],
    callback=hover_cb,
    renderers=[pts]
))

output_file("line_chart.html")
save(p)
export_png(p, filename="line_chart.png")

