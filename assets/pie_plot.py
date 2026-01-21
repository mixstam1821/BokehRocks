# pie_chart.py
from bokeh.plotting import figure, output_file, show
from bokeh.transform import cumsum
from bokeh.models import ColumnDataSource, HoverTool
from math import pi
import pandas as pd

# Output HTML file
output_file("pie_chart.html", title="Pie Chart Example")

# Sample data
data = pd.Series([30, 15, 45, 10], index=["Apples", "Bananas", "Cherries", "Dates"])
df = pd.DataFrame({'fruit': data.index, 'value': data.values})
df['angle'] = df['value']/df['value'].sum() * 2*pi
df['color'] = ["#f8766d", "#7cae00", "#00bfc4", "#c77cff"]

# Create ColumnDataSource
source = ColumnDataSource(df)

# Create figure
p = figure(height=400, width=400, title="Fruit Pie Chart",
           toolbar_location=None, tools="hover", tooltips="@fruit: @value", x_range=(-0.5, 1.0))

# Draw wedges
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='fruit', source=source)

# Style the plot
p.axis.visible = False
p.grid.visible = False
p.outline_line_color = None
p.legend.label_text_font_size = "12pt"

# Show the plot
show(p)

