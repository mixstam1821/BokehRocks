import pandas as pd
from bokeh_rocks import show, save_plot
import bokeh_rocks as br
import numpy as np
np.random.seed(42)
df1 = pd.DataFrame({"age": np.random.normal(35, 10, 1000)})

p1 = br.hist(
    df1,
    col="age",
    bins=40,
    title="Customer Age Distribution",
    xlabel="Age (years)",
    color="#4db4fd",
    theme="light",
    width=1000,
    height=600,
)
show(p1)
save_plot(p1, "output/histogram_01")