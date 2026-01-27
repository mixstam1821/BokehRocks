from bokeh.plotting import figure, curdoc
from bokeh.models import Div, InlineStyleSheet
from bokeh.layouts import column
from bokeh.io import show
from bokeh_rocks import save_plot
curdoc().theme = 'dark_minimal'
fancy_div_style = InlineStyleSheet(css="""
:host {
    position: absolute;
    background: #444444;
    color: #fff;
    border-radius: 16px;
    padding: 18px 28px;
    text-align: center;
    overflow: hidden;
    box-shadow: 0 6px 18px red;
    margin: 28px auto;
    left: 2%;
}
:host > .bk-plot-wrapper {
    border-radius: 16px !important;
    overflow: hidden !important;
}
:host::after {
    content: '';
    position: absolute;
    top: 0; left: -80%; width: 200%; height: 100%;
    background: linear-gradient(120deg, transparent 40%, rgba(118, 244, 235, 0.22) 50%, transparent 60%);
    animation: shimmer 2.4s infinite;
    pointer-events: none;
    border-radius: inherit;
    z-index: 2;
}
@keyframes shimmer {
    0%   { left: -80%; }
    100% { left: 100%; }
}
""")

p = figure(border_fill_color="#444444", background_fill_color="#444444",
           )
p.line([1,2,3,4], [2,4,3,6], color="red", line_width=2)


layout = column(p, stylesheets=[fancy_div_style])
show(layout)
save_plot(layout, "output/custom_plots_08")