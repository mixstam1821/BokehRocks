from butils import *

"""
Greek regions unemployment rate (2023)
Greece has 13 administrative regions (Περιφέρειες)
"""
# Regional unemployment rates 2023 (from Eurostat)
# Source: Eurostat regional statistics
unemployment_data = {
    'Anatoliki Makedonia kai Thraki': 13.2,  # East Macedonia and Thrace
    'Kentriki Makedonia': 13.8,              # Central Macedonia
    'Dytiki Makedonia': 12.5,                 # West Macedonia
    'Ipeiros': 14.1,                          # Epirus
    'Thessalia': 11.9,                        # Thessaly
    'Ionioi Nisoi': 10.8,                     # Ionian Islands
    'Dytiki Ellada': 13.5,                    # West Greece
    'Stereá Elláda': 11.2,                    # Central Greece
    'Attiki': 9.4,                            # Attica (Athens region)
    'Peloponnisos': 10.5,                     # Peloponnese
    'Voreio Aigaio': 9.9,                     # North Aegean
    'Notio Aigaio': 7.1,                      # South Aegean
    'Kriti': 9.7                               # Crete
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/martynafford/natural-earth-geojson/master/10m/cultural/ne_10m_admin_1_states_provinces.json",
    data_dict=unemployment_data,
    value_col='unemployment',
    country_name='🇬🇷 Greece',
    palette=["#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#fee08b", "#fdae61", "#f46d43"],
    bin_edges=[0, 8, 10, 11, 12, 13, 15],
    bin_labels=["<8%", "8-10%", "10-11%", "11-12%", "12-13%", "13%+"],
    title="🇬🇷 Greece Unemployment Rate by Region (2023)",
    name_property='name',
    legend_title='Unemployment Rate',
    tooltip_label='Unemployment',
    value_format='{0.1}%',
    width=1000,
    height=1000,
    bounds=(19.5, 34.5, 29.5, 42.0)  # Manual bounds for Greece
)

show(p)
save_plot(p, "output/geo_10")


