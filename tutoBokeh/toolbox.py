from bokeh.plotting import figure, output_file, show

output_file("poderesPalPueblo.html")

# Anadimos herramientas especificas de nuestro workspace
TOOLS = 'box_select,box_zoom,wheel_zoom,lasso_select,poly_select,pan,tap,resize,undo,redo,reset,save,crosshair' #zoom_in,zoom_out   
dominio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Creamos un nuevo grafico con la caja de herramientas abajo
#p = figure(plot_width=400, plot_height=400, title=None, toolbar_location="above", toolbar_sticky=False) #above/arriba, below/abajo
p = figure(plot_width=800, plot_height=400, title=None, tools=TOOLS, toolbar_location="below", toolbar_sticky=False) # Uso de herramientas especificas

#p.circle(dominio, [2, 5, 8, 2, 7, 6, 3, 1, 9, 7], size=10)
p.line(dominio, [2, 5, 8, 2, 7, 6, 3, 1, 9, 7], line_width=3)

show(p)
