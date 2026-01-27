from bokeh.models import Div, InlineStyleSheet
from bokeh.io import show
from bokeh_rocks import save_plot
fancy_div_style = InlineStyleSheet(css="""
:host {
    position: absolute;
    background: #21233a;
    color: #fff;
    border-radius: 12px;
    padding: 18px 28px;
    text-align: center;
    overflow: hidden;
    box-shadow: 0 6px 10px rgba(197, 153, 10, 0.2);
                                   left: 2%;
}
:host::after {
    content: '';
    position: absolute;
    top: 0; left: -80%; width: 200%; height: 100%;
    background: linear-gradient(120deg, transparent 40%, rgba(255, 255, 255, 0.355) 50%, transparent 60%);
    animation: shimmer 2.2s infinite;
    pointer-events: none;
    border-radius: inherit;
}
@keyframes shimmer {
    0%   { left: -80%; }
    100% { left: 100%; }
}
""")

merged_div = Div(
    text="""
    <img src="https://static.bokeh.org/branding/icons/bokeh-icon@5x.png" alt="Bokeh logo" style="width:120px; display:block; margin:auto; margin-bottom:20px;">
    <span style="display:block;color:deepskyblue;font-size:68px;font-weight:bold;letter-spacing:2px;">Bokeh</span>
    <span style="display:block;color:orange;font-size:30px;margin-top:-18px;"><i>Rocks</i></span>
    """,
    styles={'width': '420px', 'background-color': 'black', 'padding': '30px', 'border-radius': '22px', 'margin': '28px auto'},
    stylesheets=[fancy_div_style],
)

show(merged_div, title="Aether - Bokeh Div with Inline Stylesheet")
save_plot(merged_div, "output/custom_plots_07")