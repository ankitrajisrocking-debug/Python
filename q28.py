import pandas as pd
import plotly.express as px

data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'],
    'Mathematics': [78, 85, 67, 90, 73, 81, 69, 94, 76, 88]
}

df = pd.DataFrame(data)

fig = px.bar(df, x='Student', y='Mathematics', title='Mathematics Marks by Student')
fig.show()
