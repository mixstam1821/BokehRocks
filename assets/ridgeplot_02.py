from bokeh_rocks import save_plot
import numpy as np
from scipy.stats import gaussian_kde
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()  # Remove if running as script

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Use your favorite 12 colors
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
    "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
    "#bcbd22", "#17becf", "#aec7e8", "#ffbb78"
]

p = figure(
    width=800,
    height=600,
    y_range=months[::-1],
    x_axis_label="Temperature (°C)",
    toolbar_location=None,
    outline_line_color=None
)

for i, month in enumerate(months):
    # Simulate data for each month
    mean = 5 + 10 * np.sin((i / 12) * 2 * np.pi) + 10
    temps = np.random.normal(mean, 3, 200)
    # KDE for smooth curve
    kde = gaussian_kde(temps)
    x = np.linspace(temps.min()-4, temps.max()+4, 300)
    y = kde(x)
    # Offset
    y_offset = i * 1.0
    y_scaled = y / y.max() * 0.7
    p.patch(x, y_offset + y_scaled, color=colors[i], alpha=0.5, line_color="black", line_width=1.5)

# Style
p.yaxis.axis_label = "Month"
p.yaxis.major_label_text_font_size = "12pt"
p.xgrid.visible = False
p.ygrid.visible = False
p.background_fill_color = "#fafafa"
p.legend.visible = False
p.title.text = "Monthly Temperature Distribution Joyplot"
p.title.text_font_size = "18pt"
p.xaxis.axis_label_text_font_style = "bold"
p.yaxis.axis_label_text_font_style = "bold"
p.outline_line_alpha = 0

show(p)
save_plot(p, "output/ridgeplot_02")