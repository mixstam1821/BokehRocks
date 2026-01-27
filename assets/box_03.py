import pandas as pd, numpy as np
import bokeh_rocks as br
df3 = pd.DataFrame(
    {
        "region": np.repeat(["North", "South", "East", "West", "Central"], 60),
        "sales": np.concatenate(
            [
                np.random.lognormal(10, 0.5, 60),  # North
                np.random.lognormal(9.8, 0.6, 60),  # South
                np.random.lognormal(10.2, 0.4, 60),  # East
                np.random.lognormal(9.9, 0.55, 60),  # West
                np.random.lognormal(10.1, 0.45, 60),  # Central
            ]
        ),
    }
)

p3 = br.boxplot(
    df3,
    xcol="region",
    ycol="sales",
    title="Regional Sales Performance ($K)",
    ylabel="Monthly Sales ($1000s)",
    theme="light",
    width=1100,
    height=650,
    outlier_color="red",
    outlier_alpha=0.6,
)
p3.min_border_bottom = 130
br.save_plot(p3, 'output/box_03')