from butils import *

"""German states unemployment rate"""

# Unemployment rate % (2024)
unemployment_data = {
    'Baden-Württemberg': 3.5,
    'Bayern': 3.4,
    'Berlin': 8.1,
    'Brandenburg': 5.4,
    'Bremen': 9.8,
    'Hamburg': 6.2,
    'Hessen': 4.8,
    'Mecklenburg-Vorpommern': 7.1,
    'Niedersachsen': 5.3,
    'Nordrhein-Westfalen': 6.8,
    'Rheinland-Pfalz': 4.7,
    'Saarland': 6.3,
    'Sachsen': 5.6,
    'Sachsen-Anhalt': 7.0,
    'Schleswig-Holstein': 5.1,
    'Thüringen': 5.5
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/main/2_bundeslaender/4_niedrig.geo.json",
    data_dict=unemployment_data,
    value_col='unemployment',
    country_name='🇩🇪 Germany',
    palette=["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"],
    bin_edges=[0, 4, 5, 6, 7, 8, 10],
    bin_labels=["<4%", "4-5%", "5-6%", "6-7%", "7-8%", "8%+"],
    title="🇩🇪 Germany Unemployment Rate by State (2024)",
    name_property='name',
    legend_title='Unemployment %',
    tooltip_label='Unemployment Rate',
    value_format='{0.1}%',
    width=600,
    height=700, bg_color='#720465'
)

show(p)
save_plot(p, "output/geo_08")


