import numpy as np, pandas as pd
from bokeh_rocks import fscatter_tilemap, show, save_plot
# Simulate 500 trucks randomly distributed across Europe
n = 500
np.random.seed(42)
df_fleet = pd.DataFrame({
    "name": [f"Truck {i}" for i in range(n)],
    "lat": np.random.uniform(35, 60, n),    # latitudes roughly Europe
    "lon": np.random.uniform(-10, 30, n),   # longitudes roughly Europe
    "speed": np.random.uniform(0, 130, n),  # km/h
    "fuel": np.random.uniform(10, 100, n),  # %
    "status": np.random.choice(["On Route", "Stopped", "Returning"], n)
})

p1 = fscatter_tilemap(
    df_fleet,
    color_col="speed",
    tooltip_cols=["speed", "fuel", "status"],
    label_map={
        "speed": "🚗 Speed (km/h)",
        "fuel": "⛽ Fuel (%)",
        "status": "📦 Status"
    },
    palette="Turbo256",
    value_range=(0, 130),
    title="🚚 500-Vehicle Fleet — Europe"
)
show(p1)
save_plot(p1, "output/tiles_10")