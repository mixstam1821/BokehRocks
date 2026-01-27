import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, ImageURL, Div
from bokeh.layouts import Row
from bokeh_rocks import save_plot, show
np.random.seed(42)
years = np.arange(1980, 2026)
trend = 0.02 * (years - years[0])
noise = np.random.normal(0, 0.1, len(years))
temp = trend + noise

df = pd.DataFrame({"year": years, "temp": temp})

# --------------------------------------------------
# CONFIG (ONE BG, ONE LIGHT)
# --------------------------------------------------
BG_URL = "https://raw.githubusercontent.com/mixstam1821/bokeh_showcases/refs/heads/main/assets0/cris9.jpg"
LIGHT_URL = "https://raw.githubusercontent.com/mixstam1821/bokeh_showcases/refs/heads/main/assets0/Christmas%20Lights.svg"


years = df.iloc[:, 0].values
values = df.iloc[:, 1].values

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def smooth_path(x, y, degree=4, n_points=20):
    coeffs = np.polyfit(x, y, degree)
    poly = np.poly1d(coeffs)

    x_dense = np.linspace(x.min(), x.max(), 1000)
    y_dense = poly(x_dense)

    dx = np.diff(x_dense)
    dy = np.diff(y_dense)
    s = np.cumsum(np.sqrt(dx**2 + dy**2))
    s = np.insert(s, 0, 0)

    s_target = np.linspace(0, s[-1], n_points)
    x_s = np.interp(s_target, s, x_dense)
    y_s = np.interp(s_target, s, y_dense)

    angles = np.arctan(np.gradient(y_s, x_s))
    return x_s, y_s, angles

# --------------------------------------------------
# SCALE DATA TO SCREEN SPACE
# --------------------------------------------------
x_numeric = np.linspace(0, 650, len(years))
y_scaled = 150 + (values - values.min()) / (values.max() - values.min()) * 400

x_s, y_s, angles = smooth_path(x_numeric, y_scaled, n_points=15)

# --------------------------------------------------
# DATA SOURCE
# --------------------------------------------------
source = ColumnDataSource(dict(
    url=[LIGHT_URL] * len(x_s),
    x=x_s,
    y=y_s,
    w=[200] * len(x_s),
    h=[200] * len(x_s),
    angle=angles,
))

# --------------------------------------------------
# FIGURE
# --------------------------------------------------
p = figure(
    width=900,
    height=600,
    x_range=(-100, 700),
    y_range=(-100, 700),
    tools="",
)

p.grid.visible = False
p.outline_line_color = None
p.background_fill_color = "black"
p.border_fill_color = "black"

# --------------------------------------------------
# LIGHTS
# --------------------------------------------------
glyph = ImageURL(
    url="url",
    x="x",
    y="y",
    w="w",
    h="h",
    angle="angle",
    anchor="center",
    global_alpha=0.9,
)
p.add_glyph(source, glyph)

# --------------------------------------------------
# BACKGROUND IMAGE (STATIC DIV)
# --------------------------------------------------
bg_div = Div(
    text=f"""
    <div style="position:absolute; left:-910px; top:0px;">
        <img src="{BG_URL}" style="width:900px; height:600px; opacity:0.25;">
    </div>
    """
)
pp = Row(p, bg_div)

show(pp)
save_plot(pp, 'output/imageURL_01')
