from butils import *
regions = ['North', 'South', 'East', 'West']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sales = np.random.randint(50, 300, size=(len(regions), len(quarters)))

p = create_heatmap_figure(
    data=sales,
    x_labels=quarters,
    y_labels=regions,
    cmap='Spectral',
    title="💰 Regional Quarterly Sales Heatmap"
)
show(p)
save_plot(p, "output/heatmap_03")