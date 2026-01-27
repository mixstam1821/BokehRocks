from bokeh_rocks import *
flows_energy = [
    # 1990 -> 2000 (1990 totals: Coal=400, Oil=355, Natural Gas=210, Nuclear=65, Hydro=60, Renewables=10)
    [
        ("Coal", "Coal", 380),
        ("Coal", "Natural Gas", 20),
        ("Oil", "Oil", 340),
        ("Oil", "Natural Gas", 15),
        ("Natural Gas", "Natural Gas", 210),
        ("Nuclear", "Nuclear", 65),
        ("Hydro", "Hydro", 58),
        ("Hydro", "Renewables", 2),
        ("Renewables", "Renewables", 10),
    ],
    # 2000 -> 2010 (2000 totals: Coal=380, Oil=340, Natural Gas=245, Nuclear=65, Hydro=58, Renewables=12)
    [
        ("Coal", "Coal", 330),
        ("Coal", "Natural Gas", 40),
        ("Coal", "Renewables", 10),
        ("Oil", "Oil", 310),
        ("Oil", "Natural Gas", 30),
        ("Natural Gas", "Natural Gas", 240),
        ("Natural Gas", "Renewables", 5),
        ("Nuclear", "Nuclear", 63),
        ("Nuclear", "Renewables", 2),
        ("Hydro", "Hydro", 54),
        ("Hydro", "Renewables", 4),
        ("Renewables", "Renewables", 11),
        ("Renewables", "Hydro", 1),
    ],
    # 2010 -> 2020 (2010 totals: Coal=370, Oil=310, Natural Gas=315, Nuclear=65, Hydro=55, Renewables=32)
    [
        ("Coal", "Coal", 250),
        ("Coal", "Natural Gas", 70),
        ("Coal", "Renewables", 50),
        ("Oil", "Oil", 280),
        ("Oil", "Natural Gas", 25),
        ("Oil", "Renewables", 5),
        ("Natural Gas", "Natural Gas", 300),
        ("Natural Gas", "Renewables", 15),
        ("Nuclear", "Nuclear", 60),
        ("Nuclear", "Renewables", 5),
        ("Hydro", "Hydro", 52),
        ("Hydro", "Renewables", 3),
        ("Renewables", "Renewables", 29),
        ("Renewables", "Hydro", 3),
    ],
    # 2020 -> 2030 (2020 totals: Coal=300, Oil=285, Natural Gas=395, Nuclear=65, Hydro=55, Renewables=107)
    [
        ("Coal", "Coal", 150),
        ("Coal", "Natural Gas", 80),
        ("Coal", "Renewables", 70),
        ("Oil", "Oil", 240),
        ("Oil", "Natural Gas", 30),
        ("Oil", "Renewables", 15),
        ("Natural Gas", "Natural Gas", 350),
        ("Natural Gas", "Renewables", 45),
        ("Nuclear", "Nuclear", 58),
        ("Nuclear", "Renewables", 7),
        ("Hydro", "Hydro", 50),
        ("Hydro", "Renewables", 5),
        ("Renewables", "Renewables", 105),
        ("Renewables", "Hydro", 2),
    ],
]

time_points_energy = ["1990", "2000", "2010", "2020", "2030"]
categories_energy = ["Coal", "Oil", "Natural Gas", "Nuclear", "Hydro", "Renewables"]
colors_energy = {
    "Coal": "#2C3E50",
    "Oil": "#8B4513",
    "Natural Gas": "#3498DB",
    "Nuclear": "#9B59B6",
    "Hydro": "#1ABC9C",
    "Renewables": "#F39C12"
}

diagram3 = create_alluvial(
    flows_energy,
    time_points_energy,
    categories_energy,
    colors_energy,
    title="Global Energy Source Transition (TWh)",
    width=1400,
    height=700,
    gap=2.5
)
show(diagram3)
save_plot(diagram3, 'output/sankey_02')
