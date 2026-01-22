from butils import *

flows_college = [
    # Freshman -> Sophomore (Freshman totals: Undecided=250, Engineering=170, Business=95, Sciences=85, Liberal Arts=85, CS=110)
    [
        ("Undecided", "Business", 80),
        ("Undecided", "Engineering", 60),
        ("Undecided", "Sciences", 40),
        ("Undecided", "Liberal Arts", 50),
        ("Undecided", "Computer Science", 20),
        ("Engineering", "Engineering", 135),
        ("Engineering", "Computer Science", 35),
        ("Business", "Business", 95),
        ("Sciences", "Sciences", 75),
        ("Sciences", "Engineering", 10),
        ("Liberal Arts", "Liberal Arts", 85),
        ("Computer Science", "Computer Science", 110),
    ],
    # Sophomore -> Junior (Sophomore totals: Business=175, Engineering=205, CS=165, Sciences=115, Liberal Arts=135)
    [
        ("Business", "Business", 160),
        ("Business", "Economics", 15),
        ("Engineering", "Engineering", 165),
        ("Engineering", "Computer Science", 40),
        ("Computer Science", "Computer Science", 155),
        ("Computer Science", "Engineering", 10),
        ("Sciences", "Sciences", 80),
        ("Sciences", "Pre-Med", 35),
        ("Liberal Arts", "Liberal Arts", 100),
        ("Liberal Arts", "Communications", 35),
    ],
    # Junior -> Senior (Junior totals: Business=160, Economics=15, Engineering=175, CS=195, Sciences=80, Pre-Med=35, Liberal Arts=100, Communications=35)
    [
        ("Business", "Business", 155),
        ("Business", "Finance", 5),
        ("Economics", "Economics", 13),
        ("Economics", "Business", 2),
        ("Engineering", "Engineering", 170),
        ("Engineering", "Graduate School", 5),
        ("Computer Science", "Computer Science", 185),
        ("Computer Science", "Graduate School", 10),
        ("Sciences", "Sciences", 75),
        ("Sciences", "Graduate School", 5),
        ("Pre-Med", "Pre-Med", 30),
        ("Pre-Med", "Medical School", 5),
        ("Liberal Arts", "Liberal Arts", 95),
        ("Liberal Arts", "Graduate School", 5),
        ("Communications", "Communications", 33),
        ("Communications", "Liberal Arts", 2),
    ],
]

time_points_college = ["Freshman", "Sophomore", "Junior", "Senior"]
categories_college = [
    "Undecided", "Business", "Engineering", "Computer Science", "Sciences", 
    "Liberal Arts", "Economics", "Pre-Med", "Communications", "Finance",
    "Graduate School", "Medical School"
]
colors_college = {
    "Undecided": "#BDC3C7",
    "Business": "#E74C3C",
    "Engineering": "#3498DB",
    "Computer Science": "#9B59B6",
    "Sciences": "#1ABC9C",
    "Liberal Arts": "#F39C12",
    "Economics": "#E67E22",
    "Pre-Med": "#16A085",
    "Communications": "#D35400",
    "Finance": "#C0392B",
    "Graduate School": "#34495E",
    "Medical School": "#27AE60"
}

diagram5 = create_alluvial(
    flows_college,
    time_points_college,
    categories_college,
    colors_college,
    title="College Major Migration Across Years",
    width=1300,
    height=750,
    gap=2
)
show(diagram5)
save_plot(diagram5, 'output/sankey_03')