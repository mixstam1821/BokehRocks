import bokeh_rocks as br
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'temperature': np.random.normal(25, 5, 30),
    'humidity': np.random.normal(60, 10, 30),
})

# Define glow points with additional info
glow_pts = {
    'x': [25, 30, 20],
    'y': [65, 55, 70]
}

# Additional data for tooltips
glow_info = {
    'name': ['Station A', 'Station B', 'Station C'],
    'importance': [95, 87, 92],
    'status': ['Active', 'Maintenance', 'Active']
}

p1 = br.scatter(
    df1,
    x='temperature',
    y='humidity',
    title='Temperature vs Humidity with Key Stations',
    xlabel='Temperature (°C)',
    ylabel='Humidity (%)',
    glow=True,
    glow_points=glow_pts,
    glow_data=glow_info,  # Additional tooltip data!
    glow_color='red',
    glow_size=20,
    glow_intensity=5,
    glow_alpha=0.3,
    glow_label='Key Stations',
    size=10,
    alpha=0.7,
    width=1000,
    height=700,

)
show(p1)
br.save_plot(p1, 'output/scatter_02')