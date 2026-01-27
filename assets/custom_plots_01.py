from bokeh_rocks import create_sample_network, plot_arc_diagram, show, save_plot

nodes, edges, colors, weights = create_sample_network('simple')
arc1 = plot_arc_diagram(
    nodes=nodes,
    edges=edges,
    node_colors=colors,
    title='Interactive Arc Diagram - Simple Network',
    width=1200,
    height=700,
    arc_height_scale=2,
    node_size=18
)
show(arc1, browser=None)
save_plot(arc1, "output/custom_plots_01")


