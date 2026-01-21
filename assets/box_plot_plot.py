from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.io import export_png

source = ColumnDataSource(dict(
    group=["A", "B", "C"],
    q1=[2, 3, 4],
    q2=[3, 4, 5],
    q3=[5, 6, 7],
    low=[1, 2, 3],
    high=[6, 7, 8],
))

hover_cb = CustomJS(code="""
console.log("Hovered box:", cb_data.index['1d'].indices);
""")

p = figure(
    x_range=source.data["group"],
    title="Box Plot",
    tools="pan,wheel_zoom,reset"
)

boxes = p.vbar(
    x="group", width=0.6,
    top="q3", bottom="q1",
    source=source, fill_alpha=0.4
)

p.segment("group", "q2", "group", "q2", source=source, line_width=2)
p.segment("group", "high", "group", "q3", source=source)
p.segment("group", "low", "group", "q1", source=source)

p.add_tools(HoverTool(
    tooltips=[
        ("Group", "@group"),
        ("Q1", "@q1"),
        ("Median", "@q2"),
        ("Q3", "@q3"),
        ("Low", "@low"),
        ("High", "@high"),
    ],
    callback=hover_cb,
    renderers=[boxes]
))

output_file("box_plot.html")
save(p)
export_png(p, filename="box_plot.png")

