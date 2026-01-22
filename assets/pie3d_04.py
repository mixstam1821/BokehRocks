
from butils import *
products = ['Electronics', 'Clothing', 'Food', 'Home', 'Books', 'Sports']
product_sales = [28, 22, 18, 15, 10, 7]
colors4 = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']

pie4 = plot_3d_pie(
    values=product_sales,
    colors=colors4,
    labels=products,
    title='Product Category Distribution',
    width=900,
    height=700,
    radius=1.8,
    depth=0.48,
    tilt=33,
    rotation=60,
    dark_bg=False
)
legend4 = create_legend(products, colors4, dark_bg=False)
show(row(pie4, legend4, stylesheets=[get_light_stylesheet()]))


regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
sales = [40, 30, 22, 8]
colors5 = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

pie5 = plot_3d_pie(
    values=sales,
    colors=colors5,
    labels=regions,
    title='Sales by Region',
    width=900,
    height=700,
    radius=1.8,
    depth=0.4,
    tilt=35,
    rotation=30
)
legend5 = create_legend(regions, colors5)
save_plot(row(pie5, legend5, stylesheets=[get_dark_stylesheet()]), 'output/pie3d_04')
