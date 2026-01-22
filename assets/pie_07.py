from butils import *

data2 = [25, 15, 35, 25]
labels2 = ["HR", "R&D", "Marketing", "Sales"]
colors2 = ["#5e60ce", "#00b4d8", "#ffd166", "#ff006e"]

p = plot_rounded_annular_wedges(
    data2, labels=labels2, colors=colors2,
    inner_radius=0.5, outer_radius=1.0,
    corner_radius=0.08, gap_width=0.19,
    title="Department Budgets",tth=0,legend_y=0.15
)
save_plot(p, 'output/pie_07')