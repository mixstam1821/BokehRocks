import bokeh_rocks as br
import pandas as pd
from bokeh.io import show
import numpy as np
synthetic_ssr = pd.DataFrame(
    {
        "date": [
            str(i) for i in pd.date_range(start="2023-01-01", periods=120, freq="MS")
        ],
        "ssr": np.round(np.random.uniform(100, 400, size=120), 0),
    }
)


p10 = br.bar(
    synthetic_ssr,
    kind="vgroup",
    tick_label_step=10,
    x_axis_label_orientation=0.7,
    width=1500,
    sh=0,
    title="Stacked Sales - Interactive",
    xlabel="Months",
    ylabel="Total Sales",
)
p10.min_border_bottom = 200


show(p10)
br.save_plot(p10, "output/bar_12")