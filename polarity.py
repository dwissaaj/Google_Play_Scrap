import pandas as pd

df = pd.read_excel('posindonesia.xlsx')

def getAnalysis(score):
    if score < 3:
        return 'Negative'
    elif score == 3:
        return 'Neutral'
    else:
        return 'Positive'

import plotly.express as px
df['Analysis'] = df['score'].apply(getAnalysis)
positif = df[df.Analysis == 'Positive']
netral = df[df.Analysis == 'Neutral']
negatif = df[df.Analysis == 'Negative']


fig = px.bar(df['Analysis'])
fig.show()
fig.write_html("file.html")