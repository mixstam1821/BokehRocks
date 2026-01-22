from butils import *

energy = ['Solar', 'Wind', 'Hydro', 'Coal', 'Gas', 'Nuclear', 'Biomass']
mix = [25, 22, 18, 12, 10, 8, 5]
df6 = pd.DataFrame({'Source': energy, 'Value': mix})
p = fpie_basic(df6, title="⚡ Energy Production Mix (2025)", tth=0, bgc="#de80fa")
save_plot(p, 'output/pie_03')