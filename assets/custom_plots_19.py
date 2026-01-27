import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import (ColumnDataSource, CustomJS, Button, Slider, Select, Div, WheelZoomTool)
from bokeh.layouts import column, row
from bokeh.palettes import Turbo256, Viridis256, Plasma256, Inferno256, Cividis256
import cartopy.feature as cfeature
from shapely.geometry import LineString, MultiLineString
import json
from bokeh.models import GlobalInlineStyleSheet
from bokeh.io import curdoc
from bokeh.io import show, curdoc
from bokeh.models import Slider, InlineStyleSheet
from bokeh.layouts import column
from matplotlib import cm
from matplotlib.colors import to_hex
from bokeh_rocks import save_plot
#'RdBu_r'
def mbpal(sMpl):
    return [to_hex(cm.get_cmap(sMpl)(i/255)) for i in range(256)]

cool = mbpal('cool')
hot = mbpal('hot')
bwr = mbpal('bwr')
terrain = mbpal('terrain')
curdoc().theme = 'dark_minimal'

slider_style = InlineStyleSheet(css="""
/* Host: set the widget's container background */
:host {
  background: transparent !important;   /* even darker than black for modern dark UI */
  border-radius: 12px !important;
  padding: 12px !important;
  box-shadow: 0 4px 12px #0006 !important;
}
/* Slider title */
:host .bk-slider-title {
  color: #00ffe0 !important;     /* bright cyan for the title */
  font-size: 1.2em !important;
  font-weight: bold !important;
  letter-spacing: 1px !important;
  font-family: 'Fira Code', 'Consolas', 'Menlo', monospace !important;
  margin-bottom: 14px !important;
  text-shadow: 0 2px 12px #00ffe099;
}
/* Track (background) */
:host .noUi-base, :host .noUi-target {
  background: transparent !important;
    border: 1px solid transparent !important;

}
/* Filled portion */
:host .noUi-connect {
  background: linear-gradient(90deg, #00ffe0 10%, #d810f7 90%) !important;
  box-shadow: 0 0 12px #00ffe099;
  border-radius: 12px !important;
}
/* Handle */
:host .noUi-handle {
  background: #343838 !important;
  border: 2px solid #00ffe0 !important;
  border-radius: 50%;
  width: 20px;
  height: 20px;
}
/* Handle hover/focus */
:host .noUi-handle:hover, :host .noUi-handle:focus {
  border-color: #ff2a68 !important;
  box-shadow: 0 0 10px #ff2a6890;
}
/* Tooltip */
:host .noUi-tooltip {
  background: #343838 !important;
  color: #00ffe0 !important;
  font-family: 'Consolas', monospace;
  border-radius: 6px;
  border: 1px solid #00ffe0;
}
""")

select_css = InlineStyleSheet(css="""
/* Widget container */
:host {
    background:transparent !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 24px #0007 !important;
}
/* Title styling */
:host .bk-input-group label, :host .bk-select-title {
    color: #06f0ff !important;
    font-size: 1.18em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 12px !important;
    letter-spacing: 1px !important;
    text-shadow: 0 2px 12px #06f0ff88, 0 1px 6px #111b;
}
/* Dropdown select */
:host select {
    background-color: transparent !important;
    color: #ffdb39 !important;
    border: 2px solid #06b6d4 !important;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}

:host select option {
    background-color: #16161e !important; /* fallback */
    color: #ffdb39 !important;
}
/* Glow effect on hover/focus */
:host select:hover, :host select:focus {
    border-color: #ff3049 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 18px #ff3049cc !important;
    outline: none !important;
}

""")


from bokeh.models import GlobalInlineStyleSheet

def get_starfield_stylesheet():
    return GlobalInlineStyleSheet(css="""
    /* RESET & BASE */
    * { margin: 0; padding:0; box-sizing: border-box; }
    html, body {
        width: 100%;
        height: 100%;
        overflow: hidden;
        position: relative;
        background: radial-gradient(ellipse at bottom, #343838 0%, #130d0d 100%);
    }
    body { background: transparent !important; }

    /* ANIMATED BACKGROUND IMAGE */
    section{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url("https://images.unsplash.com/photo-1528818955841-a7f1425131b5?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c3RhcnJ5JTIwc2t5fGVufDB8fDB8fHww");
        background-size: cover;
        animation: animateBg 50s linear infinite;
        z-index: -3;
    }
    @keyframes animateBg{
        0%,100%{ transform: scale(1); }
        50%{ transform: scale(1.2); }
    }

    /* SMALL STARS (MANY) */
    html::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            radial-gradient(1px 1px at 5% 10%, white, transparent),
            radial-gradient(1px 1px at 15% 80%, white, transparent),
            radial-gradient(1px 1px at 25% 30%, white, transparent),
            radial-gradient(1px 1px at 40% 60%, white, transparent),
            radial-gradient(1px 1px at 55% 20%, white, transparent),
            radial-gradient(1px 1px at 70% 90%, white, transparent),
            radial-gradient(1px 1px at 85% 40%, white, transparent),
            radial-gradient(1px 1px at 95% 70%, white, transparent);
        background-repeat: repeat;
        background-size: 100px 100px;
        animation: twinkleSmall 6s infinite alternate;
        pointer-events: none;
        z-index: -2;
    }

    /* BIGGER STARS (FEWER) */
    html::after {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            radial-gradient(2px 2px at 20% 40%, white, transparent),
            radial-gradient(2.5px 2.5px at 60% 70%, white, transparent),
            radial-gradient(3px 3px at 80% 20%, white, transparent);
        background-repeat: repeat;
        background-size: 200px 200px;
        animation: twinkleBig 10s infinite alternate;
        pointer-events: none;
        z-index: -2;
    }

    /* SHOOTING STAR */
    span {
        position: absolute;
        top:50%;
        left:50%;
        width: 4px;
        height: 4px;
        background: yellow;
        border-radius: 50%;
        box-shadow: 0 0 0 4px rgba(242, 255, 59, 0.1).1), 0 0 0 8px rgba(251, 255, 25, 0.1), 0 0 20px rgba(255,255,255,0.1);
        animation: shooting 45s linear infinite;
        pointer-events: none;
        z-index: -2;
    }
                                  
                                  
    span::before{
        content:'';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 300px;
        height: 1px;
        background: linear-gradient(90deg,yellow,transparent);
    }
@keyframes shooting {
    0% {
        transform: rotate(315deg) translateX(0);
        opacity: 0;
    }

    1% {
        opacity: 1;
    }

    /* FAST shooting (first ~1 second) */
    3% {
        transform: rotate(315deg) translateX(-1000px);
        opacity: 0;
    }

    /* WAIT (invisible) */
    100% {
        transform: rotate(315deg) translateX(-1000px);
        opacity: 0;
    }
}


span:nth-child(1){
    top: 300px; background: aqua;
    right: 900px;
    left: initial;
   animation: shooting 60s linear infinite;
}
                                  
span:nth-of-type(1)::before {
    background: linear-gradient(90deg, aqua, transparent);}
                                  
span:nth-child(2){
    top: 0px; background: red;
    right: 800px;
    left: initial;animation-duration: 11.75s;
animation: shooting 211s linear infinite;
}

span:nth-of-type(2)::before {
    background: linear-gradient(90deg, red, transparent);}
                                  
span:nth-child(3){
    top: 0px; background: lime;
    right: 1450px;
    left: initial;
                                  animation: shooting 130s linear infinite;
}
span:nth-of-type(3)::before {
    background: linear-gradient(90deg, lime, transparent);}
    /* SMALL STAR TWINKLE */
    @keyframes twinkleSmall { from { opacity: 0.3; } to { opacity: 0.9; } }
    @keyframes twinkleBig   { from { opacity: 0.2; } to { opacity: 0.7; } }

    /* Bokeh above all stars */
    .bk-root {
        position: relative;
        z-index: 1;
        background: transparent !important;
    }

    /* UI text */
    .bk, .bk-input, .bk-btn, .bk-select, .bk-slider-title,
    .bk-title, .bk-label, .bk-legend, .bk-axis-label {
        color: white !important;
    }
    """)

# ============================================================================
# 1. GENERATE SPHERE GEOMETRY
# ============================================================================

def generate_sphere_mesh(n_lat=40, n_lon=80):
    lats = np.linspace(-90, 90, n_lat)
    lons = np.linspace(-180, 180, n_lon)
    lon_grid, lat_grid = np.meshgrid(lons, lats)
    
    return {
        'lons': lon_grid.flatten().tolist(),
        'lats': lat_grid.flatten().tolist(),
        'n_lat': n_lat,
        'n_lon': n_lon
    }

# ============================================================================
# 2. GENERATE TEMPERATURE DATA
# ============================================================================

def generate_temperature_field(lats, lons):
    lats = np.array(lats)
    lons = np.array(lons)
    
    base_temp = 30 - 50 * np.abs(lats) / 90
    wave1 = 10 * np.sin(np.radians(lons) * 3) * np.cos(np.radians(lats) * 2)
    wave2 = 8 * np.cos(np.radians(lons) * 2 + np.radians(lats))
    
    np.random.seed(42)
    noise = np.random.randn(len(lats)) * 3
    
    temps = base_temp + wave1 + wave2 + noise
    return temps.tolist()

# ============================================================================
# 3. EXTRACT COASTLINES
# ============================================================================

def extract_coastlines():
    coastlines = cfeature.NaturalEarthFeature('physical', 'coastline', '110m')
    
    coast_lons = []
    coast_lats = []
    
    for geom in coastlines.geometries():
        if isinstance(geom, LineString):
            coords = np.array(geom.coords)
            coast_lons.extend(coords[:, 0].tolist() + [None])
            coast_lats.extend(coords[:, 1].tolist() + [None])
        elif isinstance(geom, MultiLineString):
            for line in geom.geoms:
                coords = np.array(line.coords)
                coast_lons.extend(coords[:, 0].tolist() + [None])
                coast_lats.extend(coords[:, 1].tolist() + [None])
    
    return coast_lons, coast_lats

# ============================================================================
# 4. PREPARE DATA
# ============================================================================

sphere_data = generate_sphere_mesh(n_lat=30, n_lon=60)
temps = generate_temperature_field(sphere_data['lats'], sphere_data['lons'])
coast_lons, coast_lats = extract_coastlines()


raw_sphere_source = ColumnDataSource(data={
    'lons': sphere_data['lons'],
    'lats': sphere_data['lats'],
    'temps': temps
})

quad_source = ColumnDataSource(data={
    'xs': [[]],
    'ys': [[]],
    'fill_color': ['#440154']
})

coast_raw_source = ColumnDataSource(data={
    'lons': coast_lons,
    'lats': coast_lats
})

coast_render_source = ColumnDataSource(data={
    'x': [],
    'y': []
})
# Flight arc lines source
arc_render_source = ColumnDataSource(data={
    'x': [],
    'y': []
})

# Stable lines North America to South Africa
stable_lines_source = ColumnDataSource(data={
    'x': [],
    'y': []
})

# Cyan stable lines with moving points
cyan_lines_source = ColumnDataSource(data={
    'x': [],
    'y': []
})

# Moving points on cyan lines
moving_points_source = ColumnDataSource(data={
    'x': [],
    'y': [],
    'size': []
})

# 3D bars source
bars_source = ColumnDataSource(data={
    'xs': [],
    'ys': [],
    'fill_color': []
})
# ============================================================================
# 5. CREATE FIGURE
# ============================================================================

plot = figure(
    width=800, height=800,
    # title="🌍 Auto-Rotating Temperature Globe",
    toolbar_location=None,
    match_aspect=True,
    x_range=(-1.5, 1.5),
    y_range=(-1.5, 1.5), 
)
plot.toolbar.active_scroll = plot.select_one(WheelZoomTool)

plot.patches(
    xs='xs', ys='ys',
    source=quad_source,
    fill_color='fill_color',
    fill_alpha=1,
    line_color='fill_color',
    line_alpha = 1,
    line_width=1.1,


)

plot.multi_line(
    xs='x', ys='y',
    source=coast_render_source,
    line_color='black',
    line_width=1.2,
    line_alpha=1
)
# Add flight arcs
plot.multi_line(
    xs='x', ys='y',
    source=arc_render_source,
    line_color='#00ff00',
    line_width=2.5,
    line_alpha=0.8
)



# Add stable yellow lines
plot.multi_line(
    xs='x', ys='y',
    source=stable_lines_source,
    line_color='#ffff00',
    line_width=2,
    line_alpha=0.7
)

# Add stable cyan lines
plot.multi_line(
    xs='x', ys='y',
    source=cyan_lines_source,
    line_color='#00ffff',
    line_width=2,
    line_alpha=0.6
)

# Add moving blur points
plot.circle(
    x='x', y='y',
    source=moving_points_source,
    size='size',
    color='#00ffff',
    alpha=0.8,
    line_color='#ffffff',
    line_width=1
)
# Add 3D bars
plot.patches(
    xs='xs', ys='ys',
    source=bars_source,
    fill_color='fill_color',
    fill_alpha=0.8,
    line_color='white',
    line_width=1,
    line_alpha=0.6
)
plot.xaxis.visible = False
plot.yaxis.visible = False
plot.grid.visible = False
plot.background_fill_color = "#0a0a0a"
plot.border_fill_color = "#0a0a0a"
plot.background_fill_alpha = 0
plot.border_fill_alpha = 0
plot.border_line_alpha = 0
plot.outline_line_color = None

# ============================================================================
# 6. CONTROLS
# ============================================================================

play_button = Button(label="⏸ Pause", button_type="warning", width=100)
reset_button = Button(label="🔄 Reset", button_type="primary", width=100)

speed_slider = Slider(
    start=0, end=3, value=1, step=0.1,
    title="Rotation Speed",
    width=250, stylesheets=[slider_style],height=80, styles={"margin-top": "-70px"}
)

tilt_slider = Slider(
    start=-90, end=90, value=0, step=5,
    title="Elevation (°)",
    width=250, stylesheets=[slider_style],height=80, styles={"margin-top": "10px"}
)

azimuth_slider = Slider(
    start=-180, end=180, value=0, step=10,
    title="Azimuth (°)",
    width=250, stylesheets=[slider_style],height=80, styles={"margin-top": "10px"}
)

palette_select = Select(
    title="Color Palette:",
    value="Turbo256",
    width=180,
    options=["Turbo256", "Viridis256", "Plasma256", "Inferno256", "Cividis256","cool", "hot", "bwr", "terrain"], stylesheets=[select_css],height=80, styles={"margin-top": "-70px"}
)

angle_display = Div(
    text="<div style='padding:10px; background:#1a1a1a; color:#00ff00; "
         "font-family:monospace; border-radius:5px; text-align:center;'>"
         "<b>Rotation:</b> 180° | <b>Tilt:</b> 0° | <b>Az:</b> 0° | "
         "<span style='color:#ff6b35;'>⚡ PLAYING</span></div>",
    width=350
)


# ============================================================================
# 7. MAIN RENDERING AND ANIMATION CALLBACK
# ============================================================================

combined_callback = CustomJS(
    args=dict(
        raw_sphere=raw_sphere_source,
        quad_source=quad_source,
        coast_raw=coast_raw_source,
        coast_render=coast_render_source,        arc_render=arc_render_source,  
        stable_lines=stable_lines_source,  
        cyan_lines=cyan_lines_source,      
        moving_points=moving_points_source, bars_source=bars_source,
        n_lat=sphere_data['n_lat'],
        n_lon=sphere_data['n_lon'],
        palette_turbo=json.dumps(Turbo256),
        palette_viridis=json.dumps(Viridis256),
        palette_plasma=json.dumps(Plasma256),
        palette_inferno=json.dumps(Inferno256),
        palette_cividis=json.dumps(Cividis256),
        palette_cool=json.dumps(cool),
        palette_hot=json.dumps(hot),
        palette_bwr=json.dumps(bwr),
        palette_terrain=json.dumps(terrain),

        palette_select=palette_select,
        angle_display=angle_display,
        speed_slider=speed_slider,
        tilt_slider=tilt_slider,
        azimuth_slider=azimuth_slider,
        play_button=play_button,
        reset_button=reset_button
    ),
    code="""
    // ========================================================================
    // INITIALIZE ANIMATION STATE (runs once)
    // ========================================================================
    if (!window.globe_animation) {
        window.globe_animation = {
            is_playing: true,
            current_angle: 180,
            animation_id: null,
            initialized: false
        };
    }
    
    const anim = window.globe_animation;
    
    // ========================================================================
    // RENDER FUNCTION - Projects and draws the globe
    // ========================================================================
    function renderGlobe(angle_deg) {
        const angle_rad = -angle_deg * Math.PI / 180;  // REVERSED ROTATION!
        const tilt_rad = tilt_slider.value * Math.PI / 180;
        const azimuth_rad = azimuth_slider.value * Math.PI / 180;
        
        // Get palette
        const palettes = {
            'Turbo256': JSON.parse(palette_turbo),
            'Viridis256': JSON.parse(palette_viridis),
            'Plasma256': JSON.parse(palette_plasma),
            'Inferno256': JSON.parse(palette_inferno),
            'Cividis256': JSON.parse(palette_cividis),
            'cool': JSON.parse(palette_cool),
            'hot': JSON.parse(palette_hot),
            'bwr': JSON.parse(palette_bwr),

            'terrain': JSON.parse(palette_terrain)
        };
        const palette = palettes[palette_select.value];
        
        // Update angle display with status
        const status = anim.is_playing ? 
            '<span style="color:#ff6b35;">⚡ PLAYING</span>' : 
            '<span style="color:#888;">⏸ PAUSED</span>';
        angle_display.text = `<div style='padding:10px; background:#1a1a1a; color:#00ff00; 
                              font-family:monospace; border-radius:5px; text-align:center;'>
                              <b>Rot:</b> ${Math.round(angle_deg)}° | <b>Tilt:</b> ${tilt_slider.value}° | 
                              <b>Az:</b> ${azimuth_slider.value}° | ${status}</div>`;
        
        // Get data
        const lons = raw_sphere.data['lons'];
        const lats = raw_sphere.data['lats'];
        const temps = raw_sphere.data['temps'];
        
        // Project sphere points with full 3D rotation
        const x2d = new Array(lons.length);
        const y2d = new Array(lons.length);
        const y3d = new Array(lons.length);
        const visible = new Array(lons.length);
        
        const cos_angle = Math.cos(angle_rad);
        const sin_angle = Math.sin(angle_rad);
        const cos_tilt = Math.cos(tilt_rad);
        const sin_tilt = Math.sin(tilt_rad);
        const cos_azimuth = Math.cos(azimuth_rad);
        const sin_azimuth = Math.sin(azimuth_rad);
        
        for (let i = 0; i < lons.length; i++) {
            const lat_rad = lats[i] * Math.PI / 180;
            const lon_rad = lons[i] * Math.PI / 180;
            
            const x = Math.cos(lat_rad) * Math.cos(-lon_rad);
            const y = Math.cos(lat_rad) * Math.sin(-lon_rad);
            const z = Math.sin(lat_rad);
            
            // Rotation around Z-axis (spin) - REVERSED
            let x_rot = x * cos_angle - y * sin_angle;
            let y_rot = x * sin_angle + y * cos_angle;
            let z_rot = z;
            
            // Tilt around X-axis (elevation)
            const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
            const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
            
            // Azimuth rotation around Z-axis (viewing angle)
            const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
            const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
            const z_final = z_tilt;
            
            x2d[i] = x_final;
            y2d[i] = z_final;
            y3d[i] = y_final;
            visible[i] = y_final > -0.15;
        }
        
        // Create quads
        const temp_min = Math.min(...temps);
        const temp_max = Math.max(...temps);
        const quads = [];
        
        for (let i = 0; i < n_lat - 1; i++) {
            for (let j = 0; j < n_lon - 1; j++) {
                const idx0 = i * n_lon + j;
                const idx1 = i * n_lon + (j + 1);
                const idx2 = (i + 1) * n_lon + (j + 1);
                const idx3 = (i + 1) * n_lon + j;
                
                if (visible[idx0] || visible[idx1] || visible[idx2] || visible[idx3]) {
                    const xs = [x2d[idx0], x2d[idx1], x2d[idx2], x2d[idx3]];
                    const ys = [y2d[idx0], y2d[idx1], y2d[idx2], y2d[idx3]];
                    
                    const avg_temp = (temps[idx0] + temps[idx1] + temps[idx2] + temps[idx3]) / 4;
                    const depth = (y3d[idx0] + y3d[idx1] + y3d[idx2] + y3d[idx3]) / 4;
                    
                    let color_idx = 0;
                    if (temp_max > temp_min) {
                        color_idx = Math.floor((avg_temp - temp_min) / (temp_max - temp_min) * 255);
                        color_idx = Math.max(0, Math.min(255, color_idx));
                    }
                    
                    quads.push({
                        depth: depth,
                        xs: xs,
                        ys: ys,
                        color: palette[color_idx]
                    });
                }
            }
        }
        
        quads.sort((a, b) => a.depth - b.depth);
        
        quad_source.data['xs'] = quads.map(q => q.xs);
        quad_source.data['ys'] = quads.map(q => q.ys);
        quad_source.data['fill_color'] = quads.map(q => q.color);
        
        // Render coastlines - HIDE THOSE BEHIND THE SPHERE!
        const coast_lons = coast_raw.data['lons'];
        const coast_lats = coast_raw.data['lats'];
        
        const coast_x_all = [];
        const coast_y_all = [];
        let current_line_x = [];
        let current_line_y = [];
        
        for (let i = 0; i < coast_lons.length; i++) {
            if (coast_lons[i] === null || coast_lats[i] === null) {
                if (current_line_x.length > 0) {
                    coast_x_all.push(current_line_x);
                    coast_y_all.push(current_line_y);
                    current_line_x = [];
                    current_line_y = [];
                }
            } else {
                const lat_rad = coast_lats[i] * Math.PI / 180;
                const lon_rad = coast_lons[i] * Math.PI / 180;
                
                const x = Math.cos(lat_rad) * Math.cos(-lon_rad);
                const y = Math.cos(lat_rad) * Math.sin(-lon_rad);
                const z = Math.sin(lat_rad);
                
                // Rotation around Z-axis - REVERSED
                let x_rot = x * cos_angle - y * sin_angle;
                let y_rot = x * sin_angle + y * cos_angle;
                let z_rot = z;
                
                // Tilt around X-axis
                const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
                const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
                
                // Azimuth rotation
                const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
                const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
                const z_final = z_tilt;
                
                // ONLY draw visible coastlines (front of sphere)
                if (y_final > -0.05) {
                    current_line_x.push(x_final);
                    current_line_y.push(z_final);
                } else if (current_line_x.length > 0) {
                    // Break line when going behind
                    coast_x_all.push(current_line_x);
                    coast_y_all.push(current_line_y);
                    current_line_x = [];
                    current_line_y = [];
                }
            }
        }
        
        if (current_line_x.length > 0) {
            coast_x_all.push(current_line_x);
            coast_y_all.push(current_line_y);
        }
        
        coast_render.data['x'] = coast_x_all;
        coast_render.data['y'] = coast_y_all;
        // Define 4 different flight paths
        const flight_paths = [
            {from_lat: 48.8566, from_lon: 2.3522, to_lat: -23.5505, to_lon: -46.6333, color: '#00ff00'},  // Paris to São Paulo
            {from_lat: 51.5074, from_lon: -0.1278, to_lat: -22.9068, to_lon: -43.1729, color: '#ff00ff'},  // London to Rio
            {from_lat: 41.9028, from_lon: 12.4964, to_lat: -15.7942, to_lon: -47.8822, color: '#00ffff'},  // Rome to Brasília
            {from_lat: 40.4168, from_lon: -3.7038, to_lat: -25.4284, to_lon: -49.2733, color: '#ffff00'}   // Madrid to Curitiba
        ];
        
        const arc_x_all = [];
        const arc_y_all = [];
        
        for (const path of flight_paths) {
            const arc_points = 80; // Number of points along the arc
            const arc_x = [];
            const arc_y = [];
            
            for (let i = 0; i <= arc_points; i++) {
                const t = i / arc_points;
                
                // Interpolate lat/lon
                const lat = path.from_lat + t * (path.to_lat - path.from_lat);
                const lon = path.from_lon + t * (path.to_lon - path.from_lon);
                
                // Arc height (peaks at middle of journey)
                const arc_height = 1 + 0.4 * Math.sin(t * Math.PI);
                
                const lat_rad = lat * Math.PI / 180;
                const lon_rad = lon * Math.PI / 180;
                
                const x = arc_height * Math.cos(lat_rad) * Math.cos(-lon_rad);
                const y = arc_height * Math.cos(lat_rad) * Math.sin(-lon_rad);
                const z = arc_height * Math.sin(lat_rad);
                
                // Apply same rotations as globe
                let x_rot = x * cos_angle - y * sin_angle;
                let y_rot = x * sin_angle + y * cos_angle;
                let z_rot = z;
                
                const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
                const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
                
                const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
                const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
                const z_final = z_tilt;
                
                // Only draw visible parts
                if (y_final > -0.1) {
                    arc_x.push(x_final);
                    arc_y.push(z_final);
                } else if (arc_x.length > 0) {
                    // Break arc when going behind
                    arc_x_all.push(arc_x.slice());
                    arc_y_all.push(arc_y.slice());
                    arc_x.length = 0;
                    arc_y.length = 0;
                }
            }
            
            if (arc_x.length > 0) {
                arc_x_all.push(arc_x);
                arc_y_all.push(arc_y);
            }
        }
        
        arc_render.data['x'] = arc_x_all;
        arc_render.data['y'] = arc_y_all;




        // ========================================================================
        // RENDER STABLE YELLOW LINES - North America to South Africa
        // ========================================================================
        
        const stable_paths = [
            {from_lat: 40.7128, from_lon: -74.0060, to_lat: -33.9249, to_lon: 18.4241},  // NYC to Cape Town
            {from_lat: 34.0522, from_lon: -118.2437, to_lat: -26.2041, to_lon: 28.0473}, // LA to Johannesburg
            {from_lat: 41.8781, from_lon: -87.6298, to_lat: -29.8587, to_lon: 31.0218}   // Chicago to Durban
        ];
        
        const stable_x_all = [];
        const stable_y_all = [];
        
        for (const path of stable_paths) {
            const arc_points = 80;
            const arc_x = [];
            const arc_y = [];
            
            for (let i = 0; i <= arc_points; i++) {
                const t = i / arc_points;
                
                const lat = path.from_lat + t * (path.to_lat - path.from_lat);
                const lon = path.from_lon + t * (path.to_lon - path.from_lon);
                
                const arc_height = 1 + 0.35 * Math.sin(t * Math.PI);
                
                const lat_rad = lat * Math.PI / 180;
                const lon_rad = lon * Math.PI / 180;
                
                const x = arc_height * Math.cos(lat_rad) * Math.cos(-lon_rad);
                const y = arc_height * Math.cos(lat_rad) * Math.sin(-lon_rad);
                const z = arc_height * Math.sin(lat_rad);
                
                let x_rot = x * cos_angle - y * sin_angle;
                let y_rot = x * sin_angle + y * cos_angle;
                let z_rot = z;
                
                const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
                const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
                
                const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
                const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
                const z_final = z_tilt;
                
                if (y_final > -0.1) {
                    arc_x.push(x_final);
                    arc_y.push(z_final);
                } else if (arc_x.length > 0) {
                    stable_x_all.push(arc_x.slice());
                    stable_y_all.push(arc_y.slice());
                    arc_x.length = 0;
                    arc_y.length = 0;
                }
            }
            
            if (arc_x.length > 0) {
                stable_x_all.push(arc_x);
                stable_y_all.push(arc_y);
            }
        }
        
        stable_lines.data['x'] = stable_x_all;
        stable_lines.data['y'] = stable_y_all;
        
        // ========================================================================
        // RENDER CYAN LINES WITH MOVING POINTS - Asia to Australia
        // ========================================================================
        
        // Initialize animation time if needed
        if (!window.point_animation_time) {
            window.point_animation_time = 0;
        }
        window.point_animation_time += 0.02;
        
        const cyan_paths = [
            {from_lat: 35.6762, from_lon: 139.6503, to_lat: -33.8688, to_lon: 151.2093}, // Tokyo to Sydney
            {from_lat: 22.3193, from_lon: 114.1694, to_lat: -37.8136, to_lon: 144.9631}, // Hong Kong to Melbourne
            {from_lat: 1.3521, from_lon: 103.8198, to_lat: -31.9505, to_lon: 115.8605}   // Singapore to Perth
        ];
        
        const cyan_x_all = [];
        const cyan_y_all = [];
        const point_x = [];
        const point_y = [];
        const point_size = [];
        
        for (let path_idx = 0; path_idx < cyan_paths.length; path_idx++) {
            const path = cyan_paths[path_idx];
            const arc_points = 80;
            const arc_x = [];
            const arc_y = [];
            const all_points_3d = []; // Store all points for moving dot
            
            for (let i = 0; i <= arc_points; i++) {
                const t = i / arc_points;
                
                const lat = path.from_lat + t * (path.to_lat - path.from_lat);
                const lon = path.from_lon + t * (path.to_lon - path.from_lon);
                
                const arc_height = 1 + 0.4 * Math.sin(t * Math.PI);
                
                const lat_rad = lat * Math.PI / 180;
                const lon_rad = lon * Math.PI / 180;
                
                const x = arc_height * Math.cos(lat_rad) * Math.cos(-lon_rad);
                const y = arc_height * Math.cos(lat_rad) * Math.sin(-lon_rad);
                const z = arc_height * Math.sin(lat_rad);
                
                let x_rot = x * cos_angle - y * sin_angle;
                let y_rot = x * sin_angle + y * cos_angle;
                let z_rot = z;
                
                const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
                const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
                
                const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
                const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
                const z_final = z_tilt;
                
                all_points_3d.push({x: x_final, y: z_final, visible: y_final > -0.1});
                
                if (y_final > -0.1) {
                    arc_x.push(x_final);
                    arc_y.push(z_final);
                } else if (arc_x.length > 0) {
                    cyan_x_all.push(arc_x.slice());
                    cyan_y_all.push(arc_y.slice());
                    arc_x.length = 0;
                    arc_y.length = 0;
                }
            }
            
            if (arc_x.length > 0) {
                cyan_x_all.push(arc_x);
                cyan_y_all.push(arc_y);
            }
            
            // Calculate moving point position (different phase for each line)
            const point_progress = (window.point_animation_time + path_idx * 0.33) % 1.0;
            const point_idx = Math.floor(point_progress * arc_points);
            
            if (point_idx < all_points_3d.length && all_points_3d[point_idx].visible) {
                point_x.push(all_points_3d[point_idx].x);
                point_y.push(all_points_3d[point_idx].y);
                point_size.push(15); // Blur effect size
            }
        }
        
        cyan_lines.data['x'] = cyan_x_all;
        cyan_lines.data['y'] = cyan_y_all;
        moving_points.data['x'] = point_x;
        moving_points.data['y'] = point_y;
        moving_points.data['size'] = point_size;






        // ========================================================================
        // RENDER 3D BARS - Cities with bar heights
        // ========================================================================
        
        const bar_cities = [
            // Americas
            {lat: 40.7128, lon: -74.0060, height: 0.30, color: '#ff3049'}, // New York
            {lat: 34.0522, lon: -118.2437, height: 0.18, color: '#ff7a18'}, // Los Angeles
            {lat: 41.8781, lon: -87.6298, height: 0.22, color: '#00e5ff'}, // Chicago
            {lat: -23.5505, lon: -46.6333, height: 0.26, color: '#00ffff'}, // São Paulo
            {lat: -34.6037, lon: -58.3816, height: 0.20, color: '#a3e635'}, // Buenos Aires
            {lat: 19.4326, lon: -99.1332, height: 0.24, color: '#facc15'}, // Mexico City
        
            // Europe
            {lat: 51.5074, lon: -0.1278, height: 0.25, color: '#00d9ff'}, // London
            {lat: 48.8566, lon: 2.3522, height: 0.28, color: '#8b5cf6'},  // Paris
            {lat: 52.5200, lon: 13.4050, height: 0.21, color: '#22c55e'}, // Berlin
            {lat: 41.9028, lon: 12.4964, height: 0.19, color: '#fb7185'}, // Rome
            {lat: 55.7558, lon: 37.6173, height: 0.22, color: '#ff00ff'}, // Moscow
            {lat: 40.4168, lon: -3.7038, height: 0.17, color: '#38bdf8'}, // Madrid
        
            // Asia
            {lat: 35.6762, lon: 139.6503, height: 0.35, color: '#a6e22e'}, // Tokyo
            {lat: 31.2304, lon: 121.4737, height: 0.33, color: '#f97316'}, // Shanghai
            {lat: 28.6139, lon: 77.2090, height: 0.29, color: '#fde047'}, // Delhi
            {lat: 1.3521, lon: 103.8198, height: 0.24, color: '#ffff00'}, // Singapore
            {lat: 37.5665, lon: 126.9780, height: 0.27, color: '#60a5fa'}, // Seoul
            {lat: 13.7563, lon: 100.5018, height: 0.23, color: '#34d399'}, // Bangkok
        
            // Africa & Middle East
            {lat: 30.0444, lon: 31.2357, height: 0.20, color: '#eab308'}, // Cairo
            {lat: -26.2041, lon: 28.0473, height: 0.16, color: '#fb923c'}, // Johannesburg
            {lat: 25.2048, lon: 55.2708, height: 0.31, color: '#c084fc'}, // Dubai
        
            // Oceania
            {lat: -33.8688, lon: 151.2093, height: 0.20, color: '#ffb028'}, // Sydney
            {lat: -37.8136, lon: 144.9631, height: 0.17, color: '#4ade80'}, // Melbourne
        ];
        
        
        const bar_xs = [];
        const bar_ys = [];
        const bar_colors = [];
        
        for (const city of bar_cities) {
            const lat_rad = city.lat * Math.PI / 180;
            const lon_rad = city.lon * Math.PI / 180;
            
            // Base of bar (on sphere surface)
            const x_base = Math.cos(lat_rad) * Math.cos(-lon_rad);
            const y_base = Math.cos(lat_rad) * Math.sin(-lon_rad);
            const z_base = Math.sin(lat_rad);
            
            // Top of bar (extended outward)
            const bar_radius = 1 + city.height;
            const x_top = bar_radius * Math.cos(lat_rad) * Math.cos(-lon_rad);
            const y_top = bar_radius * Math.cos(lat_rad) * Math.sin(-lon_rad);
            const z_top = bar_radius * Math.sin(lat_rad);
            
            // Create bar as a rectangle (4 corners)
            const bar_width = 0.08; // Width of the bar
            
            // Calculate perpendicular vectors for bar width
            const dx = -Math.sin(-lon_rad) * bar_width / 2;
            const dy = Math.cos(-lon_rad) * bar_width / 2;
            
            // Four corners of the bar (base and top)
            const corners_base = [
                {x: x_base - dx, y: y_base - dy, z: z_base},
                {x: x_base + dx, y: y_base + dy, z: z_base}
            ];
            
            const corners_top = [
                {x: x_top - dx, y: y_top - dy, z: z_top},
                {x: x_top + dx, y: y_top + dy, z: z_top}
            ];
            
            // Apply rotations to all corners
            const rotated_corners = [];
            for (const corner of [...corners_base, ...corners_top]) {
                // Rotation around Z-axis
                let x_rot = corner.x * cos_angle - corner.y * sin_angle;
                let y_rot = corner.x * sin_angle + corner.y * cos_angle;
                let z_rot = corner.z;
                
                // Tilt around X-axis
                const y_tilt = y_rot * cos_tilt - z_rot * sin_tilt;
                const z_tilt = y_rot * sin_tilt + z_rot * cos_tilt;
                
                // Azimuth rotation
                const x_final = x_rot * cos_azimuth - y_tilt * sin_azimuth;
                const y_final = x_rot * sin_azimuth + y_tilt * cos_azimuth;
                const z_final = z_tilt;
                
                rotated_corners.push({x: x_final, y: y_final, z: z_final});
            }
            
            // Check if bar is visible (at least one corner visible)
            const is_visible = rotated_corners.some(c => c.y > -0.1);
            
            if (is_visible) {
                // Create bar as a polygon (rectangle)
                const bar_x = [
                    rotated_corners[0].x,  // base left
                    rotated_corners[1].x,  // base right
                    rotated_corners[3].x,  // top right
                    rotated_corners[2].x   // top left
                ];
                
                const bar_y = [
                    rotated_corners[0].z,
                    rotated_corners[1].z,
                    rotated_corners[3].z,
                    rotated_corners[2].z
                ];
                
                bar_xs.push(bar_x);
                bar_ys.push(bar_y);
                bar_colors.push(city.color);
            }
        }
        
        bars_source.data['xs'] = bar_xs;
        bars_source.data['ys'] = bar_ys;
        bars_source.data['fill_color'] = bar_colors;








        quad_source.change.emit();
        coast_render.change.emit();
        arc_render.change.emit();  
        stable_lines.change.emit();  
        cyan_lines.change.emit();    
        moving_points.change.emit();  
        bars_source.change.emit();

    }
    
    // ========================================================================
    // ANIMATION LOOP - Called every frame
    // ========================================================================
    function animate() {
        if (!anim.is_playing) return;
        
        anim.current_angle += speed_slider.value * 0.5;
        if (anim.current_angle >= 360) {
            anim.current_angle -= 360;
        }
        
        renderGlobe(anim.current_angle);
        anim.animation_id = requestAnimationFrame(animate);
    }
    
    // ========================================================================
    // HANDLE INTERACTIONS - SIMPLIFIED LOGIC
    // ========================================================================
    
    // Check which button was clicked
    const is_play_click = (cb_obj.id === play_button.id);
    const is_reset_click = (cb_obj.id === reset_button.id);
    
    if (is_play_click) {
        // Toggle play/pause
        anim.is_playing = !anim.is_playing;
        
        if (anim.is_playing) {
            play_button.label = '⏸ Pause';
            play_button.button_type = 'warning';
            animate();
        } else {
            if (anim.animation_id) {
                cancelAnimationFrame(anim.animation_id);
            }
            play_button.label = '▶ Play';
            play_button.button_type = 'success';
        }
        renderGlobe(anim.current_angle);
    } 
    
    if (is_reset_click) {
        anim.current_angle = 180;
        tilt_slider.value = 0;
        azimuth_slider.value = 0;
        renderGlobe(180);
    }
    
    // Handle slider changes
    if (cb_obj === palette_select || cb_obj === tilt_slider || cb_obj === azimuth_slider) {
        renderGlobe(anim.current_angle);
    }
    
    // ========================================================================
    // INITIAL RENDER AND AUTO-START
    // ========================================================================
    if (!anim.initialized) {
        anim.initialized = true;
        renderGlobe(180);
        
        // Auto-start animation after initial render
        setTimeout(function() {
            anim.is_playing = true;
            animate();
        }, 100);
    }
    """
)


# Attach callbacks - CHANGED TO ON_EVENT FOR BUTTONS
play_button.js_on_event('button_click', combined_callback)
reset_button.js_on_event('button_click', combined_callback)
palette_select.js_on_change('value', combined_callback)
tilt_slider.js_on_change('value', combined_callback)
azimuth_slider.js_on_change('value', combined_callback)



# ============================================================================
# 8. LAYOUT
# ============================================================================

controls_row1 = row(   
    # play_button,
    # reset_button,
    speed_slider,
    palette_select,
)

controls_row2 = row(
    tilt_slider,
    azimuth_slider
)

layout = column(
    plot,
    controls_row1,
    controls_row2, stylesheets=[get_starfield_stylesheet()]
)

shooting_stars_js = """
(function() {
    if (window.starsLoaded) return;
    window.starsLoaded = true;

    const section = document.createElement("section");
    document.body.appendChild(section);

    // Create 10 shooting stars
    for (let i = 0; i < 10; i++) {
        const star = document.createElement("span");
        section.appendChild(star);
    }
})();
"""

from bokeh.models import CustomJS
from bokeh.events import DocumentReady
curdoc().js_on_event(DocumentReady, CustomJS(code=shooting_stars_js))
# curdoc().js_on_event('document_ready', combined_callback)
show(layout)
save_plot(layout, 'output/custom_plots_19')