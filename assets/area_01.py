from bokeh.plotting import figure, show
from bokeh.models import InlineStyleSheet, ColumnDataSource, HoverTool
from bokeh.layouts import column, row
import numpy as np
from bokeh_rocks import save_plot

print("Example 1: Stacked Area Chart")

x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 2
y2 = y1 + np.cos(x * 1.5) + 1
y3 = y2 + np.sin(x * 2) * 0.5 + 0.8

p1 = figure(
    width=800,
    height=500,
    title="📊 Stacked Revenue Streams Over Time",
    x_axis_label="Time (months)",
    y_axis_label="Revenue ($M)"
)

# Bottom layer (Product A)
p1.varea(
    x=x,
    y1=0,
    y2=y1,
    fill_color='#ff6b6b',
    fill_alpha=0.7,
    legend_label='Product A'
)

# Middle layer (Product B)
p1.varea(
    x=x,
    y1=y1,
    y2=y2,
    fill_color='#4ecdc4',
    fill_alpha=0.7,
    legend_label='Product B'
)

# Top layer (Product C)
p1.varea(
    x=x,
    y1=y2,
    y2=y3,
    fill_color='#ffe66d',
    fill_alpha=0.7,
    legend_label='Product C'
)

# Add boundary lines for clarity
p1.line(x, y1, line_color='#d63031', line_width=2, alpha=0.8)
p1.line(x, y2, line_color='#00b894', line_width=2, alpha=0.8)
p1.line(x, y3, line_color='#fdcb6e', line_width=2, alpha=0.8)

p1.legend.location = "top_left"
p1.legend.click_policy = "hide"
p1.background_fill_color = None
p1.border_fill_color = "#f8f9fa"

css1 = InlineStyleSheet(css="""
:host {
    background: linear-gradient(to bottom, #ffffff 0%, #f1f3f5 100%);
}
""")

show(column(p1, stylesheets=[css1]))
save_plot(p1, "output/area_01")