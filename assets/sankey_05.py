from bokeh_rocks import *
energy_flows = [
    {"source": "Coal", "target": "Industrial", "value": 25},
    {"source": "Coal", "target": "Residential", "value": 10},
    {"source": "Gas", "target": "Residential", "value": 30},
    {"source": "Gas", "target": "Commercial", "value": 20},
    {"source": "Gas", "target": "Industrial", "value": 15},
    {"source": "Nuclear", "target": "Industrial", "value": 18},
    {"source": "Nuclear", "target": "Commercial", "value": 12},
    {"source": "Hydro", "target": "Residential", "value": 8},
    {"source": "Hydro", "target": "Commercial", "value": 7},
    {"source": "Solar", "target": "Residential", "value": 5},
    {"source": "Solar", "target": "Commercial", "value": 6},
]

diagram1 = create_sankey(energy_flows, title="Energy Flow Distribution (TWh) - Interactive")
show(diagram1)

save_plot(diagram1, 'output/sankey_05')


