from bokeh_rocks import create_sample_network, plot_arc_diagram, show, save_plot

nodes, edges, colors, weights = create_sample_network('social')
arc2 = plot_arc_diagram(
    nodes=nodes,
    edges=edges,
    node_colors=colors,
    edge_weights=weights,
    title='Interactive Arc Diagram - Social Network',
    width=1400,
    height=800,
    node_size=16,
    arc_height_scale=3
)
show(arc2, browser=None)
save_plot(arc2, "output/custom_plots_02")
    
