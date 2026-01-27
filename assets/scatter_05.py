import bokeh_rocks as br
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
np.random.seed(123)
categories = np.random.choice(['Category A', 'Category B', 'Category C'], 500)
df2 = pd.DataFrame({
    'sales': np.random.exponential(1000, 500),
    'profit': np.random.exponential(500, 500),
    'category': categories
})

p2 = br.scatter(
    df2,
    x='sales',
    y='profit',
    color_by='category',
    title='Sales vs Profit by Category',
    xlabel='Sales ($)',
    ylabel='Profit ($)',
    regression=True,
    regression_color='darkred',
    regression_width=3,
    size=8,
    alpha=0.6,
    palette=['#0096FF', '#FF3131', '#0FFF50'],
    width=1200,
    height=800,
    save=1,
    output_path='output/scatter_example_02'
)



show(p2)
br.save_plot(p2, 'output/scatter_05')