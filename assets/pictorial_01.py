from bokeh_rocks import save_plot
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import math
import random

# ===== Data =====
vegetables = [
    '🥦 Broccoli', '🍅 Tomato', '🥕 Carrot', '🌽 Corn', '🥔 Potato',
    '🧄 Garlic', '🥒 Cucumber', '🍆 Eggplant', '🫑 Pepper', '🧅 Onion'
]
percentages = [40, 35, 30, 25, 20, 15, 10, 10, 5, 5]

# Turn percentages into "number of icons"
icon_counts = [math.ceil(p / 5) for p in percentages]

# Expand data
x = []
y = []
icons = []
labels = []
numbers = []

for i, count in enumerate(icon_counts):
    for j in range(count):
        x.append(j)
        y.append(-i)  # Downward layout (horizontal rows)
        icons.append(vegetables[i].split()[0])  # only emoji part
        labels.append(vegetables[i])
    numbers.append(percentages[i])

source = ColumnDataSource(data=dict(x=x, y=y, icon=icons, label=labels))

# ===== Plot =====
p = figure(
    height=650, width=1100,
    title="🥗 Most Popular Vegetables (Pictogram Chart)",
    toolbar_location=None,
    x_range=(-5, max(icon_counts)+4),
    y_range=(-len(vegetables)-1, 1),
)

p.text(
    x='x', y='y', text='icon', text_font_size="32pt",
    text_align='center', text_baseline='middle', source=source
)

# Add vegetable names at the start of each row
for i, veg in enumerate(vegetables):
    p.text(
        x=[-1.5], y=[-i],
        text=[veg],
        text_font_size="16pt",
        text_align='right',
        text_baseline='middle'
    )

# Add the random percentage number at the END of each row
for i, number in enumerate(numbers):
    p.text(
        x=[max(icon_counts)+1], y=[-i],
        text=[f"{number}%"],
        text_font_size="16pt",
        text_align='left',
        text_baseline='middle'
    )

# ===== Style tweaks for better look =====
p.axis.visible = False
p.grid.visible = False
p.outline_line_color = None
p.background_fill_color = "#f9f9f9"
p.title.text_font_size = "24pt"
p.title.align = "center"
p.title.text_color = "#2a2a2a"

# ===== Output =====
show(p)
save_plot(p, 'output/pictorial_01')