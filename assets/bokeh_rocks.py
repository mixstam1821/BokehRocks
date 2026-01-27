#########################################
#
# bokeh_rocks.py: A collection of helpers and high level functions for Bokeh
#
#########################################


from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet, HoverTool, CustomJSHover
from bokeh.transform import dodge
from bokeh.models.glyphs import VBar
import itertools
import pandas as pd
from bokeh.io import export_png, output_file, save

import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource, CustomJS, GlobalInlineStyleSheet
from bokeh.palettes import Category20
from bokeh.layouts import column, row
from bokeh.models import Div
import pandas as pd, numpy as np, xarray as xr


from bokeh.layouts import row, Spacer

from bokeh.plotting import figure, show, save, curdoc, output_file

from bokeh.models import (
    VBar,
    Range1d,
    CustomJSHover,
    LinearAxis,
    ColumnDataSource,
    InlineStyleSheet,
    LassoSelectTool,
    DatetimeTickFormatter,
    NumeralTickFormatter,
    CrosshairTool,
    HoverTool,
    Span,
    Legend,
    BoxEditTool,
    FreehandDrawTool,
    WheelZoomTool,
)

from bokeh.io import export_png

jk9 = {"active_scroll": "wheel_zoom"}


from matplotlib import cm
from matplotlib.colors import to_hex


#'RdBu_r'
def mbpal(sMpl):
    return [to_hex(cm.get_cmap(sMpl)(i / 255)) for i in range(256)]


palette = bxc2 = [
    "#4db4fd",
    "#ff6464",
    "#ffc562",
    "#63ff8d",
    "#ff8bff",
    "#6385ff",
    "#FFEA00",
    "#97573a",
    "#00FFFF",
    "#ff9cff",
    "#008000",
    "#A42A04",
    "#D2B48C",
    "#878787",
]
bxc1 = ["#2EC4B6", "#FCBF49", "#CDB4DB", "#A9DEF9", "#EAE2B7"]


def get_dark_stylesheet():
    """Create a new dark theme stylesheet instance."""
    return GlobalInlineStyleSheet(
        css="""
        html, body, .bk, .bk-root {
            background-color: #343838; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: white; 
            font-family: 'Consolas', 'Helvetica', monospace; 
        }
        .bk { color: white; }
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers,
        .bk-label, .bk-title, .bk-legend, .bk-axis-label {
            color: white !important; 
        }
        .bk-input::placeholder { color: #aaaaaa !important; }
    """
    )


def get_light_stylesheet():
    """Create a new light theme stylesheet instance."""
    return GlobalInlineStyleSheet(
        css="""
        html, body, .bk, .bk-root {
            background-color: #f3f3f3; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: black; 
            font-family: 'Consolas', 'Helvetica', monospace; 
        }
        .bk { color: black; }
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers,
        .bk-label, .bk-title, .bk-legend, .bk-axis-label {
            color: black !important; 
        }
        .bk-input::placeholder { color: #555555 !important; }
    """
    )


from bokeh.io import output_file, save, reset_output
from bokeh.io.export import export_png

def save_plot(plot, fname):
    """Saves the plot to an HTML file and exports it as a PNG."""
    
    # CRITICAL: Reset Bokeh's output state before saving
    reset_output()
    
    # Now set the new output file
    output_file(fname + ".html")
    
    # Save the HTML
    save(plot)
    
    # Export PNG
    export_png(
        plot, 
        filename=fname + ".png"
    )
    
    # Optional: Reset again after saving for clean state
    reset_output()


def cusj():
    num = 1
    return CustomJSHover(
        code=f"""
    special_vars.indices = special_vars.indices.slice(0,{num})
    return special_vars.indices.includes(special_vars.index) ? " " : " hidden "
    """
    )


def hovfun(tltl):
    return (
        """<div @hidden{custom} style="background-color: #fff0eb; padding: 5px; border-radius: 5px; box-shadow: 0px 0px 5px rgba(0,0,0,0.3);">        <font size="3" style="background-color: #fff0eb; padding: 5px; border-radius: 5px;"> """
        + tltl
        + """ <br> </font> </div> <style> :host { --tooltip-border: transparent;  /* Same border color used everywhere */ --tooltip-color: transparent; --tooltip-text: #2f2f2f;} </style> """
    )


palette = bxc2 = [
    "#4db4fd",
    "#ff6464",
    "#ffc562",
    "#63ff8d",
    "#ff8bff",
    "#6385ff",
    "#FFEA00",
    "#97573a",
    "#00FFFF",
    "#ff9cff",
    "#008000",
    "#A42A04",
    "#D2B48C",
    "#878787",
]
from bokeh.plotting import figure, show
from bokeh.models import (
    ColumnDataSource,
    LabelSet,
    HoverTool,
    BoxEditTool,
    FreehandDrawTool,
    CrosshairTool,
    Span,
    Spacer,
)
from bokeh.transform import dodge
from bokeh.models.glyphs import VBar
from bokeh.layouts import layout
import itertools
import pandas as pd


def apply_theme(p, theme="light", legend_outside=False):
    """
    Apply consistent theme styling to any Bokeh figure.
    This function should be used across all high-level plotting functions.

    Parameters
    ----------
    p : bokeh.plotting.figure.Figure
        Bokeh figure to style
    theme : str, default 'light'
        Theme style: 'light' or 'dark'
    legend_outside : bool, default False
        If True, moves legend outside plot area to the right

    Returns
    -------
    bokeh.plotting.figure.Figure
        Styled figure
    """

    # Common settings for both themes
    p.toolbar.autohide = True
    p.toolbar_location = "left"
    p.min_border_bottom = 90
    p.min_border_right = 165 if legend_outside else 20

    # Font settings
    p.xaxis.axis_label_text_font_size = "15pt"
    p.yaxis.axis_label_text_font_size = "15pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.major_label_text_font_size = "15pt"
    p.xaxis.major_label_text_font = "Helvetica"
    p.yaxis.major_label_text_font = "Helvetica"
    p.xaxis.axis_label_text_font = "Helvetica"
    p.yaxis.axis_label_text_font = "Helvetica"
    p.title.text_font_size = "18pt"
    p.title.text_font = "Helvetica"
    p.title.align = "center"

    # Grid settings
    p.grid.grid_line_color = "grey"
    p.grid.grid_line_alpha = 0.1

    # Theme-specific styling
    if theme == "dark":
        p.styles = {
            "margin-top": "0px",
            "margin-left": "0px",
            "border-radius": "10px",
            "box-shadow": "0 18px 20px rgba(243, 192, 97, 0.2)",
            "padding": "5px",
            "background-color": "#343838",
            "border": "1.5px solid orange",
        }
        p.background_fill_color = "#1f1f1f"
        p.border_fill_color = "#343838"
        p.outline_line_color = "#343838"
        p.outline_line_width = 2
        p.xaxis.major_label_text_color = "white"
        p.yaxis.major_label_text_color = "white"
        p.xaxis.axis_label_text_color = "white"
        p.yaxis.axis_label_text_color = "white"
        p.title.text_color = "white"
    else:  # light theme
        p.styles = {
            "margin-top": "0px",
            "margin-left": "0px",
            "border-radius": "10px",
            "box-shadow": "0 18px 20px rgba(165, 221, 253, 0.2)",
            "padding": "5px",
            "background-color": "white",
            "border": "1.5px solid deepskyblue",
        }
        p.background_fill_color = "#EBEBEB"

    # Legend styling (if legend exists)
    if len(p.legend) > 0:
        if legend_outside:
            p.legend.location = "center"
            p.add_layout(p.legend[0], "right")
            p.add_layout(Spacer(width=5), "right")

        p.legend.click_policy = "hide"
        p.legend.label_text_font_size = "15pt"
        p.legend.label_text_font = "Helvetica"
        p.legend.border_line_width = 1.5
        p.legend.border_line_alpha = 0.7
        p.legend.background_fill_alpha = 0.1
        p.legend.background_fill_color = "silver"

        if theme == "dark":
            p.legend.label_text_color = "silver"
            p.legend.border_line_color = "silver"
        else:
            p.legend.border_line_color = "black"

    return p


def add_extras(
    p, drawline_width=5, drawalpha=0.4, drawcolor="red", cross=False, bed=False
):
    """
    Add interactive drawing and selection tools to a Bokeh figure.

    Parameters
    ----------
    p : bokeh.plotting.figure.Figure
        Bokeh figure to add tools to
    drawline_width : int, default 5
        Width of freehand drawing lines
    drawalpha : float, default 0.4
        Transparency of freehand drawing lines
    drawcolor : str, default 'red'
        Color of freehand drawing lines
    cross : bool, default False
        If True, adds crosshair tool
    bed : bool, default False
        If True, adds box edit tool for drawing rectangles

    Returns
    -------
    bokeh.plotting.figure.Figure
        Figure with added tools
    """

    # Box edit tool (wants to be first)
    if bed:
        sourcebox = ColumnDataSource(
            data=dict(
                x=[0],
                y=[0],
                width=[0],
                height=[0],
                color=["grey"],
                alpha=[0.35],
            ),
            default_values=dict(
                color="grey",
                alpha=0.35,
            ),
        )
        rbox = p.rect(
            "x", "y", "width", "height", color="color", alpha="alpha", source=sourcebox
        )
        box_tool = BoxEditTool(renderers=[rbox])
        p.add_tools(box_tool)

    # Freehand draw tool
    rdraw = p.multi_line(
        [], [], line_width=drawline_width, alpha=drawalpha, color=drawcolor
    )
    draw_tool = FreehandDrawTool(renderers=[rdraw], num_objects=100)
    p.add_tools(draw_tool)

    # Selection tools
    p.add_tools("box_select")

    # Crosshair tool
    if cross:
        span_height = Span(
            dimension="height", line_dash="dashed", line_width=2, line_color="#878787"
        )
        crosshair_tool = CrosshairTool(overlay=span_height)
        p.add_tools(crosshair_tool)

    return p


# ------------------------
# HTML Div overlay remover
# ------------------------
def rmfocus(p, dx=10):
    rmfocusdiv = Div(
        text="",
        width=p.width - dx,
        height=p.height - dx,
        styles={
            "padding": "0px",
            "position": "absolute",
            "border": "2px solid white",
            "background-color": "transparent",
            "pointer-events": "none",
        },
    )
    return rmfocusdiv



def bar(
    df,
    kind="vgroup",
    title=None,
    xlabel=None,
    ylabel=None,
    palette=None,
    showlabels=0,
    width=1400,
    height=800,
    toolbar_location="below",
    theme="light",
    legend_outside=True,
    custom_text0=None,
    sh=0,
    save=0,
    output_path="bar1",
    x_axis_label_orientation="horizontal",
    tick_label_step=1,
    border_radius=0,
):
    """
    Unified bar chart function supporting grouped and stacked bar charts
    in both vertical and horizontal orientations.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame where first column is categories and remaining columns are numeric series.
    kind : str, default 'vgroup'
        Type of bar chart:
        - 'vgroup' : Vertical grouped bars (default)
        - 'hgroup' : Horizontal grouped bars
        - 'vstack' : Vertical stacked bars
        - 'hstack' : Horizontal stacked bars
    title : str, optional
        Chart title. Auto-generated if None.
    xlabel : str, optional
        X-axis label. No label if None.
    ylabel : str, optional
        Y-axis label. No label if None.
    palette : list, optional
        List of colors for series. Uses default palette if None.
    showlabels : int, default 1
        Whether to show value labels (1=show, 0=hide).
    width : int, default 1400
        Chart width in pixels.
    height : int, default 800
        Chart height in pixels.
    toolbar_location : str, default "below"
        Location of toolbar ("below", "above", "left", "right", None).
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default False
        If True, positions legend outside plot area to the right.
    custom_text_x0 : list, optional: [[x,y,text,color,font_size], ...]
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show).
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save).
    output_path : str, default 'chart'
        File path for saving the plot (used when save=1)
    x_axis_label_orientation : (e.g., 0.785 for 45°, 1.57 for 90°)
    tick_label_step : int, default 1
        Show tick label every N ticks. For example:
        - 1 : show all labels (default)
        - 2 : show every 2nd label
        - 6 : show every 6th label
        Useful when you have many categories (e.g., 120 dates)

    Returns
    -------
    bokeh.plotting.figure.Figure
        Bokeh figure object ready to show() or save().

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'Category': ['A', 'B', 'C'],
    ...     'Series1': [10, 20, 15],
    ...     'Series2': [15, 25, 20]
    ... })
    >>> p = bar(df, kind='vgroup', title='Sales Data',
    ...          xlabel='Products', ylabel='Revenue ($)',
    ...          theme='dark', legend_outside=True)
    >>> # Chart is automatically shown

    >>> # With custom annotation and saving
    >>> p = bar(df, kind='vstack',
    ...          save=1, output_path='sales_chart')
    """

    # Validate kind parameter
    valid_kinds = ["vgroup", "hgroup", "vstack", "hstack", "vgantt", "hgantt"]
    if kind not in valid_kinds:
        raise ValueError(f"kind must be one of {valid_kinds}, got '{kind}'")

    # Validate theme parameter
    valid_themes = ["light", "dark"]
    if theme not in valid_themes:
        raise ValueError(f"theme must be one of {valid_themes}, got '{theme}'")

    # Extract data components
    cat_col = df.columns[0]

    categories = df[cat_col].astype(str).tolist()
    series = df.columns[1:]

    # Setup colors
    default_colors = bxc2
    colors = palette or list(
        itertools.islice(itertools.cycle(default_colors), len(series))
    )

    # Auto-generate title if not provided
    if title is None:
        kind_names = {
            "vgroup": "Grouped Vertical Bar Chart",
            "hgroup": "Grouped Horizontal Bar Chart",
            "vstack": "Stacked Vertical Bar Chart",
            "hstack": "Stacked Horizontal Bar Chart",
        }
        title = kind_names[kind]

    # Determine orientation
    is_vertical = kind in ["vgroup", "vstack"]
    is_grouped = kind in ["vgroup", "hgroup"]
    is_gantt = kind in ["vgantt", "hgantt"]
    if is_gantt:
        if df.shape[1] < 3:
            raise ValueError(
                "Gantt charts require df with columns: [category, start, end]"
            )

    if is_gantt:
        is_vertical = kind == "vgantt"

    # -------------------------------------------------
    # Calculate range limits (DATETIME + NUMERIC SAFE)
    # -------------------------------------------------
    is_datetime = False  # default for non-Gantt charts

    if is_gantt:
        start_col = df.columns[1]
        end_col = df.columns[2]

        from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype

        # Detect datetime vs numeric
        if not is_numeric_dtype(df[start_col]):
            # Only attempt datetime conversion if column is not numeric
            if is_datetime64_any_dtype(df[start_col]):
                is_datetime = True
            else:
                try:
                    df[start_col] = pd.to_datetime(df[start_col])
                    df[end_col] = pd.to_datetime(df[end_col])
                    is_datetime = True
                except Exception:
                    is_datetime = False
        else:
            # numeric: keep as numeric
            is_datetime = False

        # Save string versions for hover (works for both datetime and numeric)
        df["start_str"] = df[start_col].astype(str)
        df["end_str"] = df[end_col].astype(str)

        # Compute min/max and padding
        min_value = df[start_col].min()
        max_value = df[end_col].max()
        span = max_value - min_value
        if is_datetime:
            pad = span * 0.1
            if pad < pd.Timedelta(minutes=1):
                pad = pd.Timedelta(minutes=1)
        else:
            pad = span * 0.1 if span else 1

        # Set axis ranges correctly for hgantt / vgantt
        if is_vertical:  # vgantt
            x_range = df["category"].astype(str).tolist()  # categorical axis
            y_range = (min_value - pad, max_value + pad)  # numeric or datetime
        else:  # hgantt
            x_range = (min_value - pad, max_value + pad)  # numeric or datetime
            y_range = df["category"].astype(str).tolist()  # categorical axis

    else:
        # fallback for normal grouped/stacked bars
        if is_grouped:
            max_value = df.iloc[:, 1:].to_numpy().max() * 1.2
        else:
            max_value = df.iloc[:, 1:].sum(axis=1).max() * 1.25
        x_range = (0, max_value)
        y_range = (0, max_value)

    y_range = (min_value - pad, max_value + pad) if is_gantt else (0, max_value)
    x_range = (min_value - pad, max_value + pad) if is_gantt else (0, max_value)

    # Create figure with appropriate ranges
    if is_vertical:
        p = figure(
            x_range=categories,
            y_range=y_range,
            title=title,
            tools="tap,wheel_zoom,box_zoom,pan,save,reset,lasso_select,freehand_draw",
            toolbar_location=toolbar_location,
            width=width,
            height=height,
            y_axis_type="datetime" if is_datetime else "linear",
        )
    else:  # horizontal
        p = figure(
            y_range=categories[::-1],
            x_range=x_range,
            title=title,
            tools="tap,wheel_zoom,box_zoom,pan,save,reset,lasso_select,freehand_draw",
            toolbar_location=toolbar_location,
            width=width,
            height=height,
            x_axis_type="datetime" if is_datetime else "linear",
        )

    # Route to appropriate plotting function
    if is_gantt:
        _plot_gantt_bars(p, df, cat_col, colors, is_vertical, theme, border_radius)
    elif is_grouped:
        _plot_grouped_bars(
            p,
            df,
            cat_col,
            categories,
            series,
            colors,
            is_vertical,
            showlabels,
            theme,
            border_radius,
        )
    else:  # stacked
        _plot_stacked_bars(
            p,
            df,
            cat_col,
            categories,
            series,
            colors,
            is_vertical,
            showlabels,
            theme,
            border_radius,
        )

    # Apply base styling
    if is_vertical:
        p.xgrid.grid_line_color = None
        p.legend.orientation = "vertical"
    else:
        p.ygrid.grid_line_color = None
        p.legend.orientation = "vertical"
        if not legend_outside:
            p.legend.location = "top_right"

    p.legend.click_policy = "hide"

    # Set axis labels if provided
    if xlabel:
        p.xaxis.axis_label = xlabel
    if ylabel:
        p.yaxis.axis_label = ylabel

    # Apply theme
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)
    # Configure x-axis tick labels rotation and frequency
    if is_vertical:  # Only for vertical bar charts (x-axis has categories)
        p.xaxis.major_label_orientation = x_axis_label_orientation

        # Set tick label frequency using CustomJSTickFormatter
        if tick_label_step > 1:
            from bokeh.models import CustomJSTickFormatter

            tick_formatter = CustomJSTickFormatter(
                code=f"""
                var skipFactor = {tick_label_step};
                
                if (index % skipFactor !== 0) {{
                    return "";
                }}
                
                return tick;
            """
            )

            p.xaxis.formatter = tick_formatter
            p.min_border_bottom = 120  # More space for rotated labels
            p.min_border_left = 180

    else:  # Horizontal charts
        if tick_label_step > 1:
            from bokeh.models import CustomJSTickFormatter

            tick_formatter = CustomJSTickFormatter(
                code=f"""
                var skipFactor = {tick_label_step};
                
                if (index % skipFactor !== 0) {{
                    return "";
                }}
                
                return tick;
            """
            )

            p.yaxis.formatter = tick_formatter

    # Add custom text annotation if provided
    if custom_text0 is not None:
        for i in range(len(custom_text0)):
            # custom_text0 = [x, y, text, color, size]
            custom_text_color = custom_text0[i][3]
            custom_text_x = custom_text0[i][0]
            custom_text_y = custom_text0[i][1]
            custom_text = custom_text0[i][2]
            custom_text_size = custom_text0[i][4]

            from bokeh.models import Label

            text_color = (
                custom_text_color
                if custom_text_color
                else ("white" if theme == "dark" else "black")
            )
            label = Label(
                x=custom_text_x,
                y=custom_text_y,
                text=custom_text,
                text_font_size=custom_text_size,
                text_color=text_color,
                text_font_style="bold",
                # background_fill_color='rgba(255, 255, 255, 0.3)' if theme == 'light' else 'rgba(0, 0, 0, 0.3)',
                # background_fill_alpha=0.7,
                # border_line_color=text_color,
                # border_line_alpha=0.5,
            )
            p.add_layout(label)

    # Save the plot if requested
    if save == 1:
        save_plot(p, output_path)
        print(f"✓ Chart saved to: {output_path}")

    # Show the plot if requested
    if sh == 1:
        show(p)

    return p


def _plot_grouped_bars(
    p,
    df,
    cat_col,
    categories,
    series,
    colors,
    is_vertical,
    showlabels,
    theme,
    border_radius,
):
    """Plot grouped bars (vertical or horizontal)"""
    source = ColumnDataSource(df)

    # Determine label color based on theme
    label_color = "white" if theme == "dark" else "black"

    # Calculate dodge offsets
    n = len(series)
    step = 0.6 / n
    start = -0.3 + step / 2
    offsets = [start + i * step for i in range(n)]

    # Plot each series
    for col, color, offset in zip(series, colors, offsets):
        if is_vertical:
            r = p.vbar(
                x=dodge(cat_col, offset, range=p.x_range),
                top=col,
                width=step * 0.9,
                source=source,
                color=color,
                legend_label=str(col),
                line_color="black",
                name=col,
                selection_fill_alpha=1.0,
                nonselection_fill_alpha=0.2,
                border_radius=border_radius,
                hover_fill_color="#FF0000",
            )

            # Explicit hover glyph for vertical bars
            # r.hover_glyph = VBar(
            #     x=r.glyph.x,
            #     bottom=0,
            #     top=r.glyph.top,
            #     width=r.glyph.width,
            #     fill_color=r.glyph.fill_color,
            #     fill_alpha=r.glyph.fill_alpha
            #     if r.glyph.fill_alpha is not None
            #     else 1.0,
            #     line_color="red",
            #     line_width=2,
            #     line_alpha=1.0,
            # )

            # Hover tool
            p.add_tools(
                HoverTool(
                    tooltips=hovfun(
                        f"""<i>Category:</i> <b>@{cat_col}</b> <br> <i>Value:</i> <b>@{col}</b>"""
                    ),
                    renderers=[r],
                    mode="mouse",
                )
            )

            # Labels
            if showlabels == 1:
                labels = LabelSet(
                    x=dodge(cat_col, offset, range=p.x_range),
                    y=col,
                    text=col,
                    source=source,
                    text_align="center",
                    y_offset=7,
                    text_color=label_color,
                    text_font_size="12pt",
                    level="glyph",
                )
                p.add_layout(labels)

        else:  # horizontal
            r = p.hbar(
                y=dodge(cat_col, offset, range=p.y_range),
                right=col,
                height=step * 0.9,
                source=source,
                color=color,
                legend_label=str(col),
                line_color="black",
                hover_fill_color="#FF0000",
                name=col,
                selection_fill_alpha=1.0,
                nonselection_fill_alpha=0.2,
                border_radius=border_radius,
            )

            # Hover tool
            p.add_tools(
                HoverTool(
                    tooltips=hovfun(
                        f"""<i>Category:</i> <b>@{cat_col}</b> <br> <i>Value:</i> <b>@{col}</b>"""
                    ),
                    renderers=[r],
                    mode="mouse",
                )
            )

            # Labels
            if showlabels == 1:
                labels = LabelSet(
                    y=dodge(cat_col, offset, range=p.y_range),
                    x=col,
                    text=col,
                    source=source,
                    text_align="left",
                    x_offset=5,
                    y_offset=-3,
                    text_color=label_color,
                    text_font_size="12pt",
                    level="glyph",
                )
                p.add_layout(labels)


def _plot_stacked_bars(
    p,
    df,
    cat_col,
    categories,
    series,
    colors,
    is_vertical,
    showlabels,
    theme,
    border_radius,
):
    """Plot stacked bars (vertical or horizontal)"""

    # Determine label color based on theme
    total_label_color = "white" if theme == "dark" else "black"

    renderers = []

    if is_vertical:
        # Vertical stacked bars
        bottoms = [0] * len(df)
        for i, col in enumerate(series):
            tops = [bottoms[j] + df[col].iloc[j] for j in range(len(df))]
            r = p.vbar(
                x=categories,
                top=tops,
                bottom=bottoms,
                width=0.6,
                color=colors[i],
                legend_label=col,
                name=col,
                line_color="black",
                hover_fill_color="#FF0000",
                selection_fill_alpha=1.0,
                nonselection_fill_alpha=0.2,
                border_radius=border_radius,
            )
            renderers.append(r)
            bottoms = tops

        # Hover tool
        hover = HoverTool(
            tooltips=hovfun(
                """<i>Category:</i> <b>@x</b> <br> <i>Series:</i> <b>$name</b> <br> <i>Bottom:</i> <b>@bottom</b> <br> <i>Top:</i> <b>@top</b>"""
            ),
            renderers=renderers,
        )
        p.add_tools(hover)

        # Total labels
        if showlabels == 1:
            totals = df.iloc[:, 1:].sum(axis=1)
            label_source = ColumnDataSource({cat_col: categories, "total": totals})
            labels = LabelSet(
                x=cat_col,
                y="total",
                text="total",
                source=label_source,
                text_align="center",
                y_offset=6,
                text_color=total_label_color,
                text_font_size="12pt",
                level="glyph",
            )
            p.add_layout(labels)

    else:  # horizontal
        # Horizontal stacked bars
        lefts = [0] * len(df)
        for i, col in enumerate(series):
            rights = [lefts[j] + df[col].iloc[j] for j in range(len(df))]
            r = p.hbar(
                y=categories,
                left=lefts,
                right=rights,
                height=0.6,
                color=colors[i],
                legend_label=col,
                name=col,
                line_color="black",
                hover_fill_color="#FF0000",
                selection_fill_alpha=1.0,
                nonselection_fill_alpha=0.2,
                border_radius=border_radius,
            )
            renderers.append(r)
            lefts = rights

        # Hover tool
        hover = HoverTool(
            tooltips=hovfun(
                """<i>Category:</i> <b>@y</b> <br> <i>Series:</i> <b>$name</b> <br> <i>Left:</i> <b>@left</b> <br> <i>Right:</i> <b>@right</b>"""
            ),
            renderers=renderers,
        )
        p.add_tools(hover)

        # Total labels
        if showlabels == 1:
            totals = df.iloc[:, 1:].sum(axis=1)
            label_source = ColumnDataSource({cat_col: categories, "total": totals})
            labels = LabelSet(
                y=cat_col,
                x="total",
                text="total",
                source=label_source,
                text_align="left",
                x_offset=5,
                text_color=total_label_color,
                text_font_size="12pt",
                level="glyph",
            )
            p.add_layout(labels)


def _plot_gantt_bars(p, df, cat_col, colors, is_vertical, theme, border_radius):
    df["_hover_start"] = df[df.columns[1]].astype(str)
    df["_hover_end"] = df[df.columns[2]].astype(str)

    source = ColumnDataSource(df)

    start_col = df.columns[1]
    end_col = df.columns[2]

    bar_color = colors[0]

    if is_vertical:
        r = p.vbar(
            x=cat_col,
            bottom=start_col,
            top=end_col,
            width=0.6,
            source=source,
            color=bar_color,
            line_color="black",
            border_radius=border_radius,
            hover_fill_color="#FF0000",
        )
    else:
        r = p.hbar(
            y=cat_col,
            left=start_col,
            right=end_col,
            height=0.6,
            source=source,
            color=bar_color,
            line_color="black",
            border_radius=border_radius,
            hover_fill_color="#FF0000",
        )

    p.add_tools(
        HoverTool(
            tooltips=hovfun(
                f"""
                <b>@{cat_col}</b><br>
                Start: @_hover_start<br>
                End: @_hover_end
                """
            ),
            renderers=[r],
        )
    )




def line(
    df,
    x=None,
    y=None,
    title="Time Series Plot",
    xlabel=None,
    ylabel=None,
    secy=None,
    secco="#97573a",
    palette=None,
    sca=1,
    x_range=None,
    y_range=None,
    theme="light",
    legend_outside=True,
    width=1300,
    height=700,
    save=0,
    output_path="line_plot",
    sh=0,
    webgl=False,
    datetime_fmt=None,
    float_fmt="{0.00}",
):
    """
    Create interactive line charts with optional secondary y-axis.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with time series data (index or column as x-axis)
    x : str or pd.Index, optional
        Column name for x-axis or index. If None, uses df.index
    y : list of str, optional
        List of column names to plot. If None, plots all numeric columns
    title : str, default 'Time Series Plot'
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    secy : list with one str, optional
        Column name for secondary y-axis (e.g., ['temperature'])
    secco : str, default '#97573a'
        Color for secondary y-axis and its line
    palette : list, optional
        List of colors for lines. Uses default palette if None
    sca : int, default 1
        Show scatter points (1=show, 0=line only)
    x_range : tuple, optional
        (min, max) for x-axis range
    y_range : tuple, optional
        (min, max) for y-axis range
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default True
        If True, positions legend outside plot area
    width : int, default 1300
        Chart width in pixels
    height : int, default 700
        Chart height in pixels
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save)
    output_path : str, default 'line_plot'
        File path for saving
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show)
    webgl : bool, default False
        If True, uses WebGL backend for better performance with large datasets
    datetime_fmt : str, optional
        Datetime format for tooltips (e.g., "%Y-%m-%d %H:%M"). If None, auto-detects.
    float_fmt : str, default "{0.00}"
        Numeric format for tooltips (e.g., "{0.00}" for 2 decimals)

    Returns
    -------
    bokeh.plotting.figure.Figure
        Bokeh figure object

    Examples
    --------
    >>> dates = pd.date_range('2023-01-01', periods=100, freq='D')
    >>> df = pd.DataFrame({
    ...     'sales': np.cumsum(np.random.randn(100)) + 1000,
    ...     'profit': np.cumsum(np.random.randn(100)) + 500
    ... }, index=dates)
    >>> p = fline(df, title='Sales vs Profit', ylabel='Amount ($)')
    """

    # Setup data
    df = df.copy()

    # Handle x-axis
    if x is None:
        xlab = ["x_axis"]
        df[xlab[0]] = df.index
        x = df.index
    elif isinstance(x, str):
        xlab = [x]
        x = df[x]
    else:
        xlab = ["x_axis"]
        df[xlab[0]] = x

    # Handle y columns
    if y is None:
        # Auto-detect numeric columns, excluding xlab and secy
        exclude_cols = [xlab[0]]
        if secy:
            exclude_cols.append(secy[0])
        y = [
            col
            for col in df.select_dtypes(include=[np.number]).columns
            if col not in exclude_cols
        ]

    # Setup colors
    default_colors = bxc2
    if palette is None:
        palette = list(itertools.islice(itertools.cycle(default_colors), len(y)))

    # Create source with hidden column for tooltip control
    df["hidden"] = [0] * len(df.index)
    source = ColumnDataSource(df)

    # Determine ranges
    if x_range is None:
        x_range = (df[xlab[0]].min(), df[xlab[0]].max())

    if y_range is None:
        if secy is None:
            y_data = df[y]
        else:
            y_data = df[y]
        y_range = (y_data.min().min(), y_data.max().max())

    # Create figure
    fig_kwargs = {
        "x_range": x_range,
        "y_range": y_range,
        "width": width,
        "height": height,
        "title": title,
        "x_axis_label": xlabel or "",
        "y_axis_label": ylabel or "",
        "tools": "tap,wheel_zoom,box_zoom,pan,save,reset,lasso_select",
        "active_scroll": "wheel_zoom",
    }

    if webgl:
        fig_kwargs["output_backend"] = "webgl"

    p = figure(**fig_kwargs)

    # --- CRITICAL TOOLTIP SECTION - DO NOT MODIFY ---
    # --- color palette (general, reusable) ---
    columns = y
    hover_colors = dict(zip(columns, palette))
    renderers = []
    for col, color in hover_colors.items():
        if sca == 0:
            l = p.line(
                xlab[0],
                col,
                source=source,
                color=color,
                line_width=1.5,
                legend_label=col,
            )
            renderers.extend([l])
        else:
            s = p.scatter(
                xlab[0],
                col,
                source=source,
                size=7,
                color=color,
                legend_label=col,
                hover_line_width=10,
            )
            s.nonselection_glyph = None
            l = p.line(
                xlab[0],
                col,
                source=source,
                color=color,
                line_width=1.5,
                legend_label=col,
            )
            renderers.extend([s])

    tltl = build_auto_tooltip(
        df[[xlab[0]] + [c for c in df.columns if c not in [xlab[0], "hidden"]]],
        hovfun,
        datetime_fmt=datetime_fmt,
        float_fmt=float_fmt,
    )

    if secy is not None:
        from bokeh.models import LinearAxis, Range1d

        # secy = ["temperature"]
        # secco = '#97573a'
        p.extra_y_ranges = {
            secy[0]: Range1d(start=df[secy[0]].min(), end=df[secy[0]].max())
        }
        right_y_axis = LinearAxis(
            y_range_name=secy[0],
            axis_label=secy[0],
            axis_label_text_color=secco,
            axis_line_color=secco,
            major_label_text_color=secco,
            major_tick_line_color=secco,
            minor_tick_line_color=secco,
        )
        p.add_layout(right_y_axis, "right")

        if sca == 0:
            l3 = p.line(
                xlab[0],
                secy[0],
                source=source,
                line_color=secco,
                line_width=1.5,
                legend_label=secy[0],
                y_range_name=secy[0],
            )
            renderers.extend([l3])
        else:
            r3 = p.scatter(
                xlab[0],
                secy[0],
                source=source,
                size=7,
                legend_label=secy[0],
                color=secco,
                hover_line_width=10,
                y_range_name=secy[0],
            )
            l = p.line(
                xlab[0],
                secy[0],
                source=source,
                line_color=secco,
                line_width=1.5,
                legend_label=secy[0],
                y_range_name=secy[0],
            )
            renderers.extend([r3])

    if np.issubdtype(x.dtype, np.datetime64):
        p.add_tools(
            HoverTool(
                tooltips=tltl,
                formatters={"@" + xlab[0]: "datetime", "@hidden": cusj()},
                mode="vline",
                point_policy="none",
                line_policy="none",
                attachment="below",
                show_arrow=False,
                renderers=renderers,
            )
        )
    else:
        p.add_tools(
            HoverTool(
                tooltips=tltl,
                formatters={"@hidden": cusj()},
                mode="vline",
                point_policy="none",
                line_policy="none",
                attachment="below",
                show_arrow=False,
                renderers=renderers,
            )
        )
    # --- END CRITICAL TOOLTIP SECTION ---

    # Apply theme and extras
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)
    p = add_extras(p, cross=True)

    # Save if requested
    if save == 1:
        save_plot(p, output_path)
        print(f"✓ Chart saved to: {output_path}")

    # Show if requested
    if sh == 1:
        show(p)

    return p


# Helper function for auto-generating tooltips
def auto_detect_datetime_format(series):
    """
    Intelligently detect the best datetime format based on data granularity.

    Parameters
    ----------
    series : pd.Series
        Datetime series to analyze

    Returns
    -------
    str
        Optimal datetime format string for Bokeh tooltips
    """
    if not pd.api.types.is_datetime64_any_dtype(series):
        return "%Y-%m-%d"  # fallback

    # Drop NaN values for analysis
    clean_series = series.dropna()
    if len(clean_series) < 2:
        return "%Y-%m-%d"

    # Calculate time span and minimum delta
    time_span = clean_series.max() - clean_series.min()
    deltas = clean_series.diff().dropna()
    min_delta = deltas.min() if len(deltas) > 0 else pd.Timedelta(days=1)

    # Decision tree based on granularity
    if min_delta < pd.Timedelta(seconds=1):
        # Microsecond/millisecond level
        return "%Y-%m-%d %H:%M:%S.%f"
    elif min_delta < pd.Timedelta(minutes=1):
        # Second level
        return "%Y-%m-%d %H:%M:%S"
    elif min_delta < pd.Timedelta(hours=1):
        # Minute level
        return "%Y-%m-%d %H:%M"
    elif min_delta < pd.Timedelta(days=1):
        # Hour level
        return "%Y-%m-%d %H:%M"
    elif time_span < pd.Timedelta(days=60):
        # Days within 2 months - show date with day name
        return "%Y-%m-%d (%a)"
    elif time_span < pd.Timedelta(days=365):
        # Months within a year
        return "%Y-%m-%d"
    elif time_span < pd.Timedelta(days=365 * 3):
        # Multiple years but < 3 years
        return "%Y-%m-%d"
    else:
        # Long time spans - year/month only
        return "%Y-%m"


def build_auto_tooltip(df, hovfun, datetime_fmt=None, float_fmt="{0.00}"):
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
        Datetime display format. If None, auto-detects from data.
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

        # Check for datetime
        if pd.api.types.is_datetime64_any_dtype(dtype):
            # Auto-detect format if not provided
            if datetime_fmt is None:
                detected_fmt = auto_detect_datetime_format(df[col])
                tooltips[col] = f"@{col}{{{detected_fmt}}}"
                print(f"📅 Auto-detected datetime format for '{col}': {detected_fmt}")
            else:
                tooltips[col] = f"@{col}{{{datetime_fmt}}}"
        # Check for numeric types
        elif pd.api.types.is_numeric_dtype(dtype):
            tooltips[col] = f"@{col}{float_fmt}"
        # Everything else (strings, objects, etc.)
        else:
            tooltips[col] = f"@{col}"

    html = "<br>".join(f"<i>{k}:</i> <b>{v}</b>" for k, v in tooltips.items())
    return hovfun(html)




from bokeh.plotting import figure, show, output_file
from bokeh.models import (
    Label,
    HoverTool,
    ColumnDataSource,
    CustomJS,
    TapTool,
    GlobalInlineStyleSheet,
)
from bokeh.layouts import row
import numpy as np


def plot_arc_diagram(
    nodes,
    edges,
    node_colors=None,
    edge_weights=None,
    title="Arc Diagram",
    width=1200,
    height=800,
    node_size=15,
    arc_height_scale=1.5,
    dark_bg=True,
    show_labels=True,
):
    """
    Create an enhanced arc diagram with click-to-filter interactivity.

    Parameters:
    -----------
    nodes : list
        List of node names/labels
    edges : list of tuples
        List of (source, target) pairs where source and target are node indices
    node_colors : list, optional
        Colors for each node
    edge_weights : list, optional
        Weights for each edge (affects arc thickness)
    title : str
        Chart title
    width, height : int
        Figure dimensions
    node_size : int
        Size of node circles
    arc_height_scale : float
        Scale factor for arc heights
    dark_bg : bool
        Use dark background theme
    show_labels : bool
        Show node labels

    Returns:
    --------
    bokeh figure object
    """
    bg_color = "#2b2b2b" if dark_bg else "#f5f5f5"
    text_color = "white" if dark_bg else "black"

    n_nodes = len(nodes)

    # Default colors
    if node_colors is None:
        node_colors = ["#3498db"] * n_nodes

    # Normalize edge weights
    if edge_weights is None:
        edge_weights = [1.0] * len(edges)
    else:
        max_weight = max(edge_weights)
        edge_weights = [w / max_weight for w in edge_weights]

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        toolbar_location="right",
        tools="pan,wheel_zoom,reset,save",
        background_fill_color=bg_color,
        border_fill_color=bg_color,
        x_range=(-0.5, n_nodes - 0.5),
        y_range=(-0.2, 1.1),
    )

    # Styling
    p.title.text_color = text_color
    p.title.text_font_size = "18pt"
    p.title.text_font_style = "bold"
    p.xaxis.visible = False
    p.yaxis.visible = False
    p.xgrid.visible = False
    p.ygrid.visible = False
    p.outline_line_color = None

    # Node positions
    node_positions = list(range(n_nodes))

    # Store edge data for JavaScript callback
    edge_sources = []
    edge_node_pairs = []

    # Draw arcs (edges)
    for idx, ((source, target), weight) in enumerate(zip(edges, edge_weights)):
        if source == target:
            continue

        original_source = source
        original_target = target

        # Ensure source < target for arc direction
        if source > target:
            source, target = target, source

        # Arc parameters
        x_start = node_positions[source]
        x_end = node_positions[target]
        x_mid = (x_start + x_end) / 2
        span = abs(x_end - x_start)

        # Arc height
        arc_height = span / (2 * n_nodes) * arc_height_scale

        # Generate arc points
        n_points = max(50, int(span * 8))
        t = np.linspace(0, np.pi, n_points)

        x_arc = x_mid + (span / 2) * np.cos(t)
        y_arc = arc_height * np.sin(t)

        # Arc styling
        arc_color = node_colors[original_source]
        arc_alpha = 0.6
        arc_width = 2 + 4 * weight

        # Create data source with alpha control
        edge_data = ColumnDataSource(
            data=dict(
                x=x_arc,
                y=y_arc,
                edge_info=[f"{nodes[original_source]} → {nodes[original_target]}"]
                * len(x_arc),
                weight_info=[f"Weight: {weight:.2f}"] * len(x_arc),
            )
        )

        # Draw arc
        renderer = p.line(
            "x",
            "y",
            source=edge_data,
            color=arc_color,
            line_alpha=arc_alpha,
            line_width=arc_width,
            name=f"edge_{idx}",
        )

        edge_sources.append(edge_data)
        edge_node_pairs.append([original_source, original_target])

    # Add edge hover
    edge_hover = HoverTool(
        tooltips=[("Connection", "@edge_info"), ("Weight", "@weight_info")],
        mode="mouse",
        line_policy="nearest",
    )
    p.add_tools(edge_hover)

    # Create node data source
    node_source = ColumnDataSource(
        data=dict(
            x=node_positions,
            y=[0] * n_nodes,
            names=nodes,
            colors=node_colors,
            size=[node_size] * n_nodes,
            alpha=[1.0] * n_nodes,
        )
    )

    # Draw nodes
    nodes_renderer = p.circle(
        "x",
        "y",
        size="size",
        source=node_source,
        color="colors",
        fill_alpha="alpha",
        line_color="white" if dark_bg else "black",
        line_width=2.5,
        name="nodes",
    )

    # Add node hover - ONLY for nodes, placed AFTER edge hover
    node_hover = HoverTool(
        renderers=[nodes_renderer],
        tooltips=[("Node", "@names")],
        mode="mouse",
        point_policy="snap_to_data",
    )
    p.add_tools(node_hover)

    # Store original edge widths
    edge_widths = [2 + 4 * w for w in edge_weights]

    # JavaScript callback for click interaction
    callback = CustomJS(
        args=dict(
            node_source=node_source,
            edge_sources=edge_sources,
            edge_pairs=edge_node_pairs,
            edge_widths=edge_widths,
            base_node_size=node_size,
        ),
        code="""
            const indices = node_source.selected.indices;
            
            if (indices.length > 0) {
                const clicked = indices[0];
                
                // Update edges
                for (let i = 0; i < edge_sources.length; i++) {
                    const edge = edge_sources[i];
                    const [src, tgt] = edge_pairs[i];
                    
                    // Get current renderer
                    const renderers = Bokeh.documents[0].roots()[0].renderers;
                    const edge_renderer = renderers.find(r => r.name === 'edge_' + i);
                    
                    if (edge_renderer) {
                        if (src === clicked || tgt === clicked) {
                            // Highlight connected edges - keep original width
                            edge_renderer.glyph.line_alpha = 0.95;
                        } else {
                            // Dim unconnected edges
                            edge_renderer.glyph.line_alpha = 0.08;
                        }
                    }
                }
                
                // Update nodes
                const node_alphas = node_source.data['alpha'];
                const node_sizes = node_source.data['size'];
                
                for (let i = 0; i < node_alphas.length; i++) {
                    if (i === clicked) {
                        node_alphas[i] = 1.0;
                        node_sizes[i] = base_node_size * 1.5;
                    } else {
                        // Check if node is connected to clicked node
                        let connected = false;
                        for (let j = 0; j < edge_pairs.length; j++) {
                            const [src, tgt] = edge_pairs[j];
                            if ((src === clicked && tgt === i) || (tgt === clicked && src === i)) {
                                connected = true;
                                break;
                            }
                        }
                        node_alphas[i] = connected ? 1.0 : 0.2;
                        node_sizes[i] = connected ? base_node_size * 1.15 : base_node_size * 0.8;
                    }
                }
                
                node_source.change.emit();
                
            } else {
                // Reset all to original state
                for (let i = 0; i < edge_sources.length; i++) {
                    const renderers = Bokeh.documents[0].roots()[0].renderers;
                    const edge_renderer = renderers.find(r => r.name === 'edge_' + i);
                    if (edge_renderer) {
                        edge_renderer.glyph.line_alpha = 0.6;
                        edge_renderer.glyph.line_width = edge_widths[i];
                    }
                }
                
                const node_alphas = node_source.data['alpha'];
                const node_sizes = node_source.data['size'];
                
                for (let i = 0; i < node_alphas.length; i++) {
                    node_alphas[i] = 1.0;
                    node_sizes[i] = base_node_size;
                }
                
                node_source.change.emit();
            }
        """,
    )

    # Add tap tool
    tap = TapTool(renderers=[nodes_renderer], callback=callback)
    p.add_tools(tap)

    # Add a deselection callback to reset when clicking background
    deselect_callback = CustomJS(
        args=dict(
            node_source=node_source,
            edge_sources=edge_sources,
            edge_widths=edge_widths,
            base_node_size=node_size,
        ),
        code="""
            const indices = cb_obj.indices;
            
            if (indices.length === 0) {
                // Reset all edges when deselected
                for (let i = 0; i < edge_sources.length; i++) {
                    const renderers = Bokeh.documents[0].roots()[0].renderers;
                    const edge_renderer = renderers.find(r => r.name === 'edge_' + i);
                    if (edge_renderer) {
                        edge_renderer.glyph.line_alpha = 0.6;
                        edge_renderer.glyph.line_width = edge_widths[i];
                    }
                }
                
                // Reset all nodes to original size and alpha
                const node_alphas = node_source.data['alpha'];
                const node_sizes = node_source.data['size'];
                
                for (let i = 0; i < node_alphas.length; i++) {
                    node_alphas[i] = 1.0;
                    node_sizes[i] = base_node_size;
                }
                
                node_source.change.emit();
            }
        """,
    )

    node_source.selected.js_on_change("indices", deselect_callback)

    # Add labels
    if show_labels:
        for i, (pos, label) in enumerate(zip(node_positions, nodes)):
            label_obj = Label(
                x=pos,
                y=-0.08,
                text=label,
                text_color=text_color,
                text_font_size="10pt",
                text_align="center",
                text_baseline="top",
                angle=np.pi / 4,
            )
            p.add_layout(label_obj)

    return p


def create_sample_network(network_type="simple"):
    """Create sample network data."""

    if network_type == "simple":
        nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
        edges = [
            (0, 3),
            (0, 5),
            (1, 4),
            (1, 6),
            (2, 5),
            (2, 7),
            (3, 6),
            (4, 7),
            (0, 7),
            (1, 5),
        ]
        colors = [
            "#e74c3c",
            "#3498db",
            "#2ecc71",
            "#f39c12",
            "#9b59b6",
            "#1abc9c",
            "#e67e22",
            "#95a5a6",
        ]
        weights = None

    elif network_type == "social":
        nodes = [
            "Alice",
            "Bob",
            "Carol",
            "Dave",
            "Eve",
            "Frank",
            "Grace",
            "Henry",
            "Iris",
            "Jack",
        ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 5),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 6),
            (3, 7),
            (4, 5),
            (4, 8),
            (5, 9),
            (6, 7),
            (7, 9),
            (8, 9),
            (1, 6),
        ]
        colors = ["#3498db"] * len(nodes)
        weights = [3, 5, 2, 4, 3, 5, 2, 3, 4, 2, 3, 4, 5, 3, 2]

    elif network_type == "tech":
        nodes = [
            "Python",
            "JavaScript",
            "Java",
            "C++",
            "Ruby",
            "Go",
            "Rust",
            "TypeScript",
        ]
        edges = [
            (0, 1),
            (0, 2),
            (0, 4),
            (1, 7),
            (2, 3),
            (2, 5),
            (3, 6),
            (4, 5),
            (5, 6),
            (1, 4),
        ]
        colors = [
            "#3498db",
            "#f39c12",
            "#e74c3c",
            "#9b59b6",
            "#e74c3c",
            "#00d9ff",
            "#e67e22",
            "#3498db",
        ]
        weights = [5, 4, 3, 5, 3, 4, 2, 3, 2, 3]

    return nodes, edges, colors, weights


def mini_pie(
    data,
    category_col,
    y_values_col,
    values_col,
    title="Cycle Pie Plot",
    width=900,
    height=400,
    pie_radius=0.15,
    slice_names=None,
    slice_colors=None,
    show_line=True,
):
    """
    Create a mini-pie plot.
    """

    # Convert to list of dicts if needed
    if hasattr(data, "to_dict"):
        data = data.to_dict("records")

    categories = [d[category_col] for d in data]
    n_categories = len(categories)

    # Calculate global y-range
    y_values = [d[y_values_col] for d in data]
    y_min, y_max = min(y_values), max(y_values)
    y_range = y_max - y_min
    y_padding = y_range * 0.2

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, n_categories - 0.5),
        y_range=(y_min - y_padding - pie_radius, y_max + y_padding + pie_radius),
        toolbar_location="above",
        tools="pan,wheel_zoom,box_zoom,reset,save",
    )

    # Plot the main line and dots
    x_positions = list(range(n_categories))
    if show_line:
        p.line(
            x_positions,
            y_values,
            line_width=2,
            color="navy",
            alpha=0.5,
            line_dash="dashed",
        )
    # p.scatter(x_positions, y_values, size=8, color='navy', alpha=0.7)

    # Determine number of slices from first data point
    n_slices = len(data[0][values_col]) if data else 0

    # Set slice names if not provided
    if slice_names is None:
        slice_names = [f"Category {i + 1}" for i in range(n_slices)]

    # Set slice colors if not provided
    if slice_colors is None:
        from bokeh.palettes import Category10

        slice_colors = (
            Category10[n_slices] if n_slices <= 10 else Category10[10][:n_slices]
        )

    # Create separate data sources and renderers for each slice
    all_renderers = []

    for slice_idx in range(n_slices):
        # Prepare data for this specific slice only
        slice_data = {
            "x_center": [],
            "y_center": [],
            "start_angle": [],
            "end_angle": [],
            "value": [],
            "category": [],
            "slice_name": [],
            "percentage": [],
        }

        # Collect data for this slice from all data points
        for i, d in enumerate(data):
            category = d[category_col]
            y_center = d[y_values_col]
            composition = d[values_col]

            if not isinstance(composition, (list, tuple, np.ndarray)):
                continue

            total = sum(composition)
            if total == 0 or slice_idx >= len(composition):
                continue

            # Scale composition if needed
            scale_factor = y_center / total if total > 0 else 1
            scaled_composition = [v * scale_factor for v in composition]

            # Calculate cumulative angle up to this slice
            cumulative_angle = 0
            for j in range(slice_idx):
                if j < len(scaled_composition):
                    value = scaled_composition[j]
                    angle = 2 * pi * (value / y_center) if y_center > 0 else 0
                    cumulative_angle += angle

            # Calculate angle for this slice
            value = scaled_composition[slice_idx]
            angle = 2 * pi * (value / y_center) if y_center > 0 else 0

            if angle > 0:  # Only add if slice has non-zero value
                slice_data["x_center"].append(i)
                slice_data["y_center"].append(y_center)
                slice_data["start_angle"].append(cumulative_angle)
                slice_data["end_angle"].append(cumulative_angle + angle)
                slice_data["value"].append(value)
                slice_data["category"].append(category)
                slice_data["slice_name"].append(slice_names[slice_idx])
                slice_data["percentage"].append(value / y_center if y_center > 0 else 0)

        # Create source and renderer for this slice
        if slice_data["x_center"]:  # Only create if there's data
            source = ColumnDataSource(slice_data)

            # Create wedge renderer for this slice with its specific color
            renderer = p.wedge(
                x="x_center",
                y="y_center",
                radius=pie_radius,
                start_angle="start_angle",
                end_angle="end_angle",
                line_color="white",
                line_width=0.5,
                fill_color=slice_colors[slice_idx],
                source=source,
            )

            all_renderers.append((slice_names[slice_idx], renderer))

            # Add hover tool for this renderer
            hover = HoverTool(
                tooltips=[
                    ("Category", "@category"),
                    ("Component", "@slice_name"),
                    ("Value", "@value{0.0}"),
                    ("Percentage", "@percentage{0.0%}"),
                ],
                renderers=[renderer],
            )
            p.add_tools(hover)

    # Create legend with colored items
    legend_items = []
    for name, renderer in all_renderers:
        legend_items.append(LegendItem(label=name, renderers=[renderer]))

    # Add legend to the right of the plot
    legend = Legend(
        items=legend_items,
        location="center_right",
        title="Components",
        title_text_font_size="12pt",
        label_text_font_size="10pt",
    )

    p.add_layout(legend, "right")

    # Set x-axis labels
    p.xaxis.ticker = list(range(n_categories))
    p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}

    if n_categories > 8:
        p.xaxis.major_label_orientation = pi / 4

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = "#f0f0f0"
    p.xaxis.axis_label = "Category / Time"
    p.yaxis.axis_label = "Value"
    p.title.text_font_size = "14pt"

    return p


from bokeh.plotting import figure, show, output_file
from bokeh.models import (
    HoverTool,
    ColumnDataSource,
    LinearColorMapper,
    ColorBar,
    TapTool,
    BoxSelectTool,
)
from bokeh.layouts import column
from bokeh.palettes import Viridis256, Blues9
import pandas as pd
import numpy as np


def create_parallel_coordinates(
    data,
    dimensions,
    color_by=None,
    title="Parallel Coordinates",
    width=1200,
    height=600,
    line_alpha=0.3,
    line_width=1,
    palette=None,
    output_path=None,
):
    """
    Create an interactive parallel coordinates plot using Bokeh.

    Parameters:
    -----------
    data : pandas.DataFrame
        Data to visualize
    dimensions : list of str
        Column names to include as parallel axes (in order)
    color_by : str, optional
        Column name to color lines by
    title : str
        Plot title
    width : int
        Plot width in pixels
    height : int
        Plot height in pixels
    line_alpha : float
        Transparency of lines (0-1)
    line_width : float
        Width of lines
    palette : list, optional
        Color palette for coloring lines
    output_path : str
        Optional file path to save HTML output

    Returns:
    --------
    bokeh.plotting.figure
        The configured Bokeh figure with interactive features
    """

    # Prepare data
    df = data[dimensions].copy()

    # Normalize each dimension to 0-1 scale
    normalized = pd.DataFrame()
    for col in dimensions:
        col_min = df[col].min()
        col_max = df[col].max()
        if col_max > col_min:
            normalized[col] = (df[col] - col_min) / (col_max - col_min)
        else:
            normalized[col] = 0.5

    # Create x-positions for each axis
    num_axes = len(dimensions)
    x_positions = {dim: i for i, dim in enumerate(dimensions)}

    # Set up color mapping
    if color_by and color_by in data.columns:
        if palette is None:
            palette = Viridis256

        color_values = data[color_by].values
        color_min = color_values.min()
        color_max = color_values.max()

        # Map colors
        if color_max > color_min:
            color_indices = (
                (color_values - color_min)
                / (color_max - color_min)
                * (len(palette) - 1)
            ).astype(int)
            colors = [palette[i] for i in color_indices]
        else:
            colors = [palette[0]] * len(data)
    else:
        colors = ["#1f77b4"] * len(data)

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, num_axes - 0.5),
        y_range=(-0.1, 1.1),
        toolbar_location="above",
        tools="pan,wheel_zoom,box_zoom,reset,save",
    )

    # Prepare line segments data with interactivity
    all_sources = []
    all_renderers = []

    for idx in range(len(normalized)):
        xs = []
        ys = []
        hover_data = {"index": [], "dimension": [], "value": [], "normalized_value": []}

        for i, dim in enumerate(dimensions):
            xs.append(i)
            ys.append(normalized[dim].iloc[idx])
            hover_data["index"].append(idx)
            hover_data["dimension"].append(dim)
            hover_data["value"].append(df[dim].iloc[idx])
            hover_data["normalized_value"].append(normalized[dim].iloc[idx])

        # Add original data values for hover
        for col in data.columns:
            if col not in hover_data:
                hover_data[col] = [data[col].iloc[idx]] * len(dimensions)

        source = ColumnDataSource(hover_data)
        source.data["xs"] = [xs]
        source.data["ys"] = [ys]

        # Plot line with interactivity
        renderer = p.multi_line(
            xs="xs",
            ys="ys",
            line_width=line_width,
            line_alpha=line_alpha,
            color=colors[idx],
            hover_line_alpha=1.0,
            hover_line_width=line_width * 2,
            source=source,
            selection_line_alpha=1.0,
            selection_line_width=line_width * 3,
            selection_color=colors[idx],
            nonselection_line_alpha=0.1,
            nonselection_line_color="gray",
        )

        all_sources.append(source)
        all_renderers.append(renderer)

    # Add interactive hover tool
    hover = HoverTool(
        tooltips=[
            ("Record", "@index"),
            ("Dimension", "@dimension"),
            ("Value", "@value{0.2f}"),
        ]
        + [(col, f"@{col}{{0.2f}}") for col in data.columns if col in dimensions],
        mode="mouse",
    )
    p.add_tools(hover)

    # Add selection tools
    p.add_tools(TapTool())
    p.add_tools(BoxSelectTool())

    # Add vertical axes
    for i, dim in enumerate(dimensions):
        p.line([i, i], [0, 1], line_width=2, color="black", alpha=0.5)

    # Customize x-axis
    p.xaxis.ticker = list(range(num_axes))
    p.xaxis.major_label_overrides = {i: dim for i, dim in enumerate(dimensions)}
    p.xaxis.major_label_orientation = 0.3
    p.xaxis.major_label_text_font_size = "11pt"

    # Add axis labels with actual values
    for i, dim in enumerate(dimensions):
        col_min = df[dim].min()
        col_max = df[dim].max()

        # Add min/max labels
        p.text(
            x=[i],
            y=[-0.05],
            text=[f"{col_min:.0f}"],
            text_align="center",
            text_baseline="top",
            text_font_size="9pt",
            text_color="gray",
        )
        p.text(
            x=[i],
            y=[1.05],
            text=[f"{col_max:.0f}"],
            text_align="center",
            text_baseline="bottom",
            text_font_size="9pt",
            text_color="gray",
        )

    # Hide y-axis
    p.yaxis.visible = False
    p.ygrid.visible = False

    # Add color bar if coloring by a dimension
    if color_by and color_by in data.columns:
        color_mapper = LinearColorMapper(
            palette=palette, low=data[color_by].min(), high=data[color_by].max()
        )
        color_bar = ColorBar(color_mapper=color_mapper, title=color_by, location=(0, 0))
        p.add_layout(color_bar, "right")

    # Save to file if specified
    if output_path:
        output_file(output_path)

    return p


def create_treemap(
    data,
    title="Treemap",
    width=1000,
    height=600,
    palette=None,
    show_values=True,
    border_color="white",
    border_width=2,
    border_radius=0,
    theme="light",
    legend_outside=True,
    save=0,
    output_path="treemap",
    sh=0,
):
    """
    Create a professional treemap visualization using Bokeh.

    Parameters
    ----------
    data : list of dict or pd.DataFrame
        If list: Each dict must have 'category', 'subcategory', and 'value' keys
        If DataFrame: Must have columns 'category', 'subcategory', and 'value'
    title : str, default 'Treemap'
        Plot title
    width : int, default 1000
        Plot width in pixels
    height : int, default 600
        Plot height in pixels
    palette : dict, optional
        Mapping of category to color hex codes. Uses default if None.
    show_values : bool, default True
        Whether to display values in labels
    border_color : str, default 'white'
        Color of rectangle borders
    border_width : int, default 2
        Width of rectangle borders in pixels
    border_radius : int or float, default 0
        Radius for rounded corners (0 for sharp, 5-15 for rounded)
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default True
        If True, positions legend outside plot area to the right
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save)
    output_path : str, default 'treemap'
        File path for saving
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show)

    Returns
    -------
    bokeh.plotting.figure.Figure
        Bokeh figure object

    Examples
    --------
    >>> data = [
    ...     {'category': 'Tech', 'subcategory': 'Laptops', 'value': 1500},
    ...     {'category': 'Tech', 'subcategory': 'Phones', 'value': 2000},
    ...     {'category': 'Food', 'subcategory': 'Snacks', 'value': 800}
    ... ]
    >>> p = create_treemap(data, title='Sales by Category', theme='dark')
    """

    # Convert DataFrame to list of dicts if needed
    if isinstance(data, pd.DataFrame):
        if not all(col in data.columns for col in ["category", "subcategory", "value"]):
            raise ValueError(
                "DataFrame must have columns: 'category', 'subcategory', 'value'"
            )
        data = data.to_dict("records")

    # Sort by value descending for better layout
    data = sorted(data, key=lambda x: x["value"], reverse=True)

    # Extract data
    values = [d["value"] for d in data]
    labels = [d["subcategory"] for d in data]
    categories = [d["category"] for d in data]

    # Default color palette if none provided
    if palette is None:
        unique_cats = list(dict.fromkeys(categories))
        palette = {cat: bxc2[i % len(bxc2)] for i, cat in enumerate(unique_cats)}

    # Squarify algorithm for treemap layout
    total_value = sum(values)
    normalized = [v * 10000 / total_value for v in values]

    rects = []
    remaining = list(enumerate(normalized))
    x, y, w, h = 0, 0, 100, 100

    while remaining:
        if w >= h:
            # Horizontal layout
            row = []
            row_area = 0
            best_ratio = float("inf")

            for _, (idx, size) in enumerate(remaining):
                test_row = row + [(idx, size)]
                test_area = row_area + size
                col_width = test_area / h if h > 0 else 0

                ratios = []
                for _, s in test_row:
                    rect_h = s / col_width if col_width > 0 else 0
                    ratio = (
                        max(col_width / rect_h, rect_h / col_width)
                        if rect_h > 0
                        else float("inf")
                    )
                    ratios.append(ratio)
                test_ratio = max(ratios) if ratios else float("inf")

                if test_ratio <= best_ratio:
                    row = test_row
                    row_area = test_area
                    best_ratio = test_ratio
                else:
                    break

            col_width = row_area / h if h > 0 else 0
            rect_y = y
            for idx, size in row:
                rect_h = size / col_width if col_width > 0 else 0
                rects.append(
                    {"idx": idx, "x": x, "y": rect_y, "dx": col_width, "dy": rect_h}
                )
                rect_y += rect_h

            x += col_width
            w -= col_width
            remaining = remaining[len(row) :]
        else:
            # Vertical layout
            row = []
            row_area = 0
            best_ratio = float("inf")

            for _, (idx, size) in enumerate(remaining):
                test_row = row + [(idx, size)]
                test_area = row_area + size
                row_height = test_area / w if w > 0 else 0

                ratios = []
                for _, s in test_row:
                    rect_w = s / row_height if row_height > 0 else 0
                    ratio = (
                        max(rect_w / row_height, row_height / rect_w)
                        if rect_w > 0
                        else float("inf")
                    )
                    ratios.append(ratio)
                test_ratio = max(ratios) if ratios else float("inf")

                if test_ratio <= best_ratio:
                    row = test_row
                    row_area = test_area
                    best_ratio = test_ratio
                else:
                    break

            row_height = row_area / w if w > 0 else 0
            rect_x = x
            for idx, size in row:
                rect_w = size / row_height if row_height > 0 else 0
                rects.append(
                    {"idx": idx, "x": rect_x, "y": y, "dx": rect_w, "dy": row_height}
                )
                rect_x += rect_w

            y += row_height
            h -= row_height
            remaining = remaining[len(row) :]

    # Sort by original index
    rects = sorted(rects, key=lambda r: r["idx"])

    # Prepare plot data
    x_centers, y_centers, widths, heights, colors, display_labels = (
        [],
        [],
        [],
        [],
        [],
        [],
    )
    percentages = []

    for r in rects:
        idx = r["idx"]
        rx, ry, rw, rh = r["x"], r["y"], r["dx"], r["dy"]

        x_centers.append(rx + rw / 2)
        y_centers.append(ry + rh / 2)
        widths.append(rw)
        heights.append(rh)
        colors.append(palette[categories[idx]])
        percentages.append(round(100 * values[idx] / total_value, 1))

        # Label visibility based on size with smart formatting
        if show_values and rw > 10 and rh > 8:
            display_labels.append(f"{labels[idx]}\n{values[idx]}")
        elif rw > 6 and rh > 5:
            display_labels.append(labels[idx])
        else:
            display_labels.append("")

    source = ColumnDataSource(
        data={
            "x": x_centers,
            "y": y_centers,
            "width": widths,
            "height": heights,
            "color": colors,
            "label": display_labels,
            "subcategory": labels,
            "category": categories,
            "value": values,
            "percentage": percentages,
        }
    )

    # Create figure with tools
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-5, 105),
        y_range=(-5, 105),
        tools="tap,wheel_zoom,box_zoom,pan,save,reset",
        active_scroll="wheel_zoom",
        toolbar_location="left",
    )

    # Group rectangles by category for legend
    category_renderers = {}
    unique_categories = list(dict.fromkeys(categories))

    for cat in unique_categories:
        # Filter source data for this category
        mask = [c == cat for c in categories]
        cat_indices = [i for i, m in enumerate(mask) if m]

        cat_source = ColumnDataSource(
            data={
                "x": [x_centers[i] for i in cat_indices],
                "y": [y_centers[i] for i in cat_indices],
                "width": [widths[i] for i in cat_indices],
                "height": [heights[i] for i in cat_indices],
                "color": [colors[i] for i in cat_indices],
                "label": [display_labels[i] for i in cat_indices],
                "subcategory": [labels[i] for i in cat_indices],
                "category": [categories[i] for i in cat_indices],
                "value": [values[i] for i in cat_indices],
                "percentage": [percentages[i] for i in cat_indices],
            }
        )

        # Draw rectangles for this category
        r = p.rect(
            x="x",
            y="y",
            width="width",
            height="height",
            source=cat_source,
            fill_color="color",
            fill_alpha=0.85,
            line_color=border_color,
            line_width=border_width,
            hover_fill_alpha=1.0,
            selection_fill_alpha=1.0,
            nonselection_fill_alpha=0.3,
            legend_label=cat,
            border_radius=border_radius,
        )

        category_renderers[cat] = r

    # Add hover tool with styled tooltip
    hover = HoverTool(
        tooltips=hovfun("""
            <i>Category:</i> <b>@category</b><br>
            <i>Item:</i> <b>@subcategory</b><br>
            <i>Value:</i> <b>@value{0,0}</b><br>
            <i>Share:</i> <b>@percentage{0.0}%</b>
        """),
        mode="mouse",
    )
    p.add_tools(hover)

    # Add labels with dynamic sizing
    for r in rects:
        idx = r["idx"]
        rx, ry, rw, rh = r["x"], r["y"], r["dx"], r["dy"]

        # Calculate appropriate font size
        area = rw * rh
        if area > 400:
            font_size = "14pt"
        elif area > 200:
            font_size = "12pt"
        elif area > 100:
            font_size = "10pt"
        elif area > 50:
            font_size = "9pt"
        else:
            font_size = "8pt"

        if display_labels[idx]:
            label_source = ColumnDataSource(
                data={
                    "x": [rx + rw / 2],
                    "y": [ry + rh / 2],
                    "text": [display_labels[idx]],
                }
            )

            label_color = "white" if theme == "dark" else "#2C3E50"
            labels_set = LabelSet(
                x="x",
                y="y",
                text="text",
                source=label_source,
                text_align="center",
                text_baseline="middle",
                text_font_size=font_size,
                text_color=label_color,
                text_font="Helvetica",
            )
            p.add_layout(labels_set)

    # Hide axes (treemaps don't need them)
    p.xaxis.visible = False
    p.yaxis.visible = False
    p.xgrid.visible = False
    p.ygrid.visible = False

    # Apply theme styling
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)

    # Save if requested
    if save == 1:
        save_plot(p, output_path)
        print(f"✓ Treemap saved to: {output_path}")

    # Show if requested
    if sh == 1:
        show(p)

    return p



def hist(
    df,
    col=None,
    bins=30,
    title=None,
    xlabel=None,
    ylabel=None,
    color=None,
    palette=None,
    density=False,
    theme="light",
    legend_outside=False,
    width=1000,
    height=600,
    save=0,
    output_path="histogram",
    sh=0,
    show_kde=False,
    kde_color="#ff6464",
):
    """
    Create a clean, interactive histogram from a DataFrame column.

    Parameters
    ----------
    df : pd.DataFrame
        The input data
    col : str, optional
        Column name to plot. If None and df has only one numeric column, uses that column.
    bins : int, default 30
        Number of bins for histogram
    title : str, optional
        Plot title. Auto-generated if None.
    xlabel : str, optional
        X-axis label. Uses column name if None.
    ylabel : str, optional
        Y-axis label. Auto-generated based on density parameter.
    color : str, optional
        Color for bars. Uses palette[0] or default if None.
    palette : list, optional
        Color palette. Uses default bxc2 if None.
    density : bool, default False
        If True, normalize to probability density
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default False
        If True, positions legend outside plot area (useful with KDE)
    width : int, default 1000
        Plot width in pixels
    height : int, default 600
        Plot height in pixels
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save)
    output_path : str, default 'histogram'
        File path for saving
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show)
    show_kde : bool, default False
        If True, overlays a kernel density estimate curve
    kde_color : str, default '#ff6464'
        Color for KDE curve

    Returns
    -------
    bokeh.plotting.figure.Figure
        Bokeh figure object

    Examples
    --------
    >>> df = pd.DataFrame({'age': np.random.normal(35, 10, 1000)})
    >>> p = fhist(df, 'age', bins=40, title='Age Distribution', theme='dark')

    >>> # With KDE overlay
    >>> p = fhist(df, 'age', bins=30, show_kde=True, kde_color='orange')
    """

    # Auto-detect column if not provided
    if col is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            raise ValueError("DataFrame has no numeric columns")
        elif len(numeric_cols) == 1:
            col = numeric_cols[0]
        else:
            raise ValueError(
                f"Multiple numeric columns found. Please specify 'col' parameter. Options: {list(numeric_cols)}"
            )

    # Validate column
    if col not in df.columns:
        raise ValueError(
            f"Column '{col}' not found in DataFrame. Available columns: {list(df.columns)}"
        )

    # Get clean data
    clean_data = df[col].dropna()

    # Compute histogram
    hist, edges = np.histogram(clean_data, bins=bins, density=density)

    # Prepare data source
    src = ColumnDataSource(
        data=dict(
            left=edges[:-1],
            right=edges[1:],
            top=hist,
            center=(edges[:-1] + edges[1:]) / 2,
            width=np.diff(edges),
        )
    )

    # Setup colors
    if palette is None:
        palette = bxc2
    if color is None:
        color = palette[0]

    # Auto-generate title
    if title is None:
        title = f"Distribution of {col}"

    # Setup axis labels
    if xlabel is None:
        xlabel = col
    if ylabel is None:
        ylabel = "Density" if density else "Frequency"

    # Create figure
    p = figure(
        title=title,
        width=width,
        height=height,
        tools="tap,wheel_zoom,box_zoom,pan,save,reset",
        active_scroll="wheel_zoom",
        toolbar_location="left",
    )

    # Add histogram bars
    r = p.quad(
        top="top",
        bottom=0,
        left="left",
        right="right",
        fill_color=color,
        line_color="white",
        line_width=2,
        fill_alpha=0.75,
        hover_fill_alpha=0.95,
        selection_fill_alpha=1.0,
        nonselection_fill_alpha=0.3,
        source=src,
        legend_label="Histogram",
    )

    # Add hover tooltip
    hover_tool = HoverTool(
        renderers=[r],
        tooltips=hovfun(f"""
            <i>Range:</i> <b>@left{{0.00}} — @right{{0.00}}</b><br>
            <i>{"Density" if density else "Count"}:</i> <b>@top{{0.000}}</b><br>
            <i>Bin Width:</i> <b>@width{{0.00}}</b>
        """),
        mode="mouse",
    )
    p.add_tools(hover_tool)

    # Add KDE curve if requested
    if show_kde:
        from scipy import stats

        # Generate KDE
        kde = stats.gaussian_kde(clean_data)
        x_range = np.linspace(clean_data.min(), clean_data.max(), 200)
        kde_values = kde(x_range)

        # Scale KDE to match histogram height if not density
        if not density:
            kde_values = kde_values * len(clean_data) * (edges[1] - edges[0])

        kde_source = ColumnDataSource(data=dict(x=x_range, y=kde_values))

        kde_line = p.line(
            "x",
            "y",
            source=kde_source,
            line_color=kde_color,
            line_width=3,
            alpha=0.8,
            legend_label="KDE",
        )

    # Set axis labels
    p.xaxis.axis_label = xlabel
    p.yaxis.axis_label = ylabel

    # Apply theme
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)

    # Save if requested
    if save == 1:
        save_plot(p, output_path)
        print(f"✓ Histogram saved to: {output_path}")

    # Show if requested
    if sh == 1:
        show(p)

    return p



def get_light_stylesheet_3d():
    """Create a new light theme stylesheet instance."""
    return GlobalInlineStyleSheet(css=""" 
        html, body, .bk, .bk-root {
            background-color: #FDFBD4; 
            margin: 0; 
            padding: 0; 
            height: 100%; 
            color: black; 
            font-family: 'Consolas', 'Helvetica', monospace; 
        } 
        .bk { color: black; } 
        .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, 
        .bk-label, .bk-title, .bk-legend, .bk-axis-label { 
            color: black !important; 
        } 
        .bk-input::placeholder { color: #555555 !important; } 
    """)

from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, Label
from bokeh.palettes import Category10
import math


def create_sunburst(
    data,
    title="Sunburst Chart",
    width=800,
    height=800,
):
    """
    Create an interactive sunburst chart from hierarchical data.

    Parameters:
    -----------
    data : dict
        Hierarchical data with structure: {"name": str, "children": [...]},
        leaf nodes have "value": float
    title : str
        Chart title
    width, height : int
        Figure dimensions
    output_filename : str
        Output HTML filename

    Returns:
    --------
    Bokeh figure object
    """

    PALETTE = Category10[10]

    def get_node_value(node):
        """Get total value of a node"""
        if "value" in node:
            return node["value"]
        elif "children" in node:
            return sum(get_node_value(child) for child in node["children"])
        return 1

    def shade(hex_color, factor=0.2):
        """Lighten color by factor (0=no change, 1=white)"""
        hex_color = hex_color.lstrip("#")
        rgb = [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]
        rgb = [int(max(0, min(c + (255 - c) * factor, 255))) for c in rgb]
        return "#%02x%02x%02x" % tuple(rgb)

    def build_wedges(root_node):
        """Build all wedge segments for sunburst"""
        wedges = []

        def process_node(
            node, depth, start_angle, end_angle, parent_color, color_index
        ):
            # Assign colors
            if depth == 1:
                this_color = PALETTE[color_index % len(PALETTE)]
            elif depth > 1:
                this_color = shade(parent_color, factor=min(0.15 * depth, 0.8))
            else:
                this_color = None

            # Create wedge for this node
            if depth > 0:
                inner_r = 30 + (depth - 1) * 80
                outer_r = 30 + depth * 80

                mid_angle = (start_angle + end_angle) / 2
                mid_radius = (inner_r + outer_r) / 2

                wedges.append(
                    {
                        "name": node["name"],
                        "value": get_node_value(node),
                        "depth": depth,
                        "start_angle": start_angle,
                        "end_angle": end_angle,
                        "inner_radius": inner_r,
                        "outer_radius": outer_r,
                        "color": this_color,
                        "mid_angle": mid_angle,
                        "mid_radius": mid_radius,
                    }
                )

            # Recurse children
            if node.get("children"):
                children = node["children"]
                total_value = sum(get_node_value(child) for child in children)
                cur_angle = start_angle

                for i, child in enumerate(children):
                    child_value = get_node_value(child)
                    proportion = child_value / total_value if total_value else 0
                    span = (end_angle - start_angle) * proportion
                    next_angle = cur_angle + span

                    if depth == 0:
                        process_node(
                            child,
                            depth + 1,
                            cur_angle,
                            next_angle,
                            PALETTE[i % len(PALETTE)],
                            i,
                        )
                    else:
                        process_node(
                            child,
                            depth + 1,
                            cur_angle,
                            next_angle,
                            this_color,
                            color_index,
                        )

                    cur_angle = next_angle

        process_node(root_node, 0, 0, 2 * math.pi, None, -1)
        return wedges

    # Build wedges
    wedges = build_wedges(data)

    # Prepare data for Bokeh
    wedge_data = {
        "x": [0] * len(wedges),
        "y": [0] * len(wedges),
        "start_angle": [w["start_angle"] for w in wedges],
        "end_angle": [w["end_angle"] for w in wedges],
        "inner_radius": [w["inner_radius"] for w in wedges],
        "outer_radius": [w["outer_radius"] for w in wedges],
        "name": [w["name"] for w in wedges],
        "value": [w["value"] for w in wedges],
        "depth": [w["depth"] for w in wedges],
        "color": [w["color"] for w in wedges],
    }

    source = ColumnDataSource(data=wedge_data)

    # Create figure
    max_radius = max(w["outer_radius"] for w in wedges)
    p = figure(
        width=width,
        height=height,
        title=title,
        toolbar_location="above",
        tools="pan,wheel_zoom,reset,hover",
        x_range=(-max_radius * 1.3, max_radius * 1.9),
        y_range=(-max_radius * 1.3, max_radius * 1.3),
        match_aspect=True,
    )

    # Draw wedges
    p.annular_wedge(
        x="x",
        y="y",
        inner_radius="inner_radius",
        outer_radius="outer_radius",
        start_angle="start_angle",
        end_angle="end_angle",
        color="color",
        alpha=0.85,
        line_color="white",
        line_width=2,
        source=source,
        hover_alpha=1.0,
        hover_line_color="black",
        hover_line_width=3,
    )

    # Add hover tool
    hover = p.select_one(HoverTool)
    hover.tooltips = [("Name", "@name"), ("Value", "@value{,0}"), ("Depth", "@depth")]

    # Build legend - show level 1 categories with their colors
    level_1_wedges = [w for w in wedges if w["depth"] == 1]
    legend_x = max_radius * 1.1
    legend_y_start = max_radius * 0.8
    legend_spacing = max_radius * 0.15

    # Legend title
    legend_title = Label(
        x=legend_x,
        y=legend_y_start + legend_spacing * 1.5,
        text="Categories",
        text_font_size="16pt",
        text_color="#333",
        text_font_style="bold",
        text_align="left",
        text_baseline="middle",
    )
    p.add_layout(legend_title)

    # Legend items
    for i, wedge in enumerate(level_1_wedges):
        y_pos = legend_y_start - i * legend_spacing

        # Color box
        p.rect(
            x=legend_x,
            y=y_pos,
            width=max_radius * 0.08,
            height=max_radius * 0.08,
            fill_color=wedge["color"],
            line_color="white",
            line_width=2,
        )

        # Label
        label = Label(
            x=legend_x + max_radius * 0.12,
            y=y_pos,
            text=f"{wedge['name']} ({int(wedge['value'])})",
            text_font_size="12pt",
            text_color="#333",
            text_align="left",
            text_baseline="middle",
        )
        p.add_layout(label)

    # Styling
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.background_fill_color = "#fafafa"
    p.title.text_font_size = "18pt"
    p.title.text_color = "#333"
    p.title.align = "center"

    return p


import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import (
    LinearColorMapper,
    BasicTicker,
    ColorBar,
    ColumnDataSource,
    HoverTool,
)
from bokeh.palettes import interp_palette


# ───────────────────────────────────────────────
# 🌈 Default palette (Michael’s)
# ───────────────────────────────────────────────
mike2 = (
    "#000063",
    "#123aff",
    "#00aeff",
    "#26fff4",
    "#00ff95",
    "#19ff19",
    "#ffff00",
    "#ff8a15",
    "#ff2a1b",
    "#db0000",
    "#4b0000",
)
bo_mike2 = interp_palette(mike2, 255)


# ───────────────────────────────────────────────
# 🌍 Coastline extractor
# ───────────────────────────────────────────────
def crd():
    import cartopy.feature as cf, numpy as np

    # create the list of coordinates separated by nan to avoid connecting the lines
    x_coords = []
    y_coords = []
    for coord_seq in cf.COASTLINE.geometries():
        x_coords.extend([k[0] for k in coord_seq.coords] + [np.nan])
        y_coords.extend([k[1] for k in coord_seq.coords] + [np.nan])
    return (
        x_coords,
        y_coords,
    )  # x_coords2,y_coords2


x_coords, y_coords = [i for i in crd()]



# ───────────────────────────────────────────────
# 🔥 High-Level Heatmap Function
# ───────────────────────────────────────────────
def fworld_heatmap(
    data0,
    title="🌍 Global Heatmap",
    palette=bo_mike2,
    vmin=None, vmax=None,
    width=1200, height=600,
    coast_color="black",
    cbar_title = None,
    xr_=[-180,180],yr_=[-90,90],
    sh=0,
):
    """
    High-level world heatmap with coastlines using Bokeh.

    Parameters
    ----------
    data : 2D np.ndarray
        Values on a regular (lat, lon) grid.
    lon, lat : 1D arrays
        Longitude and latitude coordinates.
    title : str
        Plot title.
    palette : list
        Bokeh-compatible palette (list of hex colors).
    vmin, vmax : float
        Data range for color mapping.
    width, height : int
        Figure size.
    coast_color : str
        Color for coastlines.
    hover : bool
        Add hover tooltip.
    """

    data = data0.values

    lat = data0.lat.values
    lon = data0.lon.values
    # Compute limits
    vmin = np.nanmin(data) if vmin is None else vmin
    vmax = np.nanmax(data) if vmax is None else vmax

    # Color mapper
    mapper = LinearColorMapper(palette=palette, low=vmin, high=vmax)

    # Flatten data
    lats = np.repeat(lat, len(lon))
    lons = np.tile(lon, len(lat))
    source = ColumnDataSource(data=dict(image=[data], latitudes=[lats], longitudes=[lons]))

    p = figure(output_backend="webgl",     
    border_fill_color="#e0e0e0",
    background_fill_color="#e0e0e0",
    width=width,
    height=height,
    x_range=(xr_[0],xr_[1]), y_range=(yr_[0],yr_[1]),
    title=title,

)
    

    # Add image
    img = p.image(
        image='image', source=source,
        x=lon.min(), y=lat.min(),
        dw=lon.max() - lon.min(), dh=lat.max() - lat.min(),
        color_mapper=mapper
    )

    # Add color bar
    color_bar = ColorBar(
        color_mapper=mapper, ticker=BasicTicker(),
        label_standoff=10, location=(0, 0),
        title=cbar_title, title_text_font_size="14pt",title_text_color="black", major_label_text_font_size="14pt", background_fill_alpha=0,
    )
    p.add_layout(color_bar, "right")

    # Add coastlines

    p.line(x_coords, y_coords, line_width=1, line_color=coast_color, alpha=0.8)

    # Add hover tool

    hover_tool = HoverTool(
        renderers=[img],
        tooltips=hovfun("""
            <b>Value:</b> @image<br>
            <b>Lat:</b> @latitudes<br>
            <b>Lon:</b> @longitudes
        """)
    )
    p.add_tools(hover_tool)

    if sh==1:
       show(p)

    return p


def darken_color(hex_color, factor=0.7):
    """Darken a hex color by a factor."""
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    r, g, b = int(r * factor), int(g * factor), int(b * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def plot_3d_pie(
    values,
    colors,
    labels,
    title="3D Pie Chart",
    width=800,
    height=700,
    radius=1.5,
    depth=0.3,
    tilt=25,
    rotation=0,
    dark_bg=True,
    explode=None,
):
    """
    Create a PROPERLY WORKING 3D pie chart with correct perspective.
    """
    bg_color = "#343838" if dark_bg else "#FDFBD4"
    text_color = "white" if dark_bg else "black"

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
    p.title.text_font_size = "16pt"
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
        mid_angle = start_angles[i] + angles[i] / 2 + rotation
        # Use negative sin for proper sorting (back to front)
        slice_order.append((-np.sin(np.radians(mid_angle)), i))

    slice_order.sort()

    for _, i in slice_order:
        start_deg = start_angles[i] + rotation
        end_deg = start_deg + angles[i]
        mid_deg = start_deg + angles[i] / 2

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
            angle_mid = (theta[j] + theta[j + 1]) / 2
            # Front-facing check: sin(angle) should be NEGATIVE (towards viewer)
            if np.sin(angle_mid) < 0:
                edge_x = [
                    top_x[j],
                    top_x[j + 1],
                    bottom_x[j + 1],
                    bottom_x[j],
                    top_x[j],
                ]
                edge_y = [
                    top_y[j],
                    top_y[j + 1],
                    bottom_y[j + 1],
                    bottom_y[j],
                    top_y[j],
                ]
                p.patch(
                    edge_x,
                    edge_y,
                    color=edge_color,
                    alpha=1.0,
                    line_color="#000000",
                    line_width=0.8,
                )

        # Add vertical hatching on outer edge
        hatch_density = max(8, int(angles[i] / 360 * 50))
        hatch_indices = np.linspace(0, len(theta) - 1, hatch_density, dtype=int)

        for idx in hatch_indices:
            if idx < len(theta) and np.sin(theta[idx]) < 0:
                hatch_x = [top_x[idx], bottom_x[idx]]
                hatch_y = [top_y[idx], bottom_y[idx]]
                p.line(hatch_x, hatch_y, color="#000000", alpha=0.3, line_width=1.0)

        # Top surface
        top_wedge_x = np.concatenate([[explode_x], top_x, [explode_x]])
        top_wedge_y = np.concatenate([[explode_y], top_y, [explode_y]])

        source = ColumnDataSource(
            data=dict(
                x=top_wedge_x,
                y=top_wedge_y,
                label=[labels[i]] * len(top_wedge_x),
                value=[values[i]] * len(top_wedge_x),
                percentage=[f"{percentages[i] * 100:.1f}%"] * len(top_wedge_x),
            )
        )

        p.patch(
            "x",
            "y",
            source=source,
            color=colors[i],
            alpha=1.0,
            line_color="#000000",
            line_width=1.2,
            hover_alpha=0.8,
        )

        # Add percentage label on top surface
        label_radius = radius * 0.65
        label_x = label_radius * np.cos(np.radians(mid_deg)) + explode_x
        label_y = (
            label_radius * np.sin(np.radians(mid_deg)) * np.cos(tilt_rad) + explode_y
        )

        percentage_text = f"{percentages[i] * 100:.1f}%"
        label_obj = Label(
            x=label_x,
            y=label_y,
            text=percentage_text,
            text_color="white",
            text_font_size="14pt",
            text_align="center",
            text_baseline="middle",
            text_font_style="normal",
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
    text_color = "white" if dark_bg else "black"
    bg_color = "#343838" if dark_bg else "#FDFBD4"

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
        y_range=(0, len(labels) * item_height + 20),
    )

    legend_fig.xaxis.visible = False
    legend_fig.yaxis.visible = False
    legend_fig.xgrid.visible = False
    legend_fig.ygrid.visible = False

    for i, (label, color) in enumerate(zip(labels, colors)):
        y_pos = (len(labels) - i) * item_height - 10

        # Draw color circle
        legend_fig.circle(
            x=[0.1],
            y=[y_pos],
            size=18,
            color=color,
            alpha=1.0,
            line_color="#000000",
            line_width=2,
        )

        # Draw text label
        label_obj = Label(
            x=0.18,
            y=y_pos - 7,
            text=label,
            text_color=text_color,
            text_font_size="12pt",
            text_baseline="middle",
        )
        legend_fig.add_layout(label_obj)

    return legend_fig


import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import LinearColorMapper, ColorBar, Range1d
from bokeh.palettes import Viridis256, Plasma256


def plot_surface_bokeh(
    Z_func,
    x_range=(-3, 3),
    y_range=(-3, 3),
    n_points=40,
    cmap=Plasma256,
    elev_deg=25,
    azim_deg=45,
    title="3D Surface",
    output_path=None,
):
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
            xs = [
                X_proj[i, j],
                X_proj[i, j + 1],
                X_proj[i + 1, j + 1],
                X_proj[i + 1, j],
            ]
            ys = [
                Z_proj[i, j],
                Z_proj[i, j + 1],
                Z_proj[i + 1, j + 1],
                Z_proj[i + 1, j],
            ]
            avg_z = (Z[i, j] + Z[i, j + 1] + Z[i + 1, j + 1] + Z[i + 1, j]) / 4
            depth = (
                Y_rot[i, j] + Y_rot[i, j + 1] + Y_rot[i + 1, j + 1] + Y_rot[i + 1, j]
            ) / 4
            quads.append((depth, xs, ys, avg_z))

    quads.sort(key=lambda q: q[0], reverse=True)
    quad_xs = [q[1] for q in quads]
    quad_ys = [q[2] for q in quads]
    quad_colors = [q[3] for q in quads]

    # Color mapping
    z_min, z_max = Z.min(), Z.max()
    color_mapper = LinearColorMapper(palette=cmap, low=z_min, high=z_max)
    colors = [cmap[int((val - z_min) / (z_max - z_min) * 255)] for val in quad_colors]

    # Create figure
    p = figure(width=1200, height=800, title=title, toolbar_location=None)
    p.patches(
        xs=quad_xs,
        ys=quad_ys,
        fill_color=colors,
        line_color="#306998",
        line_alpha=0.3,
        line_width=0.5,
        alpha=0.9,
    )

    # Axis ranges
    x_min, x_max = min(min(xs) for xs in quad_xs), max(max(xs) for xs in quad_xs)
    y_min, y_max = min(min(ys) for ys in quad_ys), max(max(ys) for ys in quad_ys)
    x_pad, y_pad = (x_max - x_min) * 0.15, (y_max - y_min) * 0.15
    p.x_range = Range1d(x_min - x_pad, x_max + x_pad)
    p.y_range = Range1d(y_min - y_pad, y_max + y_pad)

    # Clean axes
    p.xaxis.visible = False
    p.yaxis.visible = False

    # Color bar
    color_bar = ColorBar(
        color_mapper=color_mapper, width=60, location=(0, 0), title="Z"
    )
    p.add_layout(color_bar, "right")

    # Save HTML if requested
    if output_path:
        output_file(output_path)

    return p


from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.models import HoverTool
from bokeh.io import output_notebook
# curdoc().theme = 'dark_minimal'
# curdoc().theme = 'light_minimal'


def dumbbell_plot(
    data,
    start_col,
    end_col,
    category_col,
    orientation="horizontal",
    title="Dumbbell Plot",
    start_color="#3498db",
    end_color="#e74c3c",
    line_color="#95a5a6",
    width=800,
    height=400,
    start_label="Start",
    end_label="End",
    glow=True,
    line_width=2,
    point_size=12,
):
    """
    Create a dumbbell plot using Bokeh.

    Parameters:
    -----------
    data : list of dict or pandas DataFrame
        Data containing categories and start/end values
    start_col : str
        Column name for start values
    end_col : str
        Column name for end values
    category_col : str
        Column name for categories
    orientation : str
        'horizontal' or 'vertical'
    title : str
        Plot title
    start_color : str
        Color for start points
    end_color : str
        Color for end points
    line_color : str
        Color for connecting lines
    width : int
        Plot width in pixels
    height : int
        Plot height in pixels
    start_label : str
        Label for start points in legend
    end_label : str
        Label for end points in legend
    glow : bool
        Enable glow effect around points
    line_width : int or float
        Width of the connecting lines (default: 2)
    point_size : int or float
        Size of the point circles (default: 12)

    Returns:
    --------
    Bokeh figure object
    """

    # Convert to list of dicts if needed
    if hasattr(data, "to_dict"):
        data = data.to_dict("records")

    categories = [str(d[category_col]) for d in data]
    starts = [d[start_col] for d in data]
    ends = [d[end_col] for d in data]

    if orientation == "horizontal":
        p = figure(
            y_range=categories,
            width=width,
            height=height,
            title=title,
            toolbar_location="above",
        )

        # Draw lines
        for cat, start, end in zip(categories, starts, ends):
            p.line(
                [start, end],
                [cat, cat],
                line_width=line_width,
                color=line_color,
                alpha=0.6,
            )

        # Add glow effect if enabled
        if glow:
            # Outer glow layers for start points
            p.circle(
                starts, categories, size=point_size * 2, color=start_color, alpha=0.1
            )
            p.circle(
                starts, categories, size=point_size * 1.5, color=start_color, alpha=0.2
            )
            p.circle(
                starts, categories, size=point_size * 1.17, color=start_color, alpha=0.3
            )

            # Outer glow layers for end points
            p.circle(ends, categories, size=point_size * 2, color=end_color, alpha=0.1)
            p.circle(
                ends, categories, size=point_size * 1.5, color=end_color, alpha=0.2
            )
            p.circle(
                ends, categories, size=point_size * 1.17, color=end_color, alpha=0.3
            )

        # Draw main circles on top
        p.circle(
            starts,
            categories,
            size=point_size,
            color=start_color,
            legend_label=start_label,
            alpha=0.9,
        )

        p.circle(
            ends,
            categories,
            size=point_size,
            color=end_color,
            legend_label=end_label,
            alpha=0.9,
        )

        p.xaxis.axis_label = "Value"
        p.yaxis.axis_label = "Category"

    else:  # vertical
        p = figure(
            x_range=categories,
            width=width,
            height=height,
            title=title,
            toolbar_location="above",
        )

        # Draw lines
        for cat, start, end in zip(categories, starts, ends):
            p.line(
                [cat, cat],
                [start, end],
                line_width=line_width,
                color=line_color,
                alpha=0.6,
            )

        # Add glow effect if enabled
        if glow:
            # Outer glow layers for start points
            p.circle(
                categories, starts, size=point_size * 2, color=start_color, alpha=0.1
            )
            p.circle(
                categories, starts, size=point_size * 1.5, color=start_color, alpha=0.2
            )
            p.circle(
                categories, starts, size=point_size * 1.17, color=start_color, alpha=0.3
            )

            # Outer glow layers for end points
            p.circle(categories, ends, size=point_size * 2, color=end_color, alpha=0.1)
            p.circle(
                categories, ends, size=point_size * 1.5, color=end_color, alpha=0.2
            )
            p.circle(
                categories, ends, size=point_size * 1.17, color=end_color, alpha=0.3
            )

        # Draw main circles on top
        p.circle(
            categories,
            starts,
            size=point_size,
            color=start_color,
            legend_label=start_label,
            alpha=0.9,
        )

        p.circle(
            categories,
            ends,
            size=point_size,
            color=end_color,
            legend_label=end_label,
            alpha=0.9,
        )

        p.xaxis.axis_label = "Category"
        p.yaxis.axis_label = "Value"
        p.xaxis.major_label_orientation = 0.8

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ("Category", "@y" if orientation == "horizontal" else "@x"),
            ("Value", "@x{0.0}" if orientation == "horizontal" else "@y{0.0}"),
        ]
    )
    p.add_tools(hover)

    p.legend.location = "center_right"
    p.legend.click_policy = "hide"
    p.add_layout(p.legend[0], "right")

    return p


from cartopy import crs as ccrs
from bokeh.plotting import figure, curdoc, show


def contourf_map(
    da,
    title=None,
    levels=10,
    palette="Viridis256",
    vmin=None,
    vmax=None,
    width=1500,
    height=780,
    show_coastlines=True,
    coastline_color="black",
    coastline_width=1.5,
    projection=None,
    cbar_title=None,
    sh=0,
    theme="dark",
):
    """
    Plot XArray DataArray with filled contours using Bokeh's native contour method.

    Supports various cartopy projections (Mollweide, Robinson, EqualEarth, EckertIV, Orthographic, Sinusoidal, Miller, AlbersEqualArea, PlateCarree) with proper handling of coordinate transformations,
    longitude wrapping for Orthographic projections, and coastline rendering without artifacts.

    Parameters
    ----------
    da : xarray.DataArray
        2D DataArray with latitude/longitude dimensions. Dimension names should contain
        'lat' and 'lon' (case-insensitive).
    title : str, optional
        Plot title. Default is None.
    levels : int or array-like, default=10
        Number of contour levels (if int) or explicit level values (if array-like).
    palette : str or list, default="Viridis256"
        Bokeh color palette name ("Viridis256", "Turbo256", "Plasma256", "Inferno256",
        "Magma256") or list of color hex codes.
    vmin, vmax : float, optional
        Min/max values for color mapping. If None, uses data min/max.
    width, height : int, default=(1500, 780)
        Figure dimensions in pixels.
    show_coastlines : bool, default=True
        Whether to overlay coastlines from Natural Earth data.
    coastline_color : str, default='black'
        Color of coastline borders.
    coastline_width : float, default=1.5
        Width of coastline borders in pixels.
    projection : cartopy.crs projection, optional
        Cartopy projection (e.g., ccrs.Orthographic(), ccrs.Robinson()).
        If None, uses PlateCarree (equirectangular).
    cbar_title : str, optional
        Title for the colorbar. Default is None.
    sh : int, default=1
        Show (sh=0) or not.
    """
    from shapely.geometry import LineString, MultiLineString
    import cartopy.feature as cfeature

    from bokeh.models import GlobalInlineStyleSheet

    gstyle = GlobalInlineStyleSheet(
        css=""" html, body, .bk, .bk-root {background-color: #343838; margin: 0; padding: 0; height: 100%; color: white; font-family: 'Consolas', 'Helvetica', monospace; } .bk { color: white; } .bk-input, .bk-btn, .bk-select, .bk-slider-title, .bk-headers, .bk-label, .bk-title, .bk-legend, .bk-axis-label { color: white !important; } .bk-input::placeholder { color: #aaaaaa !important; } """
    )

    # Get data
    if da.ndim != 2:
        raise ValueError(f"DataArray must be 2D, got {da.ndim}D")

    arr = da.values.copy()
    lat_name = [dim for dim in da.dims if "lat" in dim.lower()][0]
    lon_name = [dim for dim in da.dims if "lon" in dim.lower()][0]
    lats = da[lat_name].values
    lons = da[lon_name].values

    # Set up projection
    if projection is None:
        projection = ccrs.PlateCarree()
        use_projection = False
    else:
        use_projection = True

    # Create meshgrid for contour
    lon_grid, lat_grid = np.meshgrid(lons, lats)

    # CRITICAL FIX: Handle longitude wrapping ONLY for Orthographic projection
    # Orthographic needs this to avoid seam artifacts at ±180°
    if use_projection and isinstance(projection, ccrs.Orthographic):
        if not np.isclose(lon_grid[0, 0], lon_grid[0, -1], atol=1.0):
            # Check if this looks like global data (spans most of globe)
            lon_span = np.max(lons) - np.min(lons)
            if lon_span > 300:  # Likely global data
                # Add wrapped column at the end
                lon_grid = np.hstack([lon_grid, lon_grid[:, 0:1]])
                lat_grid = np.hstack([lat_grid, lat_grid[:, 0:1]])
                arr = np.hstack([arr, arr[:, 0:1]])

    # Transform coordinates if using projection
    if use_projection:
        transformed_points = projection.transform_points(
            ccrs.PlateCarree(), lon_grid, lat_grid
        )
        x_grid = transformed_points[:, :, 0]
        y_grid = transformed_points[:, :, 1]

        # CRITICAL FIX: Mask invalid transformed points
        # Points that are NaN, infinite, or have very large values are not visible
        invalid_mask = (
            np.isnan(x_grid)
            | np.isnan(y_grid)
            | np.isinf(x_grid)
            | np.isinf(y_grid)
            | (np.abs(x_grid) > 1e10)
            | (np.abs(y_grid) > 1e10)
        )

        # Set invalid points to NaN in both coordinates AND data
        x_grid[invalid_mask] = np.nan
        y_grid[invalid_mask] = np.nan
        arr[invalid_mask] = np.nan

        # Additional check: for orthographic projections, filter points too far from center
        # This helps with edge artifacts
        if isinstance(projection, ccrs.Orthographic):
            center_lon = projection.proj4_params.get("lon_0", 0)
            center_lat = projection.proj4_params.get("lat_0", 0)

            # Calculate angular distance from center
            from numpy import sin, cos, arccos, deg2rad

            lat_rad = deg2rad(lat_grid)
            lon_rad = deg2rad(lon_grid)
            center_lat_rad = deg2rad(center_lat)
            center_lon_rad = deg2rad(center_lon)

            # Great circle distance
            angular_dist = arccos(
                np.clip(
                    sin(center_lat_rad) * sin(lat_rad)
                    + cos(center_lat_rad)
                    * cos(lat_rad)
                    * cos(lon_rad - center_lon_rad),
                    -1,
                    1,
                )
            )

            # Mask points beyond 90 degrees (not visible on hemisphere)
            beyond_horizon = angular_dist > np.pi / 2
            x_grid[beyond_horizon] = np.nan
            y_grid[beyond_horizon] = np.nan
            arr[beyond_horizon] = np.nan
    else:
        x_grid = lon_grid
        y_grid = lat_grid

    # Set up contour levels
    if vmin is None:
        vmin = np.nanmin(arr)
    if vmax is None:
        vmax = np.nanmax(arr)

    if isinstance(levels, int):
        level_values = np.linspace(vmin, vmax, levels)
    else:
        level_values = np.array(levels)

    # Get color palette
    if isinstance(palette, str):
        from bokeh.palettes import Viridis256, Turbo256, Plasma256, Inferno256, Magma256

        palette_map = {
            "Viridis256": Viridis256,
            "Turbo256": Turbo256,
            "Plasma256": Plasma256,
            "Inferno256": Inferno256,
            "Magma256": Magma256,
        }
        palette_obj = palette_map.get(palette, Viridis256)
    else:
        palette_obj = palette

    # Sample colors from palette to match number of levels
    n_colors = len(level_values) - 1
    if len(palette_obj) > n_colors:
        indices = np.linspace(0, len(palette_obj) - 1, n_colors).astype(int)
        fill_palette = [palette_obj[i] for i in indices]
    else:
        fill_palette = palette_obj

    # Create figure with proper ranges (excluding NaN values)
    valid_x = x_grid[~np.isnan(x_grid)]
    valid_y = y_grid[~np.isnan(y_grid)]

    if len(valid_x) == 0 or len(valid_y) == 0:
        raise ValueError("No valid points after projection transformation")

    # Add small padding to ranges
    x_range_pad = (valid_x.max() - valid_x.min()) * 0.02
    y_range_pad = (valid_y.max() - valid_y.min()) * 0.02

    p = figure(
        x_range=(valid_x.min() - x_range_pad, valid_x.max() + x_range_pad),
        y_range=(valid_y.min() - y_range_pad, valid_y.max() + y_range_pad),
        width=width,
        height=height,
        title=title,
        outline_line_color=None,
        active_scroll="wheel_zoom",
        tools="pan,wheel_zoom,reset,save",  # Explicitly set tools, no default hover
    )

    # Add filled contours
    contour_renderer = p.contour(
        x_grid,
        y_grid,
        arr,
        levels=level_values,
        fill_color=fill_palette, line_color=None
    )

    # Add coastlines using cartopy
    if show_coastlines:
        try:
            coastlines = cfeature.NaturalEarthFeature("physical", "coastline", "110m")

            # Different handling for PlateCarree vs other projections
            if not use_projection or isinstance(projection, ccrs.PlateCarree):
                # For PlateCarree: Simple approach with NaN separation
                x_coords = []
                y_coords = []
                for geom in coastlines.geometries():
                    if isinstance(geom, LineString):
                        coords = np.array(geom.coords)
                        x_coords.extend(coords[:, 0].tolist() + [np.nan])
                        y_coords.extend(coords[:, 1].tolist() + [np.nan])
                    elif isinstance(geom, MultiLineString):
                        for line in geom.geoms:
                            coords = np.array(line.coords)
                            x_coords.extend(coords[:, 0].tolist() + [np.nan])
                            y_coords.extend(coords[:, 1].tolist() + [np.nan])

                p.line(
                    x_coords,
                    y_coords,
                    line_color=coastline_color,
                    line_width=coastline_width,
                )
            else:
                # For other projections: Transform and handle carefully
                def process_line_string(line_string):
                    if isinstance(line_string, (LineString, MultiLineString)):
                        if isinstance(line_string, LineString):
                            lines = [line_string]
                        else:
                            lines = list(line_string.geoms)

                        for line in lines:
                            coords = np.array(line.coords)
                            if len(coords) > 1:
                                # Transform coastline coordinates
                                tt = projection.transform_points(
                                    ccrs.PlateCarree(), coords[:, 0], coords[:, 1]
                                )
                                x = tt[:, 0]
                                y = tt[:, 1]

                                # Filter invalid points and large jumps
                                valid = ~(
                                    np.isnan(x)
                                    | np.isnan(y)
                                    | np.isinf(x)
                                    | np.isinf(y)
                                )
                                if np.sum(valid) > 1:
                                    x_valid = x[valid]
                                    y_valid = y[valid]

                                    # Split on large jumps (discontinuities)
                                    dx = np.diff(x_valid)
                                    dy = np.diff(y_valid)
                                    dist = np.sqrt(dx**2 + dy**2)
                                    threshold = (
                                        np.nanpercentile(dist, 95) * 3
                                    )  # Adaptive threshold

                                    splits = np.where(dist > threshold)[0] + 1
                                    segments = np.split(range(len(x_valid)), splits)

                                    for seg in segments:
                                        if len(seg) > 1:
                                            p.line(
                                                x_valid[seg],
                                                y_valid[seg],
                                                line_color=coastline_color,
                                                line_width=coastline_width,
                                            )

                for geom in coastlines.geometries():
                    process_line_string(geom)

        except Exception as e:
            print(f"Warning: Could not load coastlines: {e}")

    # Add color bar
    colorbar = contour_renderer.construct_color_bar( 
        title=cbar_title, background_fill_alpha=0, 
    )
    colorbar.major_label_text_font_size = "14pt"
    colorbar.title_text_font_size = "14pt"
    p.add_layout(colorbar, "right")
    p.min_border_right = 165
    p.styles = {
        "margin-top": "0px",
        "margin-left": "0px",
        "border-radius": "10px",
        "box-shadow": "0 18px 20px rgba(243, 192, 97, 0.2)",
        "padding": "5px",
        "background-color": "#343838",
        "border": "1.5px solid orange",
    }
    p.min_border_bottom = 20
    p.background_fill_color = "#1f1f1f"
    p.border_fill_color = "#343838"
    p.background_fill_alpha = 0
    p.toolbar.autohide = True
    p.toolbar_location = "left"
    p.title.text_font_size = "18pt"
    p.title.text_font = "Helvetica"
    p.title.align = "center"

    apply_theme(p, theme=theme)
    if theme == "dark":
        colorbar.major_label_text_color = "white"   # tick labels
        colorbar.title_text_color = "white"         # title (optional)
    else:
        colorbar.major_label_text_color = "black"   # tick labels
        colorbar.title_text_color = "black"         # title (optional)
    # Style
    if use_projection:
        p.xaxis.visible = False
        p.yaxis.visible = False
        p.grid.visible = False
    else:
        p.xaxis.axis_label = "Longitude"
        p.yaxis.axis_label = "Latitude"
        p.grid.grid_line_alpha = 0.3

    if sh == 1:
        show(p)

    return p


def plot_3d_bars(
    categories,
    values,
    colors,
    labels=None,
    title="3D Bar Chart",
    xlabel="",
    ylabel="",
    width=800,
    height=600,
    bar_width=0.45,
    dx=0.35,
    dy=80,
    dark_bg=True,
):
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
    bg_color = "#343838" if dark_bg else "#FDFBD4"
    text_color = "white" if dark_bg else "black"
    grid_color = "#404040" if dark_bg else "#e0e0e0"

    # Calculate y-range with padding
    max_val = max(values) * 1.5

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, len(categories)),
        y_range=(-10, max_val),
        toolbar_location="right",
        tools="pan,wheel_zoom,reset,save",
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )

    # Apply styling
    p.title.text_color = text_color
    p.title.text_font_size = "18pt"
    p.title.text_font_style = "bold"
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
    p.xaxis.major_label_text_font_size = "11pt"
    p.yaxis.major_label_text_font_size = "11pt"
    p.outline_line_color = None
    p.xaxis.ticker = list(range(len(categories)))
    p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}

    if ylabel:
        p.yaxis.axis_label = ylabel
        p.yaxis.axis_label_text_color = text_color
        p.yaxis.axis_label_text_font_size = "12pt"

    # Draw 3D bars
    for i, (value, color) in enumerate(zip(values, colors)):
        x_left = i - bar_width / 2
        x_right = i + bar_width / 2

        # Right side face (darker)
        right_x = [x_right, x_right + dx, x_right + dx, x_right, x_right]
        right_y = [0, dy, value + dy, value, 0]
        p.patch(
            right_x,
            right_y,
            color=darken_color(color, 0.6),
            alpha=1.0,
            line_color="#000000",
            line_width=1,
        )

        # Top face (medium shade)
        top_x = [x_left, x_right, x_right + dx, x_left + dx, x_left]
        top_y = [value, value, value + dy, value + dy, value]
        p.patch(
            top_x,
            top_y,
            color=darken_color(color, 0.8),
            alpha=1.0,
            line_color="#000000",
            line_width=1,
        )

        # Front face (brightest)
        p.quad(
            left=[x_left],
            right=[x_right],
            bottom=[0],
            top=[value],
            color=color,
            alpha=1.0,
            line_color="#000000",
            line_width=1.5,
        )

    return p


def plot_3d_stacked_bars(
    categories,
    data_dict,
    colors,
    labels,
    title="3D Stacked Bar Chart",
    xlabel="",
    ylabel="",
    width=800,
    height=600,
    bar_width=0.45,
    dx=0.35,
    dy=80,
    dark_bg=True,
):
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
    bg_color = "#343838" if dark_bg else "#FDFBD4"
    text_color = "white" if dark_bg else "black"
    grid_color = "#404040" if dark_bg else "#e0e0e0"

    # Calculate y-range
    max_val = max(sum(data_dict[cat]) for cat in categories) * 1.4

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-0.5, len(categories)),
        y_range=(-50, max_val),
        toolbar_location="right",
        tools="pan,wheel_zoom,reset,save",
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )

    # Apply styling
    p.title.text_color = text_color
    p.title.text_font_size = "18pt"
    p.title.text_font_style = "bold"
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
    p.xaxis.major_label_text_font_size = "11pt"
    p.yaxis.major_label_text_font_size = "11pt"
    p.outline_line_color = None
    p.xaxis.ticker = list(range(len(categories)))
    p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}

    if ylabel:
        p.yaxis.axis_label = ylabel
        p.yaxis.axis_label_text_color = text_color
        p.yaxis.axis_label_text_font_size = "12pt"

    # Draw 3D stacked bars
    for i, category in enumerate(categories):
        cumulative = 0
        category_data = data_dict[category]

        for j, (value, color) in enumerate(zip(category_data, colors)):
            bottom = cumulative
            top = cumulative + value

            x_left = i - bar_width / 2
            x_right = i + bar_width / 2

            # Right side face (darker)
            right_x = [x_right, x_right + dx, x_right + dx, x_right, x_right]
            right_y = [bottom, bottom + dy, top + dy, top, bottom]
            p.patch(
                right_x,
                right_y,
                color=darken_color(color, 0.6),
                alpha=1.0,
                line_color="#000000",
                line_width=1,
            )

            # Top face (only for top segment)
            if j == len(category_data) - 1:
                top_x = [x_left, x_right, x_right + dx, x_left + dx, x_left]
                top_y = [top, top, top + dy, top + dy, top]
                p.patch(
                    top_x,
                    top_y,
                    color=darken_color(color, 0.8),
                    alpha=1.0,
                    line_color="#000000",
                    line_width=1,
                )

            # Front face (brightest)
            p.quad(
                left=[x_left],
                right=[x_right],
                bottom=[bottom],
                top=[top],
                color=color,
                alpha=1.0,
                line_color="#000000",
                line_width=1.5,
            )

            cumulative = top

    return p


from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CustomJS, TextInput
from bokeh.layouts import column, row
from bokeh.io import curdoc
import numpy as np


class Gauge:
    """A beautiful, animated gauge component for Bokeh."""

    def __init__(
        self,
        width=500,
        height=500,
        title="",
        unit="%",
        zones=None,
        initial_value=0,
        range_min=0,
        range_max=100,
        easing=False,
        theme="dark",
        bg_color=None,
        gauge_bg_color=None,
    ):
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
            {"range": (66.66, 100), "color": "#FF3366", "label": "HIGH"},
        ]

        # Gauge geometry
        self.outer_radius = 1.0
        self.inner_radius = 0.78
        self.start_angle = np.pi + np.pi / 6  # 210 degrees
        self.end_angle = -np.pi / 6  # -30 degrees
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
            border_fill_color=self.bg_color,
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

        return ColumnDataSource(
            {
                "x": [0],
                "y": [0],
                "angle": [initial_angle],
                "value_text": [str(int(self.initial_value))],
                "pointer_color": [initial_color],
            }
        )

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
                x=[0],
                y=[-1.45],
                text=[self.title],
                text_align="center",
                text_baseline="middle",
                text_color=self.text_color,
                text_font_size="22pt",
                text_font_style="bold",
                text_alpha=0.95,
            )

        # Draw zone wedges
        for zone in self.zones:
            # Normalize zone ranges to 0-1
            zone_start_normalized = (
                zone["range"][0] - self.range_min
            ) / self.value_range
            zone_end_normalized = (zone["range"][1] - self.range_min) / self.value_range

            zone_start = (
                self.start_angle - zone_start_normalized * self.total_angle_range
            )
            zone_end = self.start_angle - zone_end_normalized * self.total_angle_range

            # Main zone rings - COMPLETELY FILL between inner and outer radius
            num_rings = 30
            radii = np.linspace(self.inner_radius, self.outer_radius, num_rings)
            for r in radii:
                self.figure.wedge(
                    x=0,
                    y=0,
                    radius=r,
                    start_angle=zone_end,
                    end_angle=zone_start,
                    color=zone["color"],
                    line_color=zone["color"],
                    line_width=3,
                    alpha=0.98,
                )

            num_glow_rings = 8
            glow_radii = np.linspace(
                self.outer_radius + 0.01, self.outer_radius + 0.08, num_glow_rings
            )
            for i, r in enumerate(glow_radii):
                alpha = 0.4 * (1 - i / num_glow_rings)
                self.figure.wedge(
                    x=0,
                    y=0,
                    radius=r,
                    start_angle=zone_end,
                    end_angle=zone_start,
                    color=zone["color"],
                    line_color=zone["color"],
                    line_width=1,
                    alpha=alpha,
                )

            # Zone label
            angle = (zone_start + zone_end) / 2
            label_radius = self.outer_radius + 0.5
            x_label = label_radius * np.cos(angle)
            y_label = label_radius * np.sin(angle)
            self.figure.text(
                x=[x_label],
                y=[y_label],
                text=[zone["label"]],
                text_align="center",
                text_baseline="middle",
                text_color=zone["color"],
                text_font_size="14pt",
                text_font_style="bold",
            )

        # Inner dark circle
        self.figure.wedge(
            x=0,
            y=0,
            radius=self.inner_radius,
            start_angle=0,
            end_angle=2 * np.pi,
            color=self.gauge_bg_color,
            line_color=self.gauge_bg_color,
        )

        # Decorative rings
        self.figure.circle(
            x=0,
            y=0,
            radius=self.outer_radius + 0.02,
            line_color=self.ring_color,
            line_width=2,
            fill_color=None,
            alpha=0.25,
        )
        self.figure.circle(
            x=0,
            y=0,
            radius=self.inner_radius - 0.02,
            line_color=self.ring_color,
            line_width=2,
            fill_color=None,
            alpha=0.3,
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

        angles_major = [
            self.start_angle - norm * self.total_angle_range
            for norm in major_normalized
        ]
        angles_minor = [
            self.start_angle - norm * self.total_angle_range
            for norm in minor_normalized
        ]

        # Minor ticks
        for angle in angles_minor:
            x0 = (self.inner_radius - 0.03) * np.cos(angle)
            y0 = (self.inner_radius - 0.03) * np.sin(angle)
            x1 = (self.inner_radius + 0.03) * np.cos(angle)
            y1 = (self.inner_radius + 0.03) * np.sin(angle)
            self.figure.line(
                [x0, x1],
                [y0, y1],
                line_color=self.tick_color,
                line_width=1.5,
                alpha=0.3,
            )

        # Major ticks and labels
        for angle, tick in zip(angles_major, major_ticks):
            x0 = (self.inner_radius - 0.05) * np.cos(angle)
            y0 = (self.inner_radius - 0.05) * np.sin(angle)
            x1 = (self.outer_radius + 0.05) * np.cos(angle)
            y1 = (self.outer_radius + 0.05) * np.sin(angle)

            self.figure.line(
                [x0, x1], [y0, y1], line_color=self.tick_color, line_width=2, alpha=0.5
            )
            self.figure.line(
                [x0, x1], [y0, y1], line_color=self.tick_color, line_width=4, alpha=0.15
            )

            # Tick label
            label_radius = self.outer_radius + 0.25
            x_label = label_radius * np.cos(angle)
            y_label = label_radius * np.sin(angle)
            self.figure.text(
                x=[x_label],
                y=[y_label],
                text=[str(int(tick))],
                text_align="center",
                text_baseline="middle",
                text_color=self.tick_color,
                text_font_size="13pt",
                text_font_style="normal",
                text_alpha=0.65,
            )

    def _draw_pointer(self):
        """Draw the animated pointer."""
        pointer_length = 0.68

        self.figure.wedge(
            x="x",
            y="y",
            radius=pointer_length,
            start_angle="angle",
            end_angle="angle",
            color="pointer_color",
            alpha=1.0,
            direction="clock",
            line_color="pointer_color",
            line_width=4,
            source=self.source,
        )

        self.figure.wedge(
            x="x",
            y="y",
            radius=pointer_length,
            start_angle="angle",
            end_angle="angle",
            color="pointer_color",
            alpha=0.4,
            direction="clock",
            line_color="pointer_color",
            line_width=12,
            source=self.source,
        )

        # Center hub
        self.figure.circle(
            x=0,
            y=0,
            radius=0.14,
            fill_color="pointer_color",
            line_color="pointer_color",
            line_width=0,
            source=self.source,
            alpha=1.0,
        )
        self.figure.circle(
            x=0,
            y=0,
            radius=0.09,
            fill_color=self.bg_color,
            line_color="pointer_color",
            line_width=3,
            source=self.source,
            alpha=1.0,
        )
        self.figure.circle(
            x=0,
            y=0,
            radius=0.05,
            fill_color="pointer_color",
            source=self.source,
            alpha=1.0,
        )

    def _draw_value_display(self):
        """Draw the value display."""
        # Main value - smaller font, moved up
        self.figure.text(
            x=0,
            y=-0.4,
            text="value_text",
            source=self.source,
            text_align="center",
            text_baseline="middle",
            text_color="pointer_color",
            text_font_size="40pt",
            text_font_style="bold",
        )
        # Glow effect
        self.figure.text(
            x=0,
            y=-0.4,
            text="value_text",
            source=self.source,
            text_align="center",
            text_baseline="middle",
            text_color="pointer_color",
            text_font_size="40pt",
            text_font_style="bold",
            text_alpha=0.3,
        )
        # Unit label - smaller, moved up
        self.figure.text(
            x=0,
            y=-0.65,
            text=[self.unit],
            text_align="center",
            text_baseline="middle",
            text_color=self.text_color,
            text_font_size="13pt",
            text_font_style="bold",
            text_alpha=0.7,
        )

    def get_animation_js(self, target_value, delay=500):
        """Generate JavaScript animation code."""
        easing_flag = 1 if self.easing else 0

        color_conditions = []
        for i, zone in enumerate(self.zones):
            if i == len(self.zones) - 1:
                color_conditions.append(f'return "{zone["color"]}";')
            else:
                color_conditions.append(
                    f'if (v <= {zone["range"][1]}) return "{zone["color"]}";'
                )
        color_func = "\n            ".join(color_conditions)

        return f"""
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
"""


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
    interactive=True,
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
    default_source_palette = [
        "#306998",
        "#FFD43B",
        "#9B59B6",
        "#3498DB",
        "#E67E22",
        "#2ECC71",
        "#E74C3C",
        "#95A5A6",
        "#F39C12",
        "#1ABC9C",
    ]
    default_target_palette = [
        "#2C3E50",
        "#16A085",
        "#C0392B",
        "#8E44AD",
        "#D35400",
        "#27AE60",
        "#2980B9",
        "#7F8C8D",
        "#F1C40F",
        "#34495E",
    ]

    if source_colors is None:
        source_colors = {
            s: default_source_palette[i % len(default_source_palette)]
            for i, s in enumerate(sources)
        }
    if target_colors is None:
        target_colors = {
            t: default_target_palette[i % len(default_target_palette)]
            for i, t in enumerate(targets)
        }

    # Calculate totals
    source_totals = {
        s: sum(f["value"] for f in flows if f["source"] == s) for s in sources
    }
    target_totals = {
        t: sum(f["value"] for f in flows if f["target"] == t) for t in targets
    }

    # Layout parameters
    left_x, right_x = 0, 100
    node_width, node_gap = 8, 3
    total_height, padding_y = 100, 5

    # Position source nodes
    source_height_total = sum(source_totals.values())
    scale = (
        total_height - 2 * padding_y - (len(sources) - 1) * node_gap
    ) / source_height_total

    source_nodes = {}
    current_y = padding_y
    for s in sources:
        h = source_totals[s] * scale
        source_nodes[s] = {
            "x": left_x,
            "y": current_y,
            "height": h,
            "value": source_totals[s],
        }
        current_y += h + node_gap

    # Position target nodes
    target_height_total = sum(target_totals.values())
    scale_t = (
        total_height - 2 * padding_y - (len(targets) - 1) * node_gap
    ) / target_height_total

    target_nodes = {}
    current_y = padding_y
    for t in targets:
        h = target_totals[t] * scale_t
        target_nodes[t] = {
            "x": right_x - node_width,
            "y": current_y,
            "height": h,
            "value": target_totals[t],
        }
        current_y += h + node_gap

    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_range=(-30, 130),
        y_range=(-5, 105),
        tools="",
        toolbar_location=None,
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
        x_path = (
            (1 - t) ** 3 * x0
            + 3 * (1 - t) ** 2 * t * cx0
            + 3 * (1 - t) * t**2 * cx1
            + t**3 * x1
        )

        # Cubic bezier for y (creates smooth S-curve)
        y_bottom = (
            (1 - t) ** 3 * y0_bottom
            + 3 * (1 - t) ** 2 * t * y0_bottom
            + 3 * (1 - t) * t**2 * y1_bottom
            + t**3 * y1_bottom
        )
        y_top = (
            (1 - t) ** 3 * y0_top
            + 3 * (1 - t) ** 2 * t * y0_top
            + 3 * (1 - t) * t**2 * y1_top
            + t**3 * y1_top
        )

        xs = list(x_path) + list(x_path[::-1])
        ys = list(y_top) + list(y_bottom[::-1])

        # Create ColumnDataSource for interactivity
        source_data = ColumnDataSource(
            data={
                "x": [xs],
                "y": [ys],
                "source": [src],
                "target": [tgt],
                "value": [value],
                "alpha": [flow_alpha],
            }
        )

        ribbon = p.patches(
            "x",
            "y",
            source=source_data,
            fill_color=source_colors[src],
            fill_alpha="alpha",
            line_color=source_colors[src],
            line_alpha="alpha",
            line_width=0.5,
        )

        ribbon_renderers.append(ribbon)
        ribbon_sources.append(source_data)

    # Draw source nodes
    source_node_renderers = []
    source_node_sources = []

    for s in sources:
        node = source_nodes[s]
        node_source = ColumnDataSource(
            data={
                "left": [node["x"]],
                "right": [node["x"] + node_width],
                "bottom": [node["y"]],
                "top": [node["y"] + node["height"]],
                "name": [s],
                "value": [node["value"]],
                "type": ["source"],
            }
        )

        renderer = p.quad(
            left="left",
            right="right",
            bottom="bottom",
            top="top",
            source=node_source,
            fill_color=source_colors[s],
            fill_alpha=node_alpha,
            line_color="white",
            line_width=2,
            hover_fill_alpha=1.0,
        )

        source_node_renderers.append(renderer)
        source_node_sources.append(node_source)

        # Add label
        label = Label(
            x=node["x"] - 1,
            y=node["y"] + node["height"] / 2,
            text=f"{s} ({node['value']})",
            text_font_size="22pt",
            text_align="right",
            text_baseline="middle",
            text_color="#333",
        )
        p.add_layout(label)

    # Draw target nodes
    target_node_renderers = []
    target_node_sources = []

    for t in targets:
        node = target_nodes[t]
        node_source = ColumnDataSource(
            data={
                "left": [node["x"]],
                "right": [node["x"] + node_width],
                "bottom": [node["y"]],
                "top": [node["y"] + node["height"]],
                "name": [t],
                "value": [node["value"]],
                "type": ["target"],
            }
        )

        renderer = p.quad(
            left="left",
            right="right",
            bottom="bottom",
            top="top",
            source=node_source,
            fill_color=target_colors[t],
            fill_alpha=node_alpha,
            line_color="white",
            line_width=2,
            hover_fill_alpha=1.0,
        )

        target_node_renderers.append(renderer)
        target_node_sources.append(node_source)

        # Add label
        label = Label(
            x=node["x"] + node_width + 1,
            y=node["y"] + node["height"] / 2,
            text=f"{t} ({node['value']})",
            text_font_size="22pt",
            text_align="left",
            text_baseline="middle",
            text_color="#333",
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
        width=300,
        margin=(10, 10, 10, 10),
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
            """,
        ),
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
            """,
        ),
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
            """,
        ),
    )
    p.add_tools(target_hover)

    # Reset on mouse leave
    p.js_on_event(
        "mouseleave",
        CustomJS(
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
        """,
        ),
    )

    return column(p, info_div)


### CONTINUE : MULTI LEVEL SANKEY
import numpy as np
from bokeh.io import show
from bokeh.models import (
    Label,
    HoverTool,
    ColumnDataSource,
    CustomJS,
    Div,
    Legend,
    LegendItem,
)
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
    interactive=True,
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
        default_palette = [
            "#306998",
            "#D62728",
            "#FFD43B",
            "#7F7F7F",
            "#2ECC71",
            "#3498DB",
            "#E67E22",
            "#9B59B6",
            "#1ABC9C",
            "#F39C12",
        ]
        colors = {
            cat: default_palette[i % len(default_palette)]
            for i, cat in enumerate(categories)
        }

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
                "value": height_flow,  # Store original value
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
        source_cursors = {
            cat: node_positions[t_idx][cat]["y_start"] for cat in categories
        }
        target_cursors = {
            cat: node_positions[t_idx + 1][cat]["y_start"] for cat in categories
        }

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
            x_top = (
                (1 - t_param) ** 3 * x_start
                + 3 * (1 - t_param) ** 2 * t_param * cx0
                + 3 * (1 - t_param) * t_param**2 * cx1
                + t_param**3 * x_end
            )
            y_top = (
                (1 - t_param) ** 3 * y_src_top
                + 3 * (1 - t_param) ** 2 * t_param * y_src_top
                + 3 * (1 - t_param) * t_param**2 * y_tgt_top
                + t_param**3 * y_tgt_top
            )

            # Bottom edge bezier
            x_bottom = (
                (1 - t_param) ** 3 * x_start
                + 3 * (1 - t_param) ** 2 * t_param * cx0
                + 3 * (1 - t_param) * t_param**2 * cx1
                + t_param**3 * x_end
            )
            y_bottom = (
                (1 - t_param) ** 3 * y_src_bottom
                + 3 * (1 - t_param) ** 2 * t_param * y_src_bottom
                + 3 * (1 - t_param) * t_param**2 * y_tgt_bottom
                + t_param**3 * y_tgt_bottom
            )

            # Create closed polygon
            xs = list(x_top) + list(x_bottom[::-1])
            ys = list(y_top) + list(y_bottom[::-1])

            # Create data source (store ORIGINAL value for display)
            source_data = ColumnDataSource(
                data={
                    "x": [xs],
                    "y": [ys],
                    "from": [from_cat],
                    "to": [to_cat],
                    "value": [value],  # Original unscaled value
                    "time_from": [time_points[t_idx]],
                    "time_to": [time_points[t_idx + 1]],
                    "alpha": [flow_alpha],
                }
            )

            ribbon = p.patches(
                "x",
                "y",
                source=source_data,
                fill_color=colors[from_cat],
                fill_alpha="alpha",
                line_color=colors[from_cat],
                line_alpha="alpha",
                line_width=0.5,
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
                node_source = ColumnDataSource(
                    data={
                        "left": [x - node_width / 2],
                        "right": [x + node_width / 2],
                        "bottom": [y_start],
                        "top": [y_end],
                        "category": [cat],
                        "time_idx": [t_idx],
                        "value": [value_original],  # Store original value
                    }
                )

                renderer = p.quad(
                    left="left",
                    right="right",
                    bottom="bottom",
                    top="top",
                    source=node_source,
                    fill_color=colors[cat],
                    fill_alpha=0.9,
                    line_color="white",
                    line_width=2,
                    hover_fill_alpha=1.0,
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
    legend_items = [
        LegendItem(label=cat, renderers=[legend_renderers[cat]])
        for cat in categories
        if cat in legend_renderers
    ]
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
        width=280,
        margin=(10, 10, 10, 10),
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
            """,
        ),
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
            """,
        ),
    )
    p.add_tools(node_hover)

    # Reset on mouse leave
    p.js_on_event(
        "mouseleave",
        CustomJS(
            args=dict(ribbons=ribbon_sources, div=info_div, base_alpha=flow_alpha),
            code="""
        for (let k = 0; k < ribbons.length; k++) {
            ribbons[k].data.alpha = [base_alpha];
            ribbons[k].change.emit();
        }
        div.text = `<div style="padding:12px;border:2px solid #333;border-radius:6px;
                     background:#FFF8DC;color:#333;"><b>Hover over flows or nodes</b></div>`;
        """,
        ),
    )

    return column(p, info_div)


from math import pi
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from bokeh.palettes import Category10, Category20, Turbo256


def fpie_basic(
    df,
    title="Pie Chart",
    colors=palette,
    bgc=None,
    offset=(0, 1),
    radius=0.8,
theme='light',    sh=0,
    height=650,
    width=800,
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
        raise ValueError(
            "DataFrame must have at least two columns: category and value."
        )

    df = df.copy()
    cat_col, val_col = df.columns[:2]
    df.columns = ["category", "value"]

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
    df["angle"] = df["value"] / df["value"].sum() * 2 * pi
    df["color"] = colors

    # --- Create figure ---
    p = figure(
        height=height,
        width=width,
        title=title,
        x_range=(-1, 1),
        y_range=(-0.5, 2.5),
        background_fill_color=bgc,
    )

    # --- Draw wedges ---
    p.wedge(
        x=offset[0],
        y=offset[1],
        radius=radius,
        start_angle=cumsum("angle", include_zero=True),
        end_angle=cumsum("angle"),
        line_color="white",
        fill_color="color",
        legend_field="category",
        source=df,
        hover_line_color="black",
        hover_line_width=5,
    )
    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.legend.location = "center_right"
    p.legend.click_policy = "none"
    p.legend.background_fill_alpha = 0.0
    p.legend.border_line_alpha = 0.0
    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None  # disables pan or box zoom
    p.toolbar.active_scroll = None  # disables wheel zoom

    p.add_tools(
        HoverTool(
            tooltips=hovfun("@category: <b>@value</b>"),
            show_arrow=False,
            point_policy="follow_mouse",
        )
    )
    # apply_theme(p,theme)

    if sh == 1:
        show(p)

    return p


from math import pi
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, AnnularWedge
from bokeh.palettes import Turbo256


def fdonut_basic(
    df,
    title="Donut Chart",
    colors=palette,
    bgc=None,
    offset=(0, 0),
    outer_radius=0.7,
    inner_radius=0.35,
    theme='light',
    sh=0,
    height=650,
    width=800,
):
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
    theme :
    sh : int
        Whether to call show() automatically.
    height, width : int
        Plot size.
    """

    # --- Validate input ---
    if len(df.columns) < 2:
        raise ValueError(
            "DataFrame must have at least two columns: category and value."
        )

    df = df.copy()
    cat_col, val_col = df.columns[:2]
    df.columns = ["category", "value"]

    n = len(df)
    if colors is None:
        colors = palette[:n]
    else:
        colors = colors[:n]
    if n > len(colors):
        step = 256 // n
        colors = Turbo256[::step][:n]

    # --- Angles ---
    df["angle"] = df["value"] / df["value"].sum() * 2 * pi
    df["start_angle"] = df["angle"].cumsum().shift(1, fill_value=0)
    df["end_angle"] = df["angle"].cumsum()
    df["color"] = colors

    src = ColumnDataSource(df)

    # --- Figure ---
    p = figure(
        width=width,
        height=height,
        title=title,
        toolbar_location=None,
        x_range=(-1, 0.8),
        y_range=(-2, 2),
        background_fill_color=bgc,
        border_fill_color=bgc,
    )
    # --- Donut wedges ---
    p.annular_wedge(
        x=offset[0],
        y=offset[1],
        inner_radius=inner_radius,
        outer_radius=outer_radius,
        start_angle="start_angle",
        end_angle="end_angle",
        line_color="white",
        fill_color="color",
        source=src,
        legend_field="category",
        hover_line_color="black",
        hover_line_width=5,
    )

    # --- Hover tooltip ---
    p.add_tools(
        HoverTool(
            tooltips=hovfun("@category: <b>@value</b>"),
            show_arrow=False,
            point_policy="follow_mouse",
        )
    )
    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None
    p.legend.location = "center_right"
    p.legend.click_policy = "none"
    p.legend.background_fill_alpha = 0.0
    p.legend.border_line_alpha = 0.0
    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None  # disables pan or box zoom
    p.toolbar.active_scroll = None  # disables wheel zoom

    apply_theme(p,theme)


    if sh == 1:
        show(p)

    return p


import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool


def rounded_annular_wedge_patch(
    center,
    inner_radius,
    outer_radius,
    start_angle,
    end_angle,
    corner_radius=0.05,
    n_points=80,
    gap_width=0,
):
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
    c1_start = start_angle_outer - np.pi / 2
    c1_end = start_angle_outer
    c1_angles = np.linspace(c1_start, c1_end, corner_points)
    x_c1 = corner1_center_x + corner_radius * np.cos(c1_angles)
    y_c1 = corner1_center_y + corner_radius * np.sin(c1_angles)
    corner2_center_x = cx + (outer_radius - corner_radius) * np.cos(end_angle_outer)
    corner2_center_y = cy + (outer_radius - corner_radius) * np.sin(end_angle_outer)
    c2_start = end_angle_outer
    c2_end = end_angle_outer + np.pi / 2
    c2_angles = np.linspace(c2_start, c2_end, corner_points)
    x_c2 = corner2_center_x + corner_radius * np.cos(c2_angles)
    y_c2 = corner2_center_y + corner_radius * np.sin(c2_angles)
    corner3_center_x = cx + (inner_radius + corner_radius) * np.cos(end_angle_inner)
    corner3_center_y = cy + (inner_radius + corner_radius) * np.sin(end_angle_inner)
    c3_start = end_angle_inner + np.pi / 2
    c3_end = end_angle_inner + np.pi
    c3_angles = np.linspace(c3_start, c3_end, corner_points)
    x_c3 = corner3_center_x + corner_radius * np.cos(c3_angles)
    y_c3 = corner3_center_y + corner_radius * np.sin(c3_angles)
    corner4_center_x = cx + (inner_radius + corner_radius) * np.cos(start_angle_inner)
    corner4_center_y = cy + (inner_radius + corner_radius) * np.sin(start_angle_inner)
    c4_start = start_angle_inner + np.pi
    c4_end = start_angle_inner + 3 * np.pi / 2
    c4_angles = np.linspace(c4_start, c4_end, corner_points)
    x_c4 = corner4_center_x + corner_radius * np.cos(c4_angles)
    y_c4 = corner4_center_y + corner_radius * np.sin(c4_angles)
    x_patch = np.concatenate([x_c1, x_outer, x_c2, x_c3, x_inner, x_c4])
    y_patch = np.concatenate([y_c1, y_outer, y_c2, y_c3, y_inner, y_c4])
    return x_patch, y_patch


def plot_rounded_annular_wedges(
    data,
    labels=None,
    colors=None,
    center=(0.3, 0),
    theme='light',
    bgc=None,
    sh=0,
    width=800,
    height=600,
    inner_radius=0.5,
    outer_radius=1.0,
    corner_radius=0.08,
    gap_width=0.19,
    n_points=80,
    title="Rounded Doughnut Chart",
    legend_y=0.2,
):
    total = sum(data)
    N = len(data)
    if not colors:
        colors = ["gold", "lime", "dodgerblue", "purple", "orange", "cyan", "magenta"]
    colors = (colors * ((N + len(colors) - 1) // len(colors)))[:N]
    if not labels:
        labels = [f"Piece {i + 1}" for i in range(N)]
    angles = [2 * np.pi * v / total for v in data]
    start_angle = np.deg2rad(30)
    starts = [start_angle]
    for a in angles[:-1]:
        starts.append(starts[-1] + a)
    ends = [s + a for s, a in zip(starts, angles)]
    percents = [f"{int(round(100 * v / total))}%" for v in data]

    xs, ys = [], []
    for s, e in zip(starts, ends):
        x, y = rounded_annular_wedge_patch(
            center,
            inner_radius,
            outer_radius,
            s,
            e,
            corner_radius,
            n_points,
            gap_width=gap_width,
        )
        xs.append(x.tolist())
        ys.append(y.tolist())

    source = ColumnDataSource(
        data=dict(xs=xs, ys=ys, label=labels, percent=percents, color=colors)
    )

    p = figure(
        width=width,
        height=height,
        x_range=(-1.2, 1.8),
        y_range=(-1.1, 1.1),
        match_aspect=True,
        title=title,
    )
    patches_renderer = p.patches(
        "xs",
        "ys",
        source=source,
        fill_color="color",
        fill_alpha=1,
        line_color="white",
        line_width=2,
        hover_line_color="black",
        hover_line_width=3,
    )

    hover = HoverTool(
        tooltips=hovfun("@label: <b>@percent</b>"),
        show_arrow=False,
        point_policy="follow_mouse",
        renderers=[patches_renderer],
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
        text_font_style="bold",
    )
    # Custom legend (top right)
    legend_x = 0.14  # 1.22
    legend_y = legend_y  # 0.2#0.8
    legend_spacing = 0.1
    for i, (c, lbl) in enumerate(zip(colors, labels)):
        y_pos = legend_y - i * legend_spacing
        p.scatter([legend_x], [y_pos], size=18, color=c, alpha=0.7)
        p.text(
            [legend_x + 0.09],
            [y_pos],
            text=[lbl],
            text_align="left",
            text_color="grey",
            text_baseline="middle",
            text_font_size="13pt",
        )

    p.toolbar_location = None
    # --- Style tweaks ---
    p.axis.visible = False
    p.grid.visible = False
    p.outline_line_color = None

    p.border_fill_color = bgc
    p.background_fill_color = bgc
    p.toolbar.active_drag = None  # disables pan or box zoom
    p.toolbar.active_scroll = None  # disables wheel zoom
    p.min_border_right = 0
    p.min_border_bottom = 0

    apply_theme(p, theme)


    if sh == 1:
        show(p)

    return p


from bokeh.models import ColumnDataSource, Whisker, HoverTool


def boxplot(
    df,
    xcol,
    ycol,
    group_col=None,
    title=None,
    xlabel=None,
    ylabel=None,
    palette=None,
    theme="light",
    legend_outside=True,
    width=1000,
    height=600,
    save=0,
    output_path="boxplot",
    sh=0,
    show_outliers=True,
    outlier_color="grey",
    outlier_alpha=0.8,
):
    """
    Create a professional Bokeh boxplot from a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input data containing category and numeric columns
    xcol : str
        Name of the categorical column (x-axis)
    ycol : str
        Name of the numeric column (y-axis)
    group_col : str, optional
        Name of grouping column for color coding (e.g., 'Continent', 'Region').
        Creates side-by-side boxes for each group within each category.
    title : str, optional
        Plot title. Auto-generated if None.
    xlabel : str, optional
        X-axis label. Uses xcol if None.
    ylabel : str, optional
        Y-axis label. Uses ycol if None.
    palette : dict or list, optional
        If group_col: dict mapping group names to colors (e.g., {'A': '#ff0000'})
        If no group_col: list of colors for each category
        Uses default bxc2 palette if None.
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default True
        If True, positions legend outside plot area to the right
    width : int, default 1000
        Plot width in pixels
    height : int, default 600
        Plot height in pixels
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save)
    output_path : str, default 'boxplot'
        File path for saving
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show)
    show_outliers : bool, default True
        Whether to display outlier points
    outlier_color : str, default 'grey'
        Color for outlier points
    outlier_alpha : float, default 0.8
        Transparency for outlier points

    Returns
    -------
    bokeh.plotting.figure.Figure
        Bokeh figure object

    Examples
    --------
    >>> # Simple boxplot
    >>> df = pd.DataFrame({
    ...     'category': ['A', 'A', 'B', 'B', 'C', 'C'],
    ...     'value': [10, 15, 20, 25, 12, 18]
    ... })
    >>> p = fboxplot(df, xcol='category', ycol='value')

    >>> # Grouped boxplot with custom colors
    >>> palette = {'North': '#4db4fd', 'South': '#ff6464'}
    >>> p = fboxplot(df, xcol='city', ycol='temperature',
    ...              group_col='region', palette=palette)
    """

    # --- Data Preparation ---
    if group_col is not None:
        d = (
            df[[xcol, ycol, group_col]]
            .dropna()
            .rename(columns={xcol: "x", ycol: "y", group_col: "group"})
        )
        # Create composite key for x-axis (category + group)
        d["x_group"] = d["x"].astype(str) + " (" + d["group"].astype(str) + ")"
        cats = sorted(d["x_group"].unique())
    else:
        d = df[[xcol, ycol]].dropna().rename(columns={xcol: "x", ycol: "y"})
        d["x_group"] = d["x"].astype(str)
        cats = sorted(d["x"].unique())

    # --- Compute Quartiles and Whiskers ---
    qs = d.groupby("x_group")["y"].quantile([0.25, 0.5, 0.75]).unstack().reset_index()
    qs.columns = ["x_group", "q1", "q2", "q3"]

    # Add group info back to qs
    if group_col is not None:
        qs = qs.merge(
            d[["x_group", "group"]].drop_duplicates(), on="x_group", how="left"
        )

    # Calculate IQR and whiskers
    iqr = qs.q3 - qs.q1
    qs["upper"] = qs.q3 + 1.5 * iqr
    qs["lower"] = qs.q1 - 1.5 * iqr

    # Clamp whiskers to actual data range
    mins = d.groupby("x_group")["y"].min()
    maxs = d.groupby("x_group")["y"].max()
    qs["upper"] = np.minimum(qs["upper"], qs["x_group"].map(maxs))
    qs["lower"] = np.maximum(qs["lower"], qs["x_group"].map(mins))

    # --- Identify Outliers ---
    merged = d.merge(qs[["x_group", "lower", "upper"]], on="x_group", how="left")
    outliers = merged[~merged.y.between(merged.lower, merged.upper)]

    # --- Color Palette Setup ---
    if group_col is not None:
        if palette is None:
            # Auto-generate colors for groups
            unique_groups = sorted(d["group"].unique())
            palette = {grp: bxc2[i % len(bxc2)] for i, grp in enumerate(unique_groups)}
        qs["color"] = qs["group"].map(palette)
    else:
        if palette is None:
            palette = bxc2
        qs["color"] = [palette[i % len(palette)] for i in range(len(qs))]

    # --- Data Sources ---
    src = ColumnDataSource(qs)
    src_out = ColumnDataSource(outliers)

    # --- Auto-generate Title and Labels ---
    if title is None:
        if group_col:
            title = f"{ycol} by {xcol} (grouped by {group_col})"
        else:
            title = f"{ycol} Distribution by {xcol}"

    if xlabel is None:
        xlabel = xcol
    if ylabel is None:
        ylabel = ycol

    # --- Create Figure ---
    p = figure(
        x_range=cats,
        width=width,
        height=height,
        title=title,
        x_axis_label=xlabel,
        y_axis_label=ylabel,
        tools="tap,wheel_zoom,box_zoom,pan,save,reset",
        active_scroll="wheel_zoom",
        toolbar_location="left",
    )

    # Line color based on theme
    line_color = "white" if theme == "dark" else "black"

    # --- Whiskers ---
    whisker = Whisker(
        base="x_group",
        upper="upper",
        lower="lower",
        source=src,
        line_color=line_color,
        line_width=2,
    )
    whisker.upper_head.size = whisker.lower_head.size = 12
    whisker.upper_head.line_color = whisker.lower_head.line_color = line_color
    p.add_layout(whisker)

    # --- Boxes ---
    if group_col is not None:
        # Grouped boxplot with legend
        r1 = p.vbar(
            x="x_group",
            width=0.7,
            top="q3",
            bottom="q2",
            source=src,
            fill_color="color",
            line_color=line_color,
            fill_alpha=1,
            hover_fill_alpha=1.0,
            selection_fill_alpha=1.0,
            nonselection_fill_alpha=0.1,
            legend_field="group",
        )
        r2 = p.vbar(
            x="x_group",
            width=0.7,
            top="q2",
            bottom="q1",
            source=src,
            fill_color="color",
            line_color=line_color,
            fill_alpha=1,
            hover_fill_alpha=1.0,
            selection_fill_alpha=1.0,
            nonselection_fill_alpha=0.1,
            legend_field="group",
        )
    else:
        # Simple boxplot without legend
        r1 = p.vbar(
            x="x_group",
            width=0.7,
            top="q3",
            bottom="q2",
            source=src,
            fill_color="color",
            line_color=line_color,
            fill_alpha=1,
            hover_fill_alpha=1.0,
            selection_fill_alpha=1.0,
            nonselection_fill_alpha=0.1,
        )
        r2 = p.vbar(
            x="x_group",
            width=0.7,
            top="q2",
            bottom="q1",
            source=src,
            fill_color="color",
            line_color=line_color,
            fill_alpha=1,
            hover_fill_alpha=1.0,
            selection_fill_alpha=1.0,
            nonselection_fill_alpha=0.1,
        )

    # --- Median Line ---
    p.segment(
        x0="x_group",
        y0="q2",
        x1="x_group",
        y1="q2",
        line_color=line_color,
        line_width=3,
        source=src,
    )

    # --- Outliers ---
    if show_outliers and not outliers.empty:
        p.scatter(
            x="x_group",
            y="y",
            source=src_out,
            size=6,
            color=outlier_color,
            alpha=outlier_alpha,
            marker="circle",
        )

    # --- Hover Tool ---
    hover_template = """
        <i>Category:</i> <b>@x_group</b><br>
        <i>Q1:</i> <b>@q1{0.00}</b><br>
        <i>Median:</i> <b>@q2{0.00}</b><br>
        <i>Q3:</i> <b>@q3{0.00}</b><br>
        <i>Lower Whisker:</i> <b>@lower{0.00}</b><br>
        <i>Upper Whisker:</i> <b>@upper{0.00}</b>
    """

    if group_col is not None:
        hover_template = "<i>Group:</i> <b>@group</b><br>" + hover_template

    p.add_tools(
        HoverTool(
            tooltips=hovfun(hover_template),
            show_arrow=False,
            mode="mouse",
            renderers=[r1, r2],
        )
    )

    # --- Rotate X-axis Labels ---
    p.xaxis.major_label_orientation = 0.8

    # --- Apply Theme ---
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)

    # Configure legend if group_col exists
    if group_col is not None:
        p.legend.click_policy = "hide"


    # --- Save if Requested ---
    if save == 1:
        save_plot(p, output_path)
        print(f"✓ Boxplot saved to: {output_path}")

    # --- Show if Requested ---
    if sh == 1:
        show(p)

    return p


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
    p.title.text_font = "'Consolas', 'Helvetica', monospace"
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
            font-family:'Consolas', 'Helvetica', monospace;
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
            <div style="padding:10px;border:2px solid ${border_color};border-radius:6px;background:${info_bg};color:${text_color};font-family:'Consolas', 'Helvetica', monospace;">
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
            <div style="padding:10px;border:2px solid ${border_color};border-radius:6px;background:${info_bg};color:${text_color};font-family:'Consolas', 'Helvetica', monospace;">
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
            font-family:'Consolas', 'Helvetica', monospace;
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




############################
# GENERIC CHOROPLETH FUNCTION
############################
import json
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import (
    GeoJSONDataSource,
    LinearColorMapper,
    ColorBar,
    FixedTicker,
    HoverTool,
)
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


def merge_data_to_geo(natural_earth_geo, source_geo, value_col="population"):
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
    for feature in source_geo.get("features", []):
        name = feature["properties"].get("name")
        value = feature["properties"].get(value_col)
        if name and value is not None:
            value_map[name] = value

    # Common name variations
    name_mappings = {
        "United States of America": "United States",
        "Russian Federation": "Russia",
        "Republic of Korea": "South Korea",
        "Korea, Republic of": "Korea",
        "Democratic Republic of the Congo": "Dem. Rep. Congo",
        "Republic of the Congo": "Congo",
        "Czech Republic": "Czechia",
        "Tanzania": "United Republic of Tanzania",
        "Côte d'Ivoire": "Ivory Coast",
        "Cote d'Ivoire": "Ivory Coast",
        "Ivory Coast": "Cote d'Ivoire",
    }

    # Add values to Natural Earth features
    for feature in natural_earth_geo.get("features", []):
        name = feature["properties"].get("NAME", "")

        # Try direct match first
        if name in value_map:
            feature["properties"][value_col] = value_map[name]
        # Try mappings
        elif name in name_mappings and name_mappings[name] in value_map:
            feature["properties"][value_col] = value_map[name_mappings[name]]
        # Try alternative names from Natural Earth
        else:
            for key in ["NAME_LONG", "FORMAL_EN", "NAME_SORT"]:
                alt_name = feature["properties"].get(key, "")
                if alt_name in value_map:
                    feature["properties"][value_col] = value_map[alt_name]
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
                        x, y = projection.transform_point(
                            coord[0], coord[1], source_crs
                        )
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


def plot_world_choropleth(
    world_geo,
    projection,
    projName,
    value_col="population",
    palette=None,
    bin_labels=None,
    bin_edges=None,
    use_natural_earth=True,
    show_plot=True,
    title=None,
    legend_title=None,
    tooltip_label=None,
    value_format="{0,0}",
    width=1400,
    height=700,
    bg_color="#f5f5f5",oceanc = '#90D5FF'
):
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
        print(
            f"Loaded {len(world_geo.get('features', []))} countries from Natural Earth"
        )

    # Handle Antarctica (set to 0 if missing)
    for feature in world_geo["features"]:
        props = feature.get("properties", {})
        name = props.get("NAME", props.get("name", ""))
        if "antarctica" in name.lower():
            if props.get(value_col) is None:
                props[value_col] = 0

    # Clean up missing data
    world_geo["features"] = [
        f
        for f in world_geo["features"]
        if f.get("properties", {}).get(value_col) is not None
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
            "<500k",
            "500k–2M",
            "2M–10M",
            "10M–30M",
            "30M–50M",
            "50M–100M",
            "100M–300M",
            "300M–1B",
            "1B+",
        ]

    if palette is None:
        palette = [
            "#ececec",
            "#b9d7c2",
            "#87b37a",
            "#65934c",
            "#c4b16a",
            "#dfc872",
            "#e7b07a",
            "#d08c60",
            "#b05f3c",
            "#7e4836",
        ]

    # Assign data bins
    for feature in world_geo_projected["features"]:
        value = feature["properties"][value_col]
        # Handle zero values - put in lowest bin
        if value == 0:
            idx = 0
        else:
            idx = next(
                (
                    i
                    for i in range(len(bin_edges) - 1)
                    if bin_edges[i] <= value < bin_edges[i + 1]
                ),
                len(bin_labels) - 1,
            )
        feature["properties"]["data_bin_index"] = idx

        # Ensure 'name' field exists for tooltips
        if "NAME" in feature["properties"] and "name" not in feature["properties"]:
            feature["properties"]["name"] = feature["properties"]["NAME"]

    # Prepare Bokeh data source
    geosource = GeoJSONDataSource(geojson=json.dumps(world_geo_projected))
    color_mapper = LinearColorMapper(palette=palette, low=0, high=len(bin_labels) - 1)

    # Create Earth boundary
    def create_earth_boundary(projection, n_points=360):
        source_crs = ccrs.PlateCarree()
        boundary_points = []

        if isinstance(projection, (ccrs.Orthographic, ccrs.NearsidePerspective)):
            angles = np.linspace(0, 2 * np.pi, n_points)
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

        lats = np.linspace(89.9, -89.9, n_points // 4)
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

        lats = np.linspace(-89.9, 89.9, n_points // 4)
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
        title = (
            f"🌎 World {value_col.replace('_', ' ').title()} by Country ~ {projName}"
        )

    if legend_title is None:
        legend_title = value_col.replace("_", " ").title()

    if tooltip_label is None:
        tooltip_label = value_col.replace("_", " ").title()

    # Bokeh figure
    p = figure(
        title=title,
        width=width,
        height=height,
        toolbar_location="right",
        tools="pan,box_zoom,reset,save,wheel_zoom",
        active_scroll="wheel_zoom",
        x_axis_location=None,
        y_axis_location=None,
    )

    # Adjust for orthographic projections
    if "orth" in str(projection).lower():
        p.width = 900

    p.grid.grid_line_color = None
    p.axis.visible = False
    p.outline_line_color = None

    # Add Earth boundary
    if earth_boundary:
        xs = [point[0] for point in earth_boundary]
        ys = [point[1] for point in earth_boundary]
        p.patch(
            xs,
            ys,
            fill_color=oceanc,
            line_color="black",
            line_width=3,
            alpha=1.0,
            level="underlay",
        )

    # Country patches
    countries = p.patches(
        "xs",
        "ys",
        source=geosource,
        fill_color={"field": "data_bin_index", "transform": color_mapper},
        line_color="black",
        line_width=0.25,
        fill_alpha=0.8,
        hover_line_color="black",
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
        """,
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
        background_fill_color=bg_color,
        location=(0, 10),
        orientation="vertical",
        title=legend_title,
        major_label_text_color="#2f2f2f" if bg_color == "#f5f5f5" else "#ffffff",
        title_text_color="#2f2f2f" if bg_color == "#f5f5f5" else "#ffffff",
        major_label_text_font_size="16pt",
        title_text_font_size="16pt",
    )
    p.add_layout(color_bar, "right")

    # Style
    p.title.text_font_size = "19pt"
    p.title.text_font = "Montserrat"
    p.title.text_color = "#7b4397" if bg_color == "#f5f5f5" else "#e0b0ff"
    p.background_fill_color = bg_color
    p.border_fill_color = bg_color
    p.legend.visible = False

    if show_plot:
        show(p)
    return p


# Keep backward compatibility
def plot_world_population(*args, **kwargs):
    """Backward compatible wrapper for population-specific plots."""
    if "value_col" not in kwargs:
        kwargs["value_col"] = "population"
    return plot_world_choropleth(*args, **kwargs)


def plot_country_choropleth(
    geojson_url,
    data_dict,
    value_col,
    country_name,
    palette,
    bin_edges,
    bin_labels,
    title=None,
    name_property="name",
    legend_title=None,
    tooltip_label=None,
    value_format="{0,0}",
    width=1200,
    height=900,
    bounds=None,
    bg_color="#f5f5f5",
):
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
    from bokeh.models import (
        GeoJSONDataSource,
        LinearColorMapper,
        ColorBar,
        FixedTicker,
        HoverTool,
    )

    # Load GeoJSON
    print(f"Loading GeoJSON from {geojson_url}")
    geo_data = requests.get(geojson_url).json()
    print(f"Loaded {len(geo_data['features'])} regions")

    # Assign data to features
    matched = 0
    for feature in geo_data["features"]:
        region_name = feature["properties"].get(name_property, "")
        value = data_dict.get(region_name, None)
        if value is not None:
            matched += 1
        feature["properties"][value_col] = value

    print(f"Matched {matched}/{len(data_dict)} regions with data")

    # Remove features without data
    geo_data["features"] = [
        f for f in geo_data["features"] if f["properties"].get(value_col) is not None
    ]

    # Assign bins
    for feature in geo_data["features"]:
        val = feature["properties"][value_col]
        if val == 0:
            idx = 0
        else:
            idx = next(
                (
                    i
                    for i in range(len(bin_edges) - 1)
                    if bin_edges[i] <= val < bin_edges[i + 1]
                ),
                len(bin_labels) - 1,
            )
        feature["properties"]["data_bin_index"] = idx

    # Calculate bounds if not provided
    if bounds is None:
        all_coords = []
        for feature in geo_data["features"]:
            geom = feature["geometry"]
            if geom["type"] == "Polygon":
                for ring in geom["coordinates"]:
                    all_coords.extend(ring)
            elif geom["type"] == "MultiPolygon":
                for polygon in geom["coordinates"]:
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
        legend_title = value_col.replace("_", " ").title()
    if tooltip_label is None:
        tooltip_label = value_col.replace("_", " ").title()

    # Create Bokeh data source
    geosource = GeoJSONDataSource(geojson=json.dumps(geo_data))
    color_mapper = LinearColorMapper(palette=palette, low=0, high=len(bin_labels) - 1)

    # Create figure
    p = figure(
        title=title,
        width=width,
        height=height,
        x_range=(min_lon, max_lon),
        y_range=(min_lat, max_lat),
        toolbar_location="right",
        tools="pan,box_zoom,reset,save,wheel_zoom",
        active_scroll="wheel_zoom",
        x_axis_location=None,
        y_axis_location=None,
        background_fill_color=bg_color,
        border_fill_color=bg_color,
    )

    p.grid.grid_line_color = None
    p.axis.visible = False
    p.outline_line_color = None
    # Add regions
    regions = p.patches(
        "xs",
        "ys",
        source=geosource,
        fill_color={"field": "data_bin_index", "transform": color_mapper},
        line_color="#555555",
        line_width=0.5,
        fill_alpha=0.8,
        hover_line_color="black",
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
        """,
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
        background_fill_color=bg_color,
        location=(0, 0),
        orientation="vertical",
        title=legend_title,
        major_label_text_color="#2f2f2f" if bg_color == "#f5f5f5" else "#f5f5f5",
        title_text_color="#2f2f2f" if bg_color == "#f5f5f5" else "#f5f5f5",
        major_label_text_font_size="16pt",
        title_text_font_size="16pt",
    )
    p.add_layout(color_bar, "right")

    # Styling
    p.title.text_font_size = "18pt"
    p.title.text_font = "Montserrat"
    p.title.text_color = "#7b4397" if bg_color == "#f5f5f5" else "#f5f5f5"

    return p


from bokeh.plotting import figure, show
from bokeh.models import LinearColorMapper, ColorBar, ColumnDataSource, HoverTool
from bokeh.transform import transform
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# -----------------------------------------------------
# 🎨 Utility: Convert matplotlib cmap to hex list
# -----------------------------------------------------
def mpl_to_hex_palette(cmap_name="viridis", n_colors=256):
    cmap = plt.get_cmap(cmap_name)
    return [to_hex(cmap(i / n_colors)) for i in range(n_colors)]


# -----------------------------------------------------
# 💡 Core Function: High-Level Heatmap Generator
# -----------------------------------------------------
def create_heatmap_figure(
    data,
    x_labels=None,
    y_labels=None,
    cmap="viridis",
    title="Heatmap",
    width=600,
    height=400,
    show_values=True,
    hover_format=None,
    text_font_size="11pt",
    text_color="grey",
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
    color_mapper = LinearColorMapper(
        palette=palette, low=np.min(vals), high=np.max(vals)
    )

    # 4️⃣ Create figure
    p = figure(
        title=title,
        x_range=x_labels,
        y_range=list(reversed(y_labels)),
        width=width,
        height=height,
        tools="",
        toolbar_location=None,
    )

    rects = p.rect(
        x="x",
        y="y",
        width=1,
        height=1,
        source=source,
        fill_color=transform("values", color_mapper),
        line_color="black",
        hover_line_color="deepskyblue",
        hover_line_width=3,
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
            text_color=text_color,
        )

    # 6️⃣ Add color bar
    color_bar = ColorBar(
        color_mapper=color_mapper,
        width=11,
        location=(0, 0),
        major_label_text_font_size="16pt",
        title_text_font_size="16pt",
    )
    p.add_layout(color_bar, "right")

    # 7️⃣ Default hover tooltip if none provided
    if hover_format is None:
        hover_format = hovfun("🧩 X: @x<br>🧭 Y: @y<br>🌡️ Value: @values{0.000}")

    hover = HoverTool(
        tooltips=hover_format,
        renderers=[rects],
        mode="mouse",
        point_policy="follow_mouse",
        attachment="below",
        show_arrow=False,
    )
    p.add_tools(hover)

    # 8️⃣ Minimalistic style
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "12pt"
    p.title.text_font_size = "14pt"

    return p




def scatter(
    df,
    x=None,
    y=None,
    title="Scatter Plot",
    xlabel=None,
    ylabel=None,
    color_by=None,
    palette=None,
    size=12,
    alpha=0.7,
    regression=False,
    regression_color='red',
    regression_width=2,
    metrics_table=False,
    metrics_data=None,
    x_range=None,
    y_range=None,
    theme="light",
    legend_outside=True,
    width=800,
    height=800,
    save=0,
    output_path="scatter_plot",
    sh=0,
    webgl=False,
    datetime_fmt=None,
    float_fmt="{0.00}",
    fill_color=None,
    line_color=None,
    hover_line_width=17,
    ripple=False,
    ripple_cols=None,
    ripple_circles=4,
    ripple_spacing=8,
    ripple_animate=True,
    glow=False,
    glow_points=None,
    glow_color='red',
    glow_size=20,
    glow_intensity=3,
    glow_alpha=0.3,
    glow_label='Glow Points',
    glow_data=None,
):
    """
    Create interactive scatter plots with optional regression, grouping, and effects.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with scatter data
    x : str, optional
        Column name for x-axis. If None, uses first numeric column
    y : str or list of str, optional
        Column name(s) for y-axis. If list, plots multiple y columns against same x.
        If None, uses second numeric column
    title : str, default 'Scatter Plot'
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    color_by : str, optional
        Column name to group by and color points differently (only works when y is single column)
    palette : list, optional
        List of colors for groups/columns. Uses default palette if None
    size : int, default 12
        Size of scatter points
    alpha : float, default 0.7
        Transparency of points (0-1)
    regression : bool, default False
        If True, adds regression line
    regression_color : str, default 'red'
        Color of regression line
    regression_width : int, default 2
        Width of regression line
    metrics_table : bool, default False
        If True, shows evaluation metrics table alongside plot
    metrics_data : dict, optional
        Custom metrics data for table. If None and regression=True, auto-calculates
    x_range : tuple, optional
        (min, max) for x-axis range
    y_range : tuple, optional
        (min, max) for y-axis range
    theme : str, default 'light'
        Visual theme: 'light' or 'dark'
    legend_outside : bool, default True
        If True, positions legend outside plot area
    width : int, default 800
        Chart width in pixels
    height : int, default 800
        Chart height in pixels
    save : int, default 0
        Whether to save the plot (1=save, 0=don't save)
    output_path : str, default 'scatter_plot'
        File path for saving
    sh : int, default 1
        Whether to show the plot (1=show, 0=don't show)
    webgl : bool, default False
        If True, uses WebGL backend for better performance with large datasets
    datetime_fmt : str, optional
        Datetime format for tooltips (e.g., "%Y-%m-%d %H:%M")
    float_fmt : str, default "{0.00}"
        Numeric format for tooltips (e.g., "{0.00}" for 2 decimals)
    fill_color : str or None, optional
        Fill color for points. If None, uses palette
    line_color : str, optional
        Line color for points. If None, uses fill_color
    hover_line_width : int, default 17
        Width of highlight on hover
    ripple : bool, default False
        If True, adds ripple effect to ALL points (when y is single column)
    ripple_cols : list of str, optional
        List of column names that should have ripple effect (when y is list of columns)
        Example: ['humidity'] will add ripple only to humidity points
    ripple_circles : int, default 4
        Number of ripple circles per point
    ripple_spacing : int, default 8
        Spacing between ripple circles
    ripple_animate : bool, default True
        If True, animates the ripple effect
    glow : bool, default False
        If True, adds glow/halo effect to specified points
    glow_points : dict, optional
        Dict with 'x' and 'y' lists for glow points (e.g., {'x': [1,2], 'y': [3,4]})
    glow_color : str, default 'red'
        Color for glow points
    glow_size : int, default 20
        Size of center glow point
    glow_intensity : int, default 3
        Number of glow layers (more = stronger glow)
    glow_alpha : float, default 0.3
        Alpha transparency for glow layers
    glow_label : str, default 'Glow Points'
        Legend label for glow points
    glow_data : dict, optional
        Additional data for glow point tooltips (e.g., {'name': ['A', 'B'], 'value': [10, 20]})
        Must have same length as glow_points['x']

    Returns
    -------
    bokeh.plotting.figure.Figure or bokeh.layouts.LayoutDOM
        Bokeh figure object or layout (if metrics_table=True)

    Examples
    --------
    >>> # Glow points with custom tooltip data
    >>> glow_pts = {'x': [1, 2], 'y': [3, 4]}
    >>> glow_info = {'name': ['Point A', 'Point B'], 'importance': [95, 87]}
    >>> p = fscatter(df, x='x', y='y', glow=True, glow_points=glow_pts, 
    ...              glow_data=glow_info)
    """
    from scipy import stats
    from bokeh.models import CustomJS, DataTable, TableColumn, Div
    from bokeh.layouts import column, row

    # Setup data
    df = df.copy()

    # Auto-detect x and y if not provided
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if x is None:
        x = numeric_cols[0] if len(numeric_cols) > 0 else df.columns[0]
    
    # Handle y as list or single column
    if y is None:
        y = [numeric_cols[1]] if len(numeric_cols) > 1 else [numeric_cols[0]]
    elif isinstance(y, str):
        y = [y]
    
    # Setup colors
    default_colors = bxc2
    
    # When multiple y columns, color_by is not supported
    if len(y) > 1 and color_by is not None:
        print("Warning: color_by is ignored when plotting multiple y columns")
        color_by = None
    
    # Handle color_by for grouped scatter (only works with single y)
    if color_by is not None and len(y) == 1:
        groups = df[color_by].unique()
        if palette is None:
            palette = list(itertools.islice(itertools.cycle(default_colors), len(groups)))
        color_map = dict(zip(groups, palette))
        df['colors'] = df[color_by].map(color_map)
    else:
        # Multiple y columns or no grouping
        if palette is None:
            palette = list(itertools.islice(itertools.cycle(default_colors), len(y)))

    # Add hidden column for tooltip control
    df['hidden'] = np.ones(len(df)) * np.min(df[y].min())

    # Determine ranges
    if x_range is None:
        x_range = (df[x].min(), df[x].max())
    if y_range is None:
        y_range = (df[y].min().min(), df[y].max().max())

    # Create figure
    fig_kwargs = {
        "x_range": x_range,
        "y_range": y_range,
        "width": width,
        "height": height,
        "title": title,
        "x_axis_label": xlabel or x,
        "y_axis_label": ylabel or (y[0] if len(y) == 1 else ""),
        "tools": "pan,wheel_zoom,box_zoom,reset,save,lasso_select",
        "active_scroll": "wheel_zoom",
    }

    if webgl:
        fig_kwargs["output_backend"] = "webgl"

    p = figure(**fig_kwargs)

    # --- SCATTER RENDERING ---
    scatter_renderers = []

    # Determine which columns should have ripple
    if ripple_cols is None:
        ripple_cols = []
    
    # If ripple=True and single y column, apply to that column
    if ripple and len(y) == 1 and len(ripple_cols) == 0:
        ripple_cols = y

    # Plot each y column
    for idx, y_col in enumerate(y):
        col_color = palette[idx]
        has_ripple = y_col in ripple_cols
        
        if has_ripple:
            # Create ripple effect for this column
            n_circles = ripple_circles
            x_ripple = np.repeat(df[x].values, n_circles)
            y_ripple = np.repeat(df[y_col].values, n_circles)
            base_sizes = [size + i * ripple_spacing for i in range(n_circles)] * len(df)
            
            ripple_df = pd.DataFrame({
                x: x_ripple,
                y_col: y_ripple,
                'size': base_sizes,
            })
            source_ripple = ColumnDataSource(ripple_df)
            
            # Outer ripple circles (hollow) - ADD TO LEGEND
            circles = p.circle(x, y_col,
                              size='size',
                              fill_color=col_color,
                              line_color=col_color,
                              fill_alpha=0,
                              line_alpha=1,
                              line_width=1,
                              source=source_ripple,
                              legend_label=f"{y_col} (ripple)")
            
            # Inner filled circles
            inner_sizes = [s / 4 for s in base_sizes]
            ripple_df['size'] = inner_sizes
            source_ripple2 = ColumnDataSource(ripple_df)
            
            circles2 = p.circle(x, y_col,
                               size='size',
                               fill_color=col_color,
                               line_color=col_color,
                               fill_alpha=1,
                               line_alpha=1,
                               source=source_ripple2,
                               legend_label=f"{y_col} (ripple)")
            
            # Add animation if requested
            if ripple_animate:
                animation = CustomJS(args=dict(source=source_ripple, base_sizes=base_sizes), code='''
                    let frame = 0;
                    const data = source.data;
                    const sizes = data['size'];
                    
                    function animate() {
                        // Update sizes with sine wave
                        for (let i = 0; i < sizes.length; i++) {
                            const baseSize = base_sizes[i];
                            sizes[i] = baseSize * (1 + 0.5 * Math.sin(frame + i * 0.5));
                        }
                        
                        // Update frame and data source
                        frame += 0.1;
                        source.change.emit();
                        
                        // Request next frame
                        setTimeout(animate, 50);
                    }
                    
                    // Start animation
                    animate();
                ''')
                from bokeh.io import curdoc
                doc = curdoc()
                doc.add_root(p)
                doc.js_on_event('document_ready', animation)
            
            # Create invisible scatter for tooltips
            source = ColumnDataSource(df)
            sc = p.scatter(x, y_col, source=source, size=size, fill_color=col_color, 
                          alpha=0, hover_line_width=hover_line_width,
                          hover_line_color=col_color, legend_label=f"{y_col} (ripple)")
            scatter_renderers.append(sc)
            
        elif color_by is not None and len(y) == 1:
            # Grouped scatter plot (only for single y column)
            groups = df[color_by].unique()
            for group in groups:
                group_data = df[df[color_by] == group].copy()
                source = ColumnDataSource(group_data)
                
                sc_fill = fill_color if fill_color is not None else color_map[group]
                sc_line = line_color if line_color is not None else color_map[group]
                
                sc = p.scatter(x, y_col, source=source, color=sc_fill, 
                              line_color=sc_line, size=size, alpha=alpha,
                              hover_line_width=hover_line_width,
                              legend_label=f"{group}")
                scatter_renderers.append(sc)
        else:
            # Regular scatter for this column
            source = ColumnDataSource(df)
            
            sc_fill = fill_color if fill_color is not None else col_color
            sc_line = line_color if line_color is not None else sc_fill
            
            sc = p.scatter(x, y_col, source=source, size=size, 
                          fill_color=sc_fill, line_color=sc_line,
                          alpha=alpha, hover_line_width=hover_line_width,
                          hover_line_color=sc_fill,
                          legend_label=y_col)
            scatter_renderers.append(sc)

    # Add glow effect (lighting/halo around points) with tooltips
    glow_renderers = []
    if glow and glow_points is not None:
        # Prepare glow data source
        glow_source_data = {
            'x': glow_points['x'],
            'y': glow_points['y'],
            'hidden': [0] * len(glow_points['x'])  # For tooltip formatter
        }
        
        # Add any additional glow data for tooltips
        if glow_data is not None:
            for key, values in glow_data.items():
                glow_source_data[key] = values
        
        glow_source = ColumnDataSource(glow_source_data)
        
        # Create multiple layers for glow effect (not in legend, no tooltips)
        for i in range(glow_intensity, 0, -1):
            glow_layer_size = glow_size + (i * 15)
            glow_layer_alpha = glow_alpha * (i / glow_intensity)
            
            p.circle(x='x', y='y', source=glow_source,
                    fill_color=glow_color, 
                    fill_alpha=glow_layer_alpha,
                    line_color=None,
                    size=glow_layer_size)
        
        # Add bright center point - THIS ONE GOES IN LEGEND AND HAS TOOLTIPS
        glow_center = p.circle(x='x', y='y', source=glow_source,
                              fill_color=glow_color, 
                              size=glow_size,
                              fill_alpha=0.9,
                              line_color='white',
                              line_width=2,
                              legend_label=glow_label,
                              )
        glow_renderers.append(glow_center)
        
        # Build glow tooltip
        glow_tooltip_cols = ['x', 'y']
        if glow_data is not None:
            glow_tooltip_cols.extend(glow_data.keys())
        
        # Create DataFrame for glow tooltips
        glow_df = pd.DataFrame(glow_source_data)
        glow_tltl = build_auto_tooltip(
            glow_df[glow_tooltip_cols],
            hovfun,
            datetime_fmt=datetime_fmt,
            float_fmt=float_fmt,
        )
        
        # Add hover tool for glow points
        p.add_tools(
            HoverTool(
                tooltips=glow_tltl,
                formatters={"@hidden": cusj()},
                mode="mouse",
                renderers=glow_renderers,
            )
        )

    # Add regression line
    slope, intercept, r_value, p_value, std_err = None, None, None, None, None
    if regression and len(y) == 1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(df[x], df[y[0]])
        x_min, x_max = df[x].min(), df[x].max()
        source_slope = ColumnDataSource(data=dict(
            x=[x_min, x_max], 
            y=[intercept + slope * x_min, intercept + slope * x_max]
        ))
        p.line('x', 'y', source=source_slope, line_color=regression_color, 
              line_width=regression_width, legend_label='Regression')

    # --- CRITICAL TOOLTIP SECTION - DO NOT MODIFY ---
    # Build tooltip columns
    tooltip_cols = [x] + y
    if color_by is not None:
        tooltip_cols.append(color_by)
    
    tltl = build_auto_tooltip(
        df[tooltip_cols],
        hovfun,
        datetime_fmt=datetime_fmt,
        float_fmt=float_fmt,
    )

    # Determine if x is datetime
    if np.issubdtype(df[x].dtype, np.datetime64):
        p.add_tools(
            HoverTool(
                tooltips=tltl,
                formatters={"@" + x: "datetime", "@hidden": cusj()},
                mode="mouse",
                point_policy="snap_to_data",
                renderers=scatter_renderers,
            )
        )
    else:
        p.add_tools(
            HoverTool(
                tooltips=tltl,
                formatters={"@hidden": cusj()},
                mode="mouse",
                point_policy="snap_to_data",
                renderers=scatter_renderers,
            )
        )
    # --- END CRITICAL TOOLTIP SECTION ---

    # Apply theme and extras
    p = apply_theme(p, theme=theme, legend_outside=legend_outside)
    p = add_extras(p, cross=False)

    # Create metrics table if requested
    final_output = p
    if metrics_table:
        if metrics_data is None and regression and len(y) == 1:
            # Auto-calculate metrics
            metrics_data = {
                'Metric': ['Pearson R', 'R²', 'Slope', 'Intercept', 'P-value', 'Std Error', 'Number of Points'],
                'Value': [
                    f"{r_value:.4f}",
                    f"{r_value**2:.4f}",
                    f"{slope:.4f}",
                    f"{intercept:.4f}",
                    f"{p_value:.4e}",
                    f"{std_err:.4f}",
                    len(df)
                ]
            }
        
        if metrics_data is not None:
            # Create table
            metrics_source = ColumnDataSource(data=metrics_data)
            columns = [
                TableColumn(field="Metric", title="Metric"),
                TableColumn(field="Value", title="Value"),
            ]
            data_table = DataTable(source=metrics_source, columns=columns, 
                                  width=300, height=280)
            table_title = Div(text="<h3>Evaluation Metrics</h3>")
            final_output = row(column(table_title, data_table), p)

    # Save if requested
    if save == 1:
        save_plot(final_output, output_path)
        print(f"✓ Chart saved to: {output_path}")

    # Show if requested
    if sh == 1:
        show(final_output)

    return final_output























################################
# BOKEH STYLES
################################
from bokeh.io import show, curdoc
from bokeh.models import Slider, InlineStyleSheet
from bokeh.layouts import column

# curdoc().theme = 'dark_minimal'

slider_style = InlineStyleSheet(css="""
/* Host: set the widget's container background */
:host {
  background: #16161e !important;   /* even darker than black for modern dark UI */
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
  background: #23233c !important;
    border: 1px solid #2a3132 !important;

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










from bokeh.io import show, curdoc
from bokeh.models import Slider, RangeSlider, InlineStyleSheet
from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.io import show, curdoc
from bokeh.models import Slider, RangeSlider, InlineStyleSheet
from bokeh.layouts import column, row

# ============================================================================
# LIGHT STYLES - 3 Beautiful Options
# ============================================================================

# LIGHT 1: Modern Gradient (Indigo/Purple/Pink)
slider_light_modern = InlineStyleSheet(css="""
:host {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
  border-radius: 16px !important;
  padding: 16px !important;
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12), 
              0 2px 8px rgba(99, 102, 241, 0.08) !important;
  border: 1px solid rgba(99, 102, 241, 0.15) !important;
}

:host .bk-slider-title {
  color: #4f46e5 !important;
  font-size: 1.15em !important;
  font-weight: 700 !important;
  letter-spacing: 0.5px !important;
  font-family: 'Inter', 'SF Pro Display', -apple-system, sans-serif !important;
  margin-bottom: 12px !important;
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

:host .noUi-base, :host .noUi-target {
  background: linear-gradient(135deg, #e0e7ff 0%, #ddd6fe 100%) !important;
  border: 2px solid rgba(139, 92, 246, 0.2) !important;
  border-radius: 12px !important;
  box-shadow: inset 0 2px 4px rgba(139, 92, 246, 0.1);
  height: 12px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    #6366f1 0%, #8b5cf6 35%, #ec4899 70%, #f59e0b 100%
  ) !important;
  box-shadow: 0 2px 12px rgba(139, 92, 246, 0.4),
              0 0 20px rgba(236, 72, 153, 0.2);
  border-radius: 12px !important;
}

:host .noUi-handle {
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%) !important;
  border: 3px solid #6366f1 !important;
  border-radius: 50%;
  width: 28px;
  height: 28px;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #8b5cf6 !important;
  box-shadow: 0 6px 16px rgba(139, 92, 246, 0.4);
  transform: scale(1.1);
  background: linear-gradient(135deg, #fef3c7 0%, #fce7f3 100%) !important;
}

:host .noUi-tooltip {
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
  color: #ffffff !important;
  font-family: 'SF Mono', 'Consolas', monospace;
  font-weight: 600;
  border-radius: 8px;
  padding: 6px 12px;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}
""")

# LIGHT 2: Warm Sunset (Orange/Coral)
slider_light_sunset = InlineStyleSheet(css="""
:host {
  background: linear-gradient(135deg, #fefefe 0%, #fff7ed 100%) !important;
  border-radius: 20px !important;
  padding: 18px !important;
  box-shadow: 0 8px 32px rgba(251, 146, 60, 0.1) !important;
  border: 2px solid rgba(251, 146, 60, 0.15) !important;
}

:host .bk-slider-title {
  color: #ea580c !important;
  font-size: 1.2em !important;
  font-weight: 700 !important;
  font-family: 'Poppins', 'Avenir', sans-serif !important;
  margin-bottom: 14px !important;
  background: linear-gradient(135deg, #ea580c 0%, #f59e0b 50%, #fbbf24 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

:host .noUi-base, :host .noUi-target {
  background: linear-gradient(135deg, #fed7aa 0%, #fef3c7 100%) !important;
  border: 2px solid rgba(251, 146, 60, 0.25) !important;
  border-radius: 14px !important;
  height: 14px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    #fb923c 0%, #f59e0b 33%, #fbbf24 66%, #fcd34d 100%
  ) !important;
  box-shadow: 0 3px 12px rgba(251, 146, 60, 0.35);
  border-radius: 14px !important;
}

:host .noUi-handle {
  background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%) !important;
  border: 3px solid #fb923c !important;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  box-shadow: 0 4px 12px rgba(251, 146, 60, 0.25);
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #ea580c !important;
  box-shadow: 0 6px 18px rgba(234, 88, 12, 0.35);
  transform: scale(1.15);
}

:host .noUi-tooltip {
  background: linear-gradient(135deg, #fb923c 0%, #f59e0b 100%) !important;
  color: #ffffff !important;
  font-weight: 700;
  border-radius: 10px;
  padding: 7px 14px;
  box-shadow: 0 4px 12px rgba(251, 146, 60, 0.3);
}
""")

# LIGHT 3: Fresh Mint (Green/Emerald)
slider_light_mint = InlineStyleSheet(css="""
:host {
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%) !important;
  border-radius: 18px !important;
  padding: 16px !important;
  box-shadow: 0 10px 30px rgba(16, 185, 129, 0.12) !important;
  border: 2px solid rgba(16, 185, 129, 0.2) !important;
}

:host .bk-slider-title {
  color: #059669 !important;
  font-size: 1.18em !important;
  font-weight: 700 !important;
  font-family: 'Roboto', 'Helvetica Neue', sans-serif !important;
  margin-bottom: 12px !important;
  background: linear-gradient(135deg, #059669 0%, #10b981 50%, #34d399 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

:host .noUi-base, :host .noUi-target {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%) !important;
  border: 2px solid rgba(16, 185, 129, 0.25) !important;
  border-radius: 13px !important;
  height: 13px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    #10b981 0%, #34d399 50%, #6ee7b7 100%
  ) !important;
  box-shadow: 0 3px 14px rgba(16, 185, 129, 0.35);
  border-radius: 13px !important;
}

:host .noUi-handle {
  background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%) !important;
  border: 3px solid #10b981 !important;
  border-radius: 50%;
  width: 29px;
  height: 29px;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #059669 !important;
  box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4);
  transform: scale(1.12);
}

:host .noUi-tooltip {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%) !important;
  color: #ffffff !important;
  font-weight: 600;
  border-radius: 9px;
  padding: 6px 13px;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
}
""")

# ============================================================================
# DARK STYLES - 3 Beautiful Options
# ============================================================================

# DARK 1: Neon Cyber (Cyan/Purple)
slider_dark_cyber = InlineStyleSheet(css="""
:host {
  background: #16161e !important;
  border-radius: 12px !important;
  padding: 14px !important;
  box-shadow: 0 4px 16px #0006 !important;
  border: 1px solid #2a2a3c !important;
}

:host .bk-slider-title {
  color: #00ffe0 !important;
  font-size: 1.2em !important;
  font-weight: bold !important;
  letter-spacing: 1px !important;
  font-family: 'Fira Code', 'Consolas', monospace !important;
  margin-bottom: 14px !important;
  text-shadow: 0 2px 12px #00ffe099;
}

:host .noUi-base, :host .noUi-target {
  background: #23233c !important;
  border: 2px solid #2a3132 !important;
  border-radius: 12px !important;
  height: 14px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, #00ffe0 10%, #d810f7 90%) !important;
  box-shadow: 0 0 16px #00ffe099, 0 0 8px #d810f799;
  border-radius: 12px !important;
}

:host .noUi-handle {
  background: #1a1a24 !important;
  border: 3px solid #00ffe0 !important;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  box-shadow: 0 0 12px #00ffe0aa;
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #ff2a68 !important;
  box-shadow: 0 0 16px #ff2a68cc;
  transform: scale(1.1);
}

:host .noUi-tooltip {
  background: #1a1a24 !important;
  color: #00ffe0 !important;
  font-family: 'Consolas', monospace;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid #00ffe0;
  padding: 6px 12px;
  box-shadow: 0 0 12px #00ffe066;
}
""")

# DARK 2: Deep Ocean (Blue/Teal)
slider_dark_ocean = InlineStyleSheet(css="""
:host {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
  border-radius: 16px !important;
  padding: 16px !important;
  box-shadow: 0 8px 24px rgba(14, 165, 233, 0.15) !important;
  border: 1px solid rgba(14, 165, 233, 0.25) !important;
}

:host .bk-slider-title {
  color: #0ea5e9 !important;
  font-size: 1.2em !important;
  font-weight: 700 !important;
  font-family: 'Inter', sans-serif !important;
  margin-bottom: 14px !important;
  text-shadow: 0 2px 12px rgba(14, 165, 233, 0.5);
  background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

:host .noUi-base, :host .noUi-target {
  background: linear-gradient(135deg, #1e3a5f 0%, #1e4d6b 100%) !important;
  border: 2px solid rgba(14, 165, 233, 0.3) !important;
  border-radius: 14px !important;
  height: 13px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    #0ea5e9 0%, #06b6d4 50%, #22d3ee 100%
  ) !important;
  box-shadow: 0 0 20px rgba(14, 165, 233, 0.5);
  border-radius: 14px !important;
}

:host .noUi-handle {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
  border: 3px solid #0ea5e9 !important;
  border-radius: 50%;
  width: 29px;
  height: 29px;
  box-shadow: 0 0 16px rgba(14, 165, 233, 0.6);
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #06b6d4 !important;
  box-shadow: 0 0 24px rgba(6, 182, 212, 0.7);
  transform: scale(1.12);
}

:host .noUi-tooltip {
  background: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 100%) !important;
  color: #ffffff !important;
  font-weight: 700;
  border-radius: 8px;
  padding: 6px 13px;
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4);
}
""")

# DARK 3: Hot Magma (Red/Orange)
slider_dark_magma = InlineStyleSheet(css="""
:host {
  background: linear-gradient(135deg, #1c1917 0%, #292524 100%) !important;
  border-radius: 15px !important;
  padding: 15px !important;
  box-shadow: 0 8px 24px rgba(239, 68, 68, 0.2) !important;
  border: 1px solid rgba(239, 68, 68, 0.3) !important;
}

:host .bk-slider-title {
  color: #f97316 !important;
  font-size: 1.18em !important;
  font-weight: 700 !important;
  font-family: 'Poppins', sans-serif !important;
  margin-bottom: 13px !important;
  text-shadow: 0 2px 16px rgba(249, 115, 22, 0.6);
  background: linear-gradient(135deg, #ef4444 0%, #f97316 50%, #fb923c 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

:host .noUi-base, :host .noUi-target {
  background: linear-gradient(135deg, #3f1f1f 0%, #4a2424 100%) !important;
  border: 2px solid rgba(239, 68, 68, 0.35) !important;
  border-radius: 13px !important;
  height: 14px !important;
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    #ef4444 0%, #f97316 50%, #fb923c 100%
  ) !important;
  box-shadow: 0 0 18px rgba(239, 68, 68, 0.6), 
              0 0 10px rgba(249, 115, 22, 0.4);
  border-radius: 13px !important;
}

:host .noUi-handle {
  background: linear-gradient(135deg, #292524 0%, #3f3f46 100%) !important;
  border: 3px solid #f97316 !important;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  box-shadow: 0 0 14px rgba(249, 115, 22, 0.6);
  top: -8px !important;
}

:host .noUi-handle:hover {
  border-color: #ef4444 !important;
  box-shadow: 0 0 20px rgba(239, 68, 68, 0.8);
  transform: scale(1.1);
}

:host .noUi-tooltip {
  background: linear-gradient(135deg, #ef4444 0%, #f97316 100%) !important;
  color: #ffffff !important;
  font-weight: 700;
  border-radius: 9px;
  padding: 7px 13px;
  box-shadow: 0 4px 14px rgba(239, 68, 68, 0.4);
}
""")

# ============================================================================
# TRANSPARENT STYLE - Works on any background!
# ============================================================================

slider_transparent = InlineStyleSheet(css="""
:host {
  background: rgba(255, 255, 255, 0.08) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-radius: 16px !important;
  padding: 16px !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1),
              inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
  border: 1px solid rgba(255, 255, 255, 0.18) !important;
}

:host .bk-slider-title {
  color: rgba(255, 255, 255, 0.95) !important;
  font-size: 1.2em !important;
  font-weight: 700 !important;
  font-family: 'SF Pro Display', -apple-system, sans-serif !important;
  margin-bottom: 14px !important;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3),
               0 0 20px rgba(255, 255, 255, 0.2);
  letter-spacing: 0.5px !important;
}

:host .noUi-base, :host .noUi-target {
  background: rgba(0, 0, 0, 0.2) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 14px !important;
  height: 14px !important;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

:host .noUi-connect {
  background: linear-gradient(90deg, 
    rgba(255, 255, 255, 0.7) 0%, 
    rgba(255, 255, 255, 0.9) 100%
  ) !important;
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.3),
              0 2px 8px rgba(0, 0, 0, 0.2);
  border-radius: 14px !important;
}

:host .noUi-handle {
  background: rgba(255, 255, 255, 0.95) !important;
  border: 3px solid rgba(255, 255, 255, 0.4) !important;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25),
              0 0 12px rgba(255, 255, 255, 0.3);
  top: -8px !important;
  backdrop-filter: blur(8px);
}

:host .noUi-handle:hover {
  border-color: rgba(255, 255, 255, 0.8) !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3),
              0 0 20px rgba(255, 255, 255, 0.5);
  transform: scale(1.15);
  background: rgba(255, 255, 255, 1) !important;
}

:host .noUi-tooltip {
  background: rgba(0, 0, 0, 0.85) !important;
  backdrop-filter: blur(10px) !important;
  color: #ffffff !important;
  font-weight: 700;
  border-radius: 8px;
  padding: 7px 14px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}
""")




from bokeh.io import show, curdoc
from bokeh.models import Select, InlineStyleSheet
from bokeh.layouts import column, row

# ============================================================================
# LIGHT STYLE - Premium Modern Design
# ============================================================================
select_light = InlineStyleSheet(css="""
/* Widget container */
:host {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    border-radius: 16px !important;
    padding: 18px !important;
    box-shadow: 0 8px 32px rgba(99, 102, 241, 0.12), 
                0 2px 8px rgba(99, 102, 241, 0.08) !important;
    border: 1px solid rgba(99, 102, 241, 0.15) !important;
}

/* Title styling */
:host .bk-input-group label, :host .bk-select-title {
    color: #4f46e5 !important;
    font-size: 1.15em !important;
    font-family: 'Inter', 'SF Pro Display', -apple-system, sans-serif !important;
    font-weight: 700 !important;
    margin-bottom: 10px !important;
    letter-spacing: 0.3px !important;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block !important;
}

/* Dropdown select */
:host select {
    background: linear-gradient(135deg, #fafbff 0%, #f3f4f6 100%) !important;
    color: #1f2937 !important;
    border: 2px solid #c7d2fe !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 1.05em !important;
    font-weight: 500 !important;
    font-family: 'SF Pro Text', -apple-system, sans-serif !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 8px rgba(99, 102, 241, 0.08) !important;
    cursor: pointer !important;
    appearance: none !important;
    -webkit-appearance: none !important;
    -moz-appearance: none !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%234f46e5' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: right 12px center !important;
    background-size: 20px !important;
    padding-right: 42px !important;
}

/* Hover state */
:host select:hover {
    border-color: #8b5cf6 !important;
    box-shadow: 0 4px 16px rgba(139, 92, 246, 0.18),
                0 0 0 3px rgba(139, 92, 246, 0.08) !important;
    background: linear-gradient(135deg, #ffffff 0%, #faf5ff 100%) !important;
    transform: translateY(-1px);
}

/* Focus state */
:host select:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.15),
                0 4px 20px rgba(124, 58, 237, 0.25) !important;
    outline: none !important;
    background: #ffffff !important;
}

/* Options styling */
:host select option {
    background: #ffffff !important;
    color: #1f2937 !important;
    padding: 10px !important;
    font-weight: 500 !important;
}

:host select option:hover {
    background: #f3f4f6 !important;
}
""")




















from bokeh.io import show, curdoc
from bokeh.models import MultiChoice, InlineStyleSheet
from bokeh.layouts import column

multi_style = InlineStyleSheet(css="""
/* Outer widget container */
:host {
    background: #ffffff !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
}

/* Title styling */
:host .bk-input-group label, :host .bk-multichoice-title {
    color: #0891b2 !important;
    font-size: 1.18em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 10px !important;
    letter-spacing: 1px !important;
    text-shadow: 0 1px 2px rgba(8, 145, 178, 0.2);
}

/* The input field when closed */
:host .choices__inner {
    background: #f8fafc !important;
    color: #1e293b !important;
    border: 2px solid #0891b2 !important;
    border-radius: 8px !important;
    font-size: 1.05em !important;
    transition: border 0.1s, box-shadow 0.1s;
    box-shadow: none !important;
}

/* Glow on hover/focus of input */
:host .choices__inner:hover, :host .choices__inner:focus-within {
    border-color: #e11d48 !important;
    box-shadow: 0 0 0 2px rgba(225, 29, 72, 0.2), 0 0 16px rgba(225, 29, 72, 0.15) !important;
    outline: none !important;
}

/* Dropdown list */
:host .choices__list--dropdown {
    background: #ffffff !important;
    border: 1.5px solid #0891b2 !important;
    border-radius: 8px !important;
    box-shadow: 0 10px 32px rgba(0, 0, 0, 0.12) !important;
}

/* Items in the dropdown */
:host .choices__item--choice {
    color: #1e293b !important;
    padding: 12px 16px !important;
    transition: all 0.15s;
    border-bottom: 1px solid rgba(226, 232, 240, 0.6) !important;
}

:host .choices__item--choice:hover {
    background: #0891b2 !important;
    color: #ffffff !important;
}

/* Active selected items in the box */
:host .choices__item--selectable {
    background: linear-gradient(90deg, #0891b2 20%, #06b6d4 100%) !important;
    color: #ffffff !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    margin: 2px 4px !important;
    padding: 6px 14px !important;
    box-shadow: 0 2px 8px rgba(8, 145, 178, 0.25);
}
""")





from bokeh.io import show, curdoc
from bokeh.models import MultiChoice, InlineStyleSheet
from bokeh.layouts import column

multi_style = InlineStyleSheet(css="""
/* Outer widget container */
:host {
    background: #181824 !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 20px #0008 !important;
}
/* Title styling */
:host .bk-input-group label, :host .bk-multichoice-title {
    color: #00ffe0 !important;
    font-size: 1.18em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 10px !important;
    letter-spacing: 1px !important;
    text-shadow: 0 2px 12px #00ffe088, 0 1px 4px #181824;
}
/* The input field when closed */
:host .choices__inner {
    background: #23233c !important;
    color: #f9fafb !important;
    border: 2px solid #06b6d4 !important;
    border-radius: 8px !important;
    font-size: 1.05em !important;
    transition: border 0.1s, box-shadow 0.1s;
    box-shadow: none !important;
}
/* Glow on hover/focus of input */
:host .choices__inner:hover, :host .choices__inner:focus-within {
    border-color: #ff3049 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 16px #ff3049cc !important;
    outline: none !important;
}
/* Dropdown list */
:host .choices__list--dropdown {
    background: #181824 !important;
    border: 1.5px solid #06b6d4 !important;
    border-radius: 8px !important;
    box-shadow: 0 10px 32px #000c !important;
}
/* Items in the dropdown */
:host .choices__item--choice {
    color: #f9fafb !important;
    padding: 12px 16px !important;
    transition: all 0.15s;
    border-bottom: 1px solid #28284666 !important;
}
:host .choices__item--choice:hover {
    background: #8b5cf6 !important;
    color: #1f2937 !important;
}
/* Active selected items in the box */
:host .choices__item--selectable {
    background: linear-gradient(90deg, #ffb028 20%, #ff4f4f 100%) !important;
    color: #181824 !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    margin: 2px 4px !important;
    padding: 6px 14px !important;
    box-shadow: 0 1px 6px #0005;
}
""")










from bokeh.io import show, curdoc
from bokeh.models import TextInput, InlineStyleSheet
from bokeh.layouts import column

textinput_css = InlineStyleSheet(css="""
/* Outer container styling */
:host {
    background: #181824 !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 18px #0006 !important;
}
/* Title label styling */
:host .bk-input-group label, :host .bk-textinput-title {
    color: #34ffe0 !important;
    font-size: 1.14em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 12px !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 2px 12px #34ffe077, 0 1px 3px #222;
}
/* The input box */
:host input[type="text"] {
    background: #23233c !important;
    color: #f9fafb !important;
    border: 2px solid #06b6d4 !important;
    border-radius: 8px !important;
    padding: 11px 15px !important;
    font-size: 1.08em !important;
    transition: border 0.12s, box-shadow 0.12s;
    box-shadow: none !important;
}
/* On hover/focus: red border with glowing effect */
:host input[type="text"]:hover,
:host input[type="text"]:focus {
    border-color: #ff3049 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 15px #ff3049bb !important;
    outline: none !important;
}
/* Placeholder text */
:host input[type="text"]::placeholder {
    color: #9ca3af !important;
    opacity: 0.7 !important;
    font-style: italic !important;
}
""")



from bokeh.io import show, curdoc
from bokeh.models import TextInput, InlineStyleSheet
from bokeh.layouts import column

textinput_css = InlineStyleSheet(css="""
/* Outer container styling */
:host {
    background: #ffffff !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08) !important;
}

/* Title label styling */
:host .bk-input-group label, :host .bk-textinput-title {
    color: #0891b2 !important;
    font-size: 1.14em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 12px !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 1px 2px rgba(8, 145, 178, 0.2);
}

/* The input box */
:host input[type="text"] {
    background: #f8fafc !important;
    color: #1e293b !important;
    border: 2px solid #0891b2 !important;
    border-radius: 8px !important;
    padding: 11px 15px !important;
    font-size: 1.08em !important;
    transition: border 0.12s, box-shadow 0.12s;
    box-shadow: none !important;
}

/* On hover/focus: rose border with glowing effect */
:host input[type="text"]:hover,
:host input[type="text"]:focus {
    border-color: #e11d48 !important;
    box-shadow: 0 0 0 2px rgba(225, 29, 72, 0.2), 0 0 15px rgba(225, 29, 72, 0.15) !important;
    outline: none !important;
}

/* Placeholder text */
:host input[type="text"]::placeholder {
    color: #64748b !important;
    opacity: 0.7 !important;
    font-style: italic !important;
}
""")









from bokeh.io import show
from bokeh.models import Button, InlineStyleSheet
# Common CSS variables for consistent theming
base_variables = """
:host {
    /* CSS Custom Properties for easy theming */
    --primary-color: #8b5cf6;
    --secondary-color: #06b6d4;
    --background-color: #1f2937;
    --surface-color: #343838;
    --text-color: #f9fafb;
    --accent-color: #f59e0b;
    --danger-color: #ef4444;
    --success-color: #10b981;
    --border-color: #4b5563;
    --hover-color: #6366f1;
    
    background: none !important;
}
"""
button_style = InlineStyleSheet(css=base_variables + """
:host button {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)) !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
}

:host button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    background: linear-gradient(135deg, var(--hover-color), var(--primary-color)) !important;
}

:host button:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
}

:host button:disabled {
    background: #6b7280 !important;
    cursor: not-allowed !important;
    transform: none !important;
    box-shadow: none !important;
}
""")






from bokeh.io import show
from bokeh.models import CheckboxGroup, InlineStyleSheet

# Common CSS variables for consistent theming
base_variables = """
:host {
    /* CSS Custom Properties for easy theming */
    --primary-color: #8b5cf6;
    --secondary-color: #06b6d4;
    --background-color: #1f2937;
    --surface-color: #343838;
    --text-color: #f9fafb;
    --accent-color: #f59e0b;
    --danger-color: #ef4444;
    --success-color: #10b981;
    --border-color: #4b5563;
    --hover-color: #6366f1;
    
    background: none !important;
}
"""
checkbox_style = InlineStyleSheet(css=base_variables + """
:host .bk-input-group {
    background: var(--surface-color) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 6px !important;
    padding: 8px !important;
}

:host input[type="checkbox"] {
    appearance: none !important;
    width: 18px !important;
    height: 18px !important;
    border: 2px solid var(--border-color) !important;
    border-radius: 3px !important;
    background: var(--surface-color) !important;
    cursor: pointer !important;
    position: relative !important;
    margin-right: 8px !important;
}

:host input[type="checkbox"]:checked {
    background: var(--primary-color) !important;
    border-color: var(--primary-color) !important;
}

:host input[type="checkbox"]:checked::after {
    content: "✓" !important;
    position: absolute !important;
    top: -2px !important;
    left: 2px !important;
    color: white !important;
    font-size: 12px !important;
    font-weight: bold !important;
}

:host label {
    color: var(--text-color) !important;
    cursor: pointer !important;
    font-size: 14px !important;
    display: flex !important;
    align-items: center !important;
    margin-bottom: 6px !important;
}
""")




from bokeh.io import show
from bokeh.models import RadioButtonGroup, InlineStyleSheet
from bokeh.layouts import column

radio_btn_css = InlineStyleSheet(css="""
/* Outer container */
:host {
    background: #181824 !important;
    border-radius: 16px !important;
    padding: 22px 22px 18px 22px !important;
    box-shadow: 0 4px 18px #0008 !important;
    max-width: 600px !important;
}
/* Title */
:host .bk-input-group label, :host .bk-radiobuttongroup-title {
    color: #f59e0b !important;
    font-size: 1.16em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold !important;
    margin-bottom: 16px !important;
    text-shadow: 0 2px 10px #f59e0b99;
    letter-spacing: 0.5px;
}
/* Button group: wrap on small screens */
:host .bk-btn-group {
    display: flex !important;
    gap: 18px !important;
    flex-wrap: wrap !important;
    justify-content: flex-start;
    margin-bottom: 6px;
}
/* Each radio button - pill shape, full text, no ellipsis */
:host button.bk-btn {
    background: #23233c !important;
    color: #f9fafb !important;
    border: 2.5px solid #f59e0b !important;
    border-radius: 999px !important;
    padding: 0.7em 2.2em !important;
    min-width: 120px !important;
    font-size: 1.09em !important;
    font-family: 'Fira Code', monospace;
    font-weight: 600 !important;
    transition: border 0.13s, box-shadow 0.14s, color 0.12s, background 0.13s;
    box-shadow: 0 2px 10px #0002 !important;
    cursor: pointer !important;
    outline: none !important;
    white-space: nowrap !important;
    overflow: visible !important;
    text-overflow: unset !important;
}
/* Orange glow on hover */
:host button.bk-btn:hover:not(.bk-active) {
    border-color: #ffa733 !important;
    color: #ffa733 !important;
    box-shadow: 0 0 0 2px #ffa73399, 0 0 13px #ffa73388 !important;
    background: #2e2937 !important;
}
/* Red glow on active/focus */
:host button.bk-btn:focus, :host button.bk-btn.bk-active {
    border-color: #ff3049 !important;
    color: #ff3049 !important;
    background: #322d36 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 19px #ff304988 !important;
}
/* Remove focus outline */
:host button.bk-btn:focus {
    outline: none !important;
}
""")




from bokeh.io import show
from bokeh.models import FileInput, InlineStyleSheet
base_variables = """
:host {
    /* CSS Custom Properties for easy theming */
    --primary-color: #8b5cf6;
    --secondary-color: #06b6d4;
    --background-color: #1f2937;
    --surface-color: #343838;
    --text-color: #f9fafb;
    --accent-color: #f59e0b;
    --danger-color: #ef4444;
    --success-color: #10b981;
    --border-color: #4b5563;
    --hover-color: #6366f1;
    
    background: none !important;
}
"""
file_input_style_dark = InlineStyleSheet(css=base_variables + """
:host input[type="file"] {
    background: var(--surface-color) !important;
    color: var(--text-color) !important;
    border: 2px dashed var(--border-color) !important;
    border-radius: 6px !important;
    padding: 20px !important;
    font-size: 14px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

:host input[type="file"]:hover {
    border-color: var(--primary-color) !important;
    background: rgba(139, 92, 246, 0.05) !important;
}

:host input[type="file"]::file-selector-button {
    background: var(--primary-color) !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 8px 16px !important;
    margin-right: 12px !important;
    cursor: pointer !important;
    font-weight: 600 !important;
}
""")



from bokeh.io import show
from bokeh.models import FileInput, InlineStyleSheet
base_variables98 = """
:host {
    /* CSS Custom Properties for easy theming */
    --primary-color: #0891b2;
    --secondary-color: #06b6d4;
    --background-color: #ffffff;
    --surface-color: #f8fafc;
    --text-color: #1e293b;
    --accent-color: #f59e0b;
    --danger-color: #ef4444;
    --success-color: #10b981;
    --border-color: #e2e8f0;
    --hover-color: #0e7490;
    
    background: none !important;
}
"""
file_input_style_light = InlineStyleSheet(css=base_variables98 + """
:host input[type="file"] {
    background: var(--surface-color) !important;
    color: var(--text-color) !important;
    border: 2px dashed var(--border-color) !important;
    border-radius: 6px !important;
    padding: 20px !important;
    font-size: 14px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

:host input[type="file"]:hover {
    border-color: var(--primary-color) !important;
    background: rgba(139, 92, 246, 0.05) !important;
}

:host input[type="file"]::file-selector-button {
    background: var(--primary-color) !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 8px 16px !important;
    margin-right: 12px !important;
    cursor: pointer !important;
    font-weight: 600 !important;
}
""")


from bokeh.io import show
from bokeh.models import RadioGroup, InlineStyleSheet
from bokeh.layouts import column

radio_css = InlineStyleSheet(css="""
/* Outer box */
:host {
    background: #181824 !important;
    border-radius: 14px !important;
    padding: 18px !important;
    box-shadow: 0 4px 18px #0007 !important;
}
/* Title (if used) */
:host .bk-input-group label, :host .bk-radiogroup-title {
    color: #f59e0b !important;
    font-size: 1.12em !important;
    font-family: 'Fira Code', monospace;
    font-weight: bold;
    margin-bottom: 11px;
    text-shadow: 0 2px 10px #f59e0b77;
}
/* Radio group styling */
:host .bk-input-group {
    background: #23233c !important;
    border-radius: 8px !important;
    padding: 10px 4px !important;
    border: 2px solid #f59e0b !important;
}
/* Each radio button */
:host input[type="radio"] {
    appearance: none !important;
    background: #23233c !important;
    border: 2px solid #f59e0b !important;
    border-radius: 50% !important;
    width: 19px !important;
    height: 19px !important;
    margin-right: 10px !important;
    vertical-align: middle;
    transition: border 0.12s, box-shadow 0.12s;
    box-shadow: none !important;
}
/* Glow on hover */
:host input[type="radio"]:hover {
    border-color: #ffa733 !important;
    box-shadow: 0 0 0 2px #ffa73399, 0 0 11px #ffa733bb !important;
}
:host input[type="radio"]:focus {
    border-color: #ff3049 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 13px #ff3049cc !important;
    outline: none !important;
}
/* Checked state */
:host input[type="radio"]:checked {
    border-color: #ff3049 !important;
    background: #f59e0b !important;
}
:host input[type="radio"]:checked::after {
    content: "";
    display: block;
    width: 9px;
    height: 9px;
    margin: 3px auto;
    border-radius: 50%;
    background: #ff3049 !important;
}
/* Label styling */
:host label {
    color: #f9fafb !important;
    font-family: 'Fira Code', monospace;
    font-size: 1.04em;
    margin-bottom: 4px;
    vertical-align: middle;
    cursor: pointer;
}
""")








from bokeh.models import TextAreaInput, InlineStyleSheet
from bokeh.io import show
# Updated stylesheet for TextAreaInput
tais = InlineStyleSheet(css="""
/* Outer container styling */
:host {
    background: #181824 !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 18px #0006 !important;
}

/* Title label styling */
:host .bk-input-group label, 
:host .bk-textinput-title {
    color: #34ffe0 !important;
    font-size: 1.14em !important;
    font-family: 'Fira Code', monospace !important;
    font-weight: bold !important;
    margin-bottom: 12px !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 2px 12px #34ffe077, 0 1px 3px #222 !important;
}

/* The textarea input box - changed from input[type="text"] to textarea */
:host textarea {
    background: #23233c !important;
    color: #f9fafb !important;
    border: 2px solid #06b6d4 !important;
    border-radius: 8px !important;
    padding: 11px 15px !important;
    font-size: 1.08em !important;
    font-family: 'Fira Code', monospace !important;
    transition: border 0.12s ease, box-shadow 0.12s ease !important;
    box-shadow: none !important;
    resize: vertical !important;
    min-height: 120px !important;
}

/* On hover/focus: red border with glowing effect */
:host textarea:hover,
:host textarea:focus {
    border-color: #ff3049 !important;
    box-shadow: 0 0 0 2px #ff304999, 0 0 15px #ff3049bb !important;
    outline: none !important;
}

/* Placeholder text */
:host textarea::placeholder {
    color: #9ca3af !important;
    opacity: 0.7 !important;
    font-style: italic !important;
}

/* Scrollbar styling for webkit browsers */
:host textarea::-webkit-scrollbar {
    width: 8px !important;
}

:host textarea::-webkit-scrollbar-track {
    background: #1a1a2e !important;
    border-radius: 4px !important;
}

:host textarea::-webkit-scrollbar-thumb {
    background: #06b6d4 !important;
    border-radius: 4px !important;
}

:host textarea::-webkit-scrollbar-thumb:hover {
    background: #ff3049 !important;
}
""")




from bokeh.models import TextAreaInput, InlineStyleSheet
from bokeh.io import show

# Updated stylesheet for TextAreaInput - Light Theme
tais_light = InlineStyleSheet(css="""
/* Outer container styling */
:host {
    background: #ffffff !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08) !important;
}

/* Title label styling */
:host .bk-input-group label, 
:host .bk-textinput-title {
    color: #0891b2 !important;
    font-size: 1.14em !important;
    font-family: 'Fira Code', monospace !important;
    font-weight: bold !important;
    margin-bottom: 12px !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 1px 2px rgba(8, 145, 178, 0.2) !important;
}

/* The textarea input box - changed from input[type="text"] to textarea */
:host textarea {
    background: #f8fafc !important;
    color: #1e293b !important;
    border: 2px solid #0891b2 !important;
    border-radius: 8px !important;
    padding: 11px 15px !important;
    font-size: 1.08em !important;
    font-family: 'Fira Code', monospace !important;
    transition: border 0.12s ease, box-shadow 0.12s ease !important;
    box-shadow: none !important;
    resize: vertical !important;
    min-height: 120px !important;
}

/* On hover/focus: rose border with glowing effect */
:host textarea:hover,
:host textarea:focus {
    border-color: #e11d48 !important;
    box-shadow: 0 0 0 2px rgba(225, 29, 72, 0.2), 0 0 15px rgba(225, 29, 72, 0.15) !important;
    outline: none !important;
}

/* Placeholder text */
:host textarea::placeholder {
    color: #64748b !important;
    opacity: 0.7 !important;
    font-style: italic !important;
}

/* Scrollbar styling for webkit browsers */
:host textarea::-webkit-scrollbar {
    width: 8px !important;
}

:host textarea::-webkit-scrollbar-track {
    background: #e2e8f0 !important;
    border-radius: 4px !important;
}

:host textarea::-webkit-scrollbar-thumb {
    background: #0891b2 !important;
    border-radius: 4px !important;
}

:host textarea::-webkit-scrollbar-thumb:hover {
    background: #e11d48 !important;
}
""")



# --- Your InlineStyleSheet for beautiful tabs ---
tabs_style = InlineStyleSheet(css="""
/* Main tabs container */
:host {
    background: #2d2d2d !important;
    border-radius: 14px !important;
    padding: 8px !important;
    margin: 10px !important;
    box-shadow: 0 6px 20px #00ffe055, 0 2px 10px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid rgba(0, 191, 255, 0.3) !important;
}
/* Tab navigation bar */
:host .bk-tabs-header {
    background: transparent !important;
    border-bottom: 2px solid #00bfff !important;
    margin-bottom: 8px !important;
}
/* Individual tab buttons */
:host .bk-tab {
    background: linear-gradient(135deg, #2d2d2d 0%, #3a3a3a 100%) !important;
    color: #00bfff !important;
    border: 1px solid #555 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 12px 20px !important;
    margin-right: 4px !important;
    font-family: 'Arial', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95em !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    overflow: hidden !important;
}
/* Tab hover effect */
:host .bk-tab:hover {
    background: linear-gradient(135deg, #dc1cdd 0%, #ff1493 100%) !important;
    color: #ffffff !important;
    border-color: #dc1cdd !important;
    box-shadow: 0 4px 15px rgba(220, 28, 221, 0.5) !important;
    transform: translateY(-2px) !important;
}
/* Active tab styling */
:host .bk-tab.bk-active {
    background: linear-gradient(135deg, #00bfff 0%, #0080ff 100%) !important;
    color: #000000 !important;
    border-color: #00bfff !important;
    box-shadow: 0 4px 20px rgba(0, 191, 255, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.3) !important;
    transform: translateY(-1px) !important;
    font-weight: 700 !important;
}
/* Active tab glow effect */
:host .bk-tab.bk-active::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 50%, transparent 70%) !important;
    animation: shimmer 2s infinite !important;
}
@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
/* Tab content area */
:host .bk-tab-content {
    background: transparent !important;
    padding: 16px !important;
    border-radius: 0 0 10px 10px !important;
}
/* Focus states for accessibility */
:host .bk-tab:focus {
    outline: 2px solid #00bfff !important;
    outline-offset: 2px !important;
}
/* Disabled tab state */
:host .bk-tab:disabled {
    background: #1a1a1a !important;
    color: #666 !important;
    cursor: not-allowed !important;
    opacity: 0.5 !important;
}
""")






def create_gradient_masked_plot(
    x_data=None,
    y_data=None,
    gradient_colors=None,
    gradient_direction="to bottom",
    mask_color="#ffffff",
    line_color="#000000",
    line_width=4,
    title="Gradient Masked Plot",
    width=800,
    height=600,
    border_color=None,
    grid_color=None,
    grid_alpha=0.2,
    title_color=None,
    axis_label_color=None,
    tick_label_color=None,
    add_hover=True
):
    """
    Create a Bokeh plot with gradient background masked by areas around a line.
    
    Parameters:
    -----------
    x_data : array-like, optional
        X-axis data. If None, generates sinusoidal data.
    y_data : array-like, optional
        Y-axis data. If None, generates sinusoidal data.
    gradient_colors : list of str, optional
        List of color stops for gradient (e.g., ["#ff0000 0%", "#00ff00 50%", "#0000ff 100%"])
        If None, uses default gradient.
    gradient_direction : str, default "to bottom"
        CSS gradient direction ("to bottom", "to right", "45deg", etc.)
    mask_color : str, default "#ffffff"
        Color for the masking areas
    line_color : str, default "#000000"
        Color of the main line
    line_width : int, default 4
        Width of the main line
    title : str, default "Gradient Masked Plot"
        Plot title
    width : int, default 800
        Plot width in pixels
    height : int, default 600
        Plot height in pixels
    border_color : str, optional
        Border fill color. If None, uses mask_color with slight adjustment
    grid_color : str, optional
        Grid line color. If None, derives from mask_color
    grid_alpha : float, default 0.2
        Grid line transparency
    title_color : str, optional
        Title text color. If None, uses line_color
    axis_label_color : str, optional
        Axis label color. If None, uses line_color
    tick_label_color : str, optional
        Tick label color. If None, uses line_color
    add_hover : bool, default True
        Whether to add hover tooltips
    
    Returns:
    --------
    bokeh.layouts.Column
        A column layout containing the styled plot
    """
    
    # Generate default data if not provided
    if x_data is None or y_data is None:
        x_data = np.linspace(0, 4 * np.pi, 100)
        y_data = np.sin(x_data) * 2 - 1
    
    # Create data source
    source = ColumnDataSource(data=dict(x=x_data, y=y_data))
    
    # Calculate masking boundaries
    max_y = np.max(y_data) * 100
    min_x = np.min(x_data)
    max_x = np.max(x_data)
    
    # Create figure
    p = figure(
        width=width,
        height=height,
        title=title,
        x_axis_label="X",
        y_axis_label="Y",
        y_range=(np.min(y_data) - np.abs(np.min(y_data))/2, 
                 np.max(y_data) + np.abs(np.max(y_data))/2),
        x_range=(min_x, max_x)
    )
    
    # Create masking areas
    # Area above the line
    p.varea(
        x=x_data,
        y1=y_data,
        y2=max_y,
        fill_color=mask_color,
        fill_alpha=0.97,
    )
    
    # Area before the data starts (left side)
    p.varea(
        x=np.linspace(-100, min_x, 100),
        y1=-max_y,
        y2=max_y,
        fill_color=mask_color,
        fill_alpha=0.97,
    )
    
    # Area after the data ends (right side)
    p.varea(
        x=np.linspace(max_x, max_x + 100, 100),
        y1=-max_y,
        y2=max_y,
        fill_color=mask_color,
        fill_alpha=0.97,
    )
    
    # Draw the main line on top
    p.line(
        x='x',
        y='y',
        source=source,
        line_color=line_color,
        line_width=line_width,
        line_alpha=1.0,
        name="main_line"
    )
    
    # Add hover tool if requested
    if add_hover:
        hover = HoverTool(
            tooltips=[
                ("X", "@x{0.00}"),
                ("Y", "@y{0.00}")
            ],
            mode='vline',
            renderers=[p.select(name="main_line")[0]]
        )
        p.add_tools(hover)
    
    # Apply styling
    p.background_fill_color = None
    p.border_fill_color = border_color if border_color else mask_color
    p.outline_line_color = grid_color if grid_color else mask_color
    p.grid.grid_line_color = grid_color if grid_color else mask_color
    p.grid.grid_line_alpha = grid_alpha
    
    p.title.text_font_size = "16pt"
    p.title.text_color = title_color if title_color else line_color
    
    p.xaxis.axis_label_text_color = axis_label_color if axis_label_color else line_color
    p.yaxis.axis_label_text_color = axis_label_color if axis_label_color else line_color
    
    p.xaxis.major_label_text_color = tick_label_color if tick_label_color else line_color
    p.yaxis.major_label_text_color = tick_label_color if tick_label_color else line_color
    
    # Create gradient CSS
    if gradient_colors is None:
        gradient_colors = ["#1de9b6 0%", "#b2ff59 50%", "#ffd600 100%"]
    
    gradient_stops = ", ".join(gradient_colors)
    
    gradient_css = InlineStyleSheet(css=f"""
    :host {{
        background: linear-gradient({gradient_direction}, {gradient_stops});
    }}
    """)
    
    return column(p, stylesheets=[gradient_css])





import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, InlineStyleSheet, FixedTicker
from bokeh.layouts import column
import matplotlib.cm as cm


def create_gradient_bar_chart(
    categories,
    values,
    orientation="vertical",
    colormap="plasma",
    custom_colors=None,
    title="Gradient Bar Chart",
    width=600,
    height=400,
    bar_thickness=0.8,
    gradient_resolution=100,
    background_gradient=None,
    theme="dark",
    hover_template=None,
    show_grid=True,
    grid_alpha=0.3
):
    """
    Create a Bokeh bar chart with gradient-filled bars.
    
    Parameters:
    -----------
    categories : list
        Category labels for each bar
    values : list or array
        Numerical values for each bar
    orientation : str, default "vertical"
        Bar orientation: "vertical" or "horizontal"
    colormap : str, default "plasma"
        Matplotlib colormap name (e.g., 'viridis', 'plasma', 'rainbow', 'coolwarm')
    custom_colors : list of lists, optional
        Custom color stops as RGB values [[R,G,B], [R,G,B], ...]
        Example: [[0,255,255], [255,255,0], [255,0,0]] for cyan->yellow->red
    title : str, default "Gradient Bar Chart"
        Chart title
    width : int, default 600
        Chart width in pixels
    height : int, default 400
        Chart height in pixels
    bar_thickness : float, default 0.8
        Bar width/height as fraction of spacing
    gradient_resolution : int, default 100
        Resolution of gradient (higher = smoother)
    background_gradient : str, optional
        CSS gradient for background (e.g., "radial-gradient(circle, #263238 0%, #000 100%)")
    theme : str, default "dark"
        Color theme: "dark" or "light"
    hover_template : str, optional
        Custom hover tooltip template. Use {cat} and {val} as placeholders.
    show_grid : bool, default True
        Whether to show grid lines
    grid_alpha : float, default 0.3
        Grid line transparency
    
    Returns:
    --------
    bokeh.layouts.Column
        A column layout containing the styled bar chart
    """
    
    num_bars = len(values)
    max_val = max(values)
    numeric_positions = np.arange(num_bars)
    
    # Custom gradient function
    def custom_gradient(gradient_vals, color_stops):
        positions = np.linspace(0, 1, len(color_stops))
        reds = np.interp(gradient_vals, positions, color_stops[:, 0])
        greens = np.interp(gradient_vals, positions, color_stops[:, 1])
        blues = np.interp(gradient_vals, positions, color_stops[:, 2])
        return np.stack([reds, greens, blues], axis=1).astype(np.uint8)
    
    # Create figure based on orientation
    if orientation == "vertical":
        p = figure(
            width=width, height=height,
            x_range=(-0.5, num_bars - 0.5),
            y_range=(0, max_val + max_val * 0.1),
            title=title,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            toolbar_location="right"
        )
    else:  # horizontal
        p = figure(
            width=width, height=height,
            y_range=(-0.5, num_bars - 0.5),
            x_range=(0, max_val + max_val * 0.1),
            title=title,
            tools="pan,wheel_zoom,box_zoom,reset,save",
            toolbar_location="right"
        )
    
    # Generate gradient images for each bar
    rgba_images = []
    for val in values:
        frac = val / max_val
        
        if orientation == "vertical":
            h_px = max(1, int(frac * gradient_resolution))
            gradient_vals = np.linspace(0, frac, h_px)
            
            # Apply colormap or custom colors
            if custom_colors is not None:
                color_stops = np.array(custom_colors)
                colors = custom_gradient(gradient_vals, color_stops)
            else:
                colors = (cm.get_cmap(colormap)(gradient_vals)[:, :3] * 255).astype(np.uint8)
            
            # Create RGBA image
            rgba = np.zeros((gradient_resolution, 20, 4), dtype=np.uint8)
            if h_px > 0:
                rgba[:h_px, :, :3] = colors[:, None, :]
                rgba[:h_px, :, 3] = 255
            
            packed = rgba.view(dtype=np.uint32).reshape((gradient_resolution, 20))
            
        else:  # horizontal
            w_px = max(1, int(frac * gradient_resolution))
            gradient_vals = np.linspace(0, frac, w_px)
            
            # Apply colormap or custom colors
            if custom_colors is not None:
                color_stops = np.array(custom_colors)
                colors = custom_gradient(gradient_vals, color_stops)
            else:
                colors = (cm.get_cmap(colormap)(gradient_vals)[:, :3] * 255).astype(np.uint8)
            
            # Create RGBA image
            rgba = np.zeros((20, gradient_resolution, 4), dtype=np.uint8)
            if w_px > 0:
                rgba[:, :w_px, :3] = colors[None, :, :]
                rgba[:, :w_px, 3] = 255
            
            packed = rgba.view(dtype=np.uint32).reshape((20, gradient_resolution))
        
        rgba_images.append(packed)
    
    # Draw gradient bars
    if orientation == "vertical":
        dw = bar_thickness
        dh = max_val
        for i in range(num_bars):
            p.image_rgba(
                image=[rgba_images[i]],
                x=[i - dw / 2],
                y=[0],
                dw=dw,
                dh=dh
            )
    else:  # horizontal
        dw = max_val
        dh = bar_thickness
        for i in range(num_bars):
            p.image_rgba(
                image=[rgba_images[i]],
                x=[0],
                y=[i - dh / 2],
                dw=dw,
                dh=dh
            )
    
    # Create hover tooltip template
    if hover_template is None:
        hover_template = "Category: {cat} | Value: {val}"
    
    tooltips = [hover_template.replace("{cat}", cat).replace("{val}", str(val)) 
                for cat, val in zip(categories, values)]
    
    # Add invisible bars for hover interaction
    if orientation == "vertical":
        source = ColumnDataSource(data=dict(
            x=numeric_positions,
            top=values,
            tooltip=tooltips
        ))
        p.vbar(
            x='x', top='top', width=bar_thickness,
            source=source,
            fill_alpha=0, line_alpha=0,
            name="bars"
        )
        hover = HoverTool(tooltips="@tooltip", mode='vline', name="bars")
        p.xaxis.ticker = FixedTicker(ticks=list(numeric_positions))
        p.xaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}
    else:  # horizontal
        source = ColumnDataSource(data=dict(
            y=numeric_positions,
            right=values,
            tooltip=tooltips
        ))
        p.hbar(
            y='y', right='right', height=bar_thickness,
            source=source,
            fill_alpha=0, line_alpha=0,
            name="bars"
        )
        hover = HoverTool(tooltips="@tooltip", mode='hline', name="bars")
        p.yaxis.ticker = FixedTicker(ticks=list(numeric_positions))
        p.yaxis.major_label_overrides = {i: cat for i, cat in enumerate(categories)}
    
    p.add_tools(hover)
    
    # Apply theme
    if theme == "dark":
        text_color = "white"
        border_color = "#121212"
        outline_color = "#444"
        grid_color = "#333"
    else:  # light
        text_color = "#2c3e50"
        border_color = "#f8f9fa"
        outline_color = "#dee2e6"
        grid_color = "#e9ecef"
    
    # Styling
    p.title.text_color = text_color
    p.title.text_font_size = "16pt"
    p.xaxis.major_label_text_color = text_color
    p.yaxis.major_label_text_color = text_color
    p.xaxis.axis_line_color = text_color
    p.yaxis.axis_line_color = text_color
    p.xaxis.axis_label_text_color = text_color
    p.yaxis.axis_label_text_color = text_color
    
    p.background_fill_color = None
    p.border_fill_color = border_color
    p.outline_line_color = outline_color
    
    if show_grid:
        p.grid.grid_line_color = grid_color
        p.grid.grid_line_alpha = grid_alpha
    else:
        p.grid.grid_line_color = None
    
    # Apply background gradient
    if background_gradient is None:
        if theme == "dark":
            background_gradient = "radial-gradient(circle at center, #263238 0%, #000000 100%)"
        else:
            background_gradient = "linear-gradient(to bottom, #ffffff 0%, #f8f9fa 100%)"
    
    gradient_css = InlineStyleSheet(css=f"""
    :host {{
        background: {background_gradient};
    }}
    """)
    
    return column(p, stylesheets=[gradient_css])


import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import (
    ColumnDataSource, HoverTool, PolarTransform, 
    LinearColorMapper, ColorBar, InlineStyleSheet
)
from bokeh.layouts import column, row
from bokeh.palettes import Category20, Plasma256, Turbo256, Viridis256


def create_radar_chart(
    categories,
    series_data,
    series_names=None,
    colors=None,
    title="Radar Chart",
    width=700,
    height=700,
    fill_alpha=0.25,
    line_width=3,
    show_grid_labels=True,
    grid_levels=5,
    background_gradient=None,
    theme="dark",
    marker_size=10,
    show_markers=True,
    show_legend=True
):
    """
    Create an enhanced radar/spider chart with polar coordinates.
    
    Parameters:
    -----------
    categories : list
        Category labels for each axis
    series_data : list of lists
        Data for each series. Each inner list should match len(categories)
    series_names : list, optional
        Names for each series
    colors : list, optional
        Colors for each series
    title : str
        Chart title
    width, height : int
        Chart dimensions
    fill_alpha : float
        Fill transparency for areas
    line_width : int
        Width of series lines
    show_grid_labels : bool
        Whether to show radial grid labels
    grid_levels : int
        Number of circular grid lines
    background_gradient : str, optional
        CSS gradient for background
    theme : str
        "dark" or "light"
    marker_size : int
        Size of data point markers
    show_markers : bool
        Whether to show data point markers
    show_legend : bool
        Whether to show legend
    
    Returns:
    --------
    bokeh.layouts.Column
        Styled radar chart
    """
    
    n_variables = len(categories)
    n_series = len(series_data)
    
    # Calculate angles for each axis
    angles = np.linspace(0, 2*np.pi, n_variables, endpoint=False)
    
    # Close the polygon
    angles_closed = np.append(angles, angles[0])
    categories_closed = np.append(categories, categories[0])
    series_data_closed = [np.append(series, series[0]) for series in series_data]
    
    # Default series names
    if series_names is None:
        series_names = [f'Series {i+1}' for i in range(n_series)]
    
    # Default colors
    if colors is None:
        colors = Category20[20][:n_series] if n_series <= 20 else Turbo256[::256//n_series][:n_series]
    
    # Create polar transform
    polar_transform = PolarTransform()
    
    # Create figure
    plot_range = 1.5
    p = figure(
        width=width, 
        height=height, 
        title=title,
        x_range=(-plot_range, plot_range), 
        y_range=(-plot_range, plot_range),
        tools="pan,box_zoom,wheel_zoom,reset,save",
        match_aspect=True
    )
    
    # Draw circular grid lines
    radii = np.linspace(0.2, 1.0, grid_levels)
    for radius in radii:
        theta = np.linspace(0, 2*np.pi, 100)
        circle_source = ColumnDataSource(data=dict(
            radius=[radius]*100,
            angle=theta
        ))
        
        grid_color = "#444444" if theme == "dark" else "#cccccc"
        p.line(
            x=polar_transform.x, 
            y=polar_transform.y,
            line_color=grid_color, 
            line_alpha=0.3,
            line_width=1,
            source=circle_source
        )
        
        # Add radius labels
        if show_grid_labels:
            label_source = ColumnDataSource(data=dict(
                radius=[radius],
                angle=[np.pi/2],
                text=[f'{radius:.1f}']
            ))
            
            label_color = "#00ff88" if theme == "dark" else "#2c3e50"
            p.text(
                x=polar_transform.x, 
                y=polar_transform.y,
                text='text',
                source=label_source,
                text_color=label_color,
                text_alpha=0.7,
                text_font_size="10pt",
                text_align="center"
            )
    
    # Draw radial lines
    for angle in angles:
        radial_source = ColumnDataSource(data=dict(
            radius=[0, 1],
            angle=[angle, angle]
        ))
        
        grid_color = "#555555" if theme == "dark" else "#dddddd"
        p.line(
            x=polar_transform.x, 
            y=polar_transform.y,
            line_color=grid_color, 
            line_alpha=0.4,
            line_width=2,
            source=radial_source
        )
    
    # Plot each series
    scatter_renderers = []
    for i, (series, color, name) in enumerate(zip(series_data_closed, colors, series_names)):
        source = ColumnDataSource(data=dict(
            radius=series,
            angle=angles_closed,
            category=categories_closed,
            series=[name] * len(series)
        ))
        
        # Draw filled area
        legend_label = name if show_legend else None
        p.patch(
            x=polar_transform.x, 
            y=polar_transform.y,
            fill_color=color,
            fill_alpha=fill_alpha,
            line_color=color,
            line_width=line_width,
            legend_label=legend_label,
            source=source
        )
        
        # Draw data points
        if show_markers:
            scatter = p.scatter(
                x=polar_transform.x, 
                y=polar_transform.y,
                size=marker_size,
                color=color,
                line_color="white",
                line_width=2,
                source=source
            )
            scatter_renderers.append(scatter)
    
    # Add category labels
    for angle, category in zip(angles, categories):
        label_source = ColumnDataSource(data=dict(
            radius=[1.22],
            angle=[angle],
            text=[category]
        ))
        
        label_color = "#ffffff" if theme == "dark" else "#2c3e50"
        p.text(
            x=polar_transform.x, 
            y=polar_transform.y,
            text='text',
            source=label_source,
            text_color=label_color,
            text_align="center",
            text_baseline="middle",
            text_font_size="12pt",
            text_font_style="bold"
        )
    
    # Add hover tool
    if show_markers and scatter_renderers:
        hover = HoverTool(
            renderers=scatter_renderers,
            tooltips=[
                ('Series', '@series'),
                ('Category', '@category'),
                ('Value', '@radius{0.3f}')
            ]
        )
        p.add_tools(hover)
    
    # Styling
    if theme == "dark":
        p.title.text_color = "#00ff88"
        p.background_fill_color = None
        p.border_fill_color = "#1a1a2e"
    else:
        p.title.text_color = "#2c3e50"
        p.background_fill_color = None
        p.border_fill_color = "#ffffff"
    
    p.title.text_font_size = "18pt"
    p.grid.grid_line_color = None
    p.xaxis.visible = False
    p.yaxis.visible = False
    p.outline_line_color = None
    
    # Legend styling
    if show_legend:
        p.legend.location = "top_right"
        p.legend.click_policy = "hide"
        p.legend.background_fill_alpha = 0.7
        if theme == "dark":
            p.legend.label_text_color = "white"
            p.legend.background_fill_color = "#2d3436"
        else:
            p.legend.label_text_color = "#2c3e50"
            p.legend.background_fill_color = "#f8f9fa"
    
    # Apply background gradient
    if background_gradient is None:
        if theme == "dark":
            background_gradient = "radial-gradient(circle at center, #16213e 0%, #0f0f0f 100%)"
        else:
            background_gradient = "radial-gradient(circle at center, #ffffff 0%, #f0f0f0 100%)"
    
    gradient_css = InlineStyleSheet(css=f"""
    :host {{
        background: {background_gradient};
    }}
    """)
    
    return column(p, stylesheets=[gradient_css])





import numpy as np
import pandas as pd
from datetime import datetime
from bokeh.plotting import figure, show
from bokeh.models import (
    ColumnDataSource, LinearColorMapper, ColorBar, HoverTool,
    WheelZoomTool, CustomJSHover, WMTSTileSource, BasicTicker
)

# ───────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────
def latlon_to_mercator(lat, lon):
    """Convert lat/lon to Web Mercator coordinates."""
    k = 6378137.0
    x = lon * (k * np.pi / 180.0)
    y = np.log(np.tan((90 + lat) * np.pi / 360.0)) * k
    return x, y


def make_hover_tool(renderers, tooltip_cols, label_map=None):
    """
    Create a styled hover tooltip dynamically from column names.

    Parameters
    ----------
    renderers : list
        Renderers (e.g., scatter glyphs) to attach tooltips to.
    tooltip_cols : list[str]
        Column names from the data source to show in the tooltip.
    label_map : dict
        Optional mapping: {colname: display_name_or_emoji}.
    """

    # Format tooltip HTML
    label_map = label_map or {}
    tooltip_html = ""
    for col in tooltip_cols:
        label = label_map.get(col, col)
        tooltip_html += f"<div style='font-size:23px; color:#FFFFFF;'>{label}: @{col}</div>\n"

    tltl = f"""
        <div style='font-size:27px; color:#FFD700; font-weight:bold;'>@name</div>
        {tooltip_html}
    """

    # JS-based visibility control (to show only one tooltip)
    def cusj():
        num = 1
        return CustomJSHover(code=f"""
            special_vars.indices = special_vars.indices.slice(0,{num})
            return special_vars.indices.includes(special_vars.index) ? " " : " hidden "
        """)

    def hovfun(tltl):
        return """<div @hidden{custom} style="background-color: #2F2F2F;
        padding: 5px; border-radius: 15px;
        box-shadow: 0px 0px 5px rgba(0,0,0,0.3);">
        """ + tltl + """
        </div>
        <style>
        :host { --tooltip-border: transparent;
        --tooltip-color: transparent;
        --tooltip-text: #2f2f2f;}
        </style>"""

    hover = HoverTool(
        renderers=renderers,
        point_policy="follow_mouse",
        tooltips=hovfun(tltl),
        formatters={"@hidden": cusj()},
        mode="mouse"
    )
    return hover


# ───────────────────────────────────────────────
# High-Level Map Function
# ───────────────────────────────────────────────
def fscatter_tilemap(df, color_col="temp", tooltip_cols=None,
                     label_map=None, title="Cyclops Map",
                     palette="Turbo256", value_range=(-10, 40),
                     width=1200, height=700):
    """
    Plot scatter points over a dark tile map with custom tooltips.

    Parameters
    ----------
    df : pd.DataFrame
        Must include 'lat', 'lon', and optionally 'name' and custom cols.
    color_col : str
        Column used for color mapping.
    tooltip_cols : list[str]
        Columns to show in hover tooltip.
    label_map : dict
        Optional mapping of column names to labels/emojis.
    title : str
        Plot title prefix.
    palette : str or list
        Bokeh palette.
    value_range : tuple
        (min, max) for color mapping.
    width, height : int
        Figure size.
    """

    # ─── Coordinates ───
    df = df.copy()
    df["x"], df["y"] = latlon_to_mercator(df["lat"], df["lon"])
    df["hidden"] = np.ones(len(df)) * np.min(df["y"])
    source = ColumnDataSource(df)

    # ─── Figure ───
    title_str = f"{title} — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Data source: openweathermap.org"
    p = figure(
        match_aspect=True,
        x_axis_type="mercator", y_axis_type="mercator",
        width=width, height=height,
        sizing_mode="stretch_both",
        title=title_str,
        background_fill_color="#2F2F2F",
        border_fill_color="#2F2F2F",
        outline_line_color="#444444"
    )

    # ─── Tile Layer ───
    dark_url = "https://basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}.png"
    tile_provider = WMTSTileSource(url=dark_url)
    p.add_tile(tile_provider)

    # ─── Toolbar and Style ───
    wheel_zoom = WheelZoomTool()
    p.add_tools(wheel_zoom)
    p.toolbar.active_scroll = wheel_zoom

    p.title.text_color = "deepskyblue"
    p.title.text_font = "Helvetica"
    p.title.text_font_style = "bold"
    p.title.text_font_size = "25pt"

    for axis in (p.xaxis, p.yaxis):
        axis.axis_line_color = "white"
        axis.major_tick_line_color = "white"
        axis.major_label_text_color = "white"
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # ─── Color Mapping ───
    color_mapper = LinearColorMapper(palette=palette,
                                     low=value_range[0], high=value_range[1])
    circles = p.scatter(
        "x", "y", source=source, size=20,
        fill_color={"field": color_col, "transform": color_mapper},
        fill_alpha=0.9, line_color=None
    )

    # ─── Dynamic Tooltip ───
    tooltip_cols = tooltip_cols or [color_col]
    hover = make_hover_tool([circles], tooltip_cols, label_map)
    p.add_tools(hover)

    # ─── Color Bar ───
    color_bar = ColorBar(
        title=f"{color_col.capitalize()}",
        title_text_font_size="16pt",
        major_label_text_font_size="14pt",
        background_fill_color="#2F2F2F",
        color_mapper=color_mapper,
        title_text_color="white",
        major_label_text_color="white",
        label_standoff=10,
        ticker=BasicTicker(desired_num_ticks=5),
        location=(0, 0),
    )
    p.add_layout(color_bar, "right")

    return p
