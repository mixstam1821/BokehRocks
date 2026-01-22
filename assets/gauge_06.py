from butils import *



gauge5 = Gauge(
    width=450, height=450,
    title="Vehicle Velocity",
    unit="km/h",
    initial_value=0,
    easing=False,
    theme="dark",
    bg_color="#1A0033",  # Custom purple background
    gauge_bg_color="#2D004D"
)

car_simulation = CustomJS(args=dict(source=gauge5.source), code=f'''
    setTimeout(function() {{
        const start_angle = Math.PI + Math.PI/6;
        const end_angle = -Math.PI/6;
        const total = start_angle - end_angle;
        
        // Get the value range
        const range_min = {gauge5.range_min};
        const range_max = {gauge5.range_max};
        const value_range = range_max - range_min;
        
        function getColor(v) {{
            if (v <= 33.33) return "#00D4FF";
            if (v <= 66.66) return "#FFD700";
            return "#FF3366";
        }}
        
        let velocity = 0;
        let time = 0;
        
        function simulate() {{
            time += 0.05;
            
            if (time < 3) {{
                velocity = 30 * time;
            }}
            else if (time < 6) {{
                velocity = 90;
            }}
            else if (time < 9) {{
                velocity = 90 - 30 * (time - 6);
            }}
            else {{
                velocity = 0;
                time = 0;
            }}
            
            velocity = Math.max(0, Math.min(100, velocity));
            
            // Normalize the value
            const normalized_value = (velocity - range_min) / value_range;
            source.data.angle = [start_angle - normalized_value * total];
            source.data.value_text = [Math.round(velocity).toString()];
            source.data.pointer_color = [getColor(velocity)];
            source.change.emit();
            
            setTimeout(simulate, 50);
        }}
        
        simulate();
    }}, 2000);
''')

doc.js_on_event('document_ready', car_simulation)

doc = curdoc()
layout = row(gauge5.figure)
doc.add_root(layout)
doc.js_on_event('document_ready', car_simulation)
show(gauge5.figure)
save_plot(gauge5.figure, "output/gauge_06")
