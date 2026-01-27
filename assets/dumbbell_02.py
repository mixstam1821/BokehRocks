from bokeh_rocks import dumbbell_plot, show, save_plot

performance_data = [
    {'department': 'Sales', 'goal': 85, 'actual': 92},
    {'department': 'Marketing', 'goal': 75, 'actual': 68},
    {'department': 'Support', 'goal': 90, 'actual': 88},
    {'department': 'Engineering', 'goal': 80, 'actual': 95},
    {'department': 'HR', 'goal': 70, 'actual': 73},
]

p2 = dumbbell_plot(
    data=performance_data,
    start_col='goal',
    end_col='actual',
    category_col='department',
    orientation='vertical',
    title='Department Performance: Goal vs Actual (With Glow)',
    start_label='Goal',
    end_label='Actual',
    start_color='#f39c12',
    end_color='#9b59b6',
    width=600,
    height=500,
    glow=True
)
show(p2)
save_plot(p2, "dumbbell_02")