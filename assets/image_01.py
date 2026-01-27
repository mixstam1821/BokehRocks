import numpy as np
from bokeh.plotting import figure, show, curdoc
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.palettes import linear_palette, interp_palette
from bokeh.models import ColumnDataSource, CustomJS,Circle, HoverTool, Div, DatetimeTickFormatter, NumeralTickFormatter, TextAreaInput
from bokeh_rocks import save_plot,apply_theme, hovfun

# Generate example data
longitudes = np.linspace(-180, 180, 576)
latitudes = np.linspace(-90, 90, 361)
LON, LAT = np.meshgrid(longitudes, latitudes)

# Create sample temperature data
temperatures = 20 * np.cos(np.radians(LAT)) + \
              5 * np.sin(np.radians(2 * LON)) + \
              np.random.normal(0, 1, LAT.shape)

mike2=('#000063','#123aff','#00aeff','#26fff4','#00ff95','#19ff19','#ffff00','#ff8a15','#ff2a1b','#db0000','#4b0000')
bo_mike2 = interp_palette(mike2, 255)

lats = np.repeat(latitudes, len(longitudes))
lons = np.tile(longitudes, len(latitudes))
s1 = ColumnDataSource(data={'image': [temperatures], 'latitudes': [lats], 'longitudes': [lons]})

def crd():
  import cartopy.feature as cf,numpy as np
  # create the list of coordinates separated by nan to avoid connecting the lines
  x_coords = []
  y_coords = []
  for coord_seq in cf.COASTLINE.geometries():
      x_coords.extend([k[0] for k in coord_seq.coords] + [np.nan])
      y_coords.extend([k[1] for k in coord_seq.coords] + [np.nan])
  return x_coords,y_coords,#x_coords2,y_coords2
x_coords,y_coords=[i for i in crd()]


color_mapper= LinearColorMapper(palette=bo_mike2, low=0, high=35)

plot = figure(x_range=(-180,180), y_range=(-90,90),active_scroll="wheel_zoom", output_backend="webgl",width=900)
r=plot.image(image='image', color_mapper=color_mapper, x=min(longitudes),
     y=min(latitudes),
     dw=max(longitudes) - min(longitudes),
     dh=max(latitudes) - min(latitudes),source = s1)
color_bar = ColorBar(color_mapper= color_mapper, title="Temperature", ticker= BasicTicker(),location=(0,0));     plot.add_layout(color_bar, 'right')
color_bar.major_label_text_font_size = "14pt"
plot.line(x = x_coords,y = y_coords, line_width=1, line_color='black')

plot.add_tools(HoverTool(renderers = [r],tooltips=hovfun("""<i>Temp:</i> <b>@image</b> <br> <i>lat:</i> <b>@latitudes</b><br> <i>lon:</i> <b>@longitudes</b>"""))) 

show(plot)
save_plot(plot, "output/image_01")