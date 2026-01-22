from butils import *


products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [1200, 950, 1450, 800, 1100]
colors_products = ['#9b59b6', '#e91e63', '#00bcd4', '#ff9800', '#4caf50']

product_chart = plot_3d_bars(
    categories=products,
    values=sales,
    colors=colors_products,
    labels=products,
    title='Product Sales Comparison - December 2024',
    ylabel='Units Sold',
    width=900,
    height=600
)

legend_products = create_legend(products, colors_products)
layout_products = row(product_chart, legend_products, stylesheets=[get_dark_stylesheet()])
show(layout_products)
save_plot(layout_products, 'output/bar3d_03')