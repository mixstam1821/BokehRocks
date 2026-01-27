from bokeh_rocks import *
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np
from bokeh.models import CustomJSHover,ColumnDataSource

# Generate random data
np.random.seed(42)  # For reproducibility
x = np.random.rand(500) * 100  # X-coordinates
y = np.random.rand(500) * 100  # Y-coordinates
colors = np.random.choice(['#0096FF','#FF3131','#FFAC1C','#0FFF50','#ea51ea','#1F51FF'], size=500)

source = ColumnDataSource(data=dict(x=x, y=y, colors=colors, hidden=np.ones(len(x))*np.min(y)))
# Create a scatter plot
p = figure(title="Scatter Plot with 500 Points", 
           x_axis_label="X-axis", y_axis_label="Y-axis", 
           width=800, height=800, tools = 'pan, wheel_zoom',**jk9)

sc = p.scatter('x', 'y', source=source, size=12, fill_color='colors', alpha=0.7, hover_line_color = 'colors',hover_line_width = 17,legend_label='scatter')


tltl = """<i>x:</i> <b>@x</b> <br> <i>y:</i> <b>@y</b>"""
p.add_tools(HoverTool(tooltips=hovfun(tltl), formatters={"@hidden": cusj()},mode="mouse",renderers = [sc]))
apply_theme(p,'dark')
show(p)
save_plot(p, 'output/scatter_01')