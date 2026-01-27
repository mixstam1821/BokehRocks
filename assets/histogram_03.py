import pandas as pd
from bokeh_rocks import show, save_plot
import bokeh_rocks as br
import numpy as np
df3 = pd.DataFrame({"test_score": np.random.beta(8, 2, 1500) * 100})

p3 = br.hist(
    df3,
    col="test_score",
    bins=30,
    density=True,
    title="Standardized Test Score Distribution",
    xlabel="Score (%)",
    color="#ffc562",
    theme="light",
    width=1000,
    height=600,
        show_kde=True,
    kde_color="#ff6464",
)

show(p3)
save_plot(p3, "output/histogram_03")