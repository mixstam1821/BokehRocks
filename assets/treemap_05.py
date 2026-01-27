from bokeh_rocks import create_treemap, save_plot
from bokeh.io import show
traffic_data = [
    {"category": "Organic", "subcategory": "Google Search", "value": 245000},
    {"category": "Organic", "subcategory": "Bing Search", "value": 32000},
    {"category": "Organic", "subcategory": "Other Search", "value": 18000},
    {"category": "Social Media", "subcategory": "Facebook", "value": 85000},
    {"category": "Social Media", "subcategory": "Twitter", "value": 42000},
    {"category": "Social Media", "subcategory": "LinkedIn", "value": 38000},
    {"category": "Social Media", "subcategory": "Instagram", "value": 55000},
    {"category": "Paid", "subcategory": "Google Ads", "value": 125000},
    {"category": "Paid", "subcategory": "Facebook Ads", "value": 78000},
    {"category": "Paid", "subcategory": "Display Network", "value": 45000},
    {"category": "Direct", "subcategory": "Type-in Traffic", "value": 95000},
    {"category": "Direct", "subcategory": "Bookmarks", "value": 62000},
    {"category": "Referral", "subcategory": "Partner Sites", "value": 48000},
    {"category": "Referral", "subcategory": "News Sites", "value": 28000},
    {"category": "Referral", "subcategory": "Blogs", "value": 22000},
]

p5 = create_treemap(
    traffic_data,
    title="Monthly Website Traffic Sources (1.02M visits)",
    width=1400,
    height=800,
    theme="dark",
    border_radius=15,
    border_color="#2c3e50",
    border_width=3,
)

p5.background_fill_color = "#2c3e50"
p5.border_fill_color = "#2c3e50"
p5.outline_line_color = None
show(p5)
save_plot(p5, "output/treemap_05")