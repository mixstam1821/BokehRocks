
from bokeh_rocks import create_radar_chart, show, save_plot


categories5 = [
    'Math',
    'Physics',
    'Chemistry',
    'Biology',
    'English',
    'History',
    'Geography',
    'Art',
    'Music',
    'PE',
    'Computer\nScience',
    'Languages'
]

student_data = [
    [0.92, 0.88, 0.75, 0.70, 0.85, 0.78, 0.80, 0.65, 0.60, 0.75, 0.95, 0.82],  # Student A
    [0.75, 0.70, 0.78, 0.85, 0.92, 0.90, 0.88, 0.80, 0.75, 0.70, 0.72, 0.88],  # Student B
]

student_names = ['Student A - STEM Focus', 'Student B - Arts Focus']
student_colors = ['#667eea', '#f093fb']

chart5 = create_radar_chart(
    categories=categories5,
    series_data=student_data,
    series_names=student_names,
    colors=student_colors,
    title="📚 Academic Performance Comparison",
    width=900,
    height=900,
    fill_alpha=0.25,
    line_width=3,
    marker_size=10,
    grid_levels=6,
    theme="dark",
    background_gradient="radial-gradient(circle at center, #2d3436 0%, #000000 100%)"
)

show(chart5)
save_plot(chart5, "output/radar_06")

