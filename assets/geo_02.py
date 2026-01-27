from bokeh_rocks import plot_world_population, save_plot, mbpal
from cartopy import crs as ccrs
import requests
# READ DATA
pop_data = requests.get("https://raw.githubusercontent.com/mixstam1821/bokeh_showcases/refs/heads/main/assets0/pop2022.json").json()
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
world_geo = requests.get(url).json()
pop_dict = {item['name']: item['value'] for item in pop_data}
for feature in world_geo['features']:
    country = feature['properties']['name']
    value = pop_dict.get(country, None)
    # Country name fallbacks
    if value is None:
        if country == 'United States of America': value = pop_dict.get('United States')
        elif country == 'Russian Federation': value = pop_dict.get('Russia')
        elif country == 'Czech Republic': value = pop_dict.get('Czech Rep.')
        elif country == "Democratic Republic of the Congo": value = pop_dict.get("Dem. Rep. Congo")
        elif country == "Republic of the Congo": value = pop_dict.get("Congo")
        elif country == "Korea, Republic of": value = pop_dict.get("Korea")
        elif country == "Egypt, Arab Rep.": value = pop_dict.get("Egypt")
        # ... add more custom matches if needed
    feature['properties']['population'] = value
    
projection = ccrs.Robinson(); projName = 'Robinson'           # Robinson projection
# projection = ccrs.EckertIV() ; projName = 'EckertIV'          # Eckert IV projection
# projection = ccrs.Sinusoidal(); projName = 'Sinusoidal'           # Sinusoidal projection
# projection = ccrs.Miller() ; projName = 'Miller'          # Miller projection
# projection = ccrs.AlbersEqualArea() ; projName = 'AlbersEqualArea'          # AlbersEqualArea projection
# projection = ccrs.PlateCarree() ; projName = 'PlateCarree'          # PlateCarree projection
# projection = ccrs.Orthographic(central_longitude = -80); projName = 'Orthographic'           # Orthographic projection
# projection = ccrs.Mollweide() ; projName = 'Mollweide'         # Mollweide projection  
# projection = ccrs.EqualEarth(); projName = 'EqualEarth' 

palette2 = mbpal('YlGn')
bin_edges = [0, 1e6, 5e6, 1e7, 5e7, 1e8, 5e8, 1e9, 2e9]
bin_labels = ["<1M", "1–5M", "5–10M", "10–50M", "50–100M", "100–500M", "500M–1B", "1B+"]

p1 = plot_world_population(world_geo, projection, projName,
                      palette=palette2,
                      bin_labels=bin_labels,
                      bin_edges=bin_edges,oceanc = '#929292' )
save_plot(p1, "output/geo_02")