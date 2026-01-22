
from butils import *
gauge1 = Gauge(
    width=450, height=450,
    title="System Performance",
    unit="%",
    initial_value=10,
    easing=True,
    theme="dark"
)

animate1 = CustomJS(args=dict(source=gauge1.source), code=gauge1.get_animation_js(75, 500))

doc = curdoc()
layout = row(gauge1.figure)
doc.add_root(layout)
doc.js_on_event('document_ready', animate1)
show(gauge1.figure)
save_plot(gauge1.figure, "output/gauge_03")


