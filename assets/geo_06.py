from butils import *

unemployment_data = {
    'Alabama': 3.0, 'Alaska': 4.7, 'Arizona': 3.6, 'Arkansas': 3.2,
    'California': 5.1, 'Colorado': 3.7, 'Connecticut': 3.9, 'Delaware': 4.0,
    'Florida': 3.3, 'Georgia': 3.5, 'Hawaii': 3.0, 'Idaho': 3.1,
    'Illinois': 4.7, 'Indiana': 3.8, 'Iowa': 3.0, 'Kansas': 2.9,
    'Kentucky': 4.2, 'Louisiana': 3.5, 'Maine': 2.7, 'Maryland': 2.4,
    'Massachusetts': 3.4, 'Michigan': 3.8, 'Minnesota': 3.1, 'Mississippi': 3.3,
    'Missouri': 3.2, 'Montana': 2.8, 'Nebraska': 2.7, 'Nevada': 5.6,
    'New Hampshire': 2.6, 'New Jersey': 4.2, 'New Mexico': 4.8, 'New York': 4.5,
    'North Carolina': 3.6, 'North Dakota': 2.2, 'Ohio': 4.0, 'Oklahoma': 3.1,
    'Oregon': 3.8, 'Pennsylvania': 3.6, 'Rhode Island': 4.0, 'South Carolina': 3.5,
    'South Dakota': 1.8, 'Tennessee': 3.4, 'Texas': 4.0, 'Utah': 2.8,
    'Vermont': 2.3, 'Virginia': 2.9, 'Washington': 4.5, 'West Virginia': 4.4,
    'Wisconsin': 3.2, 'Wyoming': 3.1
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json",
    data_dict=unemployment_data,
    value_col='unemployment',
    country_name='🇺🇸 USA',
    palette=["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"],
    bin_edges=[0, 2.5, 3.0, 3.5, 4.0, 4.5, 6.0],
    bin_labels=["<2.5%", "2.5-3.0%", "3.0-3.5%", "3.5-4.0%", "4.0-4.5%", "4.5%+"],
    title="🇺🇸 US Unemployment Rate by State (2024 Annual Average)",
    name_property='name',
    legend_title='Unemployment Rate',
    tooltip_label='Unemployment',
    value_format='{0.1}%',
    width=1400,
    height=700, bg_color='#444444'
)

save_plot(p, "output/geo_06")
show(p)
