#import packages
#import plotly 
import plotly.express as px

#lotly_colorscales = px.colors.named_colorscales()
  
# printing color scales
print(plotly_colorscales)


import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()
