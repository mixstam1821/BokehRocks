from bokeh_rocks import create_gradient_bar_chart, show, save_plot
categories4 = ['Team Alpha', 'Team Beta', 'Team Gamma', 'Team Delta']
values4 = [88, 95, 73, 102]

# Ocean gradient: Deep Blue -> Cyan -> Light Blue
ocean_colors = [
    [0, 51, 102],     # Deep blue
    [0, 153, 204],    # Medium blue
    [102, 204, 255],  # Light blue
    [204, 255, 255]   # Very light cyan
]

chart4 = create_gradient_bar_chart(
    categories=categories4,
    values=values4,
    orientation="horizontal",
    custom_colors=ocean_colors,
    title="🌊 Team Performance Scores",
    width=700,
    height=400,
    theme="light",
    background_gradient="linear-gradient(to right, #e0f7ff 0%, #ffffff 100%)",
    hover_template="{cat}: {val} points"
)
show(chart4)
save_plot(chart4, "output/bar_17")