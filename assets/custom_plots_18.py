from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Button, CustomJS
from bokeh.layouts import column, row
from bokeh_rocks import save_plot
# ======= Data =========

# Top-level continents
continents = ['Europe', 'America', 'Asia', 'Australia']
continent_population = [750, 1000, 4600, 40]  # in millions

# Second-level countries
continent_to_countries = {
    'Europe': (['Germany', 'France', 'UK', 'Italy', 'Spain'], [83, 65, 67, 60, 47]),
    'America': (['USA', 'Brazil', 'Mexico', 'Canada'], [331, 213, 128, 38]),
    'Asia': (['China', 'India', 'Japan', 'Indonesia'], [1440, 1390, 126, 276]),
    'Australia': (['Australia'], [26]),
}

# Third-level cities
country_to_cities = {
    'Germany': (['Berlin', 'Hamburg', 'Munich'], [3.6, 1.8, 1.5]),
    'France': (['Paris', 'Marseille', 'Lyon'], [2.1, 0.9, 0.5]),
    'UK': (['London', 'Manchester', 'Birmingham'], [9.0, 0.5, 1.1]),
    'Italy': (['Rome', 'Milan', 'Naples'], [2.8, 1.4, 1.0]),
    'Spain': (['Madrid', 'Barcelona', 'Valencia'], [3.2, 1.6, 0.8]),
    'USA': (['New York', 'Los Angeles', 'Chicago'], [8.4, 4.0, 2.7]),
    'Brazil': (['Sao Paulo', 'Rio de Janeiro', 'Brasilia'], [12.3, 6.7, 3.1]),
    'Mexico': (['Mexico City', 'Guadalajara', 'Monterrey'], [9.2, 1.5, 1.1]),
    'Canada': (['Toronto', 'Vancouver', 'Montreal'], [2.9, 0.6, 1.7]),
    'China': (['Beijing', 'Shanghai', 'Guangzhou'], [21.5, 24.2, 15.3]),
    'India': (['Mumbai', 'Delhi', 'Bangalore'], [20.7, 32.0, 12.3]),
    'Japan': (['Tokyo', 'Osaka', 'Nagoya'], [37.4, 19.2, 9.5]),
    'Indonesia': (['Jakarta', 'Surabaya', 'Bandung'], [10.5, 2.8, 2.4]),
    'Australia': (['Sydney', 'Melbourne', 'Brisbane'], [5.3, 5.0, 2.5]),
}

# ======= Data Sources =========

source = ColumnDataSource(data=dict(x=continents, top=continent_population))

# Create a data source to hold the navigation stack
nav_source = ColumnDataSource(data=dict(stack=[]))

# Create data sources for all the drill-down data
continent_data = ColumnDataSource(data=dict(
    names=continents,
    values=continent_population
))

# Convert country data to a format CustomJS can use
country_data = {}
for continent, (countries, populations) in continent_to_countries.items():
    country_data[continent] = {'names': countries, 'values': populations}

# Convert city data to a format CustomJS can use
city_data = {}
for country, (cities, populations) in country_to_cities.items():
    city_data[country] = {'names': cities, 'values': populations}

# ======= Plot =========

p = figure(
    x_range=continents,
    height=450,
    title="Population by Continent",
    tools="tap",
    toolbar_location=None,
)

bars = p.vbar(x='x', top='top', width=0.6, source=source, 
              fill_color="#6baed6", line_color="white", hover_fill_color="#2171b5")

p.xgrid.grid_line_color = None
p.ygrid.grid_line_dash = 'dotted'
p.y_range.start = 0
p.title.text_font_size = '20pt'
p.xaxis.major_label_text_font_size = '14pt'
p.yaxis.major_label_text_font_size = '14pt'

bars.selection_glyph = None
bars.nonselection_glyph = bars.glyph

# ======= Buttons =========

back_button = Button(label="← Go Back", button_type="primary", width=100)
back_button.visible = False

# ======= CustomJS Callbacks =========

# Drill down callback
drill_down_callback = CustomJS(
    args=dict(
        source=source,
        nav_source=nav_source,
        back_button=back_button,
        p=p,
        continent_data=continent_data,
        country_data=country_data,
        city_data=city_data
    ),
    code="""
    const indices = source.selected.indices;
    if (indices.length === 0) return;
    
    const clicked = source.data['x'][indices[0]];
    const stack = nav_source.data['stack'];
    
    const continents = continent_data.data['names'];
    const continent_values = continent_data.data['values'];
    
    if (stack.length === 0) {
        // Currently at Continent level, drill to Country
        const country_info = country_data[clicked];
        if (country_info) {
            source.data['x'] = country_info['names'];
            source.data['top'] = country_info['values'];
            p.x_range.factors = country_info['names'];
            p.title.text = 'Population of ' + clicked;
            stack.push(clicked);
            nav_source.data['stack'] = stack;
            back_button.visible = true;
            source.change.emit();
            nav_source.change.emit();
        }
    } else if (stack.length === 1) {
        // Currently at Country level, drill to City
        const city_info = city_data[clicked];
        if (city_info) {
            source.data['x'] = city_info['names'];
            source.data['top'] = city_info['values'];
            p.x_range.factors = city_info['names'];
            p.title.text = 'Population of ' + clicked;
            stack.push(clicked);
            nav_source.data['stack'] = stack;
            source.change.emit();
            nav_source.change.emit();
        }
    }
    
    // Clear selection
    source.selected.indices = [];
"""
)

# Back button callback
back_callback = CustomJS(
    args=dict(
        source=source,
        nav_source=nav_source,
        back_button=back_button,
        p=p,
        continent_data=continent_data,
        country_data=country_data
    ),
    code="""
    const stack = nav_source.data['stack'];
    
    const continents = continent_data.data['names'];
    const continent_values = continent_data.data['values'];
    
    if (stack.length === 2) {
        // From City level back to Country level
        const continent = stack[0];
        const country_info = country_data[continent];
        source.data['x'] = country_info['names'];
        source.data['top'] = country_info['values'];
        p.x_range.factors = country_info['names'];
        p.title.text = 'Population of ' + continent;
        stack.pop();
        nav_source.data['stack'] = stack;
        source.change.emit();
        nav_source.change.emit();
    } else if (stack.length === 1) {
        // From Country level back to Continent level
        source.data['x'] = continents;
        source.data['top'] = continent_values;
        p.x_range.factors = continents;
        p.title.text = 'Population by Continent';
        stack.pop();
        nav_source.data['stack'] = stack;
        back_button.visible = false;
        source.change.emit();
        nav_source.change.emit();
    }
"""
)

# Attach callbacks
source.selected.js_on_change('indices', drill_down_callback)
back_button.js_on_click(back_callback)

# ======= Layout =========

layout = column(row(back_button), p, sizing_mode="scale_width")


save_plot(layout, "output/custom_plots_18")