from bokeh_rocks import plot_rounded_annular_wedges, save_plot

data2 = [25, 15, 35, 25]
labels2 = ["HR", "R&D", "Marketing", "Sales"]
colors2 = ["#5e60ce", "#00b4d8", "#ffd166", "#ff006e"]

p = plot_rounded_annular_wedges(
    data2, labels=labels2, colors=colors2,
    inner_radius=0.5, outer_radius=1.0,
    corner_radius=0.08, gap_width=0.19,
    title="Department Budgets",legend_y=0.15
)
p.background_fill_color = '#EBEBEB'
p.border_fill_color = '#EBEBEB'
save_plot(p, 'output/pie_07')