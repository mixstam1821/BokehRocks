from bokeh_rocks import fpie_basic, save_plot, apply_theme
import pandas as pd
energy = ['Solar', 'Wind', 'Hydro', 'Coal', 'Gas', 'Nuclear', 'Biomass']
mix = [25, 22, 18, 12, 10, 8, 5]
df6 = pd.DataFrame({'Source': energy, 'Value': mix})
p = fpie_basic(df6, title="⚡ Energy Production Mix (2025)")
apply_theme(p,theme = 'light', legend_outside=True)
p.background_fill_color = 'white'
save_plot(p, 'output/pie_03')