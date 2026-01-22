from butils import save_plot
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import (
    ColumnDataSource, HoverTool, PolarTransform, 
    Label, FixedTicker
)
from bokeh.palettes import Spectral6
from bokeh.io import output_file, curdoc
curdoc().theme = 'dark_minimal'

# Generate sample data
n_variables = 8
n_series = 3
angles = np.linspace(0, 2*np.pi, n_variables, endpoint=False)
categories = [f'Variable {i+1}' for i in range(n_variables)]

# Generate random data
np.random.seed(42)
series_data = []
for _ in range(n_series):
    values = np.random.uniform(0.2, 1.0, n_variables)
    series_data.append(values)

# Close the polygons
angles_closed = np.append(angles, angles[0])
categories_closed = np.append(categories, categories[0])
series_data_closed = [np.append(series, series[0]) for series in series_data]

# Create polar transform
polar_transform = PolarTransform()

# Create figure
p = figure(
    width=600, height=600, 
    title="Advanced Radar Chart",
    x_range=(-1.7, 1.7), 
    y_range=(-1.7, 1.7),
    tools="pan,box_zoom,wheel_zoom,reset,save"
)

# Plot each series
colors = Spectral6[:n_series]
rr=[]

for i, (series, color) in enumerate(zip(series_data_closed, colors)):
    source = ColumnDataSource(data=dict(
        radius=series,
        angle=angles_closed,
        category=categories_closed,
        series=[f'Series {i+1}'] * len(series)
    ))
    
    # Use PolarTransform for plotting
    p.patch(x=polar_transform.x, 
            y=polar_transform.y,
            fill_color=colors[i],
            fill_alpha=0.2,
            line_color=colors[i],
            line_width=2,
            legend_label=f'Series {i+1}',
            source=source)
    
    
    rri = p.scatter(
        x=polar_transform.x, 
        y=polar_transform.y,
        size=8,
        color=color,
        source=source
    )
    rr.append(rri)

# Circular grid lines with PolarTransform
radii = np.linspace(0.2, 1.0, 5)
for radius in radii:
    # Create circular source
    theta = np.linspace(0, 2*np.pi, 100)
    circle_source = ColumnDataSource(data=dict(
        radius=[radius]*100,
        angle=theta
    ))
    
    # Plot circular grid lines
    p.line(
        x=polar_transform.x, 
        y=polar_transform.y,
        line_color="gray", 
        line_alpha=0.2,
        source=circle_source
    )
    
    # Add radius labels
    label_source = ColumnDataSource(data=dict(
        radius=[radius],
        angle=[3*np.pi/2],
        text=[f'{radius:.1f}']  # Add the text as a column
    ))
    
    p.text(
        x=polar_transform.x, 
        y=polar_transform.y,
        text='text',  # Reference the text column
        source=label_source,
        text_color="lime",
        text_alpha=0.6
    )
# Radial lines and category labels
for angle, category in zip(angles, categories):
    # Radial lines
    radial_source = ColumnDataSource(data=dict(
        radius=[0, 1],
        angle=[angle, angle]
    ))
    
    p.line(
        x=polar_transform.x, 
        y=polar_transform.y,
        line_color="gray", 
        line_alpha=0.2,
        source=radial_source
    )
    
    # Category labels
    label_source = ColumnDataSource(data=dict(
        radius=[1.3],
        angle=[angle],text = [category],
    ))
    
    p.text(
        x=polar_transform.x, 
        y=polar_transform.y,
        text='text',
        source=label_source,
        text_color="lime",
        text_align="center"
    )

# Hover tool
hover = HoverTool(
    
    renderers = rr,
    tooltips=[
    ('Series', '@series'),
    ('Category', '@category'),
    ('Value', '@radius{0.2f}')
])
p.add_tools(hover)

# Styling
p.title.text_color = "navy"
p.grid.grid_line_color = None
p.xaxis.visible = False
p.yaxis.visible = False
p.legend.click_policy = "hide"

show(p)
save_plot(p, 'output/radar_01')