from bokeh_rocks import plot_rounded_annular_wedges, save_plot


data3 = [7, 13, 15, 5, 3, 9]
labels3 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Weekend"]
colors3 = ["#f67280", "#ffafcc", "#a3cef1", "#b5ead7", "#f6ffe0", "#d2f6c5"]

p=plot_rounded_annular_wedges(
    data3, labels=labels3, colors=colors3,
    inner_radius=0.5, outer_radius=1,
    corner_radius=0.08, gap_width=0.19,
    title="Weekly Activity",
)
p.background_fill_color = '#EBEBEB'
p.border_fill_color = '#EBEBEB'
save_plot(p, 'output/pie_06')