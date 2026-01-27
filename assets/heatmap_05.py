from bokeh_rocks import create_heatmap_figure, save_plot, show
import numpy as np

latitudes = np.linspace(-90, 90, 9)
months = [f"Month {m}" for m in range(1, 13)]
albedo = np.round(np.random.uniform(0.1, 0.8, size=(len(latitudes), len(months))),1)

p = create_heatmap_figure(
    albedo,
    x_labels=months,
    y_labels=[f"{lat:+.0f}°" for lat in latitudes],
    cmap='YlGnBu',width = 900,height = 600,
    title="🪐 Planetary Albedo by Latitude and Month"
)
show(p)
save_plot(p, "output/heatmap_05")