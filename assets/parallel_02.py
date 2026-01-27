from bokeh_rocks import create_parallel_coordinates, show, save_plot, Blues9
import pandas as pd
import numpy as np

# Generate iris-like dataset
iris_species = ['Setosa', 'Versicolor', 'Virginica']
iris_data = []

for species_idx, species in enumerate(iris_species):
    for _ in range(50):
        # Different characteristics for each species
        if species == 'Setosa':
            sepal_length = np.random.uniform(4.3, 5.8)
            sepal_width = np.random.uniform(2.3, 4.4)
            petal_length = np.random.uniform(1.0, 1.9)
            petal_width = np.random.uniform(0.1, 0.6)
        elif species == 'Versicolor':
            sepal_length = np.random.uniform(4.9, 7.0)
            sepal_width = np.random.uniform(2.0, 3.4)
            petal_length = np.random.uniform(3.0, 5.1)
            petal_width = np.random.uniform(1.0, 1.8)
        else:  # Virginica
            sepal_length = np.random.uniform(4.9, 7.9)
            sepal_width = np.random.uniform(2.2, 3.8)
            petal_length = np.random.uniform(4.5, 6.9)
            petal_width = np.random.uniform(1.4, 2.5)
        
        iris_data.append({
            'Sepal_Length': sepal_length,
            'Sepal_Width': sepal_width,
            'Petal_Length': petal_length,
            'Petal_Width': petal_width,
            'Species_Code': species_idx,
            'Species': species
        })

iris_df = pd.DataFrame(iris_data)

plot2 = create_parallel_coordinates(
    data=iris_df,
    dimensions=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'],
    color_by='Species_Code',
    title='Interactive Parallel Coordinates: Iris Flower Dataset (Hover to see species)',
    line_alpha=0.5,
    line_width=1.5,
    palette=Blues9,
    output_path='example2_iris.html'
)

show(plot2)

save_plot(plot2, "output/parallel_02")