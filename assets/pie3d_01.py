from bokeh_rocks import *


sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Gas', 'Coal']
energy = [22, 24, 18, 16, 12, 8]
colors1 = ['#f39c12', '#3498db', '#1abc9c', '#9b59b6', '#e67e22', '#34495e']

pie1 = plot_3d_pie(
    values=energy,
    colors=colors1,
    labels=sources,
    title='Energy Sources Distribution',
    width=900,
    height=700,
    radius=1.8,
    depth=0.45,
    tilt=35,
    rotation=120
)
legend1 = create_legend(sources, colors1)
save_plot(row(pie1, legend1, stylesheets=[get_dark_stylesheet()]), 'output/pie3d_01')


