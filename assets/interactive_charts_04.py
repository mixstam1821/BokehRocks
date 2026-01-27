from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, CustomJS, CheckboxGroup, Select
from bokeh.layouts import column, row
from bokeh.transform import dodge

# Sample business data - regional breakdown
regions = ['North', 'South', 'East', 'West']

# Different time periods
time_periods = {
    'Q1_2024': {
        'online_sales': [120, 95, 140, 110],
        'retail_sales': [180, 160, 200, 175],
        'wholesale': [90, 85, 110, 95]
    },
    'Q2_2024': {
        'online_sales': [135, 105, 155, 125],
        'retail_sales': [170, 155, 190, 165],
        'wholesale': [100, 95, 120, 105]
    },
    'Q3_2024': {
        'online_sales': [150, 115, 170, 140],
        'retail_sales': [160, 145, 180, 155],
        'wholesale': [110, 105, 130, 115]
    },
    'Q4_2024': {
        'online_sales': [180, 140, 200, 170],
        'retail_sales': [150, 135, 170, 145],
        'wholesale': [120, 115, 140, 125]
    }
}

# Initial data (Q1_2024)
initial_period = 'Q1_2024'
source = ColumnDataSource(data=dict(
    regions=regions,
    online=time_periods[initial_period]['online_sales'],
    retail=time_periods[initial_period]['retail_sales'],
    wholesale=time_periods[initial_period]['wholesale']
))

# Store all data for period switching - flatten structure
all_data_dict = {}
for period, channels in time_periods.items():
    all_data_dict[f'{period}_online'] = channels['online_sales']
    all_data_dict[f'{period}_retail'] = channels['retail_sales']
    all_data_dict[f'{period}_wholesale'] = channels['wholesale']

all_data = ColumnDataSource(data=all_data_dict)

# Create figure
p = figure(x_range=regions, height=450, width=800,
           title="Regional Sales by Channel - Q1 2024",
           toolbar_location='above',
           tools="pan,wheel_zoom,reset,save,hover")

# Colors for each channel
colors = {'online': '#3498db', 'retail': '#e74c3c', 'wholesale': '#2ecc71'}

# Create stacked bars
online_bar = p.vbar(x=dodge('regions', -0.25, range=p.x_range), top='online', 
                    width=0.2, source=source, color=colors['online'], 
                    legend_label="Online", alpha=0.8)

retail_bar = p.vbar(x=dodge('regions', 0.0, range=p.x_range), top='retail', 
                    width=0.2, source=source, color=colors['retail'], 
                    legend_label="Retail", alpha=0.8)

wholesale_bar = p.vbar(x=dodge('regions', 0.25, range=p.x_range), top='wholesale', 
                       width=0.2, source=source, color=colors['wholesale'], 
                       legend_label="Wholesale", alpha=0.8)

# Styling
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.yaxis.axis_label = "Sales ($K)"
p.xaxis.axis_label = "Region"
p.legend.location = "top_right"
p.legend.click_policy = "hide"

# Period selector
period_select = Select(title="Select Time Period:", 
                       value="Q1_2024",
                       options=["Q1_2024", "Q2_2024", "Q3_2024", "Q4_2024"],
                       width=200)

# Checkbox for channels
checkbox = CheckboxGroup(labels=["Online", "Retail", "Wholesale"], 
                         active=[0, 1, 2], width=400)

# CustomJS for period selection
period_callback = CustomJS(args=dict(source=source, all_data=all_data, title=p.title), code="""
    const period = cb_obj.value;
    
    source.data['online'] = all_data.data[period + '_online'];
    source.data['retail'] = all_data.data[period + '_retail'];
    source.data['wholesale'] = all_data.data[period + '_wholesale'];
    
    // Update title
    title.text = "Regional Sales by Channel - " + period.replace('_', ' ');
    
    source.change.emit();
""")

period_select.js_on_change('value', period_callback)

# CustomJS for channel visibility
checkbox_callback = CustomJS(args=dict(
    online_bar=online_bar, 
    retail_bar=retail_bar, 
    wholesale_bar=wholesale_bar
), code="""
    const active = cb_obj.active;
    
    online_bar.visible = active.includes(0);
    retail_bar.visible = active.includes(1);
    wholesale_bar.visible = active.includes(2);
""")

checkbox.js_on_change('active', checkbox_callback)

# Layout
controls = row(period_select, checkbox)
layout = column(controls, p)

output_file("output/interactive_charts_04.html")
save(layout)