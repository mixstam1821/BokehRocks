import pandas as pd
from bokeh_rocks import show, save_plot
import bokeh_rocks as br
import numpy as np
df2 = pd.DataFrame(
    {
        "salary": np.concatenate(
            [
                np.random.lognormal(11, 0.5, 800),  # Main population
                np.random.lognormal(12.5, 0.3, 200),  # High earners
            ]
        )
    }
)

p2 = br.hist(
    df2,
    col="salary",
    bins=50,
    title="Employee Salary Distribution",
    xlabel="Annual Salary ($)",
    ylabel="Frequency",
    color="#63ff8d",
    show_kde=True,
    kde_color="#ff6464",
    theme="dark",
    legend_outside=False,
    width=1200,
    height=650,
    output_path="output/hist_02",
)

show(p2)
save_plot(p2, "output/histogram_02")