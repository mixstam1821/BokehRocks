from bokeh.plotting import figure, show
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.io import curdoc
from bokeh_rocks import save_plot
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a ColumnDataSource with initial empty data
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create a new plot with a title and axis labels
p = figure(title="Animated Line Plot with Bounce", x_axis_label='x', y_axis_label='y',
           x_range=(0, 10), y_range=(-1.5, 1.5))

# Add a line renderer with legend and gradient effect
line = p.line('x', 'y', source=source, legend_label="sin(x)", 
              line_width=3, line_color='#FF4081')  # Hot pink color for bounce effect
p.legend.click_policy = "hide"

# Create animation callback with bounce easing
animation = CustomJS(args=dict(source=source, x=x.tolist(), y=y.tolist()), code='''
    let counter = 0;
    const step = 2;  // Smaller step for smoother animation
    const total_points = x.length;
    
    function bounceOut(t) {
        const n1 = 7.5625;
        const d1 = 2.75;
        
        if (t < 1 / d1) {
            return n1 * t * t;
        } else if (t < 2 / d1) {
            t -= 1.5 / d1;
            return n1 * t * t + 0.75;
        } else if (t < 2.5 / d1) {
            t -= 2.25 / d1;
            return n1 * t * t + 0.9375;
        } else {
            t -= 2.625 / d1;
            return n1 * t * t + 0.984375;
        }
    }
    
    function frame() {
        if (counter < total_points) {
            const data = source.data;
            
            // Use bounce easing for the counter
            const progress = counter / total_points;
            const bounced_progress = bounceOut(progress);
            const current_length = Math.floor(bounced_progress * total_points);
            
            // Update data with bounced length
            data['x'] = x.slice(0, current_length);
            data['y'] = y.slice(0, current_length);
            source.change.emit();
            
            if (counter < total_points) {
                // Dynamic timing for bounce effect
                const delay = 20 + (10 * Math.sin(progress * Math.PI));  // Faster overall with slight variation
                counter += step;
                setTimeout(frame, delay);
            }
        }
    }
    
    frame();
''')

# Add plot to document and trigger animation
doc = curdoc()
doc.add_root(p)
doc.js_on_event('document_ready', animation)

# Show the plot
show(p)
save_plot(p, 'output/custom_plots_11')