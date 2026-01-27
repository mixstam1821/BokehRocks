import bokeh_rocks as br
import pandas as pd
from bokeh.io import show

dft = pd.DataFrame(
    {
        "category": ["A", "B", "C"],
        "start": ["2021-01-01", "2027-02-01", "2011-03-01"],
        "end": ["2027-02-01", "2038-03-01", "2033-04-01"],
    }
)
mytext = [
    [pd.to_datetime("2028-03-01"), 1.5, "SATURN1", "green", "18pt"],
    [pd.to_datetime("2022-03-01"), 2.5, "SATURN2", "green", "18pt"],
    [pd.to_datetime("2013-03-01"), 0.5, "SATURN3", "green", "18pt"],
]

p19 = br.bar(
    dft,
    kind="hgantt",
    title="Timeline (Horizontal)",
    palette=br.bxc2[2:],
    custom_text0=mytext,
)
show(p19)
br.save_plot(p19, "output/bar_13")

