from butils import *
df = pd.DataFrame({
    'Country': ['United States', 'United Kingdom', 'Japan', 'China', 'Germany',
                'India', 'Italy', 'Australia', 'Brazil', 'France', 'Taiwan', 'Spain'],
    'Value': [157, 93, 89, 63, 44, 42, 40, 35, 32, 31, 31, 29]
})

p = fpie_basic(df, title="Global Market Share",  tth=1)
save_plot(p, 'output/pie_01')