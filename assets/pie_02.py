from bokeh_rocks import fpie_basic, save_plot,apply_theme
import pandas as pd
df2 = pd.DataFrame({
    'Category': ['Desktop', 'Laptop', 'Tablet'],
    'Value': [60, 30, 10]
})
p = fpie_basic(df2, title="💻 Device Sales Share", )
apply_theme(p,theme = 'dark', legend_outside=True)
p.background_fill_color = '#343838'
save_plot(p, 'output/pie_02')