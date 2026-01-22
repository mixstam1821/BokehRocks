from butils import *
matrix1 = [
    [0, 5, 3, 2, 0, 8],
    [5, 0, 4, 0, 3, 0],
    [3, 4, 0, 6, 0, 0],
    [2, 0, 6, 0, 4, 3],
    [0, 3, 0, 4, 0, 5],
    [8, 0, 0, 3, 5, 0]
]
labels1 = ['A', 'B', 'C', 'D', 'E', 'F']
colors1 = ['#5470C6', '#91CC75', '#FAC858', '#EE6666', '#73C0DE', '#FDD835']

diagram1 = create_chord_diagram(matrix1, labels1, colors1, dark_mode=True,
                               title="Network Flow Between Nodes")
dark_sheet = get_dark_stylesheet()
diagram1.stylesheets = [dark_sheet]

show(diagram1)
save_plot(diagram1, "output/chord_02")