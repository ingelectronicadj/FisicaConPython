""" ******************************************************
 *              LIBRERIAS y CONSTANTES
 *********************************************************
"""
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button
from bokeh.models.widgets import CheckboxButtonGroup


output_file("tutoGLUD.html")
#Ejemplo de un boton
button = Button(label="Ejemplo-Boton", button_type="success")

#Ejemplo de un checkBox para multiples botones
checkbox_button_group = CheckboxButtonGroup(
        labels=["Boton 1", "Boton 2", "Boton 3"], active=[0, 1])

show(widgetbox(button, checkbox_button_group))


