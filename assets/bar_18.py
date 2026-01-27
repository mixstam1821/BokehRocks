from bokeh_rocks import create_gradient_bar_chart, show, save_plot

categories3 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
values3 = [23, 45, 38, 67, 54, 82]

# Fire gradient: Dark Red -> Orange -> Yellow -> White
fire_colors = [
    [139, 0, 0],      # Dark red
    [255, 69, 0],     # Orange red
    [255, 140, 0],    # Dark orange
    [255, 215, 0],    # Gold
    [255, 255, 224]   # Light yellow
]

chart3 = create_gradient_bar_chart(
    categories=categories3,
    values=values3,
    orientation="vertical",
    custom_colors=fire_colors,
    title="🔥 Monthly Temperature Trend",
    width=800,
    height=450,
    background_gradient="radial-gradient(circle at center, #2d1b00 0%, #000000 100%)",
    theme="dark",
    hover_template="Month: {cat} | Avg Temp: {val}°C"
)
show(chart3)
save_plot(chart3, "output/bar_18")