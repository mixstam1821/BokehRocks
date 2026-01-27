from bokeh_rocks import plot_country_choropleth, save_plot, show

# Using new 2016 regions
density_data = {
    'Île-de-France': 1021,
    'Hauts-de-France': 189,
    'Provence-Alpes-Côte d\'Azur': 161,
    'Auvergne-Rhône-Alpes': 113,
    'Grand Est': 96,
    'Occitanie': 80,
    'Normandie': 115,
    'Nouvelle-Aquitaine': 71,
    'Bretagne': 120,
    'Pays de la Loire': 116,
    'Centre-Val de Loire': 66,
    'Bourgogne-Franche-Comté': 59,
    'Corse': 39
}

p = plot_country_choropleth(
    geojson_url="https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson",
    data_dict=density_data,
    value_col='density',
    country_name='🇫🇷 France',
    palette=["#f7fbff", "#deebf7",  "#9ecae1", "#6baed6", "#3182bd", "#08519c"],
    bin_edges=[0, 70, 90, 110, 130, 160, 200, 1100],
    bin_labels=["<70", "70-90", "90-110", "110-130", "130-160", "160-200", "200+"],
    title="🇫🇷 France Population Density by Region (people/km²)",
    name_property='nom',
    legend_title='Density',
    tooltip_label='Population Density',
    value_format='{0}',
    width=900,
    height=800, bg_color='#9c9a9a'
)

show(p)
save_plot(p, "output/geo_07")


