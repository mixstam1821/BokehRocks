from bokeh_rocks import plot_country_choropleth, save_plot, show
from bokeh.io import curdoc
curdoc().theme = "light_minimal"
# Regional GDP per capita 2018 (from Wikipedia/Greek statistics)
gdp_data = {
    'Anatoliki Makedonia kai Thraki': 11.9,   # East Macedonia and Thrace
    'Kentriki Makedonia': 14.8,               # Central Macedonia
    'Dytiki Makedonia': 14.2,                 # West Macedonia
    'Ipeiros': 12.2,                          # Epirus
    'Thessalia': 14.1,                        # Thessaly
    'Ionioi Nisoi': 13.5,                     # Ionian Islands
    'Dytiki Ellada': 13.8,                    # West Greece
    'Stereá Elláda': 14.9,                    # Central Greece
    'Attiki': 23.3,                           # Attica (Athens) - richest region
    'Peloponnisos': 13.6,                     # Peloponnese
    'Voreio Aigaio': 11.8,                    # North Aegean - poorest region
    'Notio Aigaio': 17.2,                     # South Aegean (tourism boost)
    'Kriti': 14.5                             # Crete
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/martynafford/natural-earth-geojson/master/10m/cultural/ne_10m_admin_1_states_provinces.json",
    data_dict=gdp_data,
    value_col='gdp_per_capita',
    country_name='🇬🇷 Greece',
    palette=["#fff7bc", "#fee391",  "#fe9929", "#ec7014", "#cc4c02", "#8c2d04"],
    bin_edges=[0, 12, 13, 14, 15, 17, 20, 25],
    bin_labels=["<€12k", "€12-13k", "€13-14k", "€14-15k", "€15-17k", "€17-20k", "€20k+"],
    title="🇬🇷 Greece GDP per Capita by Region (2018)",
    name_property='name',
    legend_title='GDP per Capita',
    tooltip_label='GDP per Capita',
    value_format='{€0.1}k',
    width=1000,
    height=800,
    bounds=(19.5, 34.5, 29.5, 42.0),bg_color='#acacac'
)

show(p)
save_plot(p, "output/geo_11")

