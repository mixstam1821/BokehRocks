

from bokeh_rocks import Gauge, show, save_plot
from bokeh.models import CustomJS
from bokeh.io import curdoc
from bokeh.layouts import row

battery_zones = [
    {"range": (0, 55), "color": "#DC143C", "label": "CRIT."},
    {"range": (55, 99), "color": "#FFA500", "label": "LOW"},
    {"range": (99, 165), "color": "#00FF7F", "label": "GOOD"}
]

gauge3 = Gauge(
    width=450, height=450,
    title="Battery Level",
    unit="%",
    zones=battery_zones,
    initial_value=85,
    range_min=0,
    range_max=165,
    easing=False,
    bg_color="#9b926d",  
    gauge_bg_color="#34332a"
)

animate3 = CustomJS(args=dict(source=gauge3.source), code=gauge3.get_animation_js(25, 1500))

doc = curdoc()
layout = row(gauge3.figure)
doc.add_root(layout)
doc.js_on_event('document_ready', animate3)
show(gauge3.figure)
save_plot(gauge3.figure, "output/gauge_05")


