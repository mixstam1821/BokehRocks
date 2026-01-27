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

p4 = br.bar(
    df_test,
    kind="vstack",
    title="Cumulative Sales",
    xlabel="Product Line",
    ylabel="Total Revenue",
    showlabels=1,
    theme="dark",
    legend_outside=False,
    sh=0,  # Don't auto-show
    width=1000,
    height=600,
)

show(p4)
br.save_plot(p4, "output/bar_09")