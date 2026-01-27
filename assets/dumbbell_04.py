from bokeh_rocks import dumbbell_plot, show, save_plot

revenue_data = [
    {'quarter': 'Q1 2024', 'budget': 120, 'actual': 135},
    {'quarter': 'Q2 2024', 'budget': 130, 'actual': 125},
    {'quarter': 'Q3 2024', 'budget': 140, 'actual': 155},
    {'quarter': 'Q4 2024', 'budget': 150, 'actual': 148},
]

p4 = dumbbell_plot(
    data=revenue_data,
    start_col='budget',
    end_col='actual',
    category_col='quarter',
    orientation='vertical',
    title='Quarterly Revenue: Budget vs Actual (No Glow)',
    start_label='Budget',
    end_label='Actual',
    start_color='#81fce3',
    end_color='#f7b072',
    width=600,
    height=450,
    glow=False,
    line_width=6,
    line_color='red',
    point_size=22
)
p4.background_fill_color = 'tan'
p4.background_fill_alpha = 0.5
p4.border_fill_color = 'tan'
show(p4)
save_plot(p4, "dumbbell_04")