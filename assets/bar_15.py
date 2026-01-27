import bokeh_rocks as br
import pandas as pd
from bokeh.io import show
df = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D", "E", "F", "G"],
        "start": [1, 14, 8, 12, 6, 20, 14],
        "end": [24, 38, 92, 56, 60, 34, 98],
    }
)
p21 = br.bar(
    df, kind="hgantt", title="Timeline (Horizontal)", palette=["pink"], border_radius=50
)
show(p21)
br.save_plot(p21, "output/bar_15")



