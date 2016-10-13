from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool

output_file("python.html")

source = ColumnDataSource(
        data=dict(
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y=[3, 5, 8, 2, 7, 3, 4, 5, 7, 3],
            desc=['Jorge Ulises', 'Diego Mena', 'Don Python', 'Alejandro Cortazar', 'Sebastian Sanchez', 'Andres Acosta', 'Miguel Rodriguez', 'David Castiblanco', 'Jose Laya', 'Eduardo Echevarria'],
            imgs = [
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Jorge_Useche.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Diego_Mena.jpg',
                'http://bokeh.pydata.org/static/snake.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Alejandro_Cortazar.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Sebastian_Sanchez.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Andres_Acosta.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Miguel_Rodriguez.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/David_Castelblanco.jpg',
                'https://raw.githubusercontent.com/GLUD/SLUD-2016/master/img/expositores/Jose_Laya.jpg',
                'https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/3/005/01e/0e5/312968f.jpg'
            ]
        )
    )

hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <img
                    src="@imgs" height="110" alt="@imgs" width="110"
                    style="int: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@desc</span>
                <span style="font-size: 15px; color: #966;">[$index]</span>
            </div>
            <div>
                <span style="font-size: 15px;">Miembro</span>
                <span style="font-size: 10px; color: #696;">($x, $y)</span>
            </div>
        </div>
        """
    )

p = figure(plot_width=900, plot_height=600, tools=[hover],
           title="Mouse sobre los puntos")

p.circle('x', 'y', size=20, source=source)

show(p)
