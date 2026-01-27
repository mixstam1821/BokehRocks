from bokeh_rocks import jk9, hovfun, add_extras, save_plot, cusj,apply_theme
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, LinearAxis, Range1d
palette= ['#0096FF','#FF3131','#FFAC1C','#00ff44','#ea51ea','#1F51FF','#FFEA00','#97573a','#00FFFF','#ff9cff','#008000','#A42A04','#D2B48C','#878787',]

x = pd.date_range('2000-01-01', periods=20, freq='MS')
xx = np.arange(20)
y = np.random.rand(20)*100
y2 = np.random.rand(20)*100
df = pd.DataFrame({'radiation': y, 'temperature': y2, 'x': x, 'hidden': y});df
sca=0
# the source
source = ColumnDataSource(df)
# the figure
p = figure(title=r"Bokeh App",x_axis_label=r"time [Months]",y_axis_label=r"$$SSR~[Wm^{-2}]$$",x_axis_type='datetime', x_range=(pd.Timestamp('2000-01-01'), pd.Timestamp('2001-08-01')),y_range=(0, 110),width=1000, **jk9)
# --- color palette (general, reusable) ---
columns = ['radiation']
hover_colors = dict(zip(columns, palette))
renderers = []
for col, color in hover_colors.items():
    if sca == 0 :
        l = p.line('x', col, source=source, color=color,line_width=1.5, legend_label=col)
        renderers.extend([l])
    else:
        s = p.scatter('x', col, source=source, size=7, color=color, legend_label=col,hover_line_width=10,);s.nonselection_glyph = None
        l = p.line('x', col, source=source, color=color,line_width=1.5, legend_label=col)
        renderers.extend([s])

tltl = hovfun("""
<i>Temperature:</i> <b>@temperature</b> <br> <i>radiation:</i> <b>@radiation</b><br> <i>time:</i> <b>@x{%Y-%m}</b>
""")
secy = ["temperature"]
secco = '#97573a'
p.extra_y_ranges = {secy[0]: Range1d(start=df.temperature.min()/1.2, end=df.temperature.max()*1.2)}
right_y_axis = LinearAxis(y_range_name=secy[0], axis_label=secy[0], axis_label_text_color=secco, axis_line_color=secco, major_label_text_color=secco,major_tick_line_color=secco, minor_tick_line_color=secco)
p.add_layout(right_y_axis, 'right')
r3 = p.scatter('x',secy[0],source = source,size=7,legend_label=secy[0], color = secco, hover_line_width=10,y_range_name=secy[0])
p.line('x',secy[0],source = source,  line_color=secco,line_width=1.5, legend_label=secy[0], y_range_name=secy[0])
renderers.extend([r3])


p.add_tools(HoverTool(tooltips=tltl, formatters={"@x": "datetime","@hidden": cusj()},mode="vline", point_policy='none', line_policy="none", attachment="below",show_arrow=False, renderers = renderers))  
apply_theme(p,'light');add_extras(p,cross=1); show(p);fname = "output/line_02"; save_plot(p,fname)

