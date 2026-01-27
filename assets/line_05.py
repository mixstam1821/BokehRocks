import bokeh_rocks as br
from bokeh.io import show
import pandas as pd
import numpy as np

dates = pd.date_range("2023-01-01", periods=365, freq="D")
df2 = pd.DataFrame(
    {
        "revenue": 5000 + np.cumsum(np.random.randn(365) * 30),
        "costs": 3000 + np.cumsum(np.random.randn(365) * 25),
        "temperature": 20 + 10 * np.sin(np.arange(365) / 30) + np.random.randn(365) * 2,
    },
    index=dates,
)

p2 = br.line(
    df2,
    y=["revenue", "costs"],
    secy=["temperature"],
    secco="#ff6464",
    title="Financial Metrics vs Temperature",
    xlabel="Date",
    ylabel="Financial ($)",
    palette=["#4db4fd", "#ffc562"],
    theme="dark",
)

show(p2);   br.save_plot(p2, "output/line_05")