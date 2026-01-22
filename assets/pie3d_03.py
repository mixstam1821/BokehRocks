from butils import *


categories = ['R&D', 'Marketing', 'Operations', 'Sales', 'Admin']
budget = [30, 25, 20, 15, 10]
colors3 = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#95a5a6']

pie3 = plot_3d_pie(
    values=budget,
    colors=colors3,
    labels=categories,
    title='Budget Allocation',
    width=900,
    height=700,
    radius=1.8,
    depth=0.42,
    tilt=30,
    rotation=45
)
legend3 = create_legend(categories, colors3)
save_plot(row(pie3, legend3, stylesheets=[get_dark_stylesheet()]), 'output/pie3d_03')



