import pandas as pd
from bokeh.plotting import figure, output_file, show

misDatos = pd.read_csv("/home/glud/Documentos/FisicaConPython/tutoBokeh/csv/table.csv", parse_dates=['Date'])

output_file("tomaLoTuyo.html")

# create a new plot with a datetime axis type
p = figure(width=1100, height=300, x_axis_type="datetime", title='Graficando consumiendo fichero .csv')

p.line(misDatos['Date'], misDatos['Open'], color='navy', alpha=0.5) #Columnas: Date,Open,High,Low,Close,Volume,Adj Close

show(p)
