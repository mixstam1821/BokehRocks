
from bokeh_rocks import create_radar_chart, show, save_plot

categories4 = [
    'Food\nQuality',
    'Service',
    'Ambiance',
    'Value',
    'Cleanliness'
]

restaurant_data = [
    [0.95, 0.85, 0.90, 0.70, 0.95],  # Restaurant A
    [0.80, 0.95, 0.85, 0.90, 0.90],  # Restaurant B
    [0.70, 0.70, 0.95, 0.85, 0.85],  # Restaurant C
    [0.90, 0.80, 0.75, 0.95, 0.80],  # Restaurant D
    [0.85, 0.90, 0.88, 0.82, 0.92],  # Restaurant E
]

restaurant_names = [
    '⭐ La Bella Vita',
    '⭐ The Golden Spoon',
    '⭐ Atmosphere Bistro',
    '⭐ Budget Eats',
    '⭐ Clean & Fresh'
]

restaurant_colors = ['#e74c3c', '#9b59b6', '#3498db', '#f39c12', '#1abc9c']

chart4 = create_radar_chart(
    categories=categories4,
    series_data=restaurant_data,
    series_names=restaurant_names,
    colors=restaurant_colors,
    title="🍽️ Top 5 Restaurants - Customer Ratings",
    width=800,
    height=800,
    fill_alpha=0.15,
    line_width=4,
    marker_size=13,
    grid_levels=5,
    theme="light",
    background_gradient="linear-gradient(135deg, #ffeaa7 0%, #fd79a8 50%, #fdcb6e 100%)"
)

show(chart4)
save_plot(chart4, "output/radar_05")

