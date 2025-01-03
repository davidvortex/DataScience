import plotly.graph_object as iniciar
fig = iniciar.fig()
fig.add_tracer(
    iniciar.Scatter(
    x= [2,4,6,8,10],
    y= [,5,10,15,20],
    mode='lines',
    name='linea' #llamamos para que el grafico tenga lineas por su nombre
    )
)

fig.update_layout(
    title = 'Grafico de lineas',    
    xaxis = dict(tittle='Eje X'), # este sera mi suptitulo para la aprte de las X
    yaxis = dict(tittle='Eje y')  # este sera mi suptitulo para la aprte de las y
)

############ graficos de barra personalizado
fig2 = iniciar.Figure()

fig2.add_trace(iniciar.Bar( x=[2,4,6,8,10],
    y=[1,2,3,4,5],
    marker = dir(color= 'rgba(255,123,155,0.6)',
                 line=dict(color='rbg(0,0,0)',
                           width=1.5))))

fig2.update_layout(
    title = 'Grafico de Barras',    
    xaxis = dict(tittle='Eje X'), # este sera mi suptitulo para la aprte de las X
    yaxis = dict(tittle='Eje y')  # este sera mi suptitulo para la aprte de las y
)

################ grafico de lineas con relleno por la parte de abajo
fig3 = iniciar.Figure() 
fig3.add_trace(iniciar.Scatter(x=[2,4,6,8,10],
                               y = [1,2,3,4,5],
                               mode = 'lines',
                               fill = 'tozeroy',
                               name = 'area'))
fig3.update_layout(
    title = 'Grafico de lineas',    
    xaxis = dict(tittle='Eje X'), # este sera mi suptitulo para la aprte de las X
    yaxis = dict(tittle='Eje y')  # este sera mi suptitulo para la aprte de las y
)


###############  grafico para hacer grafico de pastel o circular
fig4 = iniciar.Figure()

fig4.add_trace(iniciar.Pie(labels=['a','b','c','d'],
                           values=[400,200,105,750]))

fig4.update_layout(
    title = 'Grafico Circular',    
    xaxis = dict(tittle='Eje X'), # este sera mi suptitulo para la aprte de las X
    yaxis = dict(tittle='Eje y')  # este sera mi suptitulo para la aprte de las y
)

################
data = iniciar.Histograma(x = [1,2,2,3,3,3,4],)
fig5 = iniciar.Figure(data = data)
fig5.update_layout(tittle='Histograma')







