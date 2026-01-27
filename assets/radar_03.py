
from bokeh_rocks import create_radar_chart, show, save_plot
categories2 = [
    'Performance',
    'Security',
    'Usability',
    'Scalability',
    'Cost\nEfficiency',
    'Support',
    'Integration',
    'Innovation'
]

product_data = [
    [0.95, 0.90, 0.70, 0.85, 0.60, 0.80, 0.75, 0.88],
    [0.75, 0.95, 0.85, 0.80, 0.70, 0.90, 0.85, 0.70],
    [0.70, 0.70, 0.95, 0.75, 0.85, 0.85, 0.90, 0.75],
    [0.80, 0.75, 0.80, 0.95, 0.90, 0.75, 0.80, 0.92],
]

product_names = [
    'Product A - Performance',
    'Product B - Security',
    'Product C - UX Focus',
    'Product D - Enterprise'
]

product_colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']

chart2 = create_radar_chart(
    categories=categories2,
    series_data=product_data,
    series_names=product_names,
    colors=product_colors,
    title="📊 Product Feature Comparison Matrix",
    width=900,
    height=900,
    fill_alpha=0.18,
    line_width=4,
    marker_size=14,
    grid_levels=6,
    show_grid_labels=True,
    theme="light",
    background_gradient="radial-gradient(circle at center, #ffffff 0%, #f8f9fa 50%, #e9ecef 100%)"
)

show(chart2)
save_plot(chart2, "output/radar_03")

