import pandas as pd
import plotly.express as px


# df = pd.read_csv('Copy+of+data+-+data.csv')
# fig = px.bar(df, x = "date",y = "cases", color = "country")
# fig.show()

# df = pd.read_csv('Copy+of+data+-+data.csv')
# fig = px.line(df, x = "date",y = "cases", color = "country")
# fig.show()

df = pd.read_csv('Copy+of+data+-+data.csv')
fig = px.scatter(df, x = "date",y = "cases", color = "country", size_max = 60)
fig.show()