import bokeh_rocks as br
from bokeh.io import show
import pandas as pd

rf3 = pd.DataFrame({
    'SurfaceDown': [120, 250, 300, 280, 260, 310, 390, 330, 340, 260, 250, 100],
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
})
rf3.month = rf3.month.astype('object')


p1 = br.line(
    rf3[['SurfaceDown']], title = "Solar Radiation Timeseries", 
    ylabel="SSR (Wm-2)",x = rf3.month, x_range=(rf3.month.unique()), theme = "dark", palette=['orange']
)

show(p1);   br.save_plot(p1, "output/line_04")