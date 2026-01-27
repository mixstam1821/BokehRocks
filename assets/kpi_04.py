from bokeh.plotting import figure, show
from bokeh.models import Div, Column
import numpy as np
from bokeh_rocks import save_plot
# KPI values
percent = 0.68  # 68%
main_value = str(percent*100)+"%"
label = "Goal Completion"

# Draw arc for radial progress
p = figure(width=120, height=120, x_range=(-1,1), y_range=(-1,1),
           toolbar_location=None, outline_line_color=None, min_border=0, tools='')
p.annular_wedge(
    0, 0, 0.88, 0.75,
    start_angle=np.pi/2, end_angle=np.pi/2 - 2*np.pi*percent, direction="anticlock",
    color="grey", alpha=0.2, line_color="grey"
)
p.annular_wedge(
    0, 0, 0.88, 0.75,
    start_angle=np.pi/2 - 2*np.pi*percent, end_angle=np.pi/2 - 2*np.pi*1.0, direction="anticlock",
    color="deepskyblue", alpha=0.9, line_color=None
)
p.axis.visible = False
p.xgrid.visible = False
p.ygrid.visible = False

# Overlay the main value using a Bokeh Div
kpi_radial = Div(text=f"""<br><br><br><br><br>
<div style="text-align:center; margin-top:-94px;margin-left:10px; margin-bottom:10px;">
  <div style="font-size:2.1em; font-weight:900; color:#195e7a;">{main_value}</div>
  <div style="font-size:1em; color:#3e7fa3;">{label}</div>
</div>
""")
lay = Column(p, kpi_radial)
show(lay)
save_plot(lay, "output/kpi_04")