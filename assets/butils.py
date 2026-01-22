import pandas as pd, numpy as np, xarray as xr
from bokeh.layouts import row, Spacer

from bokeh.themes import Theme
from bokeh.plotting import figure, show,save,  curdoc, output_notebook, output_file
from bokeh.models import VBar,Range1d, CustomJSHover,LinearAxis, ColumnDataSource, InlineStyleSheet, LassoSelectTool,DatetimeTickFormatter, NumeralTickFormatter, CrosshairTool, HoverTool, Span,Legend,BoxEditTool, FreehandDrawTool,WheelZoomTool
from bokeh.io import export_png
class ms_StandardConfigs():  pass# the standard configurations
# curdoc().theme = Theme(filename=r'C:\Users\michail.stamatis\Desktop\training\PythonProjects\misti\mike2.json')
# curdoc().theme = Theme(filename=r'/home/michael/Hypermachos/pyms/Bokeh_standards/Myrtidiotissa_bokeh-main/mike2.json')
jk9 = {"active_scroll": "wheel_zoom"}




# curdoc().theme = 'dark_minimal';tth=1


def add_extras(p,tth = 1, drawline_width=5, drawalpha=0.4, drawcolor='red',cross=1, bed=0):
    # box edit tool wants to be first
    
    if bed ==1:
        sourcebox = ColumnDataSource( data=dict( x=[0], y=[0], width=[0], height=[0], color=['grey'], alpha=[0.35], ), default_values = dict( color="grey", alpha=0.35, ), )
        rbox = p.rect("x", "y", "width", "height", color="color", alpha="alpha", source=sourcebox)
        box_tool = BoxEditTool(renderers=[rbox],)
        p.add_tools(box_tool)
    
    # draw tool
    rdraw = p.multi_line([], [], line_width=drawline_width, alpha=drawalpha, color=drawcolor)
    draw_tool = FreehandDrawTool(renderers=[rdraw], num_objects=100)
    p.add_tools(draw_tool)
    

    if tth == 1:
        curdoc().theme = 'dark_minimal'
        p.min_border_bottom=90; p.min_border_right=165;p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(243, 192, 97, 0.2)','padding': '5px','background-color': '#343838','border': '1.5px solid orange'}
        p.background_fill_color = '#1f1f1f'
        p.border_fill_color = '#343838'

    else:
        curdoc().theme = 'light_minimal'

        p.min_border_bottom=90; p.min_border_right=165;p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(165, 221, 253, 0.2)','padding': '5px','background-color': 'white','border': '1.5px solid deepskyblue'}
        p.background_fill_color = '#f2f2f2'

    p.toolbar.autohide = True
    p.xaxis.visible=True
    p.yaxis.visible=True
    p.yaxis.major_tick_out = 5
    p.xaxis.major_tick_out = 5
    p.yaxis.major_tick_line_color = "grey"
    p.xaxis.major_tick_line_color = "grey"
    p.xaxis.axis_label_text_font_size = "15pt"
    p.yaxis.axis_label_text_font_size = "15pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.major_label_text_font_size = "15pt"
    p.xaxis.major_label_text_font = "Courier New"
    p.yaxis.major_label_text_font = "Courier New"
    p.xaxis.axis_label_text_font = "Courier New"
    p.yaxis.axis_label_text_font = "Courier New"
    p.title.text_font_size = "18pt"
    p.title.text_font = "Courier New"
    p.title.align = "center"
    p.grid.grid_line_color = "grey"
    p.grid.grid_line_alpha = 0.1
    p.add_tools("box_select","lasso_select","tap",)#"point_draw","poly_draw","poly_edit","undo")
    p.toolbar_location='left'
    Span_height = Span(dimension="height", line_dash="dashed", line_width=2, line_color="#878787")
    Crosshair_Tool = CrosshairTool(overlay=Span_height)
    if cross == 1:
        p.add_tools(Crosshair_Tool)
    
    if len(p.legend)>0:
        p.legend.location = "center";p.add_layout(p.legend[0], 'right');
        p.legend.click_policy="hide"
        p.legend.label_text_font_size = "15pt"
        # change border and background of legend
        p.legend.border_line_width = 1.5
        p.legend.border_line_color = "black"
        p.legend.border_line_alpha = 0.7
        p.legend.background_fill_alpha = 0.1
        p.legend.background_fill_color = 'silver'
        p.legend.label_text_font = "Courier New"
        p.add_layout(Spacer(width=5), 'right');

    # re-arange y axis when hide a glyph! not works if i set the y_range 
    # p.y_range.only_visible = True
###############################################################################
mcol= ['#0096FF','#FF3131','#FFAC1C','#0FFF50','#ea51ea','#1F51FF','#FFEA00','#97573a','#00FFFF','#ff9cff','#008000','#A42A04','#D2B48C','#878787',]
bout = '/home/michael/Software_Developer_Training_2025/DataAnalysis/Python/dataviz/bokeh/bokeh_output/'
# define how many tooltips you want to show as maximum
def save_plot(plot,fname):
    """Saves the plot to an HTML file and exports it as a PNG."""
    output_file(fname+'.html')
    save(plot)
    export_png(plot, filename=fname+'.png',)
def cusj():
    num=1
    return CustomJSHover(code=f"""
    special_vars.indices = special_vars.indices.slice(0,{num})
    return special_vars.indices.includes(special_vars.index) ? " " : " hidden "
    """)
def hovfun(tltl):
    return """<div @hidden{custom} style="background-color: #fff0eb; padding: 5px; border-radius: 5px; box-shadow: 0px 0px 5px rgba(0,0,0,0.3);">        <font size="3" style="background-color: #fff0eb; padding: 5px; border-radius: 5px;"> """+tltl+""" <br> </font> </div> <style> :host { --tooltip-border: transparent;  /* Same border color used everywhere */ --tooltip-color: transparent; --tooltip-text: #2f2f2f;} </style> """




import pandas as pd
import numpy as np

def build_auto_tooltip(df, hovfun, datetime_fmt="%Y-%m", float_fmt="{0.00}"):
    """
    Automatically build a tooltip for all columns in a DataFrame.
    Detects types and assigns formatting automatically.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to inspect (column names become @fields in Bokeh).
    hovfun : callable
        Styling wrapper for tooltips (adds HTML/CSS).
    datetime_fmt : str, optional
        Datetime display format for datetime columns.
    float_fmt : str, optional
        Numeric display format for floats/ints.

    Returns
    -------
    str
        Formatted HTML tooltip string ready to pass to HoverTool.
    """
    tooltips = {}

    for col in df.columns:
        if col in ["hidden", "index"]:
            continue

        dtype = df[col].dtype

        if np.issubdtype(dtype, '<M8[ns]'):
            tooltips[col] = f"@{col}{{{datetime_fmt}}}"
        elif np.issubdtype(dtype, np.number):
            tooltips[col] = f"@{col}{float_fmt}"
        else:
            tooltips[col] = f"@{col}"
        # tooltips['x'] = "@x{%Y-%m}"
    html = "<br>".join(f"<i>{k}:</i> <b>{v}</b>" for k, v in tooltips.items())
    return hovfun(html)

def build_tooltip(fields: dict, title: str = None, italic_labels=True) -> str:
    """
    Dynamically build a Bokeh HTML tooltip string from a dictionary of label: field format pairs.

    Example:
        build_tooltip({
            "time": "@x{%Y-%m}",
            "radiation": "@radiation{0.00}",
            "temperature": "@temperature{0.00}"
        })
    """
    tooltip_lines = []
    for label, field in fields.items():
        label_html = f"<i>{label}:</i>" if italic_labels else f"{label}:"
        tooltip_lines.append(f"{label_html} <b>{field}</b>")

    html = " <br> ".join(tooltip_lines)
    html = f"{html}"
    return html


# palette = ['#0096FF','#FFD900','#FF6B6B', '#00CC96', '#AB63FA', '#FFA15A',]
palette= ['#0096FF','#FFAC1C','#00ff44','#FF3131','#ea51ea','#1F51FF','#FFEA00','#97573a','#00FFFF','#ff9cff','#008000','#A42A04','#D2B48C','#878787',]



from matplotlib import cm
from matplotlib.colors import to_hex
#'RdBu_r'
def mbpal(sMpl):
    return [to_hex(cm.get_cmap(sMpl)(i/255)) for i in range(256)]

############################
# GENERIC CHOROPLETH FUNCTION
############################
import json
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, FixedTicker, HoverTool
import cartopy.crs as ccrs
import requests

def load_natural_earth_countries():
    """
    Load Natural Earth countries GeoJSON from GitHub.
    Uses 1:110m resolution for better performance.
    """
    url = "https://raw.githubusercontent.com/martynafford/natural-earth-geojson/master/110m/cultural/ne_110m_admin_0_countries.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def merge_data_to_geo(natural_earth_geo, source_geo, value_col='population'):
    """
    Merge data from source_geo into Natural Earth geometries.
    Matches by country name.
    
    Parameters
    ----------
    natural_earth_geo : dict
        Natural Earth GeoJSON with geometries
    source_geo : dict
        Source GeoJSON with data values
    value_col : str
        Name of the property to merge (e.g., 'population', 'gdp', 'life_expectancy')
    """
    # Create a mapping of names to values
    value_map = {}
    for feature in source_geo.get('features', []):
        name = feature['properties'].get('name')
        value = feature['properties'].get(value_col)
        if name and value is not None:
            value_map[name] = value
    
    # Common name variations
    name_mappings = {
        'United States of America': 'United States',
        'Russian Federation': 'Russia',
        'Republic of Korea': 'South Korea',
        'Korea, Republic of': 'Korea',
        'Democratic Republic of the Congo': 'Dem. Rep. Congo',
        'Republic of the Congo': 'Congo',
        'Czech Republic': 'Czechia',
        'Tanzania': 'United Republic of Tanzania',
        "Côte d'Ivoire": 'Ivory Coast',
        "Cote d'Ivoire": 'Ivory Coast',
        "Ivory Coast": "Cote d'Ivoire",
    }
    
    # Add values to Natural Earth features
    for feature in natural_earth_geo.get('features', []):
        name = feature['properties'].get('NAME', '')
        
        # Try direct match first
        if name in value_map:
            feature['properties'][value_col] = value_map[name]
        # Try mappings
        elif name in name_mappings and name_mappings[name] in value_map:
            feature['properties'][value_col] = value_map[name_mappings[name]]
        # Try alternative names from Natural Earth
        else:
            for key in ['NAME_LONG', 'FORMAL_EN', 'NAME_SORT']:
                alt_name = feature['properties'].get(key, '')
                if alt_name in value_map:
                    feature['properties'][value_col] = value_map[alt_name]
                    break
    
    return natural_earth_geo

def transform_geojson_simple(geojson, projection):
    """Transform GeoJSON coordinates to a cartopy projection."""
    from copy import deepcopy
    result = deepcopy(geojson)
    source_crs = ccrs.PlateCarree()
    
    def transform_coords(coords, coord_type):
        if coord_type == "Point":
            x, y = projection.transform_point(coords[0], coords[1], source_crs)
            return [x, y] if not (np.isnan(x) or np.isnan(y)) else None
        
        elif coord_type in ["LineString", "MultiPoint"]:
            transformed = []
            for coord in coords:
                x, y = projection.transform_point(coord[0], coord[1], source_crs)
                if not (np.isnan(x) or np.isnan(y)):
                    transformed.append([x, y])
            return transformed if transformed else None
        
        elif coord_type == "Polygon":
            transformed = []
            for ring in coords:
                ring_coords = []
                for coord in ring:
                    x, y = projection.transform_point(coord[0], coord[1], source_crs)
                    if not (np.isnan(x) or np.isnan(y)):
                        ring_coords.append([x, y])
                if ring_coords:
                    transformed.append(ring_coords)
            return transformed if transformed else None
        
        elif coord_type == "MultiPolygon":
            transformed = []
            for polygon in coords:
                poly_coords = []
                for ring in polygon:
                    ring_coords = []
                    for coord in ring:
                        x, y = projection.transform_point(coord[0], coord[1], source_crs)
                        if not (np.isnan(x) or np.isnan(y)):
                            ring_coords.append([x, y])
                    if ring_coords:
                        poly_coords.append(ring_coords)
                if poly_coords:
                    transformed.append(poly_coords)
            return transformed if transformed else None
    
    for feature in result.get("features", []):
        geom = feature.get("geometry")
        if geom:
            geom_type = geom.get("type")
            coords = geom.get("coordinates")
            if coords:
                new_coords = transform_coords(coords, geom_type)
                if new_coords:
                    geom["coordinates"] = new_coords
    
    return result

def plot_world_choropleth(world_geo, projection, projName,
                          value_col='population',
                          palette=None, 
                          bin_labels=None, 
                          bin_edges=None,
                          use_natural_earth=True, 
                          show_plot=True, 
                          title=None,
                          legend_title=None,
                          tooltip_label=None,
                          value_format='{0,0}',
                          width=1400,
                          height=700,
                          bg_color='#f5f5f5',):
    """
    Generic high-level function to plot world choropleth maps using Bokeh and Cartopy projection.
    
    Parameters
    ----------
    world_geo : dict
        GeoJSON dictionary containing world geometries and data in properties.
    projection : cartopy.crs projection
        Cartopy projection instance (e.g., ccrs.EqualEarth()).
    projName : str
        Projection name (used in the plot title).
    value_col : str, default='population'
        Name of the property to visualize (e.g., 'population', 'gdp', 'co2').
    palette : list of str, optional
        List of hex colors for the color map.
    bin_labels : list of str, optional
        Labels for each data bin.
    bin_edges : list of float, optional
        Edges for data bins.
    use_natural_earth : bool, default=True
        If True, use Natural Earth geometries instead of provided geometries.
    show_plot : bool, default=True
        If True, display the plot immediately.
    title : str, optional
        Custom title for the plot. If None, auto-generated.
    legend_title : str, optional
        Title for the color bar legend. If None, uses value_col.
    tooltip_label : str, optional
        Label for the value in tooltips. If None, uses value_col.
    value_format : str, default='{0,0}'
        Bokeh number format string for tooltip values.
    width : int, default=1400
        Plot width in pixels.
    height : int, default=700
        Plot height in pixels.
        
    Returns
    -------
    bokeh.plotting.figure
        The Bokeh figure object.
    """
    
    print(f"Number of features before processing: {len(world_geo.get('features', []))}")
    
    # Use Natural Earth geometries if requested
    if use_natural_earth:
        print("Loading Natural Earth geometries...")
        natural_earth_geo = load_natural_earth_countries()
        world_geo = merge_data_to_geo(natural_earth_geo, world_geo, value_col)
        print(f"Loaded {len(world_geo.get('features', []))} countries from Natural Earth")
    
    # Handle Antarctica (set to 0 if missing)
    for feature in world_geo['features']:
        props = feature.get('properties', {})
        name = props.get('NAME', props.get('name', ''))
        if 'antarctica' in name.lower():
            if props.get(value_col) is None:
                props[value_col] = 0
    
    # Clean up missing data
    world_geo['features'] = [
        f for f in world_geo['features']
        if f.get('properties', {}).get(value_col) is not None
    ]
    
    print(f"Countries with {value_col} data: {len(world_geo['features'])}")
    
    # Project
    world_geo_projected = transform_geojson_simple(world_geo, projection)
    
    # Validate
    if not world_geo_projected.get("features"):
        raise ValueError("Projected GeoJSON empty — check upstream filters.")
    
    # Default bins & colors if not provided
    if bin_edges is None:
        bin_edges = [0, 5e5, 2e6, 1e7, 3e7, 5e7, 1e8, 3e8, 1e9, 2e9]

    if bin_labels is None:
        bin_labels = [
            "<500k", "500k–2M", "2M–10M", "10M–30M", "30M–50M",
            "50M–100M", "100M–300M", "300M–1B", "1B+"
        ]

    if palette is None:
        palette = [
            "#ececec", "#b9d7c2", "#87b37a", "#65934c", "#c4b16a",
            "#dfc872", "#e7b07a", "#d08c60", "#b05f3c", "#7e4836",
        ]

    # Assign data bins
    for feature in world_geo_projected['features']:
        value = feature['properties'][value_col]
        # Handle zero values - put in lowest bin
        if value == 0:
            idx = 0
        else:
            idx = next((i for i in range(len(bin_edges)-1)
                        if bin_edges[i] <= value < bin_edges[i+1]), len(bin_labels)-1)
        feature['properties']['data_bin_index'] = idx
        
        # Ensure 'name' field exists for tooltips
        if 'NAME' in feature['properties'] and 'name' not in feature['properties']:
            feature['properties']['name'] = feature['properties']['NAME']
    
    # Prepare Bokeh data source
    geosource = GeoJSONDataSource(geojson=json.dumps(world_geo_projected))
    color_mapper = LinearColorMapper(palette=palette, low=0, high=len(bin_labels)-1)

    # Create Earth boundary
    def create_earth_boundary(projection, n_points=360):
        source_crs = ccrs.PlateCarree()
        boundary_points = []

        if isinstance(projection, (ccrs.Orthographic, ccrs.NearsidePerspective)):
            angles = np.linspace(0, 2*np.pi, n_points)
            radius = 6371000
            for angle in angles:
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                boundary_points.append([x, y])
            if boundary_points:
                boundary_points.append(boundary_points[0])
            return boundary_points

        lons = np.linspace(-180, 180, n_points)
        for lon in lons:
            try:
                x, y = projection.transform_point(lon, 89.9, source_crs)
                if not (np.isnan(x) or np.isnan(y)):
                    boundary_points.append([x, y])
            except:
                continue

        lats = np.linspace(89.9, -89.9, n_points//4)
        for lat in lats:
            try:
                x, y = projection.transform_point(179.9, lat, source_crs)
                if not (np.isnan(x) or np.isnan(y)):
                    boundary_points.append([x, y])
            except:
                continue

        for lon in reversed(lons):
            try:
                x, y = projection.transform_point(lon, -89.9, source_crs)
                if not (np.isnan(x) or np.isnan(y)):
                    boundary_points.append([x, y])
            except:
                continue

        lats = np.linspace(-89.9, 89.9, n_points//4)
        for lat in lats:
            try:
                x, y = projection.transform_point(-179.9, lat, source_crs)
                if not (np.isnan(x) or np.isnan(y)):
                    boundary_points.append([x, y])
            except:
                continue

        if boundary_points:
            boundary_points.append(boundary_points[0])
        return boundary_points

    earth_boundary = create_earth_boundary(projection)

    # Default title and labels
    if title is None:
        title = f"🌎 World {value_col.replace('_', ' ').title()} by Country ~ {projName}"
    
    if legend_title is None:
        legend_title = value_col.replace('_', ' ').title()
    
    if tooltip_label is None:
        tooltip_label = value_col.replace('_', ' ').title()

    # Bokeh figure
    p = figure(
        title=title,
        width=width,
        height=height,
        toolbar_location='right',
        tools='pan,box_zoom,reset,save,wheel_zoom',
        active_scroll='wheel_zoom',
        x_axis_location=None,
        y_axis_location=None,
    )

    # Adjust for orthographic projections
    if 'orth' in str(projection).lower():
        p.width = 900

    p.grid.grid_line_color = None
    p.axis.visible = False

    # Add Earth boundary
    if earth_boundary:
        xs = [point[0] for point in earth_boundary]
        ys = [point[1] for point in earth_boundary]
        p.patch(xs, ys, fill_color='#90D5FF', line_color='black', 
                line_width=3, alpha=1.0, level='underlay')

    # Country patches
    countries = p.patches(
        'xs', 'ys',
        source=geosource,
        fill_color={'field': 'data_bin_index', 'transform': color_mapper},
        line_color='black',
        line_width=0.25,
        fill_alpha=0.8,
        hover_line_color='black',
        hover_line_width=5,
    )

    # Hover tool with dynamic value column
    hover = HoverTool(
        renderers=[countries], 
        point_policy="follow_mouse",
        attachment="above",
        show_arrow=False,
        tooltips=f"""
        <div style="background-color: #f0f0f0; padding: 5px; margin-bottom:30px; border-radius: 5px; box-shadow: 0px 0px 5px rgba(0,0,0,0.3);">
            <font size="5" style="background-color: #f0f0f0; padding: 5px; border-radius: 5px;">
                <i>Country:</i> <b>@name</b> <br>
                <i>{tooltip_label}:</i> <b>@{value_col}{value_format}</b> <br>
            </font>
        </div>
        <style>
            :host {{
                --tooltip-border: transparent;
                --tooltip-color: transparent;
                --tooltip-text: #2f2f2f;
            }}
        </style>
        """
    )
    p.add_tools(hover)

    # ColorBar
    color_bar = ColorBar(
        color_mapper=color_mapper,
        ticker=FixedTicker(ticks=list(range(len(bin_labels)))),
        major_label_overrides={i: l for i, l in enumerate(bin_labels)},
        label_standoff=12,
        width=24,
        height=600,
        border_line_color=None,
        background_fill_color= bg_color ,
        location=(0, 10),
        orientation='vertical',
        title=legend_title,
        major_label_text_color="#2f2f2f" if bg_color == '#f5f5f5' else "#ffffff",
        title_text_color="#2f2f2f" if bg_color == '#f5f5f5' else "#ffffff",
        major_label_text_font_size="16pt",
        title_text_font_size="16pt",
    )
    p.add_layout(color_bar, 'right')

    # Style
    p.title.text_font_size = '19pt'
    p.title.text_font = 'Montserrat'
    p.title.text_color = '#7b4397' if bg_color == '#f5f5f5' else '#e0b0ff'
    p.background_fill_color = bg_color  
    p.border_fill_color = bg_color
    p.legend.visible = False

    if show_plot:
        show(p)
    return p


# Keep backward compatibility
def plot_world_population(*args, **kwargs):
    """Backward compatible wrapper for population-specific plots."""
    if 'value_col' not in kwargs:
        kwargs['value_col'] = 'population'
    return plot_world_choropleth(*args, **kwargs)



def plot_country_choropleth(geojson_url, data_dict, value_col,
                           country_name,
                           palette, bin_edges, bin_labels,
                           title=None,
                           name_property='name',
                           legend_title=None,
                           tooltip_label=None,
                           value_format='{0,0}',
                           width=1200, height=900,
                           bounds=None, bg_color='#f5f5f5'):
    """
    Plot choropleth for a country's regions using lat/lon coordinates (no projection).
    
    Parameters
    ----------
    geojson_url : str
        URL to fetch the GeoJSON file
    data_dict : dict
        Dictionary mapping region names to values
    value_col : str
        Name of the value column to create
    country_name : str
        Name of the country (for title)
    palette : list
        Color palette
    bin_edges : list
        Bin edges for categorization
    bin_labels : list
        Labels for bins
    title : str, optional
        Custom map title
    name_property : str, default='name'
        Property name in GeoJSON for region names
    legend_title : str, optional
        Custom legend title
    tooltip_label : str, optional
        Custom tooltip label
    value_format : str, default='{0,0}'
        Bokeh number format string
    width, height : int
        Figure dimensions
    bounds : tuple, optional
        (min_lon, min_lat, max_lon, max_lat) to override automatic bounds
    """
    from bokeh.plotting import figure, show
    from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, FixedTicker, HoverTool
    
    # Load GeoJSON
    print(f"Loading GeoJSON from {geojson_url}")
    geo_data = requests.get(geojson_url).json()
    print(f"Loaded {len(geo_data['features'])} regions")
    
    # Assign data to features
    matched = 0
    for feature in geo_data['features']:
        region_name = feature['properties'].get(name_property, '')
        value = data_dict.get(region_name, None)
        if value is not None:
            matched += 1
        feature['properties'][value_col] = value
    
    print(f"Matched {matched}/{len(data_dict)} regions with data")
    
    # Remove features without data
    geo_data['features'] = [f for f in geo_data['features'] 
                           if f['properties'].get(value_col) is not None]
    
    # Assign bins
    for feature in geo_data['features']:
        val = feature['properties'][value_col]
        if val == 0:
            idx = 0
        else:
            idx = next((i for i in range(len(bin_edges)-1)
                       if bin_edges[i] <= val < bin_edges[i+1]), len(bin_labels)-1)
        feature['properties']['data_bin_index'] = idx
    
    # Calculate bounds if not provided
    if bounds is None:
        all_coords = []
        for feature in geo_data['features']:
            geom = feature['geometry']
            if geom['type'] == 'Polygon':
                for ring in geom['coordinates']:
                    all_coords.extend(ring)
            elif geom['type'] == 'MultiPolygon':
                for polygon in geom['coordinates']:
                    for ring in polygon:
                        all_coords.extend(ring)
        
        lons = [c[0] for c in all_coords]
        lats = [c[1] for c in all_coords]
        min_lon, max_lon = min(lons), max(lons)
        min_lat, max_lat = min(lats), max(lats)
        
        # Add 5% padding
        lon_padding = (max_lon - min_lon) * 0.05
        lat_padding = (max_lat - min_lat) * 0.05
        min_lon -= lon_padding
        max_lon += lon_padding
        min_lat -= lat_padding
        max_lat += lat_padding
    else:
        min_lon, min_lat, max_lon, max_lat = bounds
    
    # Set defaults
    if title is None:
        title = f"{country_name} {value_col.replace('_', ' ').title()}"
    if legend_title is None:
        legend_title = value_col.replace('_', ' ').title()
    if tooltip_label is None:
        tooltip_label = value_col.replace('_', ' ').title()
    
    # Create Bokeh data source
    geosource = GeoJSONDataSource(geojson=json.dumps(geo_data))
    color_mapper = LinearColorMapper(palette=palette, low=0, high=len(bin_labels)-1)
    
    # Create figure
    p = figure(
        title=title,
        width=width,
        height=height,
        x_range=(min_lon, max_lon),
        y_range=(min_lat, max_lat),
        toolbar_location='right',
        tools='pan,box_zoom,reset,save,wheel_zoom',
        active_scroll='wheel_zoom',
        x_axis_location=None,
        y_axis_location=None,
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )
    
    p.grid.grid_line_color = None
    p.axis.visible = False
    
    # Add regions
    regions = p.patches(
        'xs', 'ys',
        source=geosource,
        fill_color={'field': 'data_bin_index', 'transform': color_mapper},
        line_color='#555555',
        line_width=0.5,
        fill_alpha=0.8,
        hover_line_color='black',
        hover_line_width=2.5,
    )
    
    # Hover tool
    hover = HoverTool(
        renderers=[regions],
        point_policy="follow_mouse",
        attachment="above",
        show_arrow=False,
        tooltips=f"""
        <div style="background-color: #f0f0f0; padding: 8px; border-radius: 5px; box-shadow: 0px 0px 5px rgba(0,0,0,0.3);">
            <font size="5" style="background-color: #f0f0f0; padding: 5px; border-radius: 5px;">
                <b>@{name_property}</b><br>
                <i>{tooltip_label}:</i> <b>@{value_col}{value_format}</b>
            </font>
        </div>
                <style>
            :host {{
                --tooltip-border: transparent;
                --tooltip-color: transparent;
                --tooltip-text: #2f2f2f;
            }}
        </style>
        """
    )
    p.add_tools(hover)
    
    # Color bar
    color_bar = ColorBar(
        color_mapper=color_mapper,
        ticker=FixedTicker(ticks=list(range(len(bin_labels)))),
        major_label_overrides={i: l for i, l in enumerate(bin_labels)},
        label_standoff=12,
        width=20,
        height=500,
        border_line_color=None,
        background_fill_color= bg_color,
        location=(0, 0),
        orientation='vertical',
        title=legend_title,
        major_label_text_color="#2f2f2f" if bg_color == '#f5f5f5' else "#f5f5f5",
        title_text_color="#2f2f2f" if bg_color == '#f5f5f5' else "#f5f5f5",
        major_label_text_font_size="16pt",
        title_text_font_size="16pt",
    )
    p.add_layout(color_bar, 'right')
    
    # Styling
    p.title.text_font_size = '18pt'
    p.title.text_font = 'Montserrat'
    p.title.text_color = '#7b4397' if bg_color == '#f5f5f5' else '#f5f5f5'

    
    return p





from bokeh.plotting import figure, show
from bokeh.models import (
    LinearColorMapper, ColorBar, ColumnDataSource, HoverTool
)
from bokeh.transform import transform
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# -----------------------------------------------------
# 🎨 Utility: Convert matplotlib cmap to hex list
# -----------------------------------------------------
def mpl_to_hex_palette(cmap_name='viridis', n_colors=256):
    cmap = plt.get_cmap(cmap_name)
    return [to_hex(cmap(i / n_colors)) for i in range(n_colors)]


# -----------------------------------------------------
# 💡 Core Function: High-Level Heatmap Generator
# -----------------------------------------------------
def create_heatmap_figure(
    data,
    x_labels=None,
    y_labels=None,
    cmap='viridis',
    title="Heatmap",
    width=600,
    height=400,
    show_values=True,
    hover_format=None,
    text_font_size = '11pt',
    text_color = 'grey'
):
    """
    Create a Bokeh heatmap for any 2D dataset.

    Parameters
    ----------
    data : np.ndarray or pd.DataFrame
        2D dataset (e.g., correlation matrix, metrics table, etc.)
    x_labels : list
        X-axis labels (optional if DataFrame provided)
    y_labels : list
        Y-axis labels (optional if DataFrame provided)
    cmap : str
        Matplotlib colormap name (e.g., 'coolwarm', 'plasma', etc.)
    title : str
        Figure title
    width, height : int
        Figure size in pixels
    show_values : bool
        Whether to show numeric values in each cell
    hover_format : str
        Custom hover tooltip (optional)
    """

    # 1️⃣ Handle data input
    if isinstance(data, pd.DataFrame):
        x_labels = list(data.columns) if x_labels is None else x_labels
        y_labels = list(data.index) if y_labels is None else y_labels
        values = data.values
    else:
        values = np.array(data)
        if x_labels is None:
            x_labels = [f"X{i}" for i in range(values.shape[1])]
        if y_labels is None:
            y_labels = [f"Y{i}" for i in range(values.shape[0])]

    # 2️⃣ Prepare Bokeh-friendly data source
    x_coords, y_coords, vals = [], [], []
    for i, y in enumerate(y_labels):
        for j, x in enumerate(x_labels):
            x_coords.append(x)
            y_coords.append(y)
            vals.append(values[i, j])

    source = ColumnDataSource(data=dict(x=x_coords, y=y_coords, values=vals))

    # 3️⃣ Color mapping
    palette = mpl_to_hex_palette(cmap)
    color_mapper = LinearColorMapper(palette=palette, low=np.min(vals), high=np.max(vals))

    # 4️⃣ Create figure
    p = figure(
        title=title,
        x_range=x_labels,
        y_range=list(reversed(y_labels)),
        width=width,
        height=height,
        tools="",
        toolbar_location=None
    )

    rects = p.rect(
        x="x",
        y="y",
        width=1,
        height=1,
        source=source,
        fill_color=transform('values', color_mapper),
        line_color="black",
        hover_line_color="deepskyblue",
        hover_line_width=3
    )

    # 5️⃣ Optional text labels
    if show_values:
        p.text(
            x="x",
            y="y",
            text="values",
            source=source,
            text_align="center",
            text_baseline="middle",
            text_font_size=text_font_size,
            text_color=text_color
        )

    # 6️⃣ Add color bar
    color_bar = ColorBar(color_mapper=color_mapper,  width=11, location=(0,0), major_label_text_font_size="16pt", title_text_font_size="16pt")
    p.add_layout(color_bar, 'right')

    # 7️⃣ Default hover tooltip if none provided
    if hover_format is None:
        hover_format = hovfun("🧩 X: @x<br>🧭 Y: @y<br>🌡️ Value: @values{0.000}")

    hover = HoverTool(
        tooltips=hover_format,
        renderers=[rects],
        mode='mouse',
        point_policy='follow_mouse',
        attachment='below',
        show_arrow=False
    )
    p.add_tools(hover)

    # 8️⃣ Minimalistic style
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "12pt"
    p.title.text_font_size = "14pt"

    return p
