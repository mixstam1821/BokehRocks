import bokeh_rocks as br
from bokeh.plotting import figure, show
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd

np.random.seed(42)
df1 = pd.DataFrame({
    'temperature': np.random.normal(25, 5, 30),
    'humidity': np.random.normal(60, 10, 30)
})

p1 = br.scatter(
    df1,
    x='temperature',
    y='humidity',
    title='Temperature vs Humidity - Ripple Effect',
    xlabel='Temperature (°C)',
    ylabel='Humidity (%)',
    ripple=True,
    ripple_circles=5,
    ripple_spacing=6,
    ripple_animate=True,
    size=10,
    width=900,
    height=700,

)


show(p1)
br.save_plot(p1, 'output/scatter_04')