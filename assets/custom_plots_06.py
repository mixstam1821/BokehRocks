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


from datetime import datetime, timedelta

date_data = []
start_date = datetime(2022, 5, 1)
revenue_sources = ['Product A', 'Product B', 'Product C']

for i in range(15):
    current_date = start_date + timedelta(days=30*i)
    month_str = current_date.strftime('%b\n%Y') if i % 3 == 0 else current_date.strftime('%b')
    
    base_revenue = 100 + i * 8
    total_revenue = base_revenue + np.random.randint(-15, 15)
    
    np.random.seed(i * 50)
    composition = np.random.randint(20, 80, 3)
    
    scale = total_revenue / sum(composition)
    composition = [int(v * scale) for v in composition]
    
    date_data.append({
        'date': month_str,
        'total_revenue': total_revenue,
        'sources': composition
    })

p2 = mini_pie(
    data=date_data,
    category_col='date',
    y_values_col='total_revenue',
    values_col='sources',
    title='Monthly Revenue by Product (15 Months from 2022-05)',
    width=1300,
    height=550,
    pie_radius=0.3,
    slice_names=revenue_sources,
    slice_colors=['#1f77b4', '#ff7f0e', '#2ca02c'],  
    show_line=True
)
show(p2)
save_plot(p2, "output/custom_plots_06")