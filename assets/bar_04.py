
import bokeh_rocks as br
from bokeh.io import show
import pandas as pd

# Test dataset
df_test = pd.DataFrame(
    {
        "Product": ["Laptop", "Phone", "Tablet", "Watch"],
        "Q1": [45, 62, 38, 28],
        "Q2": [52, 58, 42, 35],
        "Q3": [48, 65, 45, 32],
    }
)

p0 = br.bar(
    df_test.iloc[:, :2],
    kind="vgroup",
    title="Sales Performance",
    xlabel="Product Categories",
    ylabel="Revenue (Thousands $)",
    theme="light",
    legend_outside=False,
    sh=0,
    width=1000,
    height=600,
    output_path="output/bar_04",
)
show(p0)
br.save_plot(p0, "output/bar_04")