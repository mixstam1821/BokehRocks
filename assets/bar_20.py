from bokeh_rocks import create_gradient_bar_chart, show, save_plot

categories1 = ['Q1', 'Q2', 'Q3', 'Q4']
values1 = [45, 78, 62, 91]

chart1 = create_gradient_bar_chart(
    categories=categories1,
    values=values1,
    orientation="vertical",
    colormap="terrain",
    title="📊 Quarterly Sales Performance",
    width=700,
    height=450,
    theme="dark"
)
show(chart1)
save_plot(chart1, "output/bar_20")