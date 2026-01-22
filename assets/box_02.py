from butils import *
import pandas as pd, numpy as np
np.random.seed(0)
df = pd.DataFrame({
    "Crop": np.repeat(["Wheat", "Corn", "Rice", "Soybean"], 60),
    "Yield": np.concatenate([
        np.random.normal(3.5, 0.4, 60),
        np.random.normal(8.0, 0.8, 60),
        np.random.normal(5.5, 0.6, 60),
        np.random.normal(2.8, 0.3, 60)
    ])
})
p = fboxplot_basic(df, "Crop", "Yield",
               title="🌾 Crop Yield Variability (t/ha)",
               palette=["#ffd700", "#66cc66", "#0096FF", "#ff6666"],
               tth=0)


save_plot(p, 'output/box_02')