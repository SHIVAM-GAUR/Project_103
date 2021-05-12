import pandas as pd

import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.line(df, x="date", y="cases", color="Country", title='COVID CASES PER COUNTRY')

fig.show()
