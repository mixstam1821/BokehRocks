from butils import *


years = ['2018', '2019', '2020', '2021', '2022']
countries = ['Saudi Arabia', 'France', 'South Korea', 'Germany']
colors_stacked = ['#f4d03f', '#e67e22', '#5dade2', '#2ecc71']

data = {
    '2018': [250, 500, 1000, 700],
    '2019': [250, 450, 900, 700],
    '2020': [200, 300, 850, 700],
    '2021': [150, 250, 900, 700],
    '2022': [100, 100, 900, 600]
}

stacked_chart = plot_3d_stacked_bars(
    categories=years,
    data_dict=data,
    colors=colors_stacked,
    labels=countries,
    title='Electricity Production by Country (2018-2022)',
    ylabel='TWh (Terawatt-hours)',
    width=900,
    height=600
)

legend_stacked = create_legend(countries, colors_stacked)
layout_stacked = row(stacked_chart, legend_stacked, stylesheets=[get_dark_stylesheet()])

show(layout_stacked)
save_plot(layout_stacked, 'output/bar3d_01')

