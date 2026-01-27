import bokeh_rocks as br
import pandas as pd
from bokeh.io import show
# Test dataset
df_test = pd.DataFrame(
    {
        "Product": ["Laptop", "Phone", "Tablet", "Watch"],
        "Q1": [45, 62, 38, 28],
        "Q2": [52, 58, 42, 35],
        "Q3": [48, 65, 45, 32],
    }
)


p00 = br.bar(
    df_test.iloc[:, :2],
    kind="hgroup",
    title="Sales Performance",
    xlabel="Product Categories",
    ylabel="Revenue (Thousands $)",
    theme="light",
    legend_outside=False,
    sh=0,
    width=1000,
    height=600,
    output_path="output/bar_16",
    border_radius=10,
)

show(p00)
br.save_plot(p00, "output/bar_05")