from butils import *

import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource, HoverTool, Legend, LegendItem

# output_notebook()

# Generate sample data
np.random.seed(42)
months = np.tile(np.arange(1, 13), 500)
temperature = np.random.normal(loc=20, scale=5, size=6000)
temperature2 = np.random.normal(loc=20, scale=5, size=6000)

data = pd.DataFrame({'Month': months, 'Temperature': temperature, 'Temperature2': temperature2})

# Define colors for months
colors = ["red", "blue", "green", "orange", "purple", "pink", "lime", "cyan", "magenta", "yellow", "brown", "gray"]
month_colors = {month: color for month, color in zip(range(1, 13), colors)}

# Add a column to the dataframe with the color for each month
data['Color'] = data['Month'].map(month_colors)
data['hidden'] = np.ones(len(data)) * np.min(data['Temperature'])

# Create figure
p = figure(title="Temperature Scatter Plot by Month", x_axis_label="Temperature", y_axis_label="Temperature2", width=1300, height=800,**jk9)

# Store scatter renderers and legend items
scatter_renderers = []
# Plot each month separately
for month in data['Month'].unique():
    month_data = data[data['Month'] == month]
    source = ColumnDataSource(month_data)
    sc = p.scatter('Temperature', 'Temperature2', source=source, color=month_colors[month], size=5, alpha=0.7,legend_label=f"Month {month}")
    scatter_renderers.append(sc)

# Tooltip content
tltl = """<i>Temperature:</i> <b>@Temperature</b> <br> <i>Temperature2:</i> <b>@Temperature2</b><br> <i>Month:</i> <b>@Month</b>"""
p.add_tools(HoverTool(tooltips=hovfun(tltl), formatters={"@hidden": cusj()},mode="mouse",renderers = scatter_renderers))
add_extras(p,cross=0);

show(p)
save_plot(p, 'scatter_03')