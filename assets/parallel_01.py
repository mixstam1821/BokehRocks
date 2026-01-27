from bokeh_rocks import create_parallel_coordinates, show, save_plot
import pandas as pd
import numpy as np
# Generate car dataset similar to the example
np.random.seed(42)
years = list(range(1970, 1983))
n_cars = 100

car_data = []
for _ in range(n_cars):
    year = np.random.choice(years)
    cylinders = np.random.choice([3, 4, 5, 6, 8])
    
    # Generate correlated attributes
    displacement = cylinders * np.random.uniform(30, 70)
    weight = displacement * np.random.uniform(5, 8)
    horsepower = cylinders * np.random.uniform(15, 30)
    acceleration = np.random.uniform(8, 24)
    mpg = 50 - (weight / 200) + np.random.uniform(-5, 5)
    
    car_data.append({
        'Cylinders': cylinders,
        'Displacement': displacement,
        'Weight_in_lbs': weight,
        'Horsepower': horsepower,
        'Acceleration': acceleration,
        'Miles_per_Gallon': mpg,
        'Year': year
    })

cars_df = pd.DataFrame(car_data)

plot1 = create_parallel_coordinates(
    data=cars_df,
    dimensions=['Cylinders', 'Displacement', 'Weight_in_lbs', 'Horsepower', 
                'Acceleration', 'Miles_per_Gallon', 'Year'],
    color_by='Year',
    title='Interactive Parallel Coordinates: Automobile Dataset (Hover, Click, or Box-Select lines)',
    line_alpha=0.4,
    line_width=1.5,
    output_path='example1_cars.html'
)

show(plot1)

save_plot(plot1, "output/parallel_01")