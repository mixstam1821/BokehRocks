from bokeh_rocks import create_treemap, save_plot
from bokeh.io import show
print("Generating Example 4: Investment Portfolio...")
portfolio_data = [
    {"category": "Stocks", "subcategory": "US Large Cap", "value": 180},
    {"category": "Stocks", "subcategory": "International", "value": 95},
    {"category": "Bonds", "subcategory": "Government", "value": 120},
    {"category": "Bonds", "subcategory": "Corporate", "value": 85},
    {"category": "Real Estate", "subcategory": "REITs", "value": 70},
    {"category": "Stocks", "subcategory": "Small Cap", "value": 60},
    {"category": "Alternatives", "subcategory": "Commodities", "value": 45},
    {"category": "Cash", "subcategory": "Money Market", "value": 35},
    {"category": "Alternatives", "subcategory": "Crypto", "value": 25},
    {"category": "Real Estate", "subcategory": "Direct", "value": 15},
]

portfolio_colors = {
    "Stocks": "#8338EC",
    "Bonds": "#06A77D",
    "Real Estate": "#FF6F59",
    "Alternatives": "#FFD23F",
    "Cash": "#3A86FF"
}

p4 = create_treemap(
    portfolio_data,
    title="Investment Portfolio Allocation ($K)",
    width=1200,
    height=700,
    palette=portfolio_colors,
    border_color="#34495E",
    border_width=1,
    border_radius=4
)
p4.background_fill_color = "#e7e7e7"
p4.border_fill_color = "#e7e7e7"
p4.outline_line_color = None
show(p4)
save_plot(p4, "output/treemap_04")


