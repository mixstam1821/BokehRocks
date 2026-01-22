from butils import *
import numpy as np, pandas as pd
energy_types = ["Solar", "Wind", "Hydro", "Nuclear", "Coal", "Gas"]
df = pd.DataFrame({
    "Energy Source": np.repeat(energy_types, 50),
    "Output (GWh)": np.concatenate([
        np.random.normal(110, 15, 50),
        np.random.normal(90, 10, 50),
        np.random.normal(75, 20, 50),
        np.random.normal(130, 12, 50),
        np.random.normal(60, 25, 50),
        np.random.normal(80, 18, 50)
    ])
})
p = fboxplot_basic(df, "Energy Source", "Output (GWh)",
               title="⚡ Energy Production Variability",
               palette=["#FFD700","#66CC66","#66CCFF","#FF99CC","#9999FF","#FFA07A"],
               )

save_plot(p, 'output/box_03')