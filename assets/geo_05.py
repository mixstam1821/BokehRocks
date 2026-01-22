from butils import *


# Regional population 2023
population_data = {
    'Anatoliki Makedonia kai Thraki': 602546,  # East Macedonia and Thrace
    'Kentriki Makedonia': 1792069,              # Central Macedonia (Thessaloniki)
    'Dytiki Makedonia': 257504,                 # West Macedonia
    'Ipeiros': 319019,                          # Epirus
    'Thessalia': 687527,                        # Thessaly
    'Ionioi Nisoi': 203579,                     # Ionian Islands
    'Dytiki Ellada': 646709,                    # West Greece
    'Stereá Elláda': 525106,                    # Central Greece
    'Attiki': 3792469,                          # Attica (Athens) - 37% of population
    'Peloponnisos': 541881,                     # Peloponnese
    'Voreio Aigaio': 195509,                    # North Aegean
    'Notio Aigaio': 326945,                     # South Aegean
    'Kriti': 622909                             # Crete
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/martynafford/natural-earth-geojson/master/10m/cultural/ne_10m_admin_1_states_provinces.json",
    data_dict=population_data,
    value_col='population',
    country_name='🇬🇷 Greece',
    palette=["#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"],
    bin_edges=[0, 250000, 400000, 600000, 800000, 1500000, 4000000],
    bin_labels=["<250k", "250-400k", "400-600k", "600-800k", "800k-1.5M", "1.5M+"],
    title="🇬🇷 Greece Population by Region (2023)",
    name_property='name',
    legend_title='Population',
    tooltip_label='Population',
    value_format='{0,0}',
    width=1000,
    height=1000,
    bounds=(19.5, 34.5, 29.5, 42.0)
)

show(p)
save_plot(p, "output/geo_05")



