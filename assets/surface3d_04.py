from butils import *

# ============================================================
# EXAMPLES
# ============================================================
best_surfaces = [
    # (lambda X,Y: np.sin(X*2) * np.cos(Y*2), "Smooth Wave Hills"),
    # (lambda X,Y: np.sin(3*np.sqrt(X**2 + Y**2))/np.sqrt(X**2 + Y**2 + 1e-6), "Circular Ripple"),
    # (lambda X,Y: (1 - (X**2 + Y**2)) * np.exp(-(X**2 + Y**2)/2), "Mexican Hat"),
    (lambda X,Y: np.sin(X)*np.cos(Y), "sin(X)*cos(Y)"),
    # (lambda X,Y: np.sin(np.sqrt(X**2 + Y**2)), "sin(sqrt(X^2+Y^2))"),
    # (lambda X,Y: np.exp(-0.1*(X**2+Y**2))*np.sin(X*2)*np.cos(Y*2), "damped sine-cosine"),
    # (lambda X,Y: np.tanh(X)*np.tanh(Y), "tanh(X)*tanh(Y)"),
    # (lambda X,Y: np.sin(X)*np.sin(Y) + np.cos(X*Y), "sin(X)*sin(Y)+cos(X*Y)")
]

for idx, (func, name) in enumerate(best_surfaces, 1):
    plot = plot_surface_bokeh(func, title=f"Surface {idx}: {name}", cmap=mbpal('terrain'), output_path=f"surface_best_{idx}.html")
    show(plot)
    save_plot(plot, 'output/surface3d_04')


