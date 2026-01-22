from butils import *
gauge0 = Gauge(
    width=450, height=450,
    title="System Performance",
    unit="%",
    initial_value=90,
    theme="dark",
    easing=False,
    bg_color="#1A0033",  
    gauge_bg_color="#2D004D"
)

show(gauge0.figure)
save_plot(gauge0.figure, "output/gauge_01")

