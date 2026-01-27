import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import PointDrawTool, ColumnDataSource, HoverTool, Div, CustomAction, CustomJS
from bokeh.layouts import column
from bokeh_rocks import save_plot
# Generate random time series data
np.random.seed(0)
N = 30
x = np.arange(N)
y = np.cumsum(np.random.randn(N)) + 10  # random walk

p = figure(width=800, height=500, title='Interactive Δx, Δy, Slope')
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Value'
main_line = p.line(x, y, line_width=2, color="#08f")
p.circle(x, y, size=7, color="#08f", alpha=0.7)

trend_source = ColumnDataSource(data={'x': [5, 20], 'y': [y[5], y[20]]})
trend_points = p.scatter(x='x', y='y', size=10, fill_color='orange', line_color='black', source=trend_source)
trend_line = p.line(x='x', y='y', line_color='orange', line_width=3, source=trend_source)

trend_points.visible = False
trend_line.visible = False

draw_tool = PointDrawTool(renderers=[trend_points], add=False)
p.add_tools(draw_tool)
p.add_tools(HoverTool(tooltips=[('Time', '$x'), ('Value', '$y')], renderers=[main_line]))

results_div = Div(
    text="<b>Interactive mode disabled. Click the toggle tool in toolbar to start analysis.</b>",
    width=800, styles={'color': 'black', 'background-color': 'lightgray', 'padding': '8px', 'border-radius': '8px'}
)

# --- JS callback for updating results_div with dx, dy, slope ---
update_callback = CustomJS(
    args=dict(
        trend_source=trend_source,
        results_div=results_div
    ),
    code="""
    const xs = trend_source.data.x, ys = trend_source.data.y;
    if (xs.length != 2 || ys.length != 2) {
        results_div.text = "<b>Drag endpoints. Slope will show here.</b>";
        return;
    }
    let x0 = xs[0], x1 = xs[1], y0 = ys[0], y1 = ys[1];
    let dx = x1 - x0, dy = y1 - y0;
    let slope_str;
    if (dx != 0) {
        let slope = dy / dx;
        slope_str = "Slope = " + slope.toFixed(3);
    } else {
        slope_str = "Slope = ∞";
    }
    results_div.text = `<b>Δx = ${dx.toFixed(2)}, Δy = ${dy.toFixed(2)}, ${slope_str}</b>`;
    """
)
trend_source.js_on_change('data', update_callback)

# --- Toolbar toggle button for interactive mode ---
toggle_callback = CustomJS(
    args=dict(
        trend_points=trend_points,
        trend_line=trend_line,
        draw_tool=draw_tool,
        results_div=results_div,
        plot=p
    ),
    code="""
    const currently_visible = trend_points.visible;
    trend_points.visible = !currently_visible;
    trend_line.visible = !currently_visible;
    if (!currently_visible) {
        plot.toolbar.active_tap = draw_tool;
        results_div.text = "<b>Interactive mode enabled! Drag the orange endpoints to analyze.</b>";
    } else {
        plot.toolbar.active_tap = null;
        results_div.text = "<b>Interactive mode disabled. Click the toggle tool in toolbar to start analysis.</b>";
    }
    """
)
toggle_action = CustomAction(
    icon="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBkPSJNNCAyMEwyMCA0IiBzdHJva2U9IiNmZjY2MDAiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+Cjwvc3ZnPgo=",
    description="Toggle Interactive Mode",
    callback=toggle_callback
)
p.add_tools(toggle_action)

show(column(p, results_div))
save_plot(p, 'output/custom_plots_15')