from bokeh_rocks import plot_world_choropleth, save_plot, mbpal
from cartopy import crs as ccrs
import requests
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
world_geo_life = requests.get(url).json()

import pandas as pd
df00 = pd.read_csv("/home/michael/Desktop/preProcess_BokehRocks/scripts/input/lifeexp.csv",sep = "\t")
df00
life_exp_data = {}
for index, row in df00.iterrows():
    life_exp_data[df00.iloc[index, 1]] = float(df00.iloc[index, 2])

# Assign life expectancy data
for feature in world_geo_life['features']:
    country = feature['properties']['name']
    value = life_exp_data.get(country, None)
    
    if value is None:
        if country == 'United States of America': 
            value = life_exp_data.get('United States')
        elif country == 'Russian Federation': 
            value = life_exp_data.get('Russia')
    
    feature['properties']['life_expectancy'] = value

# PLOT LIFE EXPECTANCY
projection = ccrs.Orthographic(central_longitude = 0, central_latitude=30)
projName = 'Natural Earth'
bin_edges = [50, 60, 65, 70, 75, 80, 85]
bin_labels = ["<60", "60-65", "65-70", "70-75", "75-80", "80+"]
palette = ["#d73027", "#fc8d59", "#fee090", "#e0f3f8", "#91bfdb", "#4575b4"]

p5 = plot_world_choropleth(world_geo_life, projection, projName,
                           value_col='life_expectancy',
                           palette=palette,
                           bin_labels=bin_labels,
                           bin_edges=bin_edges,
                           use_natural_earth=True,
                           title="🌎 Life Expectancy at Birth (1995 - 2025) ~ www.worldometers.info",
                           legend_title='Life Expectancy',
                           tooltip_label='Life Expectancy (years)',
                           value_format='{0.0}',
                           width = 900,
                           height = 750, oceanc='#d2ffc4',
                           )

save_plot(p5, "output/geo_04")

