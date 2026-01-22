from butils import *

np.random.seed(42)
data = {
    'Station': ['Station A', 'Station B', 'Station C', 'Station D'] * 60,
    'Continent': ['Europe'] * 120 + ['Asia'] * 120,
    'Temperature': np.concatenate([
        np.random.normal(15, 5, 120),  # Europe temps
        np.random.normal(25, 6, 120)   # Asia temps
    ])
}
df = pd.DataFrame(data)

# Define colors for continents
continent_colors = {
    'Europe': '#0096FF',   # Blue
    'Asia': '#FFAC1C'      # Orange
}

p = fboxplot_basic(df, xcol='Station', ycol='Temperature', group_col='Continent',
                   title="Temperature by Station and Continent", 
                   palette=continent_colors,
                   show_legend=True, tth=0, width=1000)
save_plot(p, 'output/box_01')