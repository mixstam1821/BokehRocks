
from bokeh_rocks import dumbbell_plot, show, save_plot

sales_data = [
    {'product': 'Product A', 'q1': 45, 'q4': 78},
    {'product': 'Product B', 'q1': 62, 'q4': 55},
    {'product': 'Product C', 'q1': 38, 'q4': 91},
    {'product': 'Product D', 'q1': 71, 'q4': 82},
    {'product': 'Product E', 'q1': 54, 'q4': 49},
]

p1 = dumbbell_plot(
    data=sales_data,
    start_col='q1',
    end_col='q4',
    category_col='product',
    orientation='horizontal',
    title='Sales Change: Q1 vs Q4 (With Glow)',
    start_label='Q1',
    end_label='Q4',
    start_color='orange',
    end_color='#2ecc71',
    width=700,
    height=400,
    glow=True
)
show(p1)
save_plot(p1, "dumbbell_01")

