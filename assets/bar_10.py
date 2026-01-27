import bokeh_rocks as br
import pandas as pd
from bokeh.io import show

# Large dataset
df_large = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "North": [120, 135, 145, 160, 175, 185, 195, 200, 190, 180, 170, 210],
        "South": [95, 105, 115, 125, 140, 150, 155, 165, 160, 145, 135, 180],
        "East": [110, 125, 130, 145, 155, 170, 180, 185, 175, 165, 155, 195],
        "West": [85, 95, 105, 115, 130, 140, 150, 160, 155, 140, 130, 170],
    }
)


p7 = br.bar(
    df_large,
    kind="vgroup",
    title="Annual Regional Sales Performance",
    xlabel="Month",
    ylabel="Sales Units (Thousands)",
    theme="dark",
    legend_outside=True,
    width=1400,
    height=700,
    output_path="output/bar_22",
    border_radius=10,
)

show(p7)
br.save_plot(p7, "output/bar_10")