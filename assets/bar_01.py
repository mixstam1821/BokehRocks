from bokeh.io import show
from bokeh.models import ColumnDataSource, ranges, LabelSet, HoverTool
from bokeh.plotting import figure
from bokeh_rocks import hovfun
import bokeh_rocks as br

import xarray as xr

annual_cycle = xr.tutorial.load_dataset('air_temperature').air.isel(lon=0, lat=0).groupby('time.month').mean().values
source = ColumnDataSource(dict(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                               y=[int(i) for i in annual_cycle],
                               y2 = [int(i*1.5) for i in annual_cycle],))

plot = figure( width=1300, height=800, toolbar_location='left', x_axis_label = 'months', y_axis_label = 'Tair', title='Tair',
            x_minor_ticks=2, x_range = source.data["x"], y_range= ranges.Range1d(start=200,end=280),)

r1 = plot.vbar(source=source,x='x',top='y',bottom=0,width=1,color='#2EC4B6',border_radius=14, line_color='black', hover_fill_color='#FCBF49', legend_label='Tair')

labels = LabelSet(x='x', y='y', text='y', level='glyph',text_align='center', y_offset=5, source=source, text_color = '#000000', text_font_size="18pt", angle=0)
plot.add_layout(labels)

tltl = """<i>Month:</i> <b>@x</b> <br> <i>Tair:</i> <b>@y</b>"""; plot.add_tools(HoverTool(tooltips=hovfun(tltl),renderers = [r1])); 

br.apply_theme(plot,'light'); show(plot, );fname = "output/bar_01"; br.save_plot(plot,fname)
