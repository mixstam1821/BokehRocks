
from bokeh_rocks import create_radar_chart, show, save_plot
categories1 = [
    'Technical\nExpertise',
    'Communication',
    'Leadership',
    'Problem\nSolving',
    'Creativity',
    'Team\nCollaboration'
]

team_data = [
    [0.85, 0.70, 0.60, 0.90, 0.75, 0.80],  # Alice
    [0.70, 0.85, 0.80, 0.75, 0.65, 0.85],  # Bob
    [0.60, 0.75, 0.90, 0.80, 0.85, 0.70],  # Carol
]

team_names = ['Alice - Senior Dev', 'Bob - Team Lead', 'Carol - Designer']
team_colors = ['#ff6b6b', '#4ecdc4', '#ffd93d']

chart1 = create_radar_chart(
    categories=categories1,
    series_data=team_data,
    series_names=team_names,
    colors=team_colors,
    title="🎯 Team Skills Profile Comparison",
    width=800,
    height=800,
    fill_alpha=0.2,
    line_width=3,
    marker_size=12,
    grid_levels=5,
    theme="dark",
    background_gradient="radial-gradient(circle at center, #1e3c72 0%, #2a5298 30%, #0a0a0a 100%)"
)

show(chart1)
save_plot(chart1, "output/radar_02")

