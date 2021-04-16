import pandas as pd
import plotly.express as px
df=pd.read_csv("projects/project-103/data.csv")
fig=px.line(df,x="date",y="cases",color="country",title="cases of COVID-19")
fig.show()