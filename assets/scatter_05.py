from butils import *
from bokeh.plotting import figure
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.io import curdoc,show
import numpy as np

# Generate scatter points
np.random.seed(42)
N = 30  # Number of points
x = np.random.normal(0, 1, N)
y = np.random.normal(0, 1, N)

# Create circles (3 per point)
n_circles = 4
x_ripple = np.repeat(x, n_circles)
y_ripple = np.repeat(y, n_circles)
base_sizes = [10 + i * 8 for i in range(n_circles)] * N

# Create data source
source = ColumnDataSource(data=dict(
    x=x_ripple,
    y=y_ripple,
    size=base_sizes
))

# Create data source
source2 = ColumnDataSource(data=dict(
    x=x_ripple,
    y=y_ripple,
    size=[i/4 for i in base_sizes]
))
# Create plot
p = figure(title="Animated Circles",
           x_axis_label='X Axis',
           y_axis_label='Y Axis',
           width=800,
           height=600,
           tools="pan,box_zoom,reset,save")

# Add circles
circles = p.circle('x', 'y',
                  size='size',
                  fill_color='orange',
                  line_color='orange',
                  fill_alpha=0,
                  line_alpha=1,line_width=1,
                  source=source)



# source2=source
# Add circles
circles2 = p.circle('x', 'y',
                  size='size',
                  fill_color='orange',
                  line_color='orange',
                  fill_alpha=1,
                  line_alpha=1,
                  source=source2)

p.circle(x = [-2,-1.4,-0.5,0.9,1,2.3],y = [0,1,2,-1,-2,-0.5], fill_color = 'lime',size = 20)
# Create animation callback
animation = CustomJS(args=dict(source=source, base_sizes=base_sizes), code='''
    let frame = 0;
    const data = source.data;
    const sizes = data['size'];
    
    function animate() {
        // Update sizes with sine wave
        for (let i = 0; i < sizes.length; i++) {
            const baseSize = base_sizes[i];
            sizes[i] = baseSize * (1 + 0.5 * Math.sin(frame + i * 0.5));
        }
        
        // Update frame and data source
        frame += 0.1;
        source.change.emit();
        
        // Request next frame
        setTimeout(animate, 50);
    }
    
    // Start animation
    animate();
''')

# Add plot to document and trigger animation
doc = curdoc()
doc.add_root(p)
doc.js_on_event('document_ready', animation)

# Show the plot
show(p)
save_plot(p, 'scatter_05')