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

p20 = br.bar(dft, kind="vgantt", title="Timeline (Vertical)", theme="dark")

show(p20)
br.save_plot(p20, "output/bar_14")

