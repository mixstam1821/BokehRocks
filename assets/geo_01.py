from bokeh_rocks import plot_world_choropleth, save_plot
from cartopy import crs as ccrs
import requests

# READ DATA
pop_data = requests.get("https://raw.githubusercontent.com/mixstam1821/bokeh_showcases/refs/heads/main/assets0/pop2022.json").json()
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
world_geo = requests.get(url).json()

# Convert to dict for fast lookup
pop_dict = {item['name']: item['value'] for item in pop_data}

# Assign population to GeoJSON
for feature in world_geo['features']:
    country = feature['properties']['name']
    value = pop_dict.get(country, None)
    
    # Country name fallbacks
    if value is None:
        if country == 'United States of America': 
            value = pop_dict.get('United States')
        elif country == 'Russian Federation': 
            value = pop_dict.get('Russia')
        elif country == 'Czech Republic': 
            value = pop_dict.get('Czech Rep.')
        elif country == "Democratic Republic of the Congo": 
            value = pop_dict.get("Dem. Rep. Congo")
        elif country == "Republic of the Congo": 
            value = pop_dict.get("Congo")
        elif country == "Korea, Republic of": 
            value = pop_dict.get("Korea")
        elif country == "Egypt, Arab Rep.": 
            value = pop_dict.get("Egypt")
    
    feature['properties']['population'] = value

# PLOT 1: Plate Carree Projection
projection = ccrs.PlateCarree()
projName = "Plate Carree"
palette = ["#ffffb2", "#fed976",  "#fd8d3c", "#fc4e2a", "#e31a1c", "#bd0026", "#800026"]
bin_edges = [0, 1e6, 5e6, 1e7, 5e7, 1e8, 5e8, 1e9, 2e9]
bin_labels = ["<1M", "1–5M", "5–10M", "10–50M", "50–100M", "100–500M", "500M–1B", "1B+"]

p1 = plot_world_choropleth(world_geo, projection, projName,
                           value_col='population',
                           palette=palette,
                           bin_labels=bin_labels,
                           bin_edges=bin_edges,
                           use_natural_earth=True,
                           title="🌎 World Population 2022 ~ Plate Carree Projection",
                           legend_title='Population',
                           tooltip_label='Population', oceanc='#f5f5f5',)

save_plot(p1, "output/geo_01")
