from bokeh_rocks import create_sample_network, plot_arc_diagram, show, save_plot
nodes, edges, colors, weights = create_sample_network('tech')
arc3 = plot_arc_diagram(
    nodes=nodes,
    edges=edges,
    node_colors=colors,
    edge_weights=weights,
    title='Programming Language Relationships',
    width=1200,
    height=750,
    node_size=20,
    arc_height_scale=2.2,
    dark_bg=False
)
show(arc3, browser=None)
save_plot(arc3, "output/custom_plots_03")