from bokeh.plotting import figure, show
from bokeh.models import InlineStyleSheet, ColumnDataSource, HoverTool
from bokeh.layouts import column, row
import numpy as np
from bokeh_rocks import save_plot


x = np.linspace(0, 12, 100)
revenue = np.sin(x * 0.8) * 3 + 5
cost = np.cos(x * 0.6) * 2 + 4
profit = revenue - cost

p4 = figure(
    width=800,
    height=500,
    title="💰 Revenue vs Cost Analysis",
    x_axis_label="Quarter",
    y_axis_label="Amount ($M)"
)

# Create masks for profit (green) and loss (red) regions
profit_mask = profit >= 0
loss_mask = profit < 0

# Profit areas (green) - where revenue > cost
for i in range(len(x) - 1):
    if profit[i] >= 0 and profit[i + 1] >= 0:
        p4.varea(
            x=[x[i], x[i + 1]],
            y1=[cost[i], cost[i + 1]],
            y2=[revenue[i], revenue[i + 1]],
            fill_color='#00b894',
            fill_alpha=0.3
        )

# Loss areas (red) - where cost > revenue
for i in range(len(x) - 1):
    if profit[i] < 0 and profit[i + 1] < 0:
        p4.varea(
            x=[x[i], x[i + 1]],
            y1=[revenue[i], revenue[i + 1]],
            y2=[cost[i], cost[i + 1]],
            fill_color='#d63031',
            fill_alpha=0.3
        )

# Lines
p4.line(x, revenue, line_color='#00b894', line_width=3, legend_label='Revenue')
p4.line(x, cost, line_color='#d63031', line_width=3, legend_label='Cost')

p4.legend.location = "top_left"
p4.background_fill_color = None
p4.border_fill_color = "#ffffff"
p4.grid.grid_line_alpha = 0.2

css4 = InlineStyleSheet(css="""
:host {
    background: linear-gradient(to bottom, #f8f9fa 0%, #e9ecef 100%);
}
""")

show(column(p4, stylesheets=[css4]))
save_plot(p4, "output/area_03")

