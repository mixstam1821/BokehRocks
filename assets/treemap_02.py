from bokeh_rocks import create_treemap, save_plot
from bokeh.io import show
import pandas as pd
budget_data = pd.DataFrame(
    [
        {"category": "Engineering", "subcategory": "Backend Team", "value": 2500000},
        {"category": "Engineering", "subcategory": "Frontend Team", "value": 1800000},
        {"category": "Engineering", "subcategory": "DevOps", "value": 900000},
        {"category": "Engineering", "subcategory": "QA", "value": 700000},
        {"category": "Sales", "subcategory": "Enterprise Sales", "value": 3200000},
        {"category": "Sales", "subcategory": "SMB Sales", "value": 1500000},
        {"category": "Sales", "subcategory": "Sales Ops", "value": 600000},
        {"category": "Marketing", "subcategory": "Digital Marketing", "value": 1200000},
        {"category": "Marketing", "subcategory": "Content", "value": 500000},
        {"category": "Marketing", "subcategory": "Events", "value": 800000},
        {"category": "Operations", "subcategory": "HR", "value": 450000},
        {"category": "Operations", "subcategory": "Finance", "value": 380000},
        {"category": "Operations", "subcategory": "Legal", "value": 520000},
    ]
)

custom_palette = {
    "Engineering": "#4db4fd",
    "Sales": "#63ff8d",
    "Marketing": "#ffc562",
    "Operations": "#ff8bff",
}

p2 = create_treemap(
    budget_data,
    title="2024 Department Budget Allocation",
    width=1300,
    height=700,
    palette=custom_palette,
    theme="dark",
    border_radius=10,
    border_width=3,
    legend_outside=True,
)


p2.background_fill_color = "#2c2c2c"
p2.border_fill_color = "#2c2c2c"
p2.outline_line_color = None
show(p2)
save_plot(p2, "output/treemap_02")
