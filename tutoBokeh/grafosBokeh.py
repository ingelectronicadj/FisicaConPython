from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("graficos.html")

p1 = figure(plot_width=1200, plot_height=300)
p1.circle([1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 2, 4, 5, 3, 8, 4], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="Grafico puntos")

p2 = figure(plot_width=1200, plot_height=300)
p2.line([1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 2, 4, 5, 3, 8, 4], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="Grafico lineal")

tabs = Tabs(tabs=[ tab1, tab2 ])

show(tabs)
