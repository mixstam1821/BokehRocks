import pandas as pd
from bokeh_rocks import show, save_plot
import bokeh_rocks as br
import numpy as np
df4 = pd.DataFrame(
    {
        "response_time_ms": np.concatenate(
            [
                np.random.exponential(50, 900),  # Fast responses
                np.random.exponential(200, 100),  # Slow responses
            ]
        )
    }
)

p4 = br.hist(
    df4,
    col="response_time_ms",
    bins=60,
    title="API Response Time Distribution",
    xlabel="Response Time (ms)",
    ylabel="Request Count",
    color="#ff8bff",
    show_kde=True,
    kde_color="#6385ff",
    theme="dark",
    width=1300,
    height=700,

)

show(p4)
save_plot(p4, "output/histogram_04")