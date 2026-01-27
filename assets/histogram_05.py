import pandas as pd
from bokeh_rocks import show, save_plot
import bokeh_rocks as br
import numpy as np
df5 = pd.DataFrame({"daily_return": np.random.normal(0.0005, 0.02, 2000)})

p5 = br.hist(
    df5,
    col="daily_return",
    bins=50,
    density=True,
    title="Daily Stock Return Distribution",
    xlabel="Return (%)",
    ylabel="Probability Density",
    color="#E63946",
    show_kde=True,
    kde_color="#06A77D",
    theme="light",
    legend_outside=True,
    width=1200,
    height=650,

)
show(p5)
save_plot(p5, "output/histogram_05")