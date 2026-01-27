

from bokeh_rocks import *
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
market_share = [35, 25, 20, 12, 8]
colors2 = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']

pie2 = plot_3d_pie(
    values=market_share,
    colors=colors2,
    labels=companies,
    title='Market Share Distribution',
    width=900,
    height=700,
    radius=1.8,
    depth=0.5,
    tilt=32,
    rotation=0,
    dark_bg=False
)
legend2 = create_legend(companies, colors2, dark_bg=False)
save_plot(row(pie2, legend2, stylesheets=[get_light_stylesheet_3d()]), 'output/pie3d_02')


