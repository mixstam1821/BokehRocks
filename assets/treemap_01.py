from bokeh_rocks import create_treemap, save_plot
from bokeh.io import show

tech_revenue = [
    {"category": "Hardware", "subcategory": "iPhone", "value": 191500},
    {"category": "Hardware", "subcategory": "Mac", "value": 40100},
    {"category": "Hardware", "subcategory": "iPad", "value": 29300},
    {"category": "Hardware", "subcategory": "Wearables", "value": 38400},
    {"category": "Services", "subcategory": "App Store", "value": 64200},
    {"category": "Services", "subcategory": "iCloud", "value": 18900},
    {"category": "Services", "subcategory": "Apple Music", "value": 12500},
    {"category": "Services", "subcategory": "Apple TV+", "value": 7200},
]

p1 = create_treemap(
    tech_revenue,
    title="Apple Revenue Breakdown 2023 ($M)",
    width=1200,
    height=700,
    theme="light",
    border_radius=8,
)
p1.background_fill_color = "#f5f5f5"
p1.border_fill_color = "#f5f5f5"
p1.outline_line_color = None
show(p1)
save_plot(p1, "output/treemap_01")
