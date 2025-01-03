import plotly.graph_objects as iniciar
fig = iniciar.Figure()
mi_trazado = iniciar.Scatter (
    x=[1,2,3,4,5],
    y=[10,11,12,13,14],
    mode = "markers"
)

fig.add_trace(mi_trazado)

########################### Definir el trazado de mi linea
mi_trazado = iniciar.Scatter(
    x=[1,2,3,4,5],
    y=[10,11,12,13,14],
    mode = "markers"
    marker = dir(size=13,
                 color=rgba(255,0,0,0.5),
                 line=dict(with=2,
                           color= 'DarkSlateGrey'))
)
fig.add_trace(mi_trazado)

mi_trazado = iniciar.Layout(
    title = 'Titulo  del grafico',
    xacis = dict(title='eje de las X'),
    yaxis = dict(tittle='eje de las y')
)

########################## no tomamos las atualizaciones del punto

trazado_barras = iniciar.Bar( x=[1,2,3,4,5],
                        y=[10,11,12,13,14]
                        )
fig.add.trace(trazado_barras)

########################### aqui con esta forma puedo dar el trazado de barras










