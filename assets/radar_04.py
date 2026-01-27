
from bokeh_rocks import create_radar_chart, show, save_plot
categories3 = [
    'Sleep\nQuality',
    'Nutrition',
    'Exercise',
    'Hydration',
    'Mental\nHealth',
    'Stress\nLevel',
    'Energy',
    'Social\nConnection',
    'Productivity',
    'Happiness'
]

# Weekly comparison
health_data = [
    [0.75, 0.80, 0.70, 0.85, 0.65, 0.60, 0.70, 0.75, 0.80, 0.70],  # Week 1
    [0.80, 0.85, 0.80, 0.90, 0.75, 0.65, 0.80, 0.80, 0.85, 0.80],  # Week 2
    [0.85, 0.90, 0.85, 0.95, 0.85, 0.75, 0.90, 0.85, 0.90, 0.88],  # Week 3
]

health_names = ['Week 1', 'Week 2', 'Week 3 ✨']
health_colors = ['#95a5a6', '#3498db', '#2ecc71']

chart3 = create_radar_chart(
    categories=categories3,
    series_data=health_data,
    series_names=health_names,
    colors=health_colors,
    title="💪 Personal Wellness Tracker - Monthly Progress",
    width=850,
    height=850,
    fill_alpha=0.22,
    line_width=3,
    marker_size=11,
    grid_levels=5,
    theme="dark",
    background_gradient="radial-gradient(circle at center, #134e5e 0%, #71b280 50%, #0a0a0a 100%)"
)

show(chart3)

save_plot(chart3, "output/radar_04")

