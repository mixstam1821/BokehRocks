import numpy as np
from bokeh_rocks import save_plot, create_gradient_masked_plot
from bokeh.plotting import show
x_ocean = np.linspace(0, 10, 150)
y_ocean = np.sin(x_ocean * 0.8) * 3 + np.cos(x_ocean * 1.5) * 1.5

ocean_plot = create_gradient_masked_plot(
    x_data=x_ocean,
    y_data=y_ocean,
    gradient_colors=["#1a2980 0%", "#26d0ce 50%", "#89fffd 100%"],
    gradient_direction="to bottom",
    mask_color="#0a2342",
    line_color="#00d9ff",
    line_width=4,
    title="Ocean Depths",
    width=900,
    height=500,
    border_color="#0f3057",
    grid_color="#1e5f8c",
    grid_alpha=0.25,
    title_color="#00ffff"
)
show(ocean_plot)
save_plot(ocean_plot, "output/area_06")  