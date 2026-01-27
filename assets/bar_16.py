from bokeh_rocks import create_gradient_bar_chart, show, save_plot

categories5 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
values5 = [340, 420, 380, 510, 490, 670, 580]

chart5 = create_gradient_bar_chart(
    categories=categories5,
    values=values5,
    orientation="vertical",
    colormap="Pastel1_r",
    title="📈 Weekly Website Visitors",
    width=850,
    height=500,
    bar_thickness=0.85,
    gradient_resolution=150,  # Extra smooth
    background_gradient="linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)",
    theme="dark",
    show_grid=False,
    hover_template="Day: {cat} | Visitors: {val}"
)
show(chart5)
save_plot(chart5, "output/bar_16")