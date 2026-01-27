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
p2 = br.bar(
    df_test,
    kind="vgroup",
    title="Sales Report - Q1 to Q3",
    xlabel="Products",
    ylabel="Units Sold",
    custom_text0=[
        [1, 70, "📈 Strong Growth!", "lime", "13pt"],
        [3, 40, "📉 Weak Growth", "red", "13pt"],
    ],
    theme="dark",
    legend_outside=True,
    width=1000,
    height=600,
    output_path="output/bar_19",
)
show(p2)
br.save_plot(p2, "output/bar_08")

