from bokeh_rocks import create_treemap, save_plot
from bokeh.io import show
import pandas as pd
ecommerce_sales = [
    {"category": "Electronics", "subcategory": "Smartphones", "value": 45000},
    {"category": "Electronics", "subcategory": "Laptops", "value": 38000},
    {"category": "Electronics", "subcategory": "Tablets", "value": 22000},
    {"category": "Electronics", "subcategory": "Accessories", "value": 15000},
    {"category": "Clothing", "subcategory": "Men", "value": 32000},
    {"category": "Clothing", "subcategory": "Women", "value": 41000},
    {"category": "Clothing", "subcategory": "Kids", "value": 18000},
    {"category": "Home & Garden", "subcategory": "Furniture", "value": 28000},
    {"category": "Home & Garden", "subcategory": "Decor", "value": 12000},
    {"category": "Home & Garden", "subcategory": "Kitchen", "value": 16000},
    {"category": "Books & Media", "subcategory": "Books", "value": 8500},
    {"category": "Books & Media", "subcategory": "Movies", "value": 5200},
    {"category": "Books & Media", "subcategory": "Games", "value": 9800},
]

p3 = create_treemap(
    ecommerce_sales,
    title="Q4 Sales by Product Category",
    width=1200,
    height=650,
    border_radius=5,
    border_color="#34495e",
)

p3.background_fill_color = "#e7e7e7"
p3.border_fill_color = "#e7e7e7"
p3.outline_line_color = None
show(p3)
save_plot(p3, "output/treemap_03")
