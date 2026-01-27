import bokeh_rocks as br
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd

np.random.seed(456)
x_data = np.random.randn(5000) * 10 + 50
y_data = 2.5 * x_data + np.random.randn(5000) * 15 + 20

df3 = pd.DataFrame({
    'x_var': x_data,
    'y_var': y_data
})

p3 = br.scatter(
    df3,
    x='x_var',
    y='y_var',
    title='Large Dataset Scatter - 5000 Points',
    xlabel='X Variable',
    ylabel='Y Variable',
    regression=True,
    metrics_table=True,
    webgl=True,
    size=6,
    alpha=0.5,
    fill_color='deepskyblue',
    line_color='navy',
    hover_line_width=10,
    width=1100,
    height=800,
    float_fmt="{0.000}",

)

show(p3)
br.save_plot(p3, 'output/scatter_07')