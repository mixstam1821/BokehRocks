from butils import *

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import numpy as np
from bokeh.models import CustomJSHover
from scipy import stats
# Generate random data
np.random.seed(42)  # For reproducibility
x = np.random.rand(500) * 100  # X-coordinates
y = np.random.rand(500) * 100  # Y-coordinates
colors = np.random.choice(['#0096FF','#FF3131','#FFAC1C','#0FFF50','#ea51ea','#1F51FF'], size=500)

slope,intercept, r_value, p_value, std_err = stats.linregress(x,y)
source = ColumnDataSource(data=dict(x=x, y=y, colors=colors, hidden=np.ones(len(x))*np.min(y)))
source_slope = ColumnDataSource(data=dict(x=[0,100], y=[intercept,intercept+slope*100]))
# Create a scatter plot
p = figure(title="Scatter Plot with 500 Points", 
           x_axis_label="X-axis", y_axis_label="Y-axis", 
           width=800, height=800, tools = 'pan, wheel_zoom',**jk9)

sc = p.scatter('x', 'y', line_color = 'deepskyblue',source=source, size=12, fill_color=None, alpha=1,hover_line_width = 5,legend_label='scatter')
p.line('x', 'y', source=source_slope, line_color = 'red', line_width = 2)

tltl = """<i>x:</i> <b>@x</b> <br> <i>y:</i> <b>@y</b>"""
p.add_tools(HoverTool(tooltips=hovfun(tltl), formatters={"@hidden": cusj()},mode="mouse",point_policy='snap_to_data',renderers = [sc]))
add_extras(p,tth=0,cross=0);



from bokeh.models import DataTable, TableColumn, Div
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource

# Sample evaluation metrics data
metrics_data = {
    'Metric': ['Pearson R', 'Bias', 'RMSE', 'Number of Points', 'Date Start', 'Date End'],
    'Value': [0.85, 0.2, 1.5, 500, '2023-01-01', '2023-12-31']
}

# Create a ColumnDataSource for the table
metrics_source = ColumnDataSource(data=metrics_data)

# Define the columns
columns = [
    TableColumn(field="Metric", title="Metric"),
    TableColumn(field="Value", title="Value"),
]

# Create the table
data_table = DataTable(source=metrics_source, columns=columns, width=300, height=200)

# Create a title for the table
table_title = Div(text="<h3>Evaluation Metrics</h3>")

# Arrange the table and plot in a layout
layout = row(column(table_title, data_table), p)
show(layout)
save_plot(layout, 'scatter_02')
