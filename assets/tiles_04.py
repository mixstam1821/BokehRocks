from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, Button, Div
from bokeh.layouts import column, row
import xyzservices.providers as xyz
import numpy as np

# Helper function to convert lat/lon to Web Mercator
def lat_lon_to_mercator(lat, lon):
    """Convert latitude/longitude to Web Mercator coordinates"""
    r_major = 6378137.000
    x = r_major * np.radians(lon)
    scale = x / lon
    y = 180.0 / np.pi * np.log(np.tan(np.pi / 4.0 + lat * (np.pi / 180.0) / 2.0)) * scale
    return x, y

# ============================================
# Animated Flight Routes with CustomJS
# ============================================

# Define flight routes (origin -> destination)
routes = [
    {'from': 'New York', 'to': 'Berlin', 'color': '#ff3049', 'from_lat': 40.7128, 'from_lon': -74.0060, 'to_lat': 52.5200, 'to_lon': 13.4050},
    {'from': 'London', 'to': 'Tokyo', 'color': '#00d9ff', 'from_lat': 51.5074, 'from_lon': -0.1278, 'to_lat': 35.6762, 'to_lon': 139.6503},
    {'from': 'Paris', 'to': 'Sydney', 'color': '#a6e22e', 'from_lat': 48.8566, 'from_lon': 2.3522, 'to_lat': -33.8688, 'to_lon': 151.2093},
    {'from': 'Dubai', 'to': 'Los Angeles', 'color': '#ffb028', 'from_lat': 25.2048, 'from_lon': 55.2708, 'to_lat': 34.0522, 'to_lon': -118.2437},
    {'from': 'Singapore', 'to': 'New York', 'color': '#8b5cf6', 'from_lat': 1.3521, 'from_lon': 103.8198, 'to_lat': 40.7128, 'to_lon': -74.0060},
]

# Prepare data for dynamic trail lines
trail_line_sources = []
plane_sources = []

for route in routes:
    # Convert coordinates
    x1, y1 = lat_lon_to_mercator(route['from_lat'], route['from_lon'])
    
    # Create dynamic trail line source (will be updated as plane moves)
    trail_line_source = ColumnDataSource(data=dict(
        x=[],
        y=[]
    ))
    trail_line_sources.append(trail_line_source)
    
    # Create animated plane source (moving point)
    plane_source = ColumnDataSource(data=dict(
        x=[x1],
        y=[y1],
        size=[20]
    ))
    plane_sources.append(plane_source)
    
# Create trail sources for comet tails (glow particles)
trail_sources = []
for route in routes:
    x1, y1 = lat_lon_to_mercator(route['from_lat'], route['from_lon'])
    trail_source = ColumnDataSource(data=dict(
        x=[x1] * 50,  # 50 trail points for longer tail
        y=[y1] * 50,
        alpha=[0.0] * 50,
        size=[1] * 50
    ))
    trail_sources.append(trail_source)

# Create the map figure
p = figure(x_range=(-15000000, 18000000), y_range=(-8000000, 10000000),
           x_axis_type="mercator", y_axis_type="mercator", 
           width=1000, height=600,
           title="Animated Global Flight Routes")
p.add_tile(xyz.CartoDB.DarkMatter)

# Draw the dynamic trail lines (drawn as plane moves)
for i, trail_line_source in enumerate(trail_line_sources):
    # Outer glow line
    p.line('x', 'y', source=trail_line_source, 
           line_color=routes[i]['color'], line_width=6, 
           line_alpha=0.2)
    # Main line
    p.line('x', 'y', source=trail_line_source, 
           line_color=routes[i]['color'], line_width=2, 
           line_alpha=0.6)

# Draw the animated planes (moving points with glow)
plane_glyphs = []
trail_glyphs = []

# First draw particle trails (behind the planes)
for i, trail_source in enumerate(trail_sources):
    trail = p.scatter('x', 'y', source=trail_source,
                     size='size', fill_color=routes[i]['color'],
                     fill_alpha='alpha', line_color=None)
    trail_glyphs.append(trail)

# Then draw planes on top
for i, plane_source in enumerate(plane_sources):
    # Outer glow (largest)
    glow_outer = p.scatter('x', 'y', source=plane_source, 
                          size=35, fill_color=routes[i]['color'], 
                          fill_alpha=0.2, line_color=None)
    # Middle glow
    glow_mid = p.scatter('x', 'y', source=plane_source, 
                        size=20, fill_color=routes[i]['color'], 
                        fill_alpha=0.5, line_color=None)
    # Inner bright point
    plane = p.scatter('x', 'y', source=plane_source, 
                      size=10, fill_color=routes[i]['color'], 
                      fill_alpha=1.0, line_color='white', line_width=2)
    plane_glyphs.append(plane)

# Add city markers
cities = {
    'name': ['New York', 'Berlin', 'London', 'Tokyo', 'Paris', 'Sydney', 'Dubai', 'Los Angeles', 'Singapore'],
    'lat': [40.7128, 52.5200, 51.5074, 35.6762, 48.8566, -33.8688, 25.2048, 34.0522, 1.3521],
    'lon': [-74.0060, 13.4050, -0.1278, 139.6503, 2.3522, 151.2093, 55.2708, -118.2437, 103.8198]
}
x_cities, y_cities = lat_lon_to_mercator(np.array(cities['lat']), np.array(cities['lon']))
city_source = ColumnDataSource(data=dict(x=x_cities, y=y_cities, name=cities['name']))
p.scatter('x', 'y', source=city_source, size=12, 
          fill_color='white', fill_alpha=0.8, line_color='yellow', line_width=2)

p.grid.visible = False

# CustomJS callback for animation
animation_callback = CustomJS(args=dict(
    plane_sources=plane_sources,
    trail_sources=trail_sources,
    trail_line_sources=trail_line_sources,
    routes=routes
), code="""
// Animation state
if (typeof window.animation_state === 'undefined') {
    window.animation_state = {
        progress: routes.map(() => 0),
        speeds: routes.map(() => 0.002 + Math.random() * 0.003),
        active: false,
        trails: routes.map(() => Array(50).fill().map(() => ({x: 0, y: 0}))),
        path_history: routes.map(() => []) // Store path points for the line
    };
}

function animate() {
    if (!window.animation_state.active) return;
    
    // Helper to convert lat/lon to Web Mercator
    function latLonToMercator(lat, lon) {
        const r_major = 6378137.000;
        const x = r_major * (lon * Math.PI / 180.0);
        const scale = x / lon;
        const y = 180.0 / Math.PI * Math.log(Math.tan(Math.PI / 4.0 + lat * (Math.PI / 180.0) / 2.0)) * scale;
        return [x, y];
    }
    
    // Update each plane position
    for (let i = 0; i < routes.length; i++) {
        const route = routes[i];
        const progress = window.animation_state.progress[i];
        const speed = window.animation_state.speeds[i];
        
        // Get start and end coordinates in mercator
        const [x1, y1] = latLonToMercator(route.from_lat, route.from_lon);
        const [x2, y2] = latLonToMercator(route.to_lat, route.to_lon);
        
        // Smooth cubic easing for very smooth movement
        const eased = progress < 0.5 
            ? 4 * progress * progress * progress 
            : 1 - Math.pow(-2 * progress + 2, 3) / 2;
        
        const x = x1 + (x2 - x1) * eased;
        const y = y1 + (y2 - y1) * eased;
        
        // ===== DYNAMIC LINE DRAWING =====
        // Add current position to path history
        window.animation_state.path_history[i].push({x: x, y: y});
        
        // Keep only last 80 points for the trail (adjust for longer/shorter trails)
        const max_trail_length = 80;
        if (window.animation_state.path_history[i].length > max_trail_length) {
            window.animation_state.path_history[i].shift();
        }
        
        // Update the line with current path
        const path_x = window.animation_state.path_history[i].map(p => p.x);
        const path_y = window.animation_state.path_history[i].map(p => p.y);
        
        trail_line_sources[i].data.x = path_x;
        trail_line_sources[i].data.y = path_y;
        trail_line_sources[i].change.emit();
        // ================================
        
        // Update particle trail history (comet tail effect)
        window.animation_state.trails[i].unshift({x: x, y: y});
        window.animation_state.trails[i].pop();
        
        // Update trail visualization
        const trail_x = [];
        const trail_y = [];
        const trail_alpha = [];
        const trail_size = [];
        
        for (let j = 0; j < 50; j++) {
            trail_x.push(window.animation_state.trails[i][j].x);
            trail_y.push(window.animation_state.trails[i][j].y);
            // Fade out towards the tail
            const fade = Math.pow((50 - j) / 50, 2.5);
            trail_alpha.push(fade * 0.8);
            trail_size.push(30 * fade);
        }
        
        trail_sources[i].data.x = trail_x;
        trail_sources[i].data.y = trail_y;
        trail_sources[i].data.alpha = trail_alpha;
        trail_sources[i].data.size = trail_size;
        trail_sources[i].change.emit();
        
        // Update plane position
        plane_sources[i].data.x = [x];
        plane_sources[i].data.y = [y];
        
        // Gentle pulse effect on size
        const pulse = 10 + Math.sin(progress * Math.PI * 8) * 2;
        plane_sources[i].data.size = [pulse];
        
        plane_sources[i].change.emit();
        
        // Update progress
        window.animation_state.progress[i] += speed;
        
        // Reset when complete
        if (window.animation_state.progress[i] > 1) {
            window.animation_state.progress[i] = 0;
            // Clear the path history so line disappears
            window.animation_state.path_history[i] = [];
            // Randomize speed slightly for variation
            window.animation_state.speeds[i] = 0.002 + Math.random() * 0.003;
        }
    }
    
    requestAnimationFrame(animate);
}

// Start animation if not already running
if (!window.animation_state.active) {
    window.animation_state.active = true;
    animate();
}
""")

# Start button to trigger animation
start_button = Button(label="🛫 Start Animation", button_type="success", width=200)
start_button.js_on_click(animation_callback)

# Stop button
stop_callback = CustomJS(code="""
if (typeof window.animation_state !== 'undefined') {
    window.animation_state.active = false;
}
""")
stop_button = Button(label="⏸ Stop Animation", button_type="warning", width=200)
stop_button.js_on_click(stop_callback)

# Reset button
reset_callback = CustomJS(args=dict(plane_sources=plane_sources, trail_sources=trail_sources, trail_line_sources=trail_line_sources, routes=routes), code="""
function latLonToMercator(lat, lon) {
    const r_major = 6378137.000;
    const x = r_major * (lon * Math.PI / 180.0);
    const scale = x / lon;
    const y = 180.0 / Math.PI * Math.log(Math.tan(Math.PI / 4.0 + lat * (Math.PI / 180.0) / 2.0)) * scale;
    return [x, y];
}

for (let i = 0; i < routes.length; i++) {
    const route = routes[i];
    const [x, y] = latLonToMercator(route.from_lat, route.from_lon);
    plane_sources[i].data.x = [x];
    plane_sources[i].data.y = [y];
    plane_sources[i].data.size = [20];
    plane_sources[i].change.emit();
    
    // Reset particle trails
    trail_sources[i].data.x = Array(50).fill(x);
    trail_sources[i].data.y = Array(50).fill(y);
    trail_sources[i].data.alpha = Array(50).fill(0);
    trail_sources[i].data.size = Array(50).fill(1);
    trail_sources[i].change.emit();
    
    // Clear the path lines
    trail_line_sources[i].data.x = [];
    trail_line_sources[i].data.y = [];
    trail_line_sources[i].change.emit();
}

if (typeof window.animation_state !== 'undefined') {
    window.animation_state.progress = routes.map(() => 0);
    window.animation_state.trails = routes.map(() => Array(50).fill().map(() => ({x: 0, y: 0})));
    window.animation_state.path_history = routes.map(() => []);
}
""")
reset_button = Button(label="🔄 Reset", button_type="primary", width=200)
reset_button.js_on_click(reset_callback)



# Layout
controls = row(start_button, stop_button, reset_button)
layout = column(controls, p)

show(layout)