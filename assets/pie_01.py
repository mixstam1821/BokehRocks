from bokeh_rocks import fpie_basic, save_plot,apply_theme
import pandas as pd
df = pd.DataFrame({
    'Country': ['United States', 'United Kingdom', 'Japan', 'China', 'Germany',
                'India', 'Italy', 'Australia', 'Brazil', 'France', 'Taiwan', 'Spain'],
    'Value': [157, 93, 89, 63, 44, 42, 40, 35, 32, 31, 31, 29]
})

p = fpie_basic(df, title="Global Market Share", )
apply_theme(p,theme = 'dark', legend_outside=True)
p.background_fill_color = '#343838'
save_plot(p, 'output/pie_01')