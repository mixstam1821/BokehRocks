from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Legend, LegendItem
import numpy as np
from math import pi
from bokeh_rocks import save_plot, mini_pie


np.random.seed(42)
monthly_data = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

product_categories = ['Electronics', 'Clothing', 'Home Goods', 'Books']

for i, month in enumerate(months):
    base_sales = 80 + 5 * (i % 6)
    total_sales = base_sales + np.random.randint(-10, 10)
    
    np.random.seed(i * 100)
    composition = np.random.randint(10, 50, 4)
    
    # Seasonal effects
    if month in ['Nov', 'Dec']:
        composition[0] *= 1.5
    elif month in ['Jun', 'Jul', 'Aug']:
        composition[1] *= 1.3
    
    scale = total_sales / sum(composition)
    composition = [int(v * scale) for v in composition]
    
    monthly_data.append({
        'month': month,
        'total_sales': total_sales,
        'breakdown': composition
    })

output_file("12_months_pies_fixed.html")
p1 = mini_pie(
    data=monthly_data,
    category_col='month',
    y_values_col='total_sales',
    values_col='breakdown',
    title='Monthly Sales by Product Category (12 Months)',
    width=1200,
    height=500,
    pie_radius=0.4,
    slice_names=product_categories,
    slice_colors=['#ff4da0', '#46e9ff', '#eeff53', '#cf31ff'],  
    show_line=True
)
p1.background_fill_color = "#e2e2e2"
show(p1)
save_plot(p1, "output/custom_plots_05")
