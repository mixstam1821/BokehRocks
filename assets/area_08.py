import numpy as np
from bokeh_rocks import save_plot, create_gradient_masked_plot
from bokeh.plotting import show
x_forest = np.linspace(0, 6, 120)
y_forest = np.exp(-x_forest/3) * np.sin(x_forest * 2) * 2

forest_plot = create_gradient_masked_plot(
    x_data=x_forest,
    y_data=y_forest,
    gradient_colors=["#134e5e 0%", "#71b280 50%", "#d4fc79 100%"],
    gradient_direction="to right",  # Horizontal
    mask_color="#3d3522",
    line_color="#9cff2e",
    line_width=5,
    title="Forest Canopy - Exponential Decay",
    width=850,
    height=550,
    border_color="#4a5240",
    grid_color="#6b7a5f",
    grid_alpha=0.18,
    title_color="#a8e063"
)
show(forest_plot)

save_plot(forest_plot, "output/area_08")  