import pandas as pd
import plotly.express as px
df=pd.read_csv("projects/project-103/data.csv")
fig=px.bar(df,x="date",y="cases")
fig.show()