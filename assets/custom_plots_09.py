from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import InlineStyleSheet
from bokeh.io import curdoc
from bokeh_rocks import save_plot
curdoc().theme = 'dark_minimal'
pulse_shadow_css = InlineStyleSheet(css="""
:host {
    position: absolute;
    background: #444444;
    border-radius: 20px;
    padding: 18px;
    margin: 40px auto;
    box-shadow:
        0 0 38px 10px rgba(255,70,0,0.46),
        0 0 70px 18px rgba(255,200,40,0.12),
        0 0 26px 5px rgba(255,235,90,0.22);
    width: 440px;
    height: 270px;
    box-sizing: border-box;
    z-index: 0;
    animation: pulse-shadow 2.2s infinite alternate;
    left: 2%;
}

@keyframes pulse-shadow {
    0% {
        box-shadow:
            0 0 16px 3px rgba(230, 70, 10, 0.90),
            0 0 32px 8px rgba(255, 185, 25, 0.60),
            0 0 10px 1px rgba(255, 240, 170, 0.82);
    }
    30% {
        box-shadow:
            0 0 32px 10px rgba(255, 130, 10, 0.82),
            0 0 44px 14px rgba(252, 200, 40, 0.40),
            0 0 22px 3px rgba(255, 235, 120, 0.62);
    }
    50% {
        box-shadow:
            0 0 42px 12px rgba(239, 110, 30, 0.98),
            0 0 70px 20px rgba(255, 208, 50, 0.23),
            0 0 32px 6px rgba(255, 245, 100, 0.79);
    }
    70% {
        box-shadow:
            0 0 60px 14px rgba(255, 162, 12, 0.83),
            0 0 90px 32px rgba(254, 200, 60, 0.22),
            0 0 38px 7px rgba(255, 246, 143, 0.61);
    }
    100% {
        box-shadow:
            0 0 80px 22px rgba(255, 80, 0, 0.78),
            0 0 120px 38px rgba(255, 220, 70, 0.15),
            0 0 60px 12px rgba(255, 248, 192, 0.53);
    }
}
""")

p = figure(
    title="Pulsing Fire Glow Shadow",
    border_fill_color="#444444", background_fill_color="#444444",
)
p.scatter([1,2,3,4], [2,4,3,6], color="deepskyblue", size=14)

container = column(
    p,
    stylesheets=[pulse_shadow_css],
    styles={'width': '640px', 'height': '470px', 'margin': '10 auto'}
)

show(container)
save_plot(container, "output/custom_plots_09")