import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=[2, 3, 4, 5],
    y=[1.0232558139534884, 1.0237610319076713, 1.0313778990450204, 1.0370009737098345],
    name='Headed'
)
# trace2 = go.Bar(
#     x=['Chrome Test 1', 'Chrome Test 2', 'FireFox Test'],
#     y=[1360, 1348, 1360],
#     name='Headless With UserAgent'
# )

data = [trace1]
layout = go.Layout(
    barmode='group'
)

py.iplot(go.Figure(data=data, layout=layout), filename='grouped-bar')
