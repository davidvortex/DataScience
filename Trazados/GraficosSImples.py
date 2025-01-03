import plotly.graph_object as iniciar
figura1 = iniciar.Figure()
figura1.add_tracer(iniciar.Scatter( x =[1,2,3,4,5],
                                   y = [10,15,20,25,30],
                                    mode = 'line',
                                    name = 'Linea'))

########### Graficos de barras con linea  parte su perior la linea
figura2 = iniciar.Figure()
figura2.add_tracer(iniciar.Bar( x=[1,2,3,4,5],
                               y = [],
                               marker = dict(color='rbga(0,128,524,6)',
                                             line = dict(color = 'blue',
                                                         width = 1.5 ))))

figura2.update_layout(tittle='Grafico de Barra',
                      xaxis = 'parte de x',
                      yaxis = 'parte de y')

############### este grafico de barras con espacio

figura3 = iniciar.Figure()
figura3.add_tracer(iniciar.Scatter( x =[1,2,3,4,5],
                                   y = [10,15,20,25,30],
                                    mode = 'line',
                                    fill =  'tozeroy',
                                    name = 'Linea'))
figura3.update_layout(tittle='Grafico de Area',
                      xaxis = 'parte de x',
                      yaxis = 'parte de y')

figura4 = iniciar.Figure()
figura4.add_tracer(iniciar.Pie(labels=['A','B','C','D'],
                               values = [100,300,400,200]))
figura4.update_layout(tittle='Grafico de pastel')

############################ en este grafico no necesita poner los subtitulos o indices donde marque el indice de X o Y ya que el circular

data.iniciar.Histograma(x = [1,2,2,3,3,3,4])
figura5 = iniciar.Figure(data = data)
figura4.update_layout(tittle='Grafico de Conteo de numeros')

