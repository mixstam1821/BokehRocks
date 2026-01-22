
from butils import *

temp_zones = [
    {"range": (0, 25), "color": "#0080FF", "label": "COLD"},
    {"range": (25, 50), "color": "#00C853", "label": "COOL"},
    {"range": (50, 75), "color": "#FF9800", "label": "WARM"},
    {"range": (75, 100), "color": "#D32F2F", "label": "HOT"}
]

gauge2 = Gauge(
    width=450, height=450,
    title="Temperature Monitor",
    unit="°C",
    zones=temp_zones,
    initial_value=15,
    easing=True,
    theme="light"
)

animate2 = CustomJS(args=dict(source=gauge2.source), code=gauge2.get_animation_js(82, 1000))

doc = curdoc()
layout = row(gauge2.figure)
doc.add_root(layout)
doc.js_on_event('document_ready', animate2)
show(gauge2.figure)
save_plot(gauge2.figure, "output/gauge_04")


