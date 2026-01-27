import bokeh_rocks as br
from bokeh.io import show
import pandas as pd
import numpy as np

dates = pd.date_range("2022-01-01", periods=250, freq="B")
df3 = pd.DataFrame(
    {
        "AAPL": 150 + np.cumsum(np.random.randn(250) * 2),
        "GOOGL": 100 + np.cumsum(np.random.randn(250) * 1.5),
        "MSFT": 300 + np.cumsum(np.random.randn(250) * 3),
        "TSLA": 200 + np.cumsum(np.random.randn(250) * 5),
    },
    index=dates,
)

p3 = br.line(
    df3,
    title="Tech Stock Performance",
    xlabel="Trading Day",
    ylabel="Stock Price ($)",
    palette=["#4db4fd", "#ff6464", "#63ff8d", "#ffc562"],
    legend_outside=True,
)
show(p3);   br.save_plot(p3, "output/line_06")