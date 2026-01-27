from bokeh.io import show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure
from bokeh.transform import dodge
import bokeh_rocks as br

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ['2015', '2016', '2017']
data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 3, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

source = ColumnDataSource(data=data)

p = figure(x_range=fruits, y_range=(0, 7), title="Fruit Counts by Year",
           width=1300, height=800)

labels15=LabelSet(x=dodge('fruits', -0.25, range=p.x_range),y='2015',text='2015',source=source,text_align='center',y_offset=8 ,text_color='white')
labels16=LabelSet(x=dodge('fruits', 0.0, range=p.x_range),y='2016',text='2016',source=source,text_align='center',y_offset=8 , text_color='white')
labels17=LabelSet(x=dodge('fruits', 0.25, range=p.x_range),y='2017',text='2017',source=source,text_align='center',y_offset=8 , text_color='white')

vbar1 = p.vbar(x=dodge('fruits', -0.25, range=p.x_range), top='2015', width=0.2, source=source,
       color="#2EC4B6", legend_label="2015")

p.vbar(x=dodge('fruits',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,
       color="#FCBF49", legend_label="2016")

p.vbar(x=dodge('fruits',  0.25, range=p.x_range), top='2017', width=0.2, source=source,
       color="#CDB4DB", legend_label="2017")

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "vertical"
p.add_layout(labels15)
p.add_layout(labels16)
p.add_layout(labels17)
br.apply_theme(p,'dark'); show(p);fname = "output/bar_03"; br.save_plot(p,fname)
