import numpy as np
import pandas as pd

from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, ImageURL
from bokeh_rocks import save_plot, show
# -----------------------------
# Generate fake increasing temp data
# -----------------------------
np.random.seed(42)
years = np.arange(1980, 2026)
trend = 0.02 * (years - years[0])
noise = np.random.normal(0, 0.1, len(years))
temp = trend + noise

df = pd.DataFrame({"year": years, "temp": temp})

# -----------------------------
# Map data to screen coords
# -----------------------------
# place x positions evenly across width
x_positions = np.linspace(50, 850, len(df))

# scale y values
y_positions = 100 + (df["temp"] - df["temp"].min()) / (
    df["temp"].max() - df["temp"].min()
) * 400

# use size scaled by temp for bubble effect
sizes = 30 + (df["temp"] - df["temp"].min()) * 120

SVG_URL = "https://raw.githubusercontent.com/mixstam1821/bokeh_showcases/main/assets0/S1.svg"

source = ColumnDataSource(dict(
    url=[SVG_URL] * len(df),
    x=x_positions,
    y=y_positions,
    w=sizes,
    h=sizes,
))

# -----------------------------
# Bokeh figure
# -----------------------------
p = figure(
    width=900,
    height=600,
    x_axis_label="x",
    y_axis_label="y",
)

p.yaxis.axis_label_text_font_size = "14pt"

# -----------------------------
# Add image bubbles
# -----------------------------
img = ImageURL(
    url="url",
    x="x",
    y="y",
    w="w",
    h="h",
    anchor="center",
)

p.add_glyph(source, img)
p.background_fill_color = "silver"
p.border_fill_color = "silver"
p.grid.visible = False
# -----------------------------
# Output
# -----------------------------
show(p)
save_plot(p, "output/imageURL_02")
