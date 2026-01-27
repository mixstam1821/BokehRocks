from bokeh.plotting import figure, show
from bokeh.models import InlineStyleSheet, ColumnDataSource, HoverTool
from bokeh.layouts import column
import numpy as np
from bokeh_rocks import save_plot

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



x_lavender = np.linspace(0, 8, 200)
y_lavender = np.sin(x_lavender) * np.cos(x_lavender/2) * 2.5

lavender_plot = create_gradient_masked_plot(
    x_data=x_lavender,
    y_data=y_lavender,
    gradient_colors=["#a8edea 0%", "#d5a5d6 40%", "#fed6e3 100%"],
    gradient_direction="45deg",  # Angled
    mask_color="#e8dff5",
    line_color="#6a0572",
    line_width=4,
    title="Lavender Dream - Complex Wave",
    width=800,
    height=600,
    border_color="#fce4ec",
    grid_color="#d8b5e8",
    grid_alpha=0.22,
    title_color="#8e44ad",
    add_hover=True
)
show(lavender_plot)
save_plot(lavender_plot, "output/area_01")