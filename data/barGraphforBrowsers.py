import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['Chrome', 'FireFox'],
    y=[450, 430],
    name='200'
)
trace2 = go.Bar(
    x=['Chrome', 'FireFox'],
    y=[13, 13],
    name='other'
)

trace3 = go.Bar(
    x=['Chrome', 'FireFox'],
    y=[32, 31],
    name='Error'
)

trace4 = go.Bar(
    x=['Chrome', 'FireFox'],
    y=[4, 25],
    name='Timeout'
)

data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    barmode='stack'
)

py.iplot(go.Figure(data=data, layout=layout), filename='bars for browsers')
