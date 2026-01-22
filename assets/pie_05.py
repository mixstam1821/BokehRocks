
from butils import *
data = [10, 15, 5, 12, 18]
labels = ["Apples", "Pears", "Bananas", "Plums", "Tomatoes"]
colors = ["gold", "lime", "dodgerblue", "purple", "tomato"]

p = plot_rounded_annular_wedges(
    data, labels=labels, colors=colors,
    inner_radius=0.5, outer_radius=1,
    corner_radius=0.08, gap_width=0.19, tth=0,
)
save_plot(p, 'output/pie_05')