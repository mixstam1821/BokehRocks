from bokeh.plotting import figure, show
from bokeh.models import InlineStyleSheet, ColumnDataSource, HoverTool
from bokeh.layouts import column, row
import numpy as np
from bokeh_rocks import save_plot


x = np.linspace(0, 24, 200)
temperature = 20 + np.sin(x * 0.5) * 5 + np.random.normal(0, 0.5, len(x))

danger_threshold = 24
warning_threshold = 22
safe_threshold = 18

p5 = figure(
    width=900,
    height=500,
    title="🌡️ 24-Hour Temperature Monitoring",
    x_axis_label="Time (hours)",
    y_axis_label="Temperature (°C)"
)

# Danger zone (red) - above danger threshold
p5.varea(
    x=x,
    y1=danger_threshold,
    y2=30,
    fill_color='#ff4757',
    fill_alpha=0.2,
    legend_label='Danger Zone'
)

# Warning zone (yellow) - between warning and danger
p5.varea(
    x=x,
    y1=warning_threshold,
    y2=danger_threshold,
    fill_color='#ffa502',
    fill_alpha=0.2,
    legend_label='Warning Zone'
)

# Safe zone (green) - between safe and warning
p5.varea(
    x=x,
    y1=safe_threshold,
    y2=warning_threshold,
    fill_color='#26de81',
    fill_alpha=0.2,
    legend_label='Safe Zone'
)

# Cold zone (blue) - below safe threshold
p5.varea(
    x=x,
    y1=10,
    y2=safe_threshold,
    fill_color='#45aaf2',
    fill_alpha=0.2,
    legend_label='Cold Zone'
)

# Temperature line
p5.line(x, temperature, line_color='#2d3436', line_width=3, legend_label='Temperature')

# Threshold lines
p5.line(x, [danger_threshold] * len(x), line_color='#ff4757', line_width=2, line_dash='dashed', alpha=0.7)
p5.line(x, [warning_threshold] * len(x), line_color='#ffa502', line_width=2, line_dash='dashed', alpha=0.7)
p5.line(x, [safe_threshold] * len(x), line_color='#45aaf2', line_width=2, line_dash='dashed', alpha=0.7)

p5.legend.location = "top_right"
p5.legend.click_policy = "hide"
p5.background_fill_color = None
p5.border_fill_color = "#f8f9fa"
p5.grid.grid_line_alpha = 0.3

css5 = InlineStyleSheet(css="""
:host {
    background: linear-gradient(to bottom, #ffffff 0%, #dfe6e9 100%);
}
""")

show(column(p5, stylesheets=[css5]))
save_plot(p5, "output/area_04")