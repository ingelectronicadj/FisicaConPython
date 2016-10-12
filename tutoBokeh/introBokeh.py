# Learn Python App
""" ******************************************************
 *              LIBRERIAS y CONSTANTES
 *********************************************************
"""
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button, CheckboxButtonGroup, CheckboxGroup, Dropdown, MultiSelect, RadioGroup, Select

output_file("tutoGLUD.html")
#Ejemplo de un boton
boton = Button(label="Ejemplo-Boton", button_type="success")

#Ejemplo de un checkBox para multiples botones
multiBoton = CheckboxButtonGroup(
        labels=["Boton 1", "Boton 2", "Boton 3"], active=[0, 1])

#Ejemplo de un Standard para un checkBox
checkboxBoton = CheckboxGroup(
        labels=["Opcion A", "Opcion B", "Opcion C"], active=[0, 1])

#Ejemplo de un menu desplegable
menu = [("Opcion A", "item_1"), ("Opcion B", "item_2"), None, ("Opcion C", "item_3")]
desplegable = Dropdown(label="Boton desplegable", button_type="warning", menu=menu)

#Ejemplo de una canasta de seleccion
multiSeleccion = MultiSelect(title="Multiseleccionador de opciones:", value=["foo", "quux"],
                           options=[("foo", "Opcion 1"), ("bar", "Opcion 2"), ("baz", "Opcion 3"), ("quux", "Opcion 4")])

#Ejemplo de un grupo de radioBotones
radioBotones = RadioGroup(
        labels=["Opcion 1", "Opcion 2", "Opcion 3"], active=0)

#Ejemplo de una canasta de seleccion
seleccionador = Select(title="Opciones:", value="foo", options=["Comerme una galleta", "Salir a trotar", "Jugar Fretsonfire", "darle a la tesis"])

show(widgetbox(boton, multiBoton, checkboxBoton, desplegable, multiSeleccion, radioBotones, seleccionador))


