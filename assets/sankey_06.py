from bokeh_rocks import *
traffic_flows = [
    {"source": "Google", "target": "Homepage", "value": 450},
    {"source": "Google", "target": "Blog", "value": 280},
    {"source": "Google", "target": "Products", "value": 120},
    {"source": "Facebook", "target": "Homepage", "value": 200},
    {"source": "Facebook", "target": "Blog", "value": 150},
    {"source": "Direct", "target": "Homepage", "value": 180},
    {"source": "Direct", "target": "Products", "value": 90},
    {"source": "Email", "target": "Blog", "value": 100},
    {"source": "Email", "target": "Products", "value": 60},
]

diagram2 = create_sankey(traffic_flows, title="Website Traffic Sources (thousands) - Interactive")
show(diagram2)
save_plot(diagram2, 'output/sankey_06')


