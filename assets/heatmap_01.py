from butils import hovfun, save_plot
from bokeh.plotting import figure, show
from bokeh.models import LinearColorMapper, ColorBar, ColumnDataSource,HoverTool
from bokeh.transform import transform
import numpy as np
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
cool = [to_hex(plt.get_cmap('cool')(i/255)) for i in range(256)]

# Create sample data
categories_x = ['A', 'B', 'C', 'D', 'E']
categories_y = ['Q1', 'Q2', 'Q3', 'Q4']

# Generate sample data
np.random.seed(42)
data = np.random.randint(10, 100, size=(len(categories_y), len(categories_x)))

# Prepare data for Bokeh
x_coords = []
y_coords = []
values = []

for i, y_cat in enumerate(categories_y):
    for j, x_cat in enumerate(categories_x):
        x_coords.append(x_cat)
        y_coords.append(y_cat)
        values.append(data[i, j])

# Create data source
source = ColumnDataSource(data=dict(
    x=x_coords,
    y=y_coords,
    values=values
))

# Create color mapper
color_mapper = LinearColorMapper(palette=cool, 
                                low=min(values), 
                                high=max(values))

# Create figure
p = figure(
    title="Simple Heatmap",
    x_range=categories_x,
    y_range=list(reversed(categories_y)),
    width=500,
    height=400,
    # toolbar_location=None
)

# Add rectangles
rr = p.rect(x="x", y="y", width=1, height=1,
       source=source, hover_line_color="black", hover_line_width=4,
       fill_color=transform('values', color_mapper),
       line_color="white")

# Add text
p.text(x="x", y="y", text="values", source=source,
       text_align="center", text_baseline="middle",
       text_font_size="12pt", text_color="black")

# Add color bar
color_bar = ColorBar(color_mapper=color_mapper, width=11, location=(0,0), major_label_text_font_size="16pt", title_text_font_size="16pt")
p.add_layout(color_bar, 'right')
tltl = "📊 @x <br> 🗓️ @y <br> 💰 $@values{0,0}K"
# Ultra fancy hover tool with positioning control
hover3 = HoverTool(
    tooltips = hovfun(tltl),    
    renderers=[rr],
    mode='mouse',
    point_policy='snap_to_data',
    attachment='below',  show_arrow=False,
)
p.add_tools(hover3)
# Simple styling
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "16pt"
p.title.text_font_size = '20pt'


show(p)
save_plot(p, "output/heatmap_01")
