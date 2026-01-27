from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, CustomJS, RangeSlider, CheckboxGroup
from bokeh.layouts import column, row
import numpy as np

# Generate daily business data
days = np.arange(0, 365)
dates = [f"Day {i}" for i in days]

# Simulate business metrics with trends and seasonality
np.random.seed(42)
baseline = 5000
trend = np.linspace(0, 2000, 365)
seasonal = 1000 * np.sin(2 * np.pi * days / 30)  # Monthly seasonality
noise = np.random.normal(0, 300, 365)
daily_revenue = baseline + trend + seasonal + noise

# Calculate moving averages
ma_7 = np.convolve(daily_revenue, np.ones(7)/7, mode='same')
ma_30 = np.convolve(daily_revenue, np.ones(30)/30, mode='same')

# Create data sources
source_main = ColumnDataSource(data=dict(
    x=days,
    y=daily_revenue,
    dates=dates
))

source_ma7 = ColumnDataSource(data=dict(
    x=days,
    y=ma_7
))

source_ma30 = ColumnDataSource(data=dict(
    x=days,
    y=ma_30
))

# Full data for filtering
full_data = ColumnDataSource(data=dict(
    days=days,
    revenue=daily_revenue,
    ma_7=ma_7,
    ma_30=ma_30,
    dates=dates
))

# Create figure
p = figure(height=450, width=1000,
           title="Daily Revenue Analysis with Moving Averages",
           x_axis_label='Day',
           y_axis_label='Revenue ($)',
           toolbar_location='above',
           tools="pan,wheel_zoom,box_zoom,reset,save")

# Add lines
line_main = p.line('x', 'y', source=source_main, line_width=1, 
                    color='#95a5a6', alpha=0.5, legend_label='Daily Revenue')
line_ma7 = p.line('x', 'y', source=source_ma7, line_width=2, 
                   color='#3498db', alpha=0.8, legend_label='7-Day MA', visible=True)
line_ma30 = p.line('x', 'y', source=source_ma30, line_width=2.5, 
                    color='#e74c3c', alpha=0.8, legend_label='30-Day MA', visible=True)

# Configure legend
p.legend.location = "top_left"
p.legend.click_policy = "hide"

# Range slider
range_slider = RangeSlider(start=0, end=364, value=(0, 364), step=1, 
                           title="Date Range (Days)", width=900)

# Checkbox for moving averages
checkbox = CheckboxGroup(labels=["Show 7-Day MA", "Show 30-Day MA"], 
                         active=[0, 1], width=300)

# CustomJS for range slider
slider_callback = CustomJS(args=dict(
    source_main=source_main, 
    source_ma7=source_ma7, 
    source_ma30=source_ma30,
    full_data=full_data,
    fig=p
), code="""
    const [start, end] = cb_obj.value;
    
    // Filter data
    const days = full_data.data['days'];
    const revenue = full_data.data['revenue'];
    const ma7 = full_data.data['ma_7'];
    const ma30 = full_data.data['ma_30'];
    const dates = full_data.data['dates'];
    
    const filtered_x = [];
    const filtered_revenue = [];
    const filtered_ma7 = [];
    const filtered_ma30 = [];
    const filtered_dates = [];
    
    for (let i = 0; i < days.length; i++) {
        if (days[i] >= start && days[i] <= end) {
            filtered_x.push(days[i]);
            filtered_revenue.push(revenue[i]);
            filtered_ma7.push(ma7[i]);
            filtered_ma30.push(ma30[i]);
            filtered_dates.push(dates[i]);
        }
    }
    
    source_main.data = {x: filtered_x, y: filtered_revenue, dates: filtered_dates};
    source_ma7.data = {x: filtered_x, y: filtered_ma7};
    source_ma30.data = {x: filtered_x, y: filtered_ma30};
    
    source_main.change.emit();
    source_ma7.change.emit();
    source_ma30.change.emit();
""")

range_slider.js_on_change('value', slider_callback)

# CustomJS for checkbox
checkbox_callback = CustomJS(args=dict(line_ma7=line_ma7, line_ma30=line_ma30), code="""
    const active = cb_obj.active;
    
    // Show/hide 7-day MA
    line_ma7.visible = active.includes(0);
    
    // Show/hide 30-day MA
    line_ma30.visible = active.includes(1);
""")

checkbox.js_on_change('active', checkbox_callback)

# Layout
controls = row(checkbox)
layout = column(range_slider, controls, p)
output_file("output/interactive_charts_03.html")
save(layout)