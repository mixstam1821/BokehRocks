import bokeh_rocks as br
from bokeh.io import show
import pandas as pd
import numpy as np

dates = pd.date_range("2023-01-01", periods=100, freq="D")
df1 = pd.DataFrame(
    {
        "sales": 700 + np.cumsum(np.random.randn(100) * 10),
        "profit": 500 + np.cumsum(np.random.randn(100) * 8),
    },
    index=dates,
)

p1 = br.line(
    df1,
    title="Daily Sales & Profit",
    ylabel="Amount ($)",
)

show(p1);   br.save_plot(p1, "output/line_03")