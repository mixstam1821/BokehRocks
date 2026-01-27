from bokeh_rocks import Gauge, show, save_plot
gauge0 = Gauge(
    width=450, height=450,
    title="System Performance",
    unit="%",
    initial_value=33,
    theme="light",
    easing=False,
    bg_color="#dce6fd",  
    gauge_bg_color="#d0a6ee"
)
show(gauge0.figure)

save_plot(gauge0.figure, "output/gauge_02")


