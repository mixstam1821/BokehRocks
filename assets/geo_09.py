from butils import *

# Unemployment rate % (2024)
unemployment_data = {
    'Lombardia': 4.8,
    'Veneto': 5.2,
    'Emilia-Romagna': 4.5,
    'Piemonte': 6.1,
    'Lazio': 8.5,
    'Toscana': 6.7,
    'Campania': 15.9,
    'Sicilia': 16.8,
    'Puglia': 12.4,
    'Calabria': 17.2,
    'Sardegna': 11.3,
    'Liguria': 7.2,
    'Marche': 6.9,
    'Abruzzo': 8.8,
    'Friuli-Venezia Giulia': 5.4,
    'Trentino-Alto Adige': 3.8,
    'Umbria': 7.5,
    'Basilicata': 10.1,
    'Molise': 9.2,
    'Valle d\'Aosta': 5.9
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson",
    data_dict=unemployment_data,
    value_col='unemployment',
    country_name='🇮🇹 Italy',
    palette=["#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#fee08b", "#fdae61", "#f46d43", "#d73027"],
    bin_edges=[0, 5, 7, 9, 11, 13, 15, 18],
    bin_labels=["<5%", "5-7%", "7-9%", "9-11%", "11-13%", "13-15%", "15%+"],
    title="🇮🇹 Italy Unemployment Rate by Region (2024)",
    name_property='reg_name',
    legend_title='Unemployment %',
    tooltip_label='Unemployment Rate',
    value_format='{0.1}%',
    width=600,
    height=700
)

show(p)
save_plot(p, "output/geo_09")
