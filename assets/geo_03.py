from bokeh_rocks import plot_world_choropleth, save_plot, mbpal
from cartopy import crs as ccrs
import requests
# Simulate GDP data (replace with real data from World Bank API or CSV)
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
world_geo_gdp = requests.get(url).json()

import pandas as pd
dfpp = pd.read_csv("/home/michael/Desktop/preProcess_BokehRocks/scripts/input/GDP per capita.csv")

gdp_data_dict = {}
for index, row in dfpp.iterrows():
    gdp_data_dict[dfpp.iloc[index, 0]] = dfpp.iloc[index, -1]

# gdp_data = gdp_data_dict
import math
gdp_data0 = {k: float(v) if v != 'no data' else math.nan for k, v in gdp_data_dict.items()}
gdp_data = {k: v for k, v in gdp_data0.items() if not math.isnan(v)}

# Assign GDP data
for feature in world_geo_gdp['features']:
    country = feature['properties']['name']
    value = gdp_data.get(country, None)
    
    if value is None:
        if country == 'United States of America': 
            value = gdp_data.get('United States')
        elif country == 'Russian Federation': 
            value = gdp_data.get('Russia')
        elif country == "Korea, Republic of": 
            value = gdp_data.get('Korea')
    
    feature['properties']['gdp_per_capita'] = value

# PLOT GDP
projection = ccrs.EqualEarth()
projName = 'Equal Earth'
bin_edges = [0, 5000, 10000, 20000, 30000, 40000, 50000, 70000, 100000]
bin_labels = ["<$5k", "$5-10k", "$10-20k", "$20-30k", "$30-40k", 
              "$40-50k", "$50-70k", "$70k+"]
palette = ["#fff7ec", "#fee8c8",  "#fdbb84", "#fc8d59", 
           "#ef6548", "#d7301f", "#990000"]

p4 = plot_world_choropleth(world_geo_gdp, projection, projName,
                           value_col='gdp_per_capita',
                           palette=palette,
                           bin_labels=bin_labels,
                           bin_edges=bin_edges,
                           use_natural_earth=True,
                           title="🌎 World GDP per Capita (2026) ~ International Monetary Fund",
                           legend_title='GDP per Capita',
                           tooltip_label='GDP per Capita (USD)',
                           value_format='{$0,0}')

save_plot(p4, "output/geo_03")
