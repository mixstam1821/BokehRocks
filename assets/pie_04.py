from bokeh_rocks import fdonut_basic, save_plot, apply_theme
import pandas as pd

energy = ['Solar', 'Wind', 'Hydro', 'Coal', 'Gas', 'Nuclear', 'Biomass']
mix = [25, 22, 18, 12, 10, 8, 5]
df = pd.DataFrame({'Source': energy, 'Value': mix})

p = fdonut_basic(df, title="⚡ Energy Production Mix (Donut)", )
apply_theme(p,theme = 'light', legend_outside=True)
p.background_fill_color = 'white'
save_plot(p, 'output/pie_04')