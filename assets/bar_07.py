import bokeh_rocks as br
import pandas as pd
from bokeh.io import show

df_test = pd.DataFrame(
    {
        "Product": ["Laptop", "Phone", "Tablet", "Watch"],
        "Q1": [45, 62, 38, 28],
        "Q2": [52, 58, 42, 35],
        "Q3": [48, 65, 45, 32],
    }
)

p11 = br.bar(
    df_test,
    kind="hgroup",
    title="Quarterly Sales Performance",
    xlabel="Product Categories",
    ylabel="Revenue (Thousands $)",
    theme="light",
    legend_outside=False,
    width=1000,
    height=600,
)
show(p11)
br.save_plot(p11, "output/bar_07")