# Learn Python App
""" ******************************************************
 *              LIBRERIAS y CONSTANTES
 *********************************************************
"""
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button, CheckboxButtonGroup, CheckboxGroup, Dropdown, MultiSelect, RadioGroup, Select, Slider, TextInput, Div

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

#Ejemplo de un Slider
miSlider = Slider(start=0, end=10, value=3, step=.1, title="Slider para variacion de parametros") #Slider(inicia,termina,arranca,pasos)

#Ejemplo Label
miLabel = TextInput(value="www.semanalinuxud.com", title="Label:")

#Ejemplo de un div() para html
div = Div(text="""Preparandome para la <a href="https://en.wikipedia.org/wiki/HTML">Semana Linux UDistrital</a>- en homenaje al <b>Sabio Caldas</b> y el desarrollo de tecnologias mas humanas. <i><b>Fecha</b> 24 al 28 de octubre.</i>""",
width=600, height=100)

show(widgetbox(boton, multiBoton, checkboxBoton, desplegable, multiSeleccion, radioBotones, seleccionador, miSlider, miLabel, div))


