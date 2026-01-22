from butils import *

regions = ['North', 'South', 'East', 'West']
segments = ['Enterprise', 'SMB', 'Consumer']
colors_segments = ['#e74c3c', '#3498db', '#2ecc71']

market_data = {
    'North': [300, 450, 250],
    'South': [200, 350, 300],
    'East': [400, 500, 350],
    'West': [350, 400, 280]
}

market_chart = plot_3d_stacked_bars(
    categories=regions,
    data_dict=market_data,
    colors=colors_segments,
    labels=segments,
    title='Regional Market Share by Segment',
    ylabel='Revenue ($M)',
    width=900,
    height=600,
    dark_bg=False
)

legend_market = create_legend(segments, colors_segments, dark_bg=False)
layout_market = row(market_chart, legend_market, stylesheets=[get_light_stylesheet()])
show(layout_market)
save_plot(layout_market, 'output/bar3d_04')