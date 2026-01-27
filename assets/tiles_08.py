from bokeh.models import WMTSTileSource
from bokeh.plotting import figure, show
from bokeh_rocks import save_plot
from bokeh.layouts import column, row
def make_p():
    p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
            x_axis_type="mercator", y_axis_type="mercator", width=500, height=500,
            )
    p.grid.visible = False
    return p

p = make_p()
p2 = make_p()
p3 = make_p()
p4 = make_p()
p5 = make_p()
p6 = make_p()

dark_url1 = "https://basemaps.cartocdn.com/dark_all/{Z}/{X}/{Y}.png"
dark_url2 = "https://basemaps.cartocdn.com/light_all/{Z}/{X}/{Y}.png"
dark_url3 = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}"
dark_url4 = "https://basemaps.cartocdn.com/rastertiles/voyager/{Z}/{X}/{Y}.png"
dark_url5 = "https://a.tile.opentopomap.org/{Z}/{X}/{Y}.png"
dark_url6 = "https://watercolormaps.collection.cooperhewitt.org/tile/watercolor/{z}/{x}/{y}.jpg"


tile_provider1 = WMTSTileSource(url=dark_url1)
tile_provider2 = WMTSTileSource(url=dark_url2)
tile_provider3 = WMTSTileSource(url=dark_url3)
tile_provider4 = WMTSTileSource(url=dark_url4)
tile_provider5 = WMTSTileSource(url=dark_url5)
tile_provider6 = WMTSTileSource(url=dark_url6)
p.add_tile(tile_provider1)
p2.add_tile(tile_provider2)
p3.add_tile(tile_provider3)
p4.add_tile(tile_provider4)  
p5.add_tile(tile_provider5)
p6.add_tile(tile_provider6)
lay = column(row(p,p2,p3),row(p4,p5,p6))    
show(lay)
save_plot(lay, "output/tiles_08")