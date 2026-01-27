from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select
from bokeh.layouts import column

# Sample business data - quarterly sales by region
data = {
    'Q1_2024': {
        'regions': ['North', 'South', 'East', 'West', 'Central'],
        'sales': [45000, 38000, 52000, 41000, 35000]
    },
    'Q2_2024': {
        'regions': ['North', 'South', 'East', 'West', 'Central'],
        'sales': [48000, 42000, 55000, 39000, 37000]
    },
    'Q3_2024': {
        'regions': ['North', 'South', 'East', 'West', 'Central'],
        'sales': [51000, 45000, 58000, 44000, 40000]
    },
    'Q4_2024': {
        'regions': ['North', 'South', 'East', 'West', 'Central'],
        'sales': [62000, 51000, 68000, 52000, 47000]
    }
}

# Initial data source
source = ColumnDataSource(data=dict(
    regions=data['Q1_2024']['regions'],
    sales=data['Q1_2024']['sales']
))

# Store all data in a separate source for CustomJS - flatten the structure
all_data = ColumnDataSource(data={
    'Q1_2024_regions': data['Q1_2024']['regions'],
    'Q1_2024_sales': data['Q1_2024']['sales'],
    'Q2_2024_regions': data['Q2_2024']['regions'],
    'Q2_2024_sales': data['Q2_2024']['sales'],
    'Q3_2024_regions': data['Q3_2024']['regions'],
    'Q3_2024_sales': data['Q3_2024']['sales'],
    'Q4_2024_regions': data['Q4_2024']['regions'],
    'Q4_2024_sales': data['Q4_2024']['sales']
})

# Create figure
p = figure(x_range=data['Q1_2024']['regions'], 
           height=400, 
           width=700,
           title="Regional Sales by Quarter",
           )

# Add bars
p.vbar(x='regions', top='sales', width=0.7, source=source, 
       color='#3498db', alpha=0.8)

# Styling
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.yaxis.axis_label = "Sales ($)"
p.xaxis.axis_label = "Region"
p.add_tools(HoverTool(tooltips=[("Region", "@regions"), ("Sales", "@sales")], renderers=[p.renderers[0]]))
# Dropdown menu
select = Select(title="Select Quarter:", 
                value="Q1_2024", 
                options=["Q1_2024", "Q2_2024", "Q3_2024", "Q4_2024"])

# CustomJS callback
callback = CustomJS(args=dict(source=source, all_data=all_data), code="""
    const selected = cb_obj.value;
    const new_regions = all_data.data[selected + '_regions'];
    const new_sales = all_data.data[selected + '_sales'];
    
    source.data['regions'] = new_regions;
    source.data['sales'] = new_sales;
    source.change.emit();
""")

select.js_on_change('value', callback)

# Layout
layout = column(select, p)

output_file("output/interactive_charts_01.html")
save(layout)
