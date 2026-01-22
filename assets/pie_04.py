from butils import *

energy = ['Solar', 'Wind', 'Hydro', 'Coal', 'Gas', 'Nuclear', 'Biomass']
mix = [25, 22, 18, 12, 10, 8, 5]
df = pd.DataFrame({'Source': energy, 'Value': mix})

p = fdonut_basic(df, title="⚡ Energy Production Mix (Donut)", bgc="#fff7e6", tth=0, sh=1)
save_plot(p, 'output/pie_04')