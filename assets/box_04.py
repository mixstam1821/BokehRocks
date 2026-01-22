from butils import *
import numpy as np, pandas as pd

import pandas as pd, numpy as np
np.random.seed(42)

df = pd.DataFrame({
    "Station": np.repeat(["A", "B", "C", "D"], 80),
    "Value": np.concatenate([
        np.random.normal(50, 5, 80),
        np.random.normal(60, 6, 80),
        np.random.normal(55, 4, 80),
        np.random.normal(48, 7, 80)
    ]),
    "Region": ['Europe'] * 120 + ['Asia'] * 200,
})

fboxplot_basic(df, "Station", "Value", 
               title="📊 Station Value Distribution by Region",
                tth=0,palette={"Europe": "#fa61ff", "Asia":"#29ff7b"}, show_legend=True, group_col="Region",)


save_plot(p, 'output/box_04')