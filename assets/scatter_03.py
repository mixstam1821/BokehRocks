import bokeh_rocks as br
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd

# Example 2: Multiple y columns + glow with tooltips
# ===================================================
df2 = pd.DataFrame({
    'x': np.random.normal(50, 10, 100),
    'metric_1': np.random.normal(100, 15, 100),
    'metric_2': np.random.normal(150, 20, 100)
})

glow_pts2 = {
    'x': [45, 55, 50],
    'y': [100, 150, 125]
}

glow_info2 = {
    'label': ['Target A', 'Target B', 'Target C'],
    'priority': ['High', 'Medium', 'High'],
    'value': [99.5, 148.2, 124.8]
}

p2 = br.scatter(
    df2,
    x='x',
    y=['metric_1', 'metric_2'],
    title='Metrics with Target Points',
    ripple_cols=['metric_1'],
    ripple_circles=4,
    ripple_animate=True,
    glow=True,
    glow_points=glow_pts2,
    glow_data=glow_info2,
    glow_color='gold',
    glow_size=25,
    glow_intensity=6,
    glow_label='Targets',
    palette=['#0096FF', '#FF3131'],
    size=8,
    width=1200,
    height=800,
)


show(p2)
br.save_plot(p2, 'output/scatter_03')