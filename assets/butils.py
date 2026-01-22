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



from math import pi
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from bokeh.palettes import Category10, Category20, Turbo256
palette= ['#0096FF','#FFAC1C','#00ff44','#FF3131','#ea51ea','#1F51FF','#FFEA00','#97573a','#00FFFF','#ff9cff','#008000','#A42A04','#D2B48C','#878787',]

def fpie_basic(df, title="Pie Chart", colors=palette,bgc=None,
               offset=(0, 1), radius=0.8,tth=1, sh=1,
               height=650, width=800,
               ):
    """
    Create a static pie chart (offset-style) directly from a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain two columns: category (str) and value (numeric).
    title : str
        Chart title.
    colors : list, optional
        List of color hex codes or names. Defaults to auto palette.
    offset : tuple
        (x, y) position of the pie center.
    radius : float
        Radius of the pie.
    height, width : int
        Chart size in pixels.
    cross : bool
        If True, draw faint cross lines through the pie center (for layout debugging).
    """

    # --- Validate input ---
    if len(df.columns) < 2:
        raise ValueError("DataFrame must have at least two columns: category and value.")

    df = df.copy()
    cat_col, val_col = df.columns[:2]
    df.columns = ['category', 'value']

    # --- Palette handling ---
    n = len(df)

    if colors is None:
        colors = palette[:n]
    else:
        colors = colors[:n]


    if n > len(colors):
        step = 256 // n
        colors = Turbo256[::step][:n]




    # --- Angle and color setup ---
    df['angle'] = df['value'] / df['value'].sum() * 2 * pi
    df['color'] = colors

    # --- Create figure ---
    p = figure(
        height=height, width=width, title=title,
        x_range=(-1, 1), y_range=(-0.5, 2.5),
        background_fill_color= bgc,


    )

    # --- Draw wedges ---
    p.wedge(
        x=offset[0], y=offset[1], radius=radius,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white", 
        fill_color='color',
        legend_field='category', source=df,
        hover_line_color='black', hover_line_width=5
    )
    add_extras(p, tth = tth,cross=0)
    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.legend.location = "center_right"
    p.legend.click_policy = 'none'
    p.legend.background_fill_alpha = 0.0
    p.legend.border_line_alpha = 0.0
    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None     # disables pan or box zoom
    p.toolbar.active_scroll = None   # disables wheel zoom
    
    p.add_tools(HoverTool(tooltips=hovfun("@category: <b>@value</b>"), show_arrow=False, point_policy="follow_mouse"))


    if tth==1:
        if bgc is None:
            bgc="#3d3d3d"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(243, 192, 97, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid orange'}
    else:
        if bgc is None:
            bgc="#fff6c0"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(165, 221, 253, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid deepskyblue'}
    
    if sh == 1:
        show(p)
    
    return p

from math import pi
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, AnnularWedge
from bokeh.palettes import Turbo256

# Reuse your palette
palette = ['#0096FF','#FFAC1C','#00ff44','#FF3131','#ea51ea','#1F51FF',
           '#FFEA00','#97573a','#00FFFF','#ff9cff','#008000','#A42A04',
           '#D2B48C','#878787']

def fdonut_basic(df, title="Donut Chart", colors=palette, bgc=None,
                 offset=(0, 0), outer_radius=0.7, inner_radius=0.35,
                 tth=1, sh=1, height=650, width=800):
    """
    Create a static donut (annular) chart from a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain two columns: category (str) and value (numeric).
    title : str
        Chart title.
    colors : list
        List of colors for slices.
    bgc : str
        Background color.
    offset : tuple
        Center offset (x, y).
    outer_radius, inner_radius : float
        Radii of the donut.
    tth : int
        Theme type (1=orange, 0=blue).
    sh : int
        Whether to call show() automatically.
    height, width : int
        Plot size.
    """

    # --- Validate input ---
    if len(df.columns) < 2:
        raise ValueError("DataFrame must have at least two columns: category and value.")

    df = df.copy()
    cat_col, val_col = df.columns[:2]
    df.columns = ['category', 'value']

    n = len(df)
    if colors is None:
        colors = palette[:n]
    else:
        colors = colors[:n]
    if n > len(colors):
        step = 256 // n
        colors = Turbo256[::step][:n]

    # --- Angles ---
    df['angle'] = df['value'] / df['value'].sum() * 2 * pi
    df['start_angle'] = df['angle'].cumsum().shift(1, fill_value=0)
    df['end_angle'] = df['angle'].cumsum()
    df['color'] = colors

    src = ColumnDataSource(df)

    # --- Figure ---
    p = figure(
        width=width, height=height, title=title,
        toolbar_location=None,
        x_range=(-1, 0.8), y_range=(-2, 2),
        background_fill_color=bgc,
        border_fill_color=bgc
    )
    # --- Donut wedges ---
    p.annular_wedge(
        x=offset[0], y=offset[1],
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        start_angle='start_angle',
        end_angle='end_angle',
        line_color="white",
        fill_color='color',
        source=src,
        legend_field='category',
        hover_line_color='black', hover_line_width=5
    )

    # --- Hover tooltip ---
    p.add_tools(HoverTool(
        tooltips=hovfun("@category: <b>@value</b>"),
        show_arrow=False,
        point_policy="follow_mouse"
    ))
    add_extras(p, tth = tth,cross=0)
    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.legend.location = "center_right"
    p.legend.click_policy = 'none'
    p.legend.background_fill_alpha = 0.0
    p.legend.border_line_alpha = 0.0
    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None     # disables pan or box zoom
    p.toolbar.active_scroll = None   # disables wheel zoom


    if tth==1:
        if bgc is None:
            bgc="#3d3d3d"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(243, 192, 97, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid orange'}
    else:
        if bgc is None:
            bgc="#fff6c0"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(165, 221, 253, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid deepskyblue'}
    
    if sh == 1:
        show(p)
    
    return p




import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

def rounded_annular_wedge_patch(center, inner_radius, outer_radius, start_angle, end_angle, 
                               corner_radius=0.05, n_points=80, gap_width=0):
    cx, cy = center
    if gap_width > 0:
        inner_gap_angle = gap_width / inner_radius / 2.5
        outer_gap_angle = gap_width / outer_radius / 2
        start_angle_inner = start_angle + inner_gap_angle
        end_angle_inner = end_angle - inner_gap_angle
        start_angle_outer = start_angle + outer_gap_angle  
        end_angle_outer = end_angle - outer_gap_angle
    else:
        start_angle_inner = start_angle_outer = start_angle
        end_angle_inner = end_angle_outer = end_angle
    corner_points = 15
    angular_corner_offset_inner = corner_radius / inner_radius
    angular_corner_offset_outer = corner_radius / outer_radius
    outer_start_adj = start_angle_outer + angular_corner_offset_outer
    outer_end_adj = end_angle_outer - angular_corner_offset_outer
    if outer_end_adj > outer_start_adj:
        outer_angles = np.linspace(outer_start_adj, outer_end_adj, n_points)
        x_outer = cx + outer_radius * np.cos(outer_angles)
        y_outer = cy + outer_radius * np.sin(outer_angles)
    else:
        x_outer = np.array([])
        y_outer = np.array([])
    inner_start_adj = end_angle_inner - angular_corner_offset_inner
    inner_end_adj = start_angle_inner + angular_corner_offset_inner
    if inner_start_adj > inner_end_adj:
        inner_angles = np.linspace(inner_start_adj, inner_end_adj, n_points)
        x_inner = cx + inner_radius * np.cos(inner_angles)
        y_inner = cy + inner_radius * np.sin(inner_angles)
    else:
        x_inner = np.array([])
        y_inner = np.array([])
    # Corners
    corner1_center_x = cx + (outer_radius - corner_radius) * np.cos(start_angle_outer)
    corner1_center_y = cy + (outer_radius - corner_radius) * np.sin(start_angle_outer)
    c1_start = start_angle_outer - np.pi/2
    c1_end = start_angle_outer
    c1_angles = np.linspace(c1_start, c1_end, corner_points)
    x_c1 = corner1_center_x + corner_radius * np.cos(c1_angles)
    y_c1 = corner1_center_y + corner_radius * np.sin(c1_angles)
    corner2_center_x = cx + (outer_radius - corner_radius) * np.cos(end_angle_outer)
    corner2_center_y = cy + (outer_radius - corner_radius) * np.sin(end_angle_outer)
    c2_start = end_angle_outer
    c2_end = end_angle_outer + np.pi/2
    c2_angles = np.linspace(c2_start, c2_end, corner_points)
    x_c2 = corner2_center_x + corner_radius * np.cos(c2_angles)
    y_c2 = corner2_center_y + corner_radius * np.sin(c2_angles)
    corner3_center_x = cx + (inner_radius + corner_radius) * np.cos(end_angle_inner)
    corner3_center_y = cy + (inner_radius + corner_radius) * np.sin(end_angle_inner)
    c3_start = end_angle_inner + np.pi/2
    c3_end = end_angle_inner + np.pi
    c3_angles = np.linspace(c3_start, c3_end, corner_points)
    x_c3 = corner3_center_x + corner_radius * np.cos(c3_angles)
    y_c3 = corner3_center_y + corner_radius * np.sin(c3_angles)
    corner4_center_x = cx + (inner_radius + corner_radius) * np.cos(start_angle_inner)
    corner4_center_y = cy + (inner_radius + corner_radius) * np.sin(start_angle_inner)
    c4_start = start_angle_inner + np.pi
    c4_end = start_angle_inner + 3*np.pi/2
    c4_angles = np.linspace(c4_start, c4_end, corner_points)
    x_c4 = corner4_center_x + corner_radius * np.cos(c4_angles)
    y_c4 = corner4_center_y + corner_radius * np.sin(c4_angles)
    x_patch = np.concatenate([
        x_c1, x_outer, x_c2, x_c3, x_inner, x_c4
    ])
    y_patch = np.concatenate([
        y_c1, y_outer, y_c2, y_c3, y_inner, y_c4
    ])
    return x_patch, y_patch

def plot_rounded_annular_wedges(
    data, labels=None, colors=None, center=(0.3,0),tth=1,bgc=None,sh=1,width=800,height=600,
    inner_radius=0.5, outer_radius=1.0, corner_radius=0.08, gap_width=0.19, n_points=80,
    title="Rounded Doughnut Chart",legend_y=0.2
):
    total = sum(data)
    N = len(data)
    if not colors:
        colors = ["gold", "lime", "dodgerblue", "purple", "orange", "cyan", "magenta"]
    colors = (colors * ((N + len(colors) - 1) // len(colors)))[:N]
    if not labels:
        labels = [f"Piece {i+1}" for i in range(N)]
    angles = [2*np.pi*v/total for v in data]
    start_angle = np.deg2rad(30)
    starts = [start_angle]
    for a in angles[:-1]:
        starts.append(starts[-1] + a)
    ends = [s + a for s, a in zip(starts, angles)]
    percents = [f"{int(round(100 * v / total))}%" for v in data]

    xs, ys = [], []
    for s, e in zip(starts, ends):
        x, y = rounded_annular_wedge_patch(
            center, inner_radius, outer_radius, s, e, corner_radius, n_points, gap_width=gap_width
        )
        xs.append(x.tolist())
        ys.append(y.tolist())

    source = ColumnDataSource(data=dict(
        xs=xs, ys=ys, label=labels, percent=percents, color=colors
    ))

    p = figure(width=width, height=height, x_range=(-1.2, 1.8), y_range=(-1.1, 1.1),
               match_aspect=True, title=title)
    patches_renderer = p.patches('xs', 'ys', source=source,
                                 fill_color='color', fill_alpha=1,
                                 line_color="white", line_width=2,
                                 hover_line_color='black', hover_line_width=3)

    hover = HoverTool(
        tooltips=hovfun("@label: <b>@percent</b>"),
        show_arrow=False,
        point_policy="follow_mouse",
        renderers=[patches_renderer]
    )
    p.add_tools(hover)

    # Percentage text labels
    label_coords_x = []
    label_coords_y = []
    for s, e in zip(starts, ends):
        mid_angle = (s + e) / 2
        r_label = (inner_radius + outer_radius) / 2
        lx = center[0] + r_label * np.cos(mid_angle)
        ly = center[1] + r_label * np.sin(mid_angle)
        label_coords_x.append(lx)
        label_coords_y.append(ly)

    p.text(
        x=label_coords_x,
        y=label_coords_y,
        text=percents,
        text_align="center",
        text_baseline="middle",
        text_font_size="14pt",
        text_color="black",
        text_font_style="bold"
    )
    # Custom legend (top right)
    legend_x = 0.14#1.22
    legend_y = legend_y#0.2#0.8
    legend_spacing = 0.1
    for i, (c, lbl) in enumerate(zip(colors, labels)):
        y_pos = legend_y - i * legend_spacing
        p.scatter([legend_x], [y_pos], size=18, color=c, alpha=0.7)
        p.text([legend_x + 0.09], [y_pos], text=[lbl], text_align="left", text_color="grey", text_baseline="middle", text_font_size="13pt")

    add_extras(p, tth = tth,cross=0)
    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None

    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None     # disables pan or box zoom
    p.toolbar.active_scroll = None   # disables wheel zoom
    p.min_border_right=0
    p.min_border_bottom=0

    if tth==1:
        if bgc is None:
            bgc="#3d3d3d"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(243, 192, 97, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid orange'}
    else:
        if bgc is None:
            bgc="#fff6c0"
        p.styles = {'margin-top': '0px','margin-left': '0px','border-radius': '10px','box-shadow': '0 18px 20px rgba(165, 221, 253, 0.2)','padding': '5px','background-color': bgc,'border': '1.5px solid deepskyblue'}
    
    if sh == 1:
        show(p)
    
    return p


import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Whisker, HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10, Turbo256

def fboxplot_basic(df, xcol, ycol, group_col=None, tth=1,
                   title="Boxplot", palette=None,
                   width=800, height=500,
                   bgc=None, sh=1, show_legend=True):
    """
    Create a simple Bokeh boxplot from a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input data containing category and numeric columns.
    xcol : str
        Name of the categorical column (x-axis).
    ycol : str
        Name of the numeric column (y-axis).
    group_col : str, optional
        Name of grouping column (e.g., 'Continent'). If provided, will color by group.
    tth : int
        Theme type (1=dark/orange, 0=light/blue).
    title : str
        Plot title.
    palette : dict or list
        If group_col provided: dict mapping group names to colors.
        Otherwise: list of colors for each category.
    width, height : int
        Figure size.
    bgc : str
        Background color.
    sh : int
        Whether to display the figure with show().
    show_legend : bool
        Whether to display the legend (default True).
    """

    # --- Prep ---
    if group_col is not None:
        d = df[[xcol, ycol, group_col]].dropna().rename(columns={xcol: "x", ycol: "y", group_col: "group"})
        # Create composite key for x-axis (station + group)
        d['x_group'] = d['x'].astype(str) + ' (' + d['group'].astype(str) + ')'
        cats = list(d["x_group"].unique())
    else:
        d = df[[xcol, ycol]].dropna().rename(columns={xcol: "x", ycol: "y"})
        d['x_group'] = d['x']
        cats = list(d["x"].unique())

    # --- Compute quartiles and whiskers ---
    qs = d.groupby("x_group")["y"].quantile([0.25, 0.5, 0.75]).unstack().reset_index()
    qs.columns = ["x_group", "q1", "q2", "q3"]
    
    # Add group info back to qs
    if group_col is not None:
        qs = qs.merge(d[['x_group', 'group']].drop_duplicates(), on='x_group', how='left')
    
    iqr = qs.q3 - qs.q1
    qs["upper"] = qs.q3 + 1.5 * iqr
    qs["lower"] = qs.q1 - 1.5 * iqr

    # Clamp whiskers to actual data
    mins = d.groupby("x_group")["y"].min()
    maxs = d.groupby("x_group")["y"].max()
    qs["upper"] = np.minimum(qs["upper"], qs["x_group"].map(maxs))
    qs["lower"] = np.maximum(qs["lower"], qs["x_group"].map(mins))

    # --- Outliers ---
    merged = d.merge(qs[["x_group", "lower", "upper"]], on="x_group", how="left")
    outliers = merged[~merged.y.between(merged.lower, merged.upper)]

    # --- Palette ---
    if group_col is not None and palette is not None:
        # Use provided palette dict for groups
        qs['color'] = qs['group'].map(palette)
    else:
        n = len(cats)
        if palette is None:
            palette = [Turbo256[i] for i in np.linspace(0, 255, n, dtype=int)]
        elif isinstance(palette, str) and palette == "Category10":
            palette = Category10[n] if n <= 10 else [Category10[10][i % 10] for i in range(n)]
        qs['color'] = [palette[i % len(palette)] for i in range(len(qs))]

    # --- Sources ---
    src = ColumnDataSource(qs)
    src_out = ColumnDataSource(outliers)

    # --- Figure ---
    p = figure(
        x_range=cats, width=width, height=height,
        title=title, background_fill_color=bgc,
        y_axis_label=ycol
    )
    
    if tth == 1:
        llc = 'white'
    else:
        llc = 'black'
    
    # --- Whiskers ---
    whisker = Whisker(base="x_group", upper="upper", lower="lower", source=src, line_color=llc)
    whisker.upper_head.size = whisker.lower_head.size = 12
    whisker.upper_head.line_color = whisker.lower_head.line_color = llc
    p.add_layout(whisker)

    # --- Boxes ---
    if show_legend and group_col is not None:
        r1 = p.vbar(x="x_group", width=0.7, top="q3", bottom="q2",
                    source=src, fill_color='color', line_color=llc,
                    legend_field="group")
        r2 = p.vbar(x="x_group", width=0.7, top="q2", bottom="q1",
                    source=src, fill_color='color', line_color=llc,
                    legend_field="group")
    else:
        r1 = p.vbar(x="x_group", width=0.7, top="q3", bottom="q2",
                    source=src, fill_color='color', line_color=llc)
        r2 = p.vbar(x="x_group", width=0.7, top="q2", bottom="q1",
                    source=src, fill_color='color', line_color=llc)

    # Median line
    p.segment(x0="x_group", y0="q2", x1="x_group", y1="q2",
              line_color=llc, line_width=3, source=src)

    # --- Outliers ---
    if not outliers.empty:
        p.scatter(x="x_group", y="y", source=src_out, size=6, color="grey", alpha=0.8)

    # --- Hover ---
    hover_template = """
        <b>Category:</b> @x_group <br>
        <b>Q1:</b> @q1{0.0} <br>
        <b>Median:</b> @q2{0.0} <br>
        <b>Q3:</b> @q3{0.0} <br>
        <b>Lower:</b> @lower{0.0} <br>
        <b>Upper:</b> @upper{0.0}
    """
    if group_col is not None:
        hover_template = """
        <b>Group:</b> @group <br>
        """ + hover_template
    
    p.add_tools(HoverTool(
        tooltips=hovfun(hover_template),
        show_arrow=False, 
        point_policy="follow_mouse",
        renderers=[r1, r2]
    ))
    add_extras(p, tth=tth, cross=0)
    # --- Legend configuration ---
    if show_legend and group_col is not None:
        # p.legend.location = "center_right"
        p.legend.click_policy = "none"


    # --- Style tweaks ---
    p.xaxis.major_label_orientation = 0.8  # Rotate labels for readability
    
    if tth == 1:
        if bgc is None:
            bgc = "#343838"
        p.styles = {
            'margin-top': '0px', 'margin-left': '0px', 'border-radius': '10px',
            'box-shadow': '0 18px 20px rgba(243, 192, 97, 0.2)', 'padding': '5px',
            'background-color': bgc, 'border': '1.5px solid orange'
        }
    else:
        if bgc is None:
            bgc = "white"
        p.styles = {
            'margin-top': '0px', 'margin-left': '0px', 'border-radius': '10px',
            'box-shadow': '0 18px 20px rgba(165, 221, 253, 0.2)', 'padding': '5px',
            'background-color': bgc, 'border': '1.5px solid deepskyblue'
        }
    
    if sh == 1:
        show(p)
    
    return p



import numpy as np
from bokeh.io import show
from bokeh.models import Label, HoverTool, ColumnDataSource, CustomJS, Div
from bokeh.plotting import figure
from bokeh.layouts import column


def create_sankey(
    flows,
    source_colors=None,
    target_colors=None,
    title="Sankey Diagram",
    width=1500,
    height=700,
    flow_alpha=0.4,
    node_alpha=0.9,
    interactive=True
):
    """
    Create an interactive Sankey diagram with smooth bezier ribbons and hover effects.
    
    Parameters:
    -----------
    flows : list of dict
        Each dict must have 'source', 'target', and 'value' keys.
    source_colors : dict, optional
        Colors for source nodes. Auto-generated if None.
    target_colors : dict, optional
        Colors for target nodes. Auto-generated if None.
    title : str
        Plot title
    width : int
        Plot width in pixels
    height : int
        Plot height in pixels
    flow_alpha : float
        Base transparency of flow ribbons (0-1)
    node_alpha : float
        Transparency of nodes (0-1)
    interactive : bool
        Enable hover interactions
    
    Returns:
    --------
    bokeh.layouts.Layout or bokeh.plotting.figure
        Interactive Sankey diagram with info panel
    """
    
    # Extract unique sources and targets
    sources = []
    targets = []
    for f in flows:
        if f["source"] not in sources:
            sources.append(f["source"])
        if f["target"] not in targets:
            targets.append(f["target"])
    
    # Auto-generate colors if not provided
    default_source_palette = ["#306998", "#FFD43B", "#9B59B6", "#3498DB", "#E67E22", 
                             "#2ECC71", "#E74C3C", "#95A5A6", "#F39C12", "#1ABC9C"]
    default_target_palette = ["#2C3E50", "#16A085", "#C0392B", "#8E44AD", "#D35400",
                             "#27AE60", "#2980B9", "#7F8C8D", "#F1C40F", "#34495E"]
    
    if source_colors is None:
        source_colors = {s: default_source_palette[i % len(default_source_palette)] 
                        for i, s in enumerate(sources)}
    if target_colors is None:
        target_colors = {t: default_target_palette[i % len(default_target_palette)] 
                        for i, t in enumerate(targets)}
    
    # Calculate totals
    source_totals = {s: sum(f["value"] for f in flows if f["source"] == s) for s in sources}
    target_totals = {t: sum(f["value"] for f in flows if f["target"] == t) for t in targets}
    
    # Layout parameters
    left_x, right_x = 0, 100
    node_width, node_gap = 8, 3
    total_height, padding_y = 100, 5
    
    # Position source nodes
    source_height_total = sum(source_totals.values())
    scale = (total_height - 2 * padding_y - (len(sources) - 1) * node_gap) / source_height_total
    
    source_nodes = {}
    current_y = padding_y
    for s in sources:
        h = source_totals[s] * scale
        source_nodes[s] = {"x": left_x, "y": current_y, "height": h, "value": source_totals[s]}
        current_y += h + node_gap
    
    # Position target nodes
    target_height_total = sum(target_totals.values())
    scale_t = (total_height - 2 * padding_y - (len(targets) - 1) * node_gap) / target_height_total
    
    target_nodes = {}
    current_y = padding_y
    for t in targets:
        h = target_totals[t] * scale_t
        target_nodes[t] = {"x": right_x - node_width, "y": current_y, "height": h, "value": target_totals[t]}
        current_y += h + node_gap
    
    # Create figure
    p = figure(
        width=width, height=height, title=title,
        x_range=(-30, 130), y_range=(-5, 105),
        tools="", toolbar_location=None
    )
    
    # Track flow offsets
    source_offsets = {s: 0 for s in sources}
    target_offsets = {t: 0 for t in targets}
    
    # Store ribbon renderers and sources for interactivity
    ribbon_renderers = []
    ribbon_sources = []
    
    # Draw flows with SMOOTH BEZIER CURVES
    for f in flows:
        src, tgt, value = f["source"], f["target"], f["value"]
        src_node, tgt_node = source_nodes[src], target_nodes[tgt]
        
        src_flow_h = (value / source_totals[src]) * src_node["height"]
        tgt_flow_h = (value / target_totals[tgt]) * tgt_node["height"]
        
        x0 = src_node["x"] + node_width
        y0_bottom = src_node["y"] + source_offsets[src]
        y0_top = y0_bottom + src_flow_h
        
        x1 = tgt_node["x"]
        y1_bottom = tgt_node["y"] + target_offsets[tgt]
        y1_top = y1_bottom + tgt_flow_h
        
        source_offsets[src] += src_flow_h
        target_offsets[tgt] += tgt_flow_h
        
        # SMOOTH BEZIER with more points for smoothness
        t = np.linspace(0, 1, 100)
        cx0, cx1 = x0 + (x1 - x0) * 0.5, x0 + (x1 - x0) * 0.5
        
        # Cubic bezier for x
        x_path = (1-t)**3 * x0 + 3*(1-t)**2*t * cx0 + 3*(1-t)*t**2 * cx1 + t**3 * x1
        
        # Cubic bezier for y (creates smooth S-curve)
        y_bottom = (1-t)**3 * y0_bottom + 3*(1-t)**2*t * y0_bottom + 3*(1-t)*t**2 * y1_bottom + t**3 * y1_bottom
        y_top = (1-t)**3 * y0_top + 3*(1-t)**2*t * y0_top + 3*(1-t)*t**2 * y1_top + t**3 * y1_top
        
        xs = list(x_path) + list(x_path[::-1])
        ys = list(y_top) + list(y_bottom[::-1])
        
        # Create ColumnDataSource for interactivity
        source_data = ColumnDataSource(data={
            'x': [xs],
            'y': [ys],
            'source': [src],
            'target': [tgt],
            'value': [value],
            'alpha': [flow_alpha]
        })
        
        ribbon = p.patches(
            'x', 'y',
            source=source_data,
            fill_color=source_colors[src],
            fill_alpha='alpha',
            line_color=source_colors[src],
            line_alpha='alpha',
            line_width=0.5
        )
        
        ribbon_renderers.append(ribbon)
        ribbon_sources.append(source_data)
    
    # Draw source nodes
    source_node_renderers = []
    source_node_sources = []
    
    for s in sources:
        node = source_nodes[s]
        node_source = ColumnDataSource(data={
            'left': [node["x"]],
            'right': [node["x"] + node_width],
            'bottom': [node["y"]],
            'top': [node["y"] + node["height"]],
            'name': [s],
            'value': [node['value']],
            'type': ['source']
        })
        
        renderer = p.quad(
            left='left', right='right', bottom='bottom', top='top',
            source=node_source,
            fill_color=source_colors[s],
            fill_alpha=node_alpha,
            line_color="white",
            line_width=2,
            hover_fill_alpha=1.0
        )
        
        source_node_renderers.append(renderer)
        source_node_sources.append(node_source)
        
        # Add label
        label = Label(
            x=node["x"] - 1, y=node["y"] + node["height"] / 2,
            text=f"{s} ({node['value']})", text_font_size="22pt",
            text_align="right", text_baseline="middle", text_color="#333"
        )
        p.add_layout(label)
    
    # Draw target nodes
    target_node_renderers = []
    target_node_sources = []
    
    for t in targets:
        node = target_nodes[t]
        node_source = ColumnDataSource(data={
            'left': [node["x"]],
            'right': [node["x"] + node_width],
            'bottom': [node["y"]],
            'top': [node["y"] + node["height"]],
            'name': [t],
            'value': [node['value']],
            'type': ['target']
        })
        
        renderer = p.quad(
            left='left', right='right', bottom='bottom', top='top',
            source=node_source,
            fill_color=target_colors[t],
            fill_alpha=node_alpha,
            line_color="white",
            line_width=2,
            hover_fill_alpha=1.0
        )
        
        target_node_renderers.append(renderer)
        target_node_sources.append(node_source)
        
        # Add label
        label = Label(
            x=node["x"] + node_width + 1, y=node["y"] + node["height"] / 2,
            text=f"{t} ({node['value']})", text_font_size="22pt",
            text_align="left", text_baseline="middle", text_color="#333"
        )
        p.add_layout(label)
    
    # Styling
    p.title.text_font_size = "32pt"
    p.title.align = "center"
    p.xaxis.visible = p.yaxis.visible = False
    p.xgrid.visible = p.ygrid.visible = False
    p.outline_line_color = None
    p.background_fill_color = "#FAFAFA"
    p.border_fill_color = "#FFFFFF"
    
    if not interactive:
        return p
    
    # Add interactive info panel
    info_div = Div(
        text="""
        <div style="
            padding:15px;
            border:2px solid #333;
            border-radius:8px;
            background:#FFF8DC;
            font-family:'Arial', sans-serif;
            font-size:14px;
            color:#333;
            min-height:80px;
        ">
            <b>Hover over flows or nodes to explore</b>
        </div>
        """,
        width=300, margin=(10,10,10,10)
    )
    
    # RIBBON HOVER - highlight specific flow
    ribbon_hover = HoverTool(
        renderers=ribbon_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div),
            code="""
            const r = cb_data.renderer.data_source;
            const i = cb_data.index.indices[0];
            if (i == null) return;
            
            // Dim all ribbons
            for (let k = 0; k < ribbons.length; k++) {
                ribbons[k].data.alpha = [0.08];
                ribbons[k].change.emit();
            }
            
            // Highlight hovered ribbon
            r.data.alpha = [0.85];
            r.change.emit();
            
            // Update info panel
            div.text = `
            <div style="padding:15px;border:2px solid #333;border-radius:8px;background:#FFF8DC;color:#333;">
                <div style="font-size:16px;font-weight:bold;margin-bottom:10px;">Flow Details</div>
                <div style="line-height:1.8;">
                    <b>From:</b> ${r.data.source[0]}<br>
                    <b>To:</b> ${r.data.target[0]}<br>
                    <b>Value:</b> ${r.data.value[0]}
                </div>
            </div>`;
            """
        )
    )
    p.add_tools(ribbon_hover)
    
    # SOURCE NODE HOVER - highlight all outgoing flows
    source_hover = HoverTool(
        renderers=source_node_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div),
            code="""
            const i = cb_data.index.indices[0];
            if (i == null) return;
            
            const node_name = cb_data.renderer.data_source.data.name[i];
            
            let total = 0;
            let count = 0;
            
            for (let k = 0; k < ribbons.length; k++) {
                if (ribbons[k].data.source[0] === node_name) {
                    ribbons[k].data.alpha = [0.8];
                    total += ribbons[k].data.value[0];
                    count++;
                } else {
                    ribbons[k].data.alpha = [0.08];
                }
                ribbons[k].change.emit();
            }
            
            div.text = `
            <div style="padding:15px;border:2px solid #333;border-radius:8px;background:#FFF8DC;color:#333;">
                <div style="font-size:16px;font-weight:bold;margin-bottom:10px;">Source Node</div>
                <div style="line-height:1.8;">
                    <b>Name:</b> ${node_name}<br>
                    <b>Total Output:</b> ${total}<br>
                    <b>Flows:</b> ${count}
                </div>
            </div>`;
            """
        )
    )
    p.add_tools(source_hover)
    
    # TARGET NODE HOVER - highlight all incoming flows
    target_hover = HoverTool(
        renderers=target_node_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div),
            code="""
            const i = cb_data.index.indices[0];
            if (i == null) return;
            
            const node_name = cb_data.renderer.data_source.data.name[i];
            
            let total = 0;
            let count = 0;
            
            for (let k = 0; k < ribbons.length; k++) {
                if (ribbons[k].data.target[0] === node_name) {
                    ribbons[k].data.alpha = [0.8];
                    total += ribbons[k].data.value[0];
                    count++;
                } else {
                    ribbons[k].data.alpha = [0.08];
                }
                ribbons[k].change.emit();
            }
            
            div.text = `
            <div style="padding:15px;border:2px solid #333;border-radius:8px;background:#FFF8DC;color:#333;">
                <div style="font-size:16px;font-weight:bold;margin-bottom:10px;">Target Node</div>
                <div style="line-height:1.8;">
                    <b>Name:</b> ${node_name}<br>
                    <b>Total Input:</b> ${total}<br>
                    <b>Flows:</b> ${count}
                </div>
            </div>`;
            """
        )
    )
    p.add_tools(target_hover)
    
    # Reset on mouse leave
    p.js_on_event('mouseleave', CustomJS(
        args=dict(ribbons=ribbon_sources, div=info_div, base_alpha=flow_alpha),
        code="""
        for (let k = 0; k < ribbons.length; k++) {
            ribbons[k].data.alpha = [base_alpha];
            ribbons[k].change.emit();
        }
        
        div.text = `
        <div style="padding:15px;border:2px solid #333;border-radius:8px;background:#FFF8DC;color:#333;min-height:80px;">
            <b>Hover over flows or nodes to explore</b>
        </div>`;
        """
    ))
    
    return column(p, info_div)




### CONTINUE : MULTI LEVEL SANKEY
import numpy as np
from bokeh.io import show
from bokeh.models import Label, HoverTool, ColumnDataSource, CustomJS, Div, Legend, LegendItem
from bokeh.plotting import figure
from bokeh.layouts import column


def create_alluvial(
    flows_data,
    time_points,
    categories,
    colors=None,
    title="Alluvial Diagram",
    width=1500,
    height=800,
    node_width=0.12,
    gap=2,
    flow_alpha=0.5,
    interactive=True
):
    """
    Create an interactive Alluvial (multi-level Sankey) diagram.
    
    Parameters:
    -----------
    flows_data : list of list of tuples
        Each inner list represents flows between consecutive time points.
        Each tuple: (from_category, to_category, value)
        Example: [[("A", "B", 10), ("A", "C", 5)], [("B", "C", 8), ...]]
    time_points : list of str
        Labels for each time point
    categories : list of str
        All unique categories across time points
    colors : dict, optional
        Color mapping for categories {category: hex_color}
    title : str
        Plot title
    width : int
        Plot width in pixels
    height : int
        Plot height in pixels
    node_width : float
        Width of nodes
    gap : float
        Gap between nodes as percentage of total height (0-100)
    flow_alpha : float
        Transparency of flows
    interactive : bool
        Enable hover interactions
    
    Returns:
    --------
    bokeh.layouts.Layout or bokeh.plotting.figure
        Alluvial diagram
    """
    
    # Auto-generate colors if not provided
    if colors is None:
        default_palette = ["#306998", "#D62728", "#FFD43B", "#7F7F7F", "#2ECC71", 
                          "#3498DB", "#E67E22", "#9B59B6", "#1ABC9C", "#F39C12"]
        colors = {cat: default_palette[i % len(default_palette)] 
                 for i, cat in enumerate(categories)}
    
    # Calculate node heights at each time point (in flow units)
    node_heights = []
    for t_idx in range(len(time_points)):
        heights = {}
        if t_idx == 0:
            # First time point: sum outgoing flows
            for cat in categories:
                heights[cat] = sum(f[2] for f in flows_data[0] if f[0] == cat)
        elif t_idx == len(time_points) - 1:
            # Last time point: sum incoming flows
            for cat in categories:
                heights[cat] = sum(f[2] for f in flows_data[-1] if f[1] == cat)
        else:
            # Middle time points: sum incoming flows from previous
            for cat in categories:
                heights[cat] = sum(f[2] for f in flows_data[t_idx - 1] if f[1] == cat)
        node_heights.append(heights)
    
    # Find max total flow at any time point
    max_total_flow = 0
    for t_idx in range(len(time_points)):
        total = sum(node_heights[t_idx].get(cat, 0) for cat in categories)
        max_total_flow = max(max_total_flow, total)
    
    # Count active categories at each time point for gap calculation
    num_active_categories = []
    for t_idx in range(len(time_points)):
        count = sum(1 for cat in categories if node_heights[t_idx].get(cat, 0) > 0)
        num_active_categories.append(count)
    
    max_active = max(num_active_categories)
    
    # Target y-range is 70% of figure height
    target_y_range = height * 0.7
    
    # Calculate gap size in scaled units
    # gap parameter is percentage, convert to actual units
    gap_size = target_y_range * (gap / 100.0)
    total_gap = gap_size * (max_active - 1) if max_active > 1 else 0
    
    # Available space for nodes
    available_for_nodes = target_y_range - total_gap
    
    # Scale factor converts flow units to display units
    scale_factor = available_for_nodes / max_total_flow if max_total_flow > 0 else 1
    
    # Calculate x positions evenly spaced
    x_positions = list(range(len(time_points)))
    
    # Calculate node positions in scaled coordinates
    node_positions = []
    max_y = 0
    for t_idx in range(len(time_points)):
        positions = {}
        y_cursor = 0
        for cat in categories:
            height_flow = node_heights[t_idx].get(cat, 0)
            height_scaled = height_flow * scale_factor
            positions[cat] = {
                "y_start": y_cursor, 
                "y_end": y_cursor + height_scaled,
                "value": height_flow  # Store original value
            }
            if height_scaled > 0:
                y_cursor += height_scaled + gap_size
            else:
                y_cursor += 0
        node_positions.append(positions)
        max_y = max(max_y, y_cursor)
    
    # Create figure with proper ranges
    x_margin = 1
    y_margin = max_y * 0.15
    
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-x_margin, len(time_points) - 1 + x_margin),
        y_range=(-y_margin, max_y + y_margin),
        tools="",
        toolbar_location=None,
    )
    
    # Style
    p.title.text_font_size = "20pt"
    p.title.align = "center"
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.xaxis.visible = False
    p.yaxis.visible = False
    p.outline_line_color = None
    p.background_fill_color = "#FAFAFA"
    
    # Store ribbon data for interactivity
    ribbon_renderers = []
    ribbon_sources = []
    
    # Draw flows between consecutive time points
    n_points = 100
    t_param = np.linspace(0, 1, n_points)
    
    for t_idx, flows in enumerate(flows_data):
        x_start = x_positions[t_idx] + node_width / 2
        x_end = x_positions[t_idx + 1] - node_width / 2
        
        # Track current position for stacking
        source_cursors = {cat: node_positions[t_idx][cat]["y_start"] for cat in categories}
        target_cursors = {cat: node_positions[t_idx + 1][cat]["y_start"] for cat in categories}
        
        for from_cat, to_cat, value in flows:
            if value == 0:
                continue
            
            # Scale the value for visual display
            scaled_value = value * scale_factor
            
            # Source coordinates
            y_src_bottom = source_cursors[from_cat]
            y_src_top = y_src_bottom + scaled_value
            source_cursors[from_cat] = y_src_top
            
            # Target coordinates
            y_tgt_bottom = target_cursors[to_cat]
            y_tgt_top = y_tgt_bottom + scaled_value
            target_cursors[to_cat] = y_tgt_top
            
            # Bezier control points
            cx0 = x_start + (x_end - x_start) / 3
            cx1 = x_start + 2 * (x_end - x_start) / 3
            
            # Top edge bezier
            x_top = ((1 - t_param) ** 3 * x_start +
                    3 * (1 - t_param) ** 2 * t_param * cx0 +
                    3 * (1 - t_param) * t_param ** 2 * cx1 +
                    t_param ** 3 * x_end)
            y_top = ((1 - t_param) ** 3 * y_src_top +
                    3 * (1 - t_param) ** 2 * t_param * y_src_top +
                    3 * (1 - t_param) * t_param ** 2 * y_tgt_top +
                    t_param ** 3 * y_tgt_top)
            
            # Bottom edge bezier
            x_bottom = ((1 - t_param) ** 3 * x_start +
                       3 * (1 - t_param) ** 2 * t_param * cx0 +
                       3 * (1 - t_param) * t_param ** 2 * cx1 +
                       t_param ** 3 * x_end)
            y_bottom = ((1 - t_param) ** 3 * y_src_bottom +
                       3 * (1 - t_param) ** 2 * t_param * y_src_bottom +
                       3 * (1 - t_param) * t_param ** 2 * y_tgt_bottom +
                       t_param ** 3 * y_tgt_bottom)
            
            # Create closed polygon
            xs = list(x_top) + list(x_bottom[::-1])
            ys = list(y_top) + list(y_bottom[::-1])
            
            # Create data source (store ORIGINAL value for display)
            source_data = ColumnDataSource(data={
                'x': [xs],
                'y': [ys],
                'from': [from_cat],
                'to': [to_cat],
                'value': [value],  # Original unscaled value
                'time_from': [time_points[t_idx]],
                'time_to': [time_points[t_idx + 1]],
                'alpha': [flow_alpha]
            })
            
            ribbon = p.patches(
                'x', 'y',
                source=source_data,
                fill_color=colors[from_cat],
                fill_alpha='alpha',
                line_color=colors[from_cat],
                line_alpha='alpha',
                line_width=0.5
            )
            
            ribbon_renderers.append(ribbon)
            ribbon_sources.append(source_data)
    
    # Draw nodes and collect for legend
    legend_renderers = {}
    node_renderers = []
    node_sources = []
    
    for t_idx in range(len(time_points)):
        x = x_positions[t_idx]
        for cat in categories:
            y_start = node_positions[t_idx][cat]["y_start"]
            y_end = node_positions[t_idx][cat]["y_end"]
            value_original = node_positions[t_idx][cat]["value"]
            
            if y_end > y_start:
                node_source = ColumnDataSource(data={
                    'left': [x - node_width / 2],
                    'right': [x + node_width / 2],
                    'bottom': [y_start],
                    'top': [y_end],
                    'category': [cat],
                    'time_idx': [t_idx],
                    'value': [value_original]  # Store original value
                })
                
                renderer = p.quad(
                    left='left', right='right', bottom='bottom', top='top',
                    source=node_source,
                    fill_color=colors[cat],
                    fill_alpha=0.9,
                    line_color="white",
                    line_width=2,
                    hover_fill_alpha=1.0
                )
                
                node_renderers.append(renderer)
                node_sources.append(node_source)
                
                # Collect for legend (one per category)
                if cat not in legend_renderers:
                    legend_renderers[cat] = renderer
                
                # Add labels on first and last time points (with original values)
                if t_idx == 0:
                    label = Label(
                        x=x - node_width / 2 - 0.03,
                        y=(y_start + y_end) / 2,
                        text=f"{cat} ({int(value_original)})",
                        text_font_size="11pt",
                        text_baseline="middle",
                        text_align="right",
                        text_color="#333333",
                    )
                    p.add_layout(label)
                elif t_idx == len(time_points) - 1:
                    label = Label(
                        x=x + node_width / 2 + 0.03,
                        y=(y_start + y_end) / 2,
                        text=f"{cat} ({int(value_original)})",
                        text_font_size="11pt",
                        text_baseline="middle",
                        text_color="#333333",
                    )
                    p.add_layout(label)
    
    # Add time point labels
    for t_idx, t in enumerate(time_points):
        label = Label(
            x=x_positions[t_idx],
            y=-y_margin * 0.5,
            text=t,
            text_font_size="14pt",
            text_align="center",
            text_baseline="top",
            text_color="#333333",
            text_font_style="bold",
        )
        p.add_layout(label)
    
    # Create legend on the right
    legend_items = [LegendItem(label=cat, renderers=[legend_renderers[cat]]) 
                   for cat in categories if cat in legend_renderers]
    legend = Legend(
        items=legend_items,
        location="center",
        label_text_font_size="11pt",
        glyph_width=20,
        glyph_height=20,
        spacing=8,
        padding=12,
        background_fill_alpha=0.9,
        background_fill_color="white",
        border_line_color="#cccccc",
    )
    p.add_layout(legend, "right")
    
    if not interactive:
        return p
    
    # Add interactivity
    info_div = Div(
        text="""
        <div style="padding:12px;border:2px solid #333;border-radius:6px;
                    background:#FFF8DC;font-family:Arial;font-size:13px;color:#333;">
            <b>Hover over flows or nodes</b>
        </div>
        """,
        width=280, margin=(10,10,10,10)
    )
    
    # Ribbon hover
    ribbon_hover = HoverTool(
        renderers=ribbon_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div),
            code="""
            const i = cb_data.index.indices[0];
            if (i == null) return;
            const r = cb_data.renderer.data_source;
            
            for (let k = 0; k < ribbons.length; k++) {
                ribbons[k].data.alpha = [0.05];
                ribbons[k].change.emit();
            }
            
            r.data.alpha = [0.85];
            r.change.emit();
            
            div.text = `
            <div style="padding:12px;border:2px solid #333;border-radius:6px;background:#FFF8DC;color:#333;">
                <b>Flow: ${r.data.time_from[0]} → ${r.data.time_to[0]}</b><br><br>
                <b>From:</b> ${r.data.from[0]}<br>
                <b>To:</b> ${r.data.to[0]}<br>
                <b>Value:</b> ${r.data.value[0]}
            </div>`;
            """
        )
    )
    p.add_tools(ribbon_hover)
    
    # Node hover
    node_hover = HoverTool(
        renderers=node_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div, time_points=time_points),
            code="""
            const i = cb_data.index.indices[0];
            if (i == null) return;
            const node = cb_data.renderer.data_source.data;
            const cat = node.category[i];
            const t_idx = node.time_idx[i];
            
            let highlighted = 0;
            for (let k = 0; k < ribbons.length; k++) {
                const r = ribbons[k].data;
                if (r.from[0] === cat || r.to[0] === cat) {
                    ribbons[k].data.alpha = [0.75];
                    highlighted++;
                } else {
                    ribbons[k].data.alpha = [0.05];
                }
                ribbons[k].change.emit();
            }
            
            div.text = `
            <div style="padding:12px;border:2px solid #333;border-radius:6px;background:#FFF8DC;color:#333;">
                <b>${cat}</b> at <b>${time_points[t_idx]}</b><br><br>
                <b>Value:</b> ${node.value[i]}<br>
                <b>Connected flows:</b> ${highlighted}
            </div>`;
            """
        )
    )
    p.add_tools(node_hover)
    
    # Reset on mouse leave
    p.js_on_event('mouseleave', CustomJS(
        args=dict(ribbons=ribbon_sources, div=info_div, base_alpha=flow_alpha),
        code="""
        for (let k = 0; k < ribbons.length; k++) {
            ribbons[k].data.alpha = [base_alpha];
            ribbons[k].change.emit();
        }
        div.text = `<div style="padding:12px;border:2px solid #333;border-radius:6px;
                     background:#FFF8DC;color:#333;"><b>Hover over flows or nodes</b></div>`;
        """
    ))
    
    return column(p, info_div)







import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, CustomJS, GlobalInlineStyleSheet
from bokeh.palettes import Category20
from bokeh.layouts import column, row
from bokeh.models import Div

def get_dark_stylesheet():
    """Create a new dark theme stylesheet instance."""
    return GlobalInlineStyleSheet(css="""
        html, body, .bk, .bk-root {
            background-color: #343838; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: white; 
            font-family: 'Consolas', 'Courier New', monospace; 
        }
        .bk { color: white; }
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers,
        .bk-label, .bk-title, .bk-legend, .bk-axis-label {
            color: white !important; 
        }
        .bk-input::placeholder { color: #aaaaaa !important; }
    """)

def get_light_stylesheet():
    """Create a new light theme stylesheet instance."""
    return GlobalInlineStyleSheet(css="""
        html, body, .bk, .bk-root {
            background-color: #f3f3f3; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: black; 
            font-family: 'Consolas', 'Courier New', monospace; 
        }
        .bk { color: black; }
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers,
        .bk-label, .bk-title, .bk-legend, .bk-axis-label {
            color: black !important; 
        }
        .bk-input::placeholder { color: #555555 !important; }
    """)

def create_chord_diagram(matrix, labels, colors=None, title="Chord Diagram", width=800, height=800, dark_mode=False):
    """
    Create an interactive chord diagram using Bokeh.
    
    Parameters:
    -----------
    matrix : 2D array-like
        Square matrix representing connections between nodes
    labels : list of str
        Labels for each node
    colors : list of str, optional
        Colors for each node (hex format)
    title : str
        Title of the diagram
    width : int
        Width of the plot
    height : int
        Height of the plot
    dark_mode : bool
        Enable dark theme
    
    Returns:
    --------
    bokeh.layouts.Layout
        Bokeh layout containing the chord diagram
    """
    n = len(labels)
    matrix = np.array(matrix)
    
    # Theme colors
    if dark_mode:
        bg_color = "#343838"
        text_color = "white"
        border_color = "#666"
        info_bg = "#2a2a2a"
        line_color = "#555"
    else:
        bg_color = "#f3f3f3"
        text_color = "black"
        border_color = "#333"
        info_bg = "#FFF8DC"
        line_color = "#CCC"
    
    # Generate colors if not provided
    if colors is None:
        colors = Category20[20][:n] if n <= 20 else Category20[20] * (n // 20 + 1)
    
    # Calculate outgoing total for each node
    outgoing = matrix.sum(axis=1)
    total_flow = outgoing.sum()
    
    # Create arc positions based on outgoing flow
    gap = 0.03
    total_gap = gap * n
    arc_positions = []
    current_pos = 0
    hover_state = ColumnDataSource(data=dict(active=["none"]))

    for i in range(n):
        arc_length = (outgoing[i] / total_flow) * (2 * np.pi - total_gap) if total_flow > 0 else 0
        arc_positions.append({
            'start': current_pos,
            'end': current_pos + arc_length,
            'mid': current_pos + arc_length / 2,
            'label': labels[i],
            'color': colors[i],
            'value': outgoing[i]
        })
        current_pos += arc_length + gap
    
    # Create plot
    p = figure(width=width, height=height, title=title,
               x_range=(-1.4, 1.4), y_range=(-1.4, 1.4),
               toolbar_location=None, match_aspect=True)
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.background_fill_color = bg_color
    p.border_fill_color = bg_color
    p.title.text_color = text_color
    p.title.text_font = "'Consolas', 'Courier New', monospace"
    p.title.text_font_size = "18pt"
    
    # Store all ribbon renderers and data sources
    ribbon_renderers = []
    ribbon_sources = []
    
    # Draw ribbons first
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] > 0:
                src_arc = arc_positions[i]
                dst_arc = arc_positions[j]
                
                # Calculate source position (outgoing)
                offset_i = matrix[i][:j].sum()
                src_start_angle = src_arc['start'] + (offset_i / outgoing[i]) * (src_arc['end'] - src_arc['start']) if outgoing[i] > 0 else src_arc['start']
                src_end_angle = src_start_angle + (matrix[i][j] / outgoing[i]) * (src_arc['end'] - src_arc['start']) if outgoing[i] > 0 else src_start_angle
                
                # Calculate destination position (incoming)
                incoming_j = matrix[:, j]
                offset_j = incoming_j[:i].sum()
                dst_start_angle = dst_arc['start'] + (offset_j / incoming_j.sum()) * (dst_arc['end'] - dst_arc['start']) if incoming_j.sum() > 0 else dst_arc['start']
                dst_end_angle = dst_start_angle + (matrix[i][j] / incoming_j.sum()) * (dst_arc['end'] - dst_arc['start']) if incoming_j.sum() > 0 else dst_start_angle
                
                # Create ribbon with quadratic bezier curves
                r = 0.85
                
                # Source edge points
                src_angles = np.linspace(src_start_angle, src_end_angle, 20)
                src_x = r * np.cos(src_angles)
                src_y = r * np.sin(src_angles)
                
                # Destination edge points
                dst_angles = np.linspace(dst_end_angle, dst_start_angle, 20)
                dst_x = r * np.cos(dst_angles)
                dst_y = r * np.sin(dst_angles)
                
                # Create bezier curve
                t = np.linspace(0, 1, 30)
                
                src_x_end = r * np.cos(src_end_angle)
                src_y_end = r * np.sin(src_end_angle)
                dst_x_start = r * np.cos(dst_start_angle)
                dst_y_start = r * np.sin(dst_start_angle)
                
                curve1_x = (1-t)**2 * src_x_end + 2*(1-t)*t * 0 + t**2 * dst_x_start
                curve1_y = (1-t)**2 * src_y_end + 2*(1-t)*t * 0 + t**2 * dst_y_start
                
                dst_x_end = r * np.cos(dst_end_angle)
                dst_y_end = r * np.sin(dst_end_angle)
                src_x_start = r * np.cos(src_start_angle)
                src_y_start = r * np.sin(src_start_angle)
                
                curve2_x = (1-t)**2 * dst_x_end + 2*(1-t)*t * 0 + t**2 * src_x_start
                curve2_y = (1-t)**2 * dst_y_end + 2*(1-t)*t * 0 + t**2 * src_y_start
                
                # Build complete ribbon path
                ribbon_x = np.concatenate([src_x, curve1_x, dst_x, curve2_x])
                ribbon_y = np.concatenate([src_y, curve1_y, dst_y, curve2_y])
                
                source = ColumnDataSource(data=dict(
                    x=[ribbon_x], 
                    y=[ribbon_y],
                    source=[labels[i]],
                    target=[labels[j]],
                    value=[f"{matrix[i][j]:.1f}"],
                    source_idx=[i],
                    target_idx=[j]
                ))
                
                source.data['alpha'] = [0.35]

                ribbon = p.patches(
                    'x', 'y',
                    source=source,
                    fill_color=colors[i],
                    fill_alpha='alpha',
                    line_color=None
                )
                
                ribbon_renderers.append(ribbon)
                ribbon_sources.append(source)
    
    info_div = Div(
        text=f"""
        <div style="
            padding:10px;
            border:2px solid {border_color};
            border-radius:6px;
            background:{info_bg};
            font-family:'Consolas', 'Courier New', monospace;
            font-size:13px;
            width:200px;
            color:{text_color};
        ">
            <b></b>
        </div>
        """,
        width=200, margin=(-40,10,10,10)
    )

    # Create hover tool for ribbons
    ribbon_hover = HoverTool(
        renderers=ribbon_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div, state=hover_state, 
                     border_color=border_color, info_bg=info_bg, text_color=text_color),
            code="""
            state.data.active[0] = "ribbon";
            state.change.emit();

            const r = cb_data.renderer.data_source;
            const i = cb_data.index.indices[0];
            if (i == null) return;

            for (let k = 0; k < ribbons.length; k++) {
                ribbons[k].data.alpha = [0.05];
            }

            r.data.alpha = [0.8];

            for (let k = 0; k < ribbons.length; k++) {
                ribbons[k].change.emit();
            }

            div.text = `
            <div style="padding:10px;border:2px solid ${border_color};border-radius:6px;background:${info_bg};color:${text_color};font-family:'Consolas', 'Courier New', monospace;">
                <b>From:</b> ${r.data.source[i]}<br>
                <b>To:</b> ${r.data.target[i]}<br>
                <b>Value:</b> ${r.data.value[i]}
            </div>`;
            """
        )
    )
    p.add_tools(ribbon_hover)
    
    # Store all arc renderers and sources
    arc_renderers = []
    arc_sources = []
    
    # Draw outer arcs
    for i, arc in enumerate(arc_positions):
        if arc['end'] > arc['start']:
            theta = np.linspace(arc['start'], arc['end'], 100)
            outer_r = 1.0
            inner_r = 0.85
            
            x_outer = outer_r * np.cos(theta)
            y_outer = outer_r * np.sin(theta)
            x_inner = inner_r * np.cos(theta[::-1])
            y_inner = inner_r * np.sin(theta[::-1])
            
            x_arc = np.concatenate([x_outer, x_inner])
            y_arc = np.concatenate([y_outer, y_inner])
            
            source = ColumnDataSource(data=dict(
                x=[x_arc], 
                y=[y_arc],
                label=[arc['label']],
                value=[f"{arc['value']:.1f}"],
                idx=[i]
            ))
            
            arc_patch = p.patches('x', 'y', source=source, 
                                 fill_color=arc['color'], 
                                 fill_alpha=0.9,
                                 line_color=line_color, 
                                 line_width=3,
                                 hover_fill_alpha=1.0,
                                 hover_line_width=4)
            
            arc_renderers.append(arc_patch)
            arc_sources.append(source)
    
    # Add arc hover tool
    arc_hover = HoverTool(
        renderers=arc_renderers,
        tooltips=None,
        callback=CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div,
                     border_color=border_color, info_bg=info_bg, text_color=text_color),
            code="""
            const arc_data = cb_data.renderer.data_source.data;
            const arc_idx = arc_data.idx[cb_data.index.indices[0]];
            if (arc_idx == null) return;

            for (let k = 0; k < ribbons.length; k++) {
                const src = ribbons[k].data.source_idx[0];
                const tgt = ribbons[k].data.target_idx[0];

                if (src === arc_idx || tgt === arc_idx) {
                    ribbons[k].data.alpha = [0.7];
                } else {
                    ribbons[k].data.alpha = [0.05];
                }
                ribbons[k].change.emit();
            }

            div.text = `
            <div style="padding:10px;border:2px solid ${border_color};border-radius:6px;background:${info_bg};color:${text_color};font-family:'Consolas', 'Courier New', monospace;">
                <b>Node:</b> ${arc_data.label[0]}<br>
                <b>Total Outgoing:</b> ${arc_data.value[0]}
            </div>
            `;
            """
        )
    )
    p.add_tools(arc_hover)
    
    # Add background click to reset
    p.js_on_event('tap', CustomJS(args=dict(ribbons=ribbon_sources), code="""
        for (let k = 0; k < ribbons.length; k++) {
            ribbons[k].data['alpha'] = [0.35];
            ribbons[k].change.emit();
        }
    """))
    
    # Reset on mouse leave
    p.js_on_event('mouseleave', CustomJS(
        args=dict(ribbons=ribbon_sources, div=info_div,
                 border_color=border_color, info_bg=info_bg, text_color=text_color),
        code="""
        for (let k = 0; k < ribbons.length; k++) {
            ribbons[k].data.alpha = [0.35];
            ribbons[k].change.emit();
        }
        
        div.text = `
        <div style="
            padding:10px;
            border:2px solid ${border_color};
            border-radius:6px;
            background:${info_bg};
            font-family:'Consolas', 'Courier New', monospace;
            font-size:13px;
            width:200px;
            color:${text_color};
        ">
            <b>Hover over a ribbon or arc</b>
        </div>
        `;
        """
    ))

    # Add labels outside the circle
    for arc in arc_positions:
        if arc['end'] > arc['start']:
            label_r = 1.18
            label_x = label_r * np.cos(arc['mid'])
            label_y = label_r * np.sin(arc['mid'])
            
            angle = arc['mid'] % (2 * np.pi)
            if 0 <= angle < np.pi/2 or 3*np.pi/2 <= angle < 2*np.pi:
                align = 'left'
            else:
                align = 'right'
            
            p.text(x=[label_x], y=[label_y], text=[arc['label']],
                   text_align=align, text_baseline='middle',
                   text_font_size='13pt', text_font_style='bold',
                   text_color=text_color)
    
    return column(p, info_div)




from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, TextInput
from bokeh.layouts import column, row
from bokeh.io import curdoc
import numpy as np


class Gauge:
    """A beautiful, animated gauge component for Bokeh."""
    
    def __init__(self, width=500, height=500, title="", unit="%", 
                 zones=None, initial_value=0, range_min=0, range_max=100,
                 easing=False, theme="dark",
                 bg_color=None, gauge_bg_color=None):
        """
        Create a beautiful gauge.
        
        Parameters:
        -----------
        width, height : int
            Dimensions of the gauge
        title : str
            Title displayed above the gauge
        unit : str
            Unit label displayed below the value
        zones : list of dict
            Zone definitions with 'range', 'color', and 'label' keys
            Example: [{"range": (0, 33), "color": "#00D4FF", "label": "LOW"}]
        initial_value : float
            Starting value
        range_min : float
            Minimum value of the gauge scale
        range_max : float
            Maximum value of the gauge scale
        easing : bool
            Enable smooth easing animation (True) or instant updates (False)
        theme : str
            "dark" or "light" theme
        bg_color : str
            Custom background color (overrides theme default)
        gauge_bg_color : str
            Custom gauge inner circle color (overrides theme default)
        """
        self.width = width
        self.height = height
        self.title = title
        self.unit = unit
        self.initial_value = initial_value
        self.range_min = range_min
        self.range_max = range_max
        self.easing = easing
        self.theme = theme
        
        # Calculate value range
        self.value_range = range_max - range_min
        
        # Theme colors
        if theme == "light":
            self.bg_color = bg_color or "#F5F5F5"
            self.gauge_bg_color = gauge_bg_color or "#E0E0E0"
            self.text_color = "#2C2C2C"
            self.tick_color = "#4A4A4A"
            self.ring_color = "#6A6A6A"
        else:  # dark
            self.bg_color = bg_color or "#0D0D0D"
            self.gauge_bg_color = gauge_bg_color or "#1A1A1A"
            self.text_color = "#FFFFFF"
            self.tick_color = "#FFFFFF"
            self.ring_color = "#FFFFFF"
        
        # Default zones
        self.zones = zones or [
            {"range": (0, 33.33), "color": "#00D4FF", "label": "LOW"},
            {"range": (33.33, 66.66), "color": "#FFD700", "label": "MEDIUM"},
            {"range": (66.66, 100), "color": "#FF3366", "label": "HIGH"}
        ]
        
        # Gauge geometry
        self.outer_radius = 1.0
        self.inner_radius = 0.78
        self.start_angle = np.pi + np.pi/6  # 210 degrees
        self.end_angle = -np.pi/6           # -30 degrees
        self.total_angle_range = self.start_angle - self.end_angle
        
        # Create components
        self.figure = self._create_figure()
        self.source = self._create_datasource()
        self._draw_gauge()
        
    def _create_figure(self):
        """Create the base figure."""
        p = figure(
            width=self.width, 
            height=self.height, 
            x_range=(-1.7, 1.7), 
            y_range=(-1.7, 1.7),
            tools="", 
            toolbar_location=None,
            background_fill_color=self.bg_color,
            border_fill_color=self.bg_color
        )
        p.axis.visible = False
        p.grid.visible = False
        p.outline_line_color = None
        return p
    
    def _create_datasource(self):
        """Create the data source for the pointer."""
        # Normalize initial value to 0-1 range
        normalized_value = (self.initial_value - self.range_min) / self.value_range
        initial_angle = self.start_angle - normalized_value * self.total_angle_range
        initial_color = self._get_zone_color(self.initial_value)
        
        return ColumnDataSource({
            'x': [0],
            'y': [0],
            'angle': [initial_angle],
            'value_text': [str(int(self.initial_value))],
            'pointer_color': [initial_color]
        })
    
    def _get_zone_color(self, value):
        """Get color based on value and zones."""
        for zone in self.zones:
            if zone["range"][0] <= value <= zone["range"][1]:
                return zone["color"]
        if value >= self.zones[-1]["range"][1]:
            return self.zones[-1]["color"]
        return self.zones[0]["color"]
    
    def _draw_gauge(self):
        """Draw all gauge elements."""
        # Title
        if self.title:
            self.figure.text(
                x=[0], y=[-1.45], text=[self.title],
                text_align="center", text_baseline="middle",
                text_color=self.text_color, text_font_size="22pt",
                text_font_style="bold", text_alpha=0.95
            )
        
        # Draw zone wedges
        for zone in self.zones:
            # Normalize zone ranges to 0-1
            zone_start_normalized = (zone["range"][0] - self.range_min) / self.value_range
            zone_end_normalized = (zone["range"][1] - self.range_min) / self.value_range
            
            zone_start = self.start_angle - zone_start_normalized * self.total_angle_range
            zone_end = self.start_angle - zone_end_normalized * self.total_angle_range
            
            # Main zone rings - COMPLETELY FILL between inner and outer radius
            num_rings = 30
            radii = np.linspace(self.inner_radius, self.outer_radius, num_rings)
            for r in radii:
                self.figure.wedge(
                    x=0, y=0, radius=r,
                    start_angle=zone_end, end_angle=zone_start,
                    color=zone["color"], line_color=zone["color"],
                    line_width=3, alpha=0.98
                )
            
            num_glow_rings = 8
            glow_radii = np.linspace(self.outer_radius + 0.01, self.outer_radius + 0.08, num_glow_rings)
            for i, r in enumerate(glow_radii):
                alpha = 0.4 * (1 - i/num_glow_rings)
                self.figure.wedge(
                    x=0, y=0, radius=r,
                    start_angle=zone_end, end_angle=zone_start,
                    color=zone["color"], line_color=zone["color"],
                    line_width=1, alpha=alpha
                )
            
            # Zone label
            angle = (zone_start + zone_end) / 2
            label_radius = self.outer_radius + 0.5
            x_label = label_radius * np.cos(angle)
            y_label = label_radius * np.sin(angle)
            self.figure.text(
                x=[x_label], y=[y_label], text=[zone["label"]],
                text_align="center", text_baseline="middle",
                text_color=zone["color"], text_font_size="14pt",
                text_font_style="bold"
            )
        
        # Inner dark circle
        self.figure.wedge(
            x=0, y=0, radius=self.inner_radius,
            start_angle=0, end_angle=2*np.pi,
            color=self.gauge_bg_color, line_color=self.gauge_bg_color
        )
        
        # Decorative rings
        self.figure.circle(
            x=0, y=0, radius=self.outer_radius + 0.02, 
            line_color=self.ring_color, line_width=2, fill_color=None, alpha=0.25
        )
        self.figure.circle(
            x=0, y=0, radius=self.inner_radius - 0.02, 
            line_color=self.ring_color, line_width=2, fill_color=None, alpha=0.3
        )
        
        # Tick marks
        self._draw_ticks()
        
        # Pointer
        self._draw_pointer()
        
        # Value display
        self._draw_value_display()
    
    def _draw_ticks(self):
        """Draw tick marks and labels."""
        # Generate ticks based on actual range
        num_major_ticks = 11
        num_minor_ticks = 51
        
        major_ticks = np.linspace(self.range_min, self.range_max, num_major_ticks)
        minor_ticks = np.linspace(self.range_min, self.range_max, num_minor_ticks)
        
        # Normalize tick positions to 0-1
        major_normalized = (major_ticks - self.range_min) / self.value_range
        minor_normalized = (minor_ticks - self.range_min) / self.value_range
        
        angles_major = [self.start_angle - norm * self.total_angle_range for norm in major_normalized]
        angles_minor = [self.start_angle - norm * self.total_angle_range for norm in minor_normalized]
        
        # Minor ticks
        for angle in angles_minor:
            x0 = (self.inner_radius - 0.03) * np.cos(angle)
            y0 = (self.inner_radius - 0.03) * np.sin(angle)
            x1 = (self.inner_radius + 0.03) * np.cos(angle)
            y1 = (self.inner_radius + 0.03) * np.sin(angle)
            self.figure.line([x0, x1], [y0, y1], line_color=self.tick_color, line_width=1.5, alpha=0.3)
        
        # Major ticks and labels
        for angle, tick in zip(angles_major, major_ticks):
            x0 = (self.inner_radius - 0.05) * np.cos(angle)
            y0 = (self.inner_radius - 0.05) * np.sin(angle)
            x1 = (self.outer_radius + 0.05) * np.cos(angle)
            y1 = (self.outer_radius + 0.05) * np.sin(angle)
            
            self.figure.line([x0, x1], [y0, y1], line_color=self.tick_color, line_width=2, alpha=0.5)
            self.figure.line([x0, x1], [y0, y1], line_color=self.tick_color, line_width=4, alpha=0.15)
            
            # Tick label
            label_radius = self.outer_radius + 0.25
            x_label = label_radius * np.cos(angle)
            y_label = label_radius * np.sin(angle)
            self.figure.text(
                x=[x_label], y=[y_label], text=[str(int(tick))],
                text_align="center", text_baseline="middle",
                text_color=self.tick_color, text_font_size="13pt",
                text_font_style="normal", text_alpha=0.65
            )
    
    def _draw_pointer(self):
        """Draw the animated pointer."""
        pointer_length = 0.68
        
        self.figure.wedge(
            x='x', y='y', radius=pointer_length,
            start_angle='angle', end_angle='angle',
            color='pointer_color', alpha=1.0,
            direction='clock', line_color='pointer_color',
            line_width=4, source=self.source
        )
        
        self.figure.wedge(
            x='x', y='y', radius=pointer_length,
            start_angle='angle', end_angle='angle',
            color='pointer_color', alpha=0.4,
            direction='clock', line_color='pointer_color',
            line_width=12, source=self.source
        )
        
        # Center hub
        self.figure.circle(x=0, y=0, radius=0.14, fill_color='pointer_color',
                          line_color='pointer_color', line_width=0, source=self.source, alpha=1.0)
        self.figure.circle(x=0, y=0, radius=0.09, fill_color=self.bg_color,
                          line_color='pointer_color', line_width=3, source=self.source, alpha=1.0)
        self.figure.circle(x=0, y=0, radius=0.05, fill_color='pointer_color',
                          source=self.source, alpha=1.0)
    
    def _draw_value_display(self):
        """Draw the value display."""
        # Main value - smaller font, moved up
        self.figure.text(
            x=0, y=-0.4, text='value_text', source=self.source,
            text_align="center", text_baseline="middle",
            text_color='pointer_color', text_font_size="40pt",
            text_font_style="bold"
        )
        # Glow effect
        self.figure.text(
            x=0, y=-0.4, text='value_text', source=self.source,
            text_align="center", text_baseline="middle",
            text_color='pointer_color', text_font_size="40pt",
            text_font_style="bold", text_alpha=0.3
        )
        # Unit label - smaller, moved up
        self.figure.text(
            x=0, y=-0.65, text=[self.unit],
            text_align="center", text_baseline="middle",
            text_color=self.text_color, text_font_size="13pt",
            text_font_style="bold", text_alpha=0.7
        )
    
    def get_animation_js(self, target_value, delay=500):
        """Generate JavaScript animation code."""
        easing_flag = 1 if self.easing else 0
        
        color_conditions = []
        for i, zone in enumerate(self.zones):
            if i == len(self.zones) - 1:
                color_conditions.append(f'return "{zone["color"]}";')
            else:
                color_conditions.append(f'if (v <= {zone["range"][1]}) return "{zone["color"]}";')
        color_func = '\n            '.join(color_conditions)
        
        return f'''
    setTimeout(function() {{
        const target = {target_value};
        const start_angle = Math.PI + Math.PI/6;
        const end_angle = -Math.PI/6;
        const total = start_angle - end_angle;
        const easing = {easing_flag};
        
        // Get the value range
        const range_min = {self.range_min};
        const range_max = {self.range_max};
        const value_range = range_max - range_min;
        
        function getColor(v) {{
            {color_func}
        }}
        
        let curr = parseFloat(source.data.value_text[0]) || 0;
        
        function update() {{
            if (easing) {{
                const diff = target - curr;
                if (Math.abs(diff) > 0.2) {{
                    curr += diff * 0.08;
                    // Normalize the value
                    const normalized_value = (curr - range_min) / value_range;
                    source.data.angle = [start_angle - normalized_value * total];
                    source.data.value_text = [Math.round(curr).toString()];
                    source.data.pointer_color = [getColor(curr)];
                    source.change.emit();
                    setTimeout(update, 20);
                }}
            }} else {{
                curr = target;
                // Normalize the value
                const normalized_value = (curr - range_min) / value_range;
                source.data.angle = [start_angle - normalized_value * total];
                source.data.value_text = [Math.round(curr).toString()];
                source.data.pointer_color = [getColor(curr)];
                source.change.emit();
            }}
        }}
        update();
    }}, {delay});
'''











from bokeh.plotting import figure, show, output_file
from bokeh.models import Label, GlobalInlineStyleSheet
from bokeh.layouts import row
import numpy as np

def get_dark_stylesheet():
    """Create a new dark theme stylesheet instance."""
    return GlobalInlineStyleSheet(css=""" 
        html, body, .bk, .bk-root {
            background-color: #343838; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: white; 
            font-family: 'Consolas', 'Courier New', monospace; 
        } 
        .bk { color: white; } 
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, 
        .bk-label, .bk-title, .bk-legend, .bk-axis-label { 
            color: white !important; 
        } 
        .bk-input::placeholder { color: #aaaaaa !important; } 
    """)

def get_light_stylesheet():
    """Create a new light theme stylesheet instance."""
    return GlobalInlineStyleSheet(css=""" 
        html, body, .bk, .bk-root {
            background-color: #FDFBD4; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: black; 
            font-family: 'Consolas', 'Courier New', monospace; 
        } 
        .bk { color: black; } 
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, 
        .bk-label, .bk-title, .bk-legend, .bk-axis-label { 
            color: black !important; 
        } 
        .bk-input::placeholder { color: #555555 !important; } 
    """)

def darken_color(hex_color, factor=0.7):
    """
    Darken a hex color by a factor.
    
    Parameters:
    -----------
    hex_color : str
        Hex color code (e.g., '#ff0000')
    factor : float
        Darkening factor (0-1, lower is darker)
    
    Returns:
    --------
    str : Darkened hex color
    """
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = int(r * factor), int(g * factor), int(b * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def plot_3d_bars(categories, values, colors, labels=None, 
                 title='3D Bar Chart', xlabel='', ylabel='',
                 width=800, height=600, bar_width=0.45,
                 dx=0.35, dy=80, dark_bg=True):
    """
    Create a 3D bar chart with simple (non-stacked) bars.
    
    Parameters:
    -----------
    categories : list
        Category names for x-axis
    values : list
        Values for each category
    colors : list
        Colors for each bar
    labels : list, optional
        Labels for legend (if None, uses categories)
    title : str
        Chart title
    xlabel, ylabel : str
        Axis labels
    width, height : int
        Figure dimensions
    bar_width : float
        Width of bars (0-1)
    dx, dy : float
        3D depth offsets (horizontal and vertical)
    dark_bg : bool
        Use dark background theme
    
    Returns:
    --------
    bokeh figure object
    """
    # Validate inputs
    if len(categories) != len(values) != len(colors):
        raise ValueError("categories, values, and colors must have same length")
    
    # Theme colors
    bg_color = '#343838' if dark_bg else '#FDFBD4'
    text_color = 'white' if dark_bg else 'black'
    grid_color = '#404040' if dark_bg else '#e0e0e0'
    
    # Calculate y-range with padding
    max_val = max(values) * 1.5
    
    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, len(categories)),
        y_range=(-10, max_val),
        toolbar_location='right',
        tools='pan,wheel_zoom,reset,save',
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )
    
    # Apply styling
    p.title.text_color = text_color
    p.title.text_font_size = '18pt'
    p.title.text_font_style = 'bold'
    p.xgrid.grid_line_color = grid_color
    p.ygrid.grid_line_color = grid_color
    p.xaxis.axis_line_color = text_color
    p.yaxis.axis_line_color = text_color
    p.xaxis.major_tick_line_color = text_color
    p.yaxis.major_tick_line_color = text_color
    p.xaxis.minor_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.major_label_text_color = text_color
    p.yaxis.major_label_text_color = text_color
    p.xaxis.major_label_text_font_size = '11pt'
    p.yaxis.major_label_text_font_size = '11pt'
    p.outline_line_color = None
    p.xaxis.ticker = list(range(len(categories)))
    p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}
    
    if ylabel:
        p.yaxis.axis_label = ylabel
        p.yaxis.axis_label_text_color = text_color
        p.yaxis.axis_label_text_font_size = '12pt'
    
    # Draw 3D bars
    for i, (value, color) in enumerate(zip(values, colors)):
        x_left = i - bar_width/2
        x_right = i + bar_width/2
        
        # Right side face (darker)
        right_x = [x_right, x_right + dx, x_right + dx, x_right, x_right]
        right_y = [0, dy, value + dy, value, 0]
        p.patch(right_x, right_y, color=darken_color(color, 0.6), 
                alpha=1.0, line_color='#000000', line_width=1)
        
        # Top face (medium shade)
        top_x = [x_left, x_right, x_right + dx, x_left + dx, x_left]
        top_y = [value, value, value + dy, value + dy, value]
        p.patch(top_x, top_y, color=darken_color(color, 0.8), 
                alpha=1.0, line_color='#000000', line_width=1)
        
        # Front face (brightest)
        p.quad(left=[x_left], right=[x_right], bottom=[0], top=[value],
               color=color, alpha=1.0, line_color='#000000', line_width=1.5)
    
    return p

def plot_3d_stacked_bars(categories, data_dict, colors, labels,
                         title='3D Stacked Bar Chart', xlabel='', ylabel='',
                         width=800, height=600, bar_width=0.45,
                         dx=0.35, dy=80, dark_bg=True):
    """
    Create a 3D stacked bar chart.
    
    Parameters:
    -----------
    categories : list
        Category names for x-axis
    data_dict : dict
        Dictionary mapping categories to lists of values (bottom to top)
    colors : list
        Colors for each stack segment
    labels : list
        Labels for each stack segment
    title : str
        Chart title
    xlabel, ylabel : str
        Axis labels
    width, height : int
        Figure dimensions
    bar_width : float
        Width of bars (0-1)
    dx, dy : float
        3D depth offsets (horizontal and vertical)
    dark_bg : bool
        Use dark background theme
    
    Returns:
    --------
    bokeh figure object
    """
    # Validate inputs
    if not all(cat in data_dict for cat in categories):
        raise ValueError("data_dict must contain all categories")
    
    # Theme colors
    bg_color = '#343838' if dark_bg else '#FDFBD4'
    text_color = 'white' if dark_bg else 'black'
    grid_color = '#404040' if dark_bg else '#e0e0e0'
    
    # Calculate y-range
    max_val = max(sum(data_dict[cat]) for cat in categories) * 1.4
    
    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, len(categories)),
        y_range=(-50, max_val),
        toolbar_location='right',
        tools='pan,wheel_zoom,reset,save',
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )
    
    # Apply styling
    p.title.text_color = text_color
    p.title.text_font_size = '18pt'
    p.title.text_font_style = 'bold'
    p.xgrid.grid_line_color = grid_color
    p.ygrid.grid_line_color = grid_color
    p.xaxis.axis_line_color = text_color
    p.yaxis.axis_line_color = text_color
    p.xaxis.major_tick_line_color = text_color
    p.yaxis.major_tick_line_color = text_color
    p.xaxis.minor_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.major_label_text_color = text_color
    p.yaxis.major_label_text_color = text_color
    p.xaxis.major_label_text_font_size = '11pt'
    p.yaxis.major_label_text_font_size = '11pt'
    p.outline_line_color = None
    p.xaxis.ticker = list(range(len(categories)))
    p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}
    
    if ylabel:
        p.yaxis.axis_label = ylabel
        p.yaxis.axis_label_text_color = text_color
        p.yaxis.axis_label_text_font_size = '12pt'
    
    # Draw 3D stacked bars
    for i, category in enumerate(categories):
        cumulative = 0
        category_data = data_dict[category]
        
        for j, (value, color) in enumerate(zip(category_data, colors)):
            bottom = cumulative
            top = cumulative + value
            
            x_left = i - bar_width/2
            x_right = i + bar_width/2
            
            # Right side face (darker)
            right_x = [x_right, x_right + dx, x_right + dx, x_right, x_right]
            right_y = [bottom, bottom + dy, top + dy, top, bottom]
            p.patch(right_x, right_y, color=darken_color(color, 0.6),
                    alpha=1.0, line_color='#000000', line_width=1)
            
            # Top face (only for top segment)
            if j == len(category_data) - 1:
                top_x = [x_left, x_right, x_right + dx, x_left + dx, x_left]
                top_y = [top, top, top + dy, top + dy, top]
                p.patch(top_x, top_y, color=darken_color(color, 0.8),
                        alpha=1.0, line_color='#000000', line_width=1)
            
            # Front face (brightest)
            p.quad(left=[x_left], right=[x_right], bottom=[bottom], top=[top],
                   color=color, alpha=1.0, line_color='#000000', line_width=1.5)
            
            cumulative = top
    
    return p

def create_legend(labels, colors, dark_bg=True, height=600):
    """
    Create a separate legend figure.
    
    Parameters:
    -----------
    labels : list
        Legend labels
    colors : list
        Colors corresponding to labels
    dark_bg : bool
        Use dark background theme
    height : int
        Height of legend figure
    
    Returns:
    --------
    bokeh figure object
    """
    text_color = 'white' if dark_bg else 'black'
    bg_color = '#343838' if dark_bg else '#FDFBD4'
    
    # Calculate required height based on number of items
    item_height = 40  # Height per legend item
    total_height = len(labels) * item_height + 60
    
    legend_fig = figure(
        width=250,
        height=min(total_height, height),
        toolbar_location=None,
        background_fill_color=bg_color,
        border_fill_color=bg_color,
        outline_line_color=None,
        x_range=(0, 1),
        y_range=(0, len(labels) * item_height + 20)
    )
    
    # Remove axes and grid
    legend_fig.xaxis.visible = False
    legend_fig.yaxis.visible = False
    legend_fig.xgrid.visible = False
    legend_fig.ygrid.visible = False
    
    # Add legend items from top to bottom
    for i, (label, color) in enumerate(zip(labels, colors)):
        y_pos = (len(labels) - i) * item_height - 10
        
        # Colored circle
        legend_fig.circle(x=[0.1], y=[y_pos], size=18, color=color, 
                         alpha=1.0, line_color='#000000', line_width=2)
        
        # Label text positioned right next to the circle
        label_obj = Label(
            x=0.18, y=y_pos - 7,
            text=label,
            text_color=text_color,
            text_font_size='12pt'
        )
        legend_fig.add_layout(label_obj)
    
    return legend_fig


from bokeh.plotting import figure, show, output_file
from bokeh.models import Label, ColumnDataSource, GlobalInlineStyleSheet
from bokeh.layouts import row
import numpy as np

def get_dark_stylesheet():
    """Create a new dark theme stylesheet instance."""
    return GlobalInlineStyleSheet(css=""" 
        html, body, .bk, .bk-root {
            background-color: #343838; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: white; 
            font-family: 'Consolas', 'Courier New', monospace; 
        } 
        .bk { color: white; } 
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, 
        .bk-label, .bk-title, .bk-legend, .bk-axis-label { 
            color: white !important; 
        } 
        .bk-input::placeholder { color: #aaaaaa !important; } 
    """)

def get_light_stylesheet():
    """Create a new light theme stylesheet instance."""
    return GlobalInlineStyleSheet(css=""" 
        html, body, .bk, .bk-root {
            background-color: #FDFBD4; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: black; 
            font-family: 'Consolas', 'Courier New', monospace; 
        } 
        .bk { color: black; } 
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, 
        .bk-label, .bk-title, .bk-legend, .bk-axis-label { 
            color: black !important; 
        } 
        .bk-input::placeholder { color: #555555 !important; } 
    """)

def darken_color(hex_color, factor=0.7):
    """Darken a hex color by a factor."""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = int(r * factor), int(g * factor), int(b * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def plot_3d_pie(values, colors, labels, title='3D Pie Chart',
                width=800, height=700, radius=1.5, depth=0.3,
                tilt=25, rotation=0, dark_bg=True, explode=None):
    """
    Create a PROPERLY WORKING 3D pie chart with correct perspective.
    """
    bg_color = '#343838' if dark_bg else '#FDFBD4'
    text_color = 'white' if dark_bg else 'black'
    
    # Normalize values
    total = sum(values)
    percentages = [v / total for v in values]
    
    if explode is None:
        explode = [0] * len(values)
    
    
    p = figure(
        width=width,
        height=height,
        title=title,
        toolbar_location=None,
        background_fill_color=bg_color,
        border_fill_color=bg_color,
        match_aspect=True,
    )
    
    # Styling
    p.title.text_color = text_color
    p.title.text_font_size = '16pt'
    p.xaxis.visible = False
    p.yaxis.visible = False
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.outline_line_color = None
    
    # 3D transformation parameters
    tilt_rad = np.radians(tilt)
    
    # Calculate cumulative angles
    angles = [p * 360 for p in percentages]
    start_angles = [0]
    for angle in angles[:-1]:
        start_angles.append(start_angles[-1] + angle)
    
    # Determine drawing order: back to front based on mid-angle
    slice_order = []
    for i in range(len(values)):
        mid_angle = start_angles[i] + angles[i]/2 + rotation
        # Use negative sin for proper sorting (back to front)
        slice_order.append((-np.sin(np.radians(mid_angle)), i))
    
    slice_order.sort()
    
    for _, i in slice_order:
        start_deg = start_angles[i] + rotation
        end_deg = start_deg + angles[i]
        mid_deg = start_deg + angles[i]/2
        
        # Explode offset
        explode_offset = explode[i] * radius * 0.15
        explode_x = explode_offset * np.cos(np.radians(mid_deg))
        explode_y = explode_offset * np.sin(np.radians(mid_deg)) * np.cos(tilt_rad)
        
        # Generate points for the slice
        n_points = max(30, int(angles[i] / 360 * 60))
        theta = np.linspace(np.radians(start_deg), np.radians(end_deg), n_points)
        
        # Top surface coordinates
        top_x = radius * np.cos(theta) + explode_x
        top_y = radius * np.sin(theta) * np.cos(tilt_rad) + explode_y
        
        # Bottom surface coordinates
        bottom_x = top_x.copy()
        bottom_y = top_y - depth
        
        edge_color = darken_color(colors[i], 0.6)
        
        # Draw the OUTER CURVED EDGE (visible from front)
        for j in range(len(theta) - 1):
            angle_mid = (theta[j] + theta[j+1]) / 2
            # Front-facing check: sin(angle) should be NEGATIVE (towards viewer)
            if np.sin(angle_mid) < 0:
                edge_x = [top_x[j], top_x[j+1], bottom_x[j+1], bottom_x[j], top_x[j]]
                edge_y = [top_y[j], top_y[j+1], bottom_y[j+1], bottom_y[j], top_y[j]]
                p.patch(edge_x, edge_y, color=edge_color, alpha=1.0, 
                       line_color='#000000', line_width=0.8)
        
        # Add vertical hatching on outer edge
        hatch_density = max(8, int(angles[i] / 360 * 50))
        hatch_indices = np.linspace(0, len(theta)-1, hatch_density, dtype=int)
        
        for idx in hatch_indices:
            if idx < len(theta) and np.sin(theta[idx]) < 0:
                hatch_x = [top_x[idx], bottom_x[idx]]
                hatch_y = [top_y[idx], bottom_y[idx]]
                p.line(hatch_x, hatch_y, color='#000000', 
                      alpha=0.3, line_width=1.0)
        
        # Top surface
        top_wedge_x = np.concatenate([[explode_x], top_x, [explode_x]])
        top_wedge_y = np.concatenate([[explode_y], top_y, [explode_y]])
        
        source = ColumnDataSource(data=dict(
            x=top_wedge_x,
            y=top_wedge_y,
            label=[labels[i]] * len(top_wedge_x),
            value=[values[i]] * len(top_wedge_x),
            percentage=[f'{percentages[i]*100:.1f}%'] * len(top_wedge_x)
        ))
        
        p.patch('x', 'y', source=source, color=colors[i], alpha=1.0,
               line_color='#000000', line_width=1.2,
               hover_alpha=0.8)
        
        # Add percentage label on top surface
        label_radius = radius * 0.65
        label_x = label_radius * np.cos(np.radians(mid_deg)) + explode_x
        label_y = label_radius * np.sin(np.radians(mid_deg)) * np.cos(tilt_rad) + explode_y
        
        percentage_text = f'{percentages[i]*100:.1f}%'
        label_obj = Label(
            x=label_x, y=label_y,
            text=percentage_text,
            text_color='white',
            text_font_size='14pt',
            text_align='center',
            text_baseline='middle',
            text_font_style='normal'
        )
        p.add_layout(label_obj)
    
    # Set ranges
    margin = radius * 1.5
    p.x_range.start = -margin
    p.x_range.end = margin
    p.y_range.start = -margin - depth
    p.y_range.end = margin
    
    return p

def create_legend(labels, colors, dark_bg=True):
    """Create a separate legend figure."""
    text_color = 'white' if dark_bg else 'black'
    bg_color = '#343838' if dark_bg else '#FDFBD4'
    
    # Calculate required height
    item_height = 40
    total_height = len(labels) * item_height + 60
    
    legend_fig = figure(
        width=250,
        height=total_height,
        toolbar_location=None,
        background_fill_color=bg_color,
        border_fill_color=bg_color,
        outline_line_color=None,
        x_range=(0, 1),
        y_range=(0, len(labels) * item_height + 20)
    )
    
    legend_fig.xaxis.visible = False
    legend_fig.yaxis.visible = False
    legend_fig.xgrid.visible = False
    legend_fig.ygrid.visible = False
    
    for i, (label, color) in enumerate(zip(labels, colors)):
        y_pos = (len(labels) - i) * item_height - 10
        
        # Draw color circle
        legend_fig.circle(x=[0.1], y=[y_pos], size=18, color=color, 
                         alpha=1.0, line_color='#000000', line_width=2)
        
        # Draw text label
        label_obj = Label(
            x=0.18, y=y_pos - 7,
            text=label,
            text_color=text_color,
            text_font_size='12pt',
            text_baseline='middle'
        )
        legend_fig.add_layout(label_obj)
    
    return legend_fig




import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import LinearColorMapper, ColorBar, Range1d
from bokeh.palettes import Viridis256, Plasma256

def plot_surface_bokeh(Z_func, x_range=(-3,3), y_range=(-3,3), n_points=40, cmap=Plasma256,
                       elev_deg=25, azim_deg=45, title="3D Surface", output_path=None):
    """
    High-level function to create a 3D-like surface plot in Bokeh using patches.
    
    Parameters:
    -----------
    Z_func : callable
        Function Z(X,Y) -> Z values, takes two 2D arrays
    x_range, y_range : tuple
        Min and max of X and Y
    n_points : int
        Resolution of grid
    elev_deg : float
        Elevation angle in degrees
    azim_deg : float
        Azimuth angle in degrees
    title : str
        Plot title
    output_path : str
        Optional path to save HTML
    
    Returns:
    --------
    Bokeh figure
    """
    # Grid
    x = np.linspace(x_range[0], x_range[1], n_points)
    y = np.linspace(y_range[0], y_range[1], n_points)
    X, Y = np.meshgrid(x, y)
    Z = Z_func(X, Y)
    
    # Isometric-like projection
    elev_rad = np.radians(elev_deg)
    azim_rad = np.radians(azim_deg)
    X_rot = X * np.cos(azim_rad) - Y * np.sin(azim_rad)
    Y_rot = X * np.sin(azim_rad) + Y * np.cos(azim_rad)
    X_proj = X_rot
    Z_proj = Y_rot * np.sin(elev_rad) + Z * np.cos(elev_rad)
    
    # Prepare quads
    quads = []
    for i in range(n_points - 1):
        for j in range(n_points - 1):
            xs = [X_proj[i, j], X_proj[i, j + 1], X_proj[i + 1, j + 1], X_proj[i + 1, j]]
            ys = [Z_proj[i, j], Z_proj[i, j + 1], Z_proj[i + 1, j + 1], Z_proj[i + 1, j]]
            avg_z = (Z[i, j] + Z[i, j+1] + Z[i+1, j+1] + Z[i+1, j]) / 4
            depth = (Y_rot[i, j] + Y_rot[i, j+1] + Y_rot[i+1, j+1] + Y_rot[i+1, j]) / 4
            quads.append((depth, xs, ys, avg_z))
    
    quads.sort(key=lambda q: q[0], reverse=True)
    quad_xs = [q[1] for q in quads]
    quad_ys = [q[2] for q in quads]
    quad_colors = [q[3] for q in quads]
    
    # Color mapping
    z_min, z_max = Z.min(), Z.max()
    color_mapper = LinearColorMapper(palette=cmap, low=z_min, high=z_max)
    colors = [cmap[int((val - z_min)/(z_max - z_min)*255)] for val in quad_colors]
    
    # Create figure
    p = figure(width=1200, height=800, title=title, toolbar_location=None)
    p.patches(xs=quad_xs, ys=quad_ys, fill_color=colors,
              line_color="#306998", line_alpha=0.3, line_width=0.5, alpha=0.9)
    
    # Axis ranges
    x_min, x_max = min(min(xs) for xs in quad_xs), max(max(xs) for xs in quad_xs)
    y_min, y_max = min(min(ys) for ys in quad_ys), max(max(ys) for ys in quad_ys)
    x_pad, y_pad = (x_max - x_min)*0.15, (y_max - y_min)*0.15
    p.x_range = Range1d(x_min - x_pad, x_max + x_pad)
    p.y_range = Range1d(y_min - y_pad, y_max + y_pad)
    
    # Clean axes
    p.xaxis.visible = False
    p.yaxis.visible = False
    
    # Color bar
    color_bar = ColorBar(color_mapper=color_mapper, width=60, location=(0,0), title="Z")
    p.add_layout(color_bar, "right")
    
    # Save HTML if requested
    if output_path:
        output_file(output_path)
    
    return p

