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

p1 = br.bar(
    df_test,
    kind="vgroup",
    title="Quarterly Sales Performance",
    xlabel="Product Categories",
    ylabel="Revenue (Thousands $)",
    theme="light",
    legend_outside=False,
    width=1000,
    height=600,
)

show(p1)
br.save_plot(p1, "output/bar_06")