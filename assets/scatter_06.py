from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, LabelSet, Div
from bokeh.layouts import column, row
import pandas as pd
import numpy as np

# ============================================================================
# ORION CONSTELLATION - Real Star Data
# ============================================================================
# Coordinates are in Right Ascension (RA) and Declination (Dec)
# Converted to X,Y for plotting

orion_stars = pd.DataFrame({
'name': [
        'Betelgeuse', 'Rigel', 'Bellatrix', 'Mintaka', 'Alnilam', 'Alnitak',
        'Saiph', 'Meissa', 'Hatsya', 'Tabit', 'Thabit'
    ],
    'ra': [
        88.79, 78.63, 81.28, 83.00, 84.05, 85.19, 
        86.94, 83.78, 83.86, 72.46, 82.98
    ],
    'dec': [
        7.41, -8.20, 6.35, -0.30, -1.20, -1.94, 
        -9.67, 9.93, -5.91, 6.96, -7.30
    ],  
    'magnitude': [0.42, 0.18, 1.64, 2.23, 1.69, 1.77, 2.07, 3.39, 3.35, 3.19, 3.7],  # Brightness (lower = brighter)
    'color': ['#ff6b35', '#a8d8ea', '#ffffff', '#a8d8ea', '#a8d8ea', '#a8d8ea', 
              '#a8d8ea', '#ffffff', '#ffffff', '#ffffff', '#ffffff'],
    'star_type': ['Red Supergiant', 'Blue Supergiant', 'Blue Giant', 'Blue Giant', 
                  'Blue Supergiant', 'Blue Supergiant', 'Blue Supergiant', 
                  'Blue Giant', 'Blue Giant', 'Main Sequence', 'Main Sequence']
})

# Normalize coordinates for plotting (center around 0)
orion_stars['x'] = (orion_stars['ra'] - orion_stars['ra'].mean()) * 10
orion_stars['y'] = (orion_stars['dec'] - orion_stars['dec'].mean()) * 10

# Calculate star sizes (brighter stars = larger size)
# Inverse relationship: lower magnitude = brighter = larger
orion_stars['size'] = 30 - (orion_stars['magnitude'] * 8)

# Add glow intensity based on brightness
orion_stars['glow_intensity'] = 5 - orion_stars['magnitude']

# Create glow layer sizes
orion_stars['glow_size_1'] = orion_stars['size'] * 4
orion_stars['glow_size_2'] = orion_stars['size'] * 3
orion_stars['glow_size_3'] = orion_stars['size'] * 2

# ============================================================================
# ADD BACKGROUND STARS (Random field)
# ============================================================================
np.random.seed(42)
n_background = 400

background_stars = pd.DataFrame({
    'x': np.random.uniform(-90, 90, n_background),
    'y': np.random.uniform(-150, 150, n_background),
    'size': np.random.uniform(2, 8, n_background),
    'alpha': np.random.uniform(0.2, 0.6, n_background),
    'color': np.random.choice(['#ffffff', '#a8d8ea', '#ffe5b4'], n_background)
})



# ============================================================================
# CREATE THE PLOT
# ============================================================================

p = figure(
    width=1000, 
    height=1000,
    title="✨ Orion Constellation - Interactive Star Map ✨",
    match_aspect=True,
    x_range=(90, -90),
    y_range=(-150, 150)
)

# Dark space background
p.background_fill_color = "#0a0a0a"
p.border_fill_color = "#0a0a0a"
p.xgrid.visible = False
p.ygrid.visible = False
p.xaxis.visible = False
p.yaxis.visible = False
p.outline_line_color = None

# ============================================================================
# RENDER LAYERS (back to front)
# ============================================================================

# 1. Background stars (dim)
bg_source = ColumnDataSource(background_stars)
p.circle('x', 'y', source=bg_source, size='size', 
         color='color', alpha='alpha', line_color=None)

# 3. Named stars - GLOW LAYERS
orion_source = ColumnDataSource(orion_stars)

# Glow layer 1 (outermost, faintest)
p.circle('x', 'y', source=orion_source, 
        size='glow_size_1', color='color', alpha=0.1, line_color=None)

# Glow layer 2 (middle)
p.circle('x', 'y', source=orion_source, 
        size='glow_size_2', color='color', alpha=0.2, line_color=None)

# 4. Main star bodies
main_stars = p.circle('x', 'y', source=orion_source, 
                      size='size', color='color', alpha=0.9,
                      line_color='white', line_width=1)

# 5. RIPPLE EFFECT for brightest stars (Betelgeuse and Rigel)
brightest = orion_stars[orion_stars['magnitude'] < 0.5].copy()
brightest['ripple_1'] = brightest['size'] * 2


ripple_source = ColumnDataSource(brightest)

# Create ripple circles
p.circle('x', 'y', source=ripple_source, size='ripple_1',
        color='color', fill_alpha=0, line_color='color', line_width=2, line_alpha=0.4)

p.circle('x', 'y', source=ripple_source, size='ripple_2',
        color='color', fill_alpha=0, line_color='color', line_width=2, line_alpha=0.32)

p.circle('x', 'y', source=ripple_source, size='ripple_3',
        color='color', fill_alpha=0, line_color='color', line_width=2, line_alpha=0.24)

p.circle('x', 'y', source=ripple_source, size='ripple_4',
        color='color', fill_alpha=0, line_color='color', line_width=2, line_alpha=0.16)

# ============================================================================
# HOVER TOOLTIPS
# ============================================================================

hover = HoverTool(renderers=[main_stars], tooltips=[
    ("Star Name", "@name"),
    ("Type", "@star_type"),
    ("Magnitude", "@magnitude{0.00}"),
    ("RA", "@ra{0.00}°"),
    ("Dec", "@dec{0.00}°"),
])
p.add_tools(hover)

# ============================================================================
# ADD STAR LABELS
# ============================================================================

labels = LabelSet(
    x='x', y='y', text='name',
    source=orion_source,
    text_color='white',
    text_font_size='10pt',
    text_font_style='italic',
    x_offset=10, y_offset=10,
    text_alpha=0.7
)
p.add_layout(labels)
layout = row(p)
show(layout)