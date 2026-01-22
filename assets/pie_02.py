from butils import *

df2 = pd.DataFrame({
    'Category': ['Desktop', 'Laptop', 'Tablet'],
    'Value': [60, 30, 10]
})
p = fpie_basic(df2, title="💻 Device Sales Share", )
save_plot(p, 'output/pie_02')