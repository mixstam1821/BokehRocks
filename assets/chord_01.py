from bokeh_rocks import create_chord_diagram, get_dark_stylesheet,get_light_stylesheet, save_plot
from bokeh.io import show
# Data represents TWh (terawatt-hours) traded annually
matrix_energy = [
    [0, 45, 32, 18, 28, 15, 22, 12],        # Germany
    [38, 0, 28, 15, 35, 8, 18, 10],         # France
    [25, 22, 0, 42, 12, 18, 8, 15],         # Norway
    [15, 12, 38, 0, 8, 28, 6, 20],          # Sweden
    [30, 40, 10, 6, 0, 18, 25, 8],          # Netherlands
    [12, 6, 15, 25, 20, 0, 32, 18],         # Poland
    [18, 15, 5, 4, 22, 35, 0, 12],          # Spain
    [10, 8, 12, 18, 6, 15, 10, 0]           # Italy
]

labels_energy = ['Germany', 'France', 'Norway', 'Sweden', 
                 'Netherlands', 'Poland', 'Spain', 'Italy']

colors_energy = ['#FFC947', '#FF6B6B', '#4ECDC4', '#45B7D1',
                 '#96CEB4', '#DDA15E', '#BC6C25', '#A8DADC']

diagram_energy = create_chord_diagram(
    matrix_energy, labels_energy, colors_energy,
    title="European Energy Trading Network (TWh/Year)",
    dark_mode=False,
    width=900, height=900
)

# Apply light stylesheet
light_sheet = get_light_stylesheet()
diagram_energy.stylesheets = [light_sheet]

show(diagram_energy)
save_plot(diagram_energy, "output/chord_01")