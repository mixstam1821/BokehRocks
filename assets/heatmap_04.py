from butils import *
latitudes = np.linspace(-90, 90, 10)
months = [f"M{i}" for i in range(1, 13)]
ssr_data = np.round(np.random.uniform(100, 400, size=(len(latitudes), len(months))),0)

p = create_heatmap_figure(
    data=ssr_data,
    x_labels=months,
    y_labels=[f"{lat:.0f}°" for lat in latitudes],
    cmap='cividis',
    title="☀️ Monthly SSR by Latitude",width = 900,height = 600,
)
show(p)
save_plot(p, "output/heatmap_04")