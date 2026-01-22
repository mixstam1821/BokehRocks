from butils import *

labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
confusion = np.random.randint(0, 100, size=(5, 5))

p = create_heatmap_figure(
    data=confusion,
    x_labels=labels,
    y_labels=list(reversed(labels)),
    cmap='magma',
    title="🧮 Confusion Matrix Example"
)
show(p)
save_plot(p, "output/heatmap_02")