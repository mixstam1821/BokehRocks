from butils import *


categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [450, 580, 620, 700]
colors_simple = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
labels_simple = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']

simple_chart = plot_3d_bars(
    categories=categories,
    values=values,
    colors=colors_simple,
    labels=labels_simple,
    title='Quarterly Sales Performance - 2024',
    ylabel='Revenue ($K)',
    width=900,
    height=600,
    dark_bg=False
)

legend_simple = create_legend(labels_simple, colors_simple, dark_bg=False)
layout_simple = row(simple_chart, legend_simple, stylesheets=[get_light_stylesheet()])

show(layout_simple)
save_plot(layout_simple, 'output/bar3d_02')