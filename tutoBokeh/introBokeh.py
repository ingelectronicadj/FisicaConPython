""" ********************************************************************
 *              LIBRERIAS y CONSTANTES
 ***********************************************************************
"""
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button

output_file("tutoGLUD.html")

button = Button(label="Ejemplo-Boton", button_type="success")

show(widgetbox(button))
