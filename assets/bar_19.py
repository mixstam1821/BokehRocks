from bokeh_rocks import create_gradient_bar_chart, show, save_plot

categories2 = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values2 = [120, 85, 145, 95, 160]

chart2 = create_gradient_bar_chart(
    categories=categories2,
    values=values2,
    orientation="horizontal",
    colormap="cool",
    title="🌈 Product Revenue Comparison",
    width=700,
    height=500,
    bar_thickness=0.7,
    theme="dark",
    hover_template="Product: {cat} | Revenue: ${val}K"
)
show(chart2)

save_plot(chart2, "output/bar_19")