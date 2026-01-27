import numpy as np
from bokeh_rocks import save_plot, create_gradient_masked_plot
from bokeh.plotting import show
x_ocean = np.linspace(0, 10, 150)
y_ocean = np.sin(x_ocean * 0.8) * 3 + np.cos(x_ocean * 1.5) * 1.5

neon_plot = create_gradient_masked_plot(
    x_data=x_ocean,
    y_data=y_ocean,
    gradient_colors=["#22223b 0%", "#383ba8 40%", "#7b2ff2 55%", "#f357a8 75%", "#03e9f4 100%"],
    gradient_direction="135deg",  # Diagonal
    mask_color="#181843",
    line_color="#03e9f4",
    line_width=4,
    title="Neon Cyberpunk",
    border_color="#0b0824",
    grid_color="#282872",
    grid_alpha=0.15,
    title_color="#f500ea",
    axis_label_color="#1de9b6",
    tick_label_color="#b2ff59"
)
show(neon_plot)

save_plot(neon_plot, "output/area_07")  