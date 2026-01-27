from bokeh_rocks import dumbbell_plot, show, save_plot

temp_data = [
    {'city': 'New York', 'jan_temp': 32, 'jul_temp': 77},
    {'city': 'Los Angeles', 'jan_temp': 58, 'jul_temp': 73},
    {'city': 'Chicago', 'jan_temp': 26, 'jul_temp': 75},
    {'city': 'Houston', 'jan_temp': 53, 'jul_temp': 84},
    {'city': 'Phoenix', 'jan_temp': 58, 'jul_temp': 94},
    {'city': 'Miami', 'jan_temp': 68, 'jul_temp': 83},
]

p3 = dumbbell_plot(
    data=temp_data,
    start_col='jan_temp',
    end_col='jul_temp',
    category_col='city',
    orientation='horizontal',
    title='Temperature Range: January vs July (No Glow)',
    start_label='January',
    end_label='July',
    start_color='#3498db',
    end_color='#e74c3c',
    width=800,
    height=400,
    glow=False
)
show(p3)
save_plot(p3, "dumbbell_03")