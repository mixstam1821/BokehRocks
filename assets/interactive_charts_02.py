from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select
from bokeh.layouts import column

# Sample business data - different metrics over time
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

data = {
    'Revenue': {
        'x': list(range(len(months))),
        'y': [120, 135, 142, 155, 168, 175, 182, 190, 195, 205, 218, 235],
        'label': 'Revenue ($K)'
    },
    'Customers': {
        'x': list(range(len(months))),
        'y': [450, 475, 490, 520, 545, 570, 590, 615, 640, 660, 685, 720],
        'label': 'Active Customers'
    },
    'Conversion_Rate': {
        'x': list(range(len(months))),
        'y': [2.3, 2.5, 2.7, 2.8, 3.1, 3.3, 3.2, 3.5, 3.6, 3.8, 4.0, 4.2],
        'label': 'Conversion Rate (%)'
    },
    'Avg_Order_Value': {
        'x': list(range(len(months))),
        'y': [85, 88, 92, 95, 98, 102, 105, 108, 112, 115, 118, 122],
        'label': 'Avg Order Value ($)'
    }
}

# Initial data source
source = ColumnDataSource(data=dict(
    x=data['Revenue']['x'],
    y=data['Revenue']['y']
))

# Store all data for CustomJS - flatten the structure
all_data = ColumnDataSource(data={
    'Revenue_x': data['Revenue']['x'],
    'Revenue_y': data['Revenue']['y'],
    'Revenue_label': [data['Revenue']['label']] * len(data['Revenue']['x']),
    'Customers_x': data['Customers']['x'],
    'Customers_y': data['Customers']['y'],
    'Customers_label': [data['Customers']['label']] * len(data['Customers']['x']),
    'Conversion_Rate_x': data['Conversion_Rate']['x'],
    'Conversion_Rate_y': data['Conversion_Rate']['y'],
    'Conversion_Rate_label': [data['Conversion_Rate']['label']] * len(data['Conversion_Rate']['x']),
    'Avg_Order_Value_x': data['Avg_Order_Value']['x'],
    'Avg_Order_Value_y': data['Avg_Order_Value']['y'],
    'Avg_Order_Value_label': [data['Avg_Order_Value']['label']] * len(data['Avg_Order_Value']['x'])
})

# Create figure
p = figure(height=400, width=800,
           title="Business Metrics Over Time",
           x_axis_label='Month',
           y_axis_label='Revenue ($K)',
           toolbar_location='above',
           tools="pan,wheel_zoom,box_zoom,reset,save")

# Customize x-axis
p.xaxis.ticker = list(range(len(months)))
p.xaxis.major_label_overrides = {i: month for i, month in enumerate(months)}

# Add line
line = p.line('x', 'y', source=source, line_width=3, color='#e74c3c', alpha=0.8)
p.scatter('x', 'y', source=source, size=8, color='#e74c3c', alpha=0.6)
p.add_tools(HoverTool(tooltips=[("Month", "@x"), ("Value", "@y")], renderers=[p.renderers[0]]))

# Dropdown menu
select = Select(title="Select Metric:", 
                value="Revenue", 
                options=["Revenue", "Customers", "Conversion_Rate", "Avg_Order_Value"])

# CustomJS callback
callback = CustomJS(args=dict(source=source, all_data=all_data, yaxis=p.yaxis[0], title=p.title), code="""
    const selected = cb_obj.value;
    
    source.data['x'] = all_data.data[selected + '_x'];
    source.data['y'] = all_data.data[selected + '_y'];
    
    // Update y-axis label
    yaxis.axis_label = all_data.data[selected + '_label'][0];
    
    // Update title
    title.text = "Business Metrics Over Time - " + selected.replace('_', ' ');
    
    source.change.emit();
""")

select.js_on_change('value', callback)

# Layout
layout = column(select, p)
output_file("output/interactive_charts_02.html")
save(layout)