import pandas as pd, numpy as np
import bokeh_rocks as br
df5 = pd.DataFrame(
    {
        "server": np.repeat(["Server-A", "Server-B", "Server-C"], 150),
        "load": np.tile(np.repeat(["Low", "Medium", "High"], 50), 3),
        "response_time": np.concatenate(
            [
                # Server-A
                np.random.gamma(2, 10, 50),  # Low load
                np.random.gamma(3, 15, 50),  # Medium load
                np.random.gamma(5, 20, 50),  # High load
                # Server-B
                np.random.gamma(1.8, 12, 50),  # Low load
                np.random.gamma(2.5, 18, 50),  # Medium load
                np.random.gamma(4, 25, 50),  # High load
                # Server-C
                np.random.gamma(2.2, 8, 50),  # Low load
                np.random.gamma(3.2, 12, 50),  # Medium load
                np.random.gamma(4.5, 18, 50),  # High load
            ]
        ),
    }
)

load_palette = {"Low": "#63ff8d", "Medium": "#ffc562", "High": "#ff6464"}

p5 = br.boxplot(
    df5,
    xcol="server",
    ycol="response_time",
    group_col="load",
    title="Server Response Time Analysis by Load Level",
    xlabel="Server",
    ylabel="Response Time (ms)",
    palette=load_palette,
    theme="dark",
    legend_outside=True,
    width=1300,
    height=700,

)
p5.min_border_bottom = 190
br.save_plot(p5, 'output/box_05')