from bokeh.models import Div
from bokeh.plotting import figure, show
import numpy as np
import tempfile
import os
from bokeh.io import export_svg
from bokeh_rocks import save_plot
from bokeh.layouts import row

# Generate sparkline data
spark = np.cumsum(np.random.randn(30)) + 20

# Make sparkline plot
f = figure(width=120, height=34, toolbar_location=None, min_border=0, outline_line_color=None)
f.line(np.arange(len(spark)), spark, line_width=2, color="#00b3ff")
f.background_fill_color = None
f.xaxis.visible = False
f.yaxis.visible = False
f.grid.visible = False

# Export as SVG to a temp file, then read SVG code
with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as tmp_svg:
    export_svg(f, filename=tmp_svg.name)
    tmp_svg.seek(0)
    svg_data = tmp_svg.read().decode()
os.remove(tmp_svg.name)  # Clean up the temp file

# Build the KPI card with embedded SVG sparkline
kpi_sparkline = Div(text=f"""
<div style="
    background: #fff;
    border-radius: 1.5em;
    box-shadow: 0 6px 18px #0096c744;
    padding: 2.1em 1.8em 1.7em 1.8em;
    min-width: 210px;
    text-align: center;
    margin: 1.2em auto;
">
    <div style="font-size:2.4em; font-weight:800; color:#003459;">7,853</div>
    <div style="font-size:1em; color:#3975a6; margin-bottom:0.5em;">
        Website Signups
    </div>
    <div style="margin:0 auto 0.2em auto; display:inline-block;">
        {svg_data}
    </div>
</div>
""")



# Simulate some mini bar data (7 days)
bars = np.random.randint(20, 90, 7)
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

f = figure(width=120, height=36, toolbar_location=None, min_border=0, outline_line_color=None)
f.vbar(x=np.arange(7), top=bars, width=0.5, color="#34b6e4")
f.background_fill_color = None
f.xaxis.visible = False
f.yaxis.visible = False
f.grid.visible = False

with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as tmp_svg:
    export_svg(f, filename=tmp_svg.name)
    tmp_svg.seek(0)
    svg_data = tmp_svg.read().decode()
os.remove(tmp_svg.name)

kpi_bar = Div(text=f"""
<div style="
    background: #fff;
    border-radius: 1.3em;
    box-shadow: 0 6px 18px #34b6e444;
    padding: 2em 1.6em 1.1em 1.6em;
    min-width: 210px;
    text-align: center;
    margin: 1.2em auto;
">
    <div style="font-size:2.3em; font-weight:800; color:#195e7a;">869</div>
    <div style="font-size:1em; color:#3e7fa3;">
        Weekly Orders
    </div>
    <div style="margin:0.6em auto 0.2em auto; display:inline-block;">
        {svg_data}
    </div>
    <div style="font-size:0.97em; color:#28648a;">
        Last 7 days
    </div>
</div>
""")



# Example: random calendar heatmap (7 days x 5 weeks)
data = np.random.randint(0, 25, (7, 5))
f = figure(width=90, height=60, toolbar_location=None, min_border=0, outline_line_color=None,
           x_range=(0,5), y_range=(0,7))
f.rect(x=np.repeat(np.arange(5),7), y=np.tile(np.arange(7),5), width=1, height=1,
       color=["#f7fbff","#deebf7","#c6dbef","#9ecae1","#6baed6","#3182bd","#08519c"] * 5,
       alpha=0.9)
f.background_fill_color = None
f.axis.visible = False
f.grid.visible = False

with tempfile.NamedTemporaryFile(suffix='.svg', delete=False) as tmp_svg:
    export_svg(f, filename=tmp_svg.name)
    tmp_svg.seek(0)
    svg_data = tmp_svg.read().decode()
os.remove(tmp_svg.name)

kpi_heatmap = Div(text=f"""
<div style="
    background: #fff;
    border-radius: 1.4em;
    box-shadow: 0 3px 14px #44337a13;
    padding: 2em 1.4em 1.1em 1.4em;
    min-width: 230px;
    text-align: center;
    margin: 1em auto;
">
    <div style="font-size:2.15em; color:#003459; font-weight:800;">
        72%
    </div>
    <div style="font-size:1.08em; color:#2b3a67; margin-top:0.1em;">
        Daily Goal
    </div>
    <div style="margin:0.55em auto 0.2em auto; display:inline-block;">
        {svg_data}
    </div>
    <div style="font-size:0.98em; color:#038aff;">
        This Month's Pattern
    </div>
</div>
""")

layout = row(kpi_sparkline,kpi_bar,kpi_heatmap)
show(layout)
save_plot(layout, "output/kpi_02")