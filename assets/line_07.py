import bokeh_rocks as br
from bokeh.io import show
from bokeh.layouts import row
import pandas as pd
import numpy as np
dates = pd.date_range("2023-01-01", periods=5000, freq="min")
df4 = pd.DataFrame(
    {
        "sensor_1": np.cumsum(np.random.randn(5000) * 0.1) + 100,
        "sensor_2": np.cumsum(np.random.randn(5000) * 0.15) + 95,
        "sensor_3": np.cumsum(np.random.randn(5000) * 0.08) + 105,
    },
    index=dates,
)

p4 = br.line(
    df4,
    title="High-Frequency Sensor Data (5000 points)",
    xlabel="Time",
    ylabel="Sensor Reading",
    sca=0,  # Line only for performance
    webgl=True,  # Enable WebGL for better performance
    theme="dark",
    sh=0,
)
show(row(p4, stylesheets=[br.get_dark_stylesheet()]))

show(p4);   br.save_plot(p4, "output/line_07")