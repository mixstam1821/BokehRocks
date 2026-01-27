from bokeh.plotting import figure, show
from bokeh.models import InlineStyleSheet, ColumnDataSource, HoverTool
from bokeh.layouts import column, row
import numpy as np
from bokeh_rocks import save_plot

x = np.linspace(0, 10, 80)
y_mean = np.sin(x) * 2 + 5
y_upper = y_mean + np.random.uniform(0.5, 1.5, len(x))
y_lower = y_mean - np.random.uniform(0.5, 1.5, len(x))

p2 = figure(
    width=800,
    height=500,
    title="🔬 Experimental Data with 95% Confidence Interval",
    x_axis_label="Sample Number",
    y_axis_label="Measurement Value"
)

# Confidence band
p2.varea(
    x=x,
    y1=y_lower,
    y2=y_upper,
    fill_color='#a29bfe',
    fill_alpha=0.3,
    legend_label='95% CI'
)

# Mean line
p2.line(x, y_mean, line_color='#6c5ce7', line_width=3, legend_label='Mean')

# Data points
p2.circle(x[::5], y_mean[::5], size=8, color='#6c5ce7', alpha=0.6)

p2.legend.location = "top_right"
p2.background_fill_color = None
p2.border_fill_color = "#2d3436"
p2.title.text_color = "white"
p2.xaxis.major_label_text_color = "white"
p2.yaxis.major_label_text_color = "white"
p2.xaxis.axis_line_color = "white"
p2.yaxis.axis_line_color = "white"
p2.grid.grid_line_color = "#636e72"
p2.grid.grid_line_alpha = 0.3

css2 = InlineStyleSheet(css="""
:host {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
""")

show(column(p2, stylesheets=[css2]))
save_plot(p2, "output/area_02")
