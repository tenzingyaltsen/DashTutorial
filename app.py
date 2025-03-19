import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Import data set
insurance = pd.read_csv('insurance.csv')

# Unique regions for subplots
regions = insurance['region'].unique()
sexes = ['male', 'female']

# Create subplot structure
fig = make_subplots(
    rows=1, cols=len(regions), subplot_titles=[f"Region: {region}" for region in regions]
)

# Define colors for sex
colors = {'male': 'blue', 'female': 'red'}

# Loop through each region to create a subplot
for i, region in enumerate(regions):
    subset = insurance[insurance['region'] == region]
    
    for sex in sexes:
        sex_subset = subset[subset['sex'] == sex]
        fig.add_trace(
            go.Scatter(
                x=sex_subset['age'],
                y=sex_subset['charges'],
                mode='markers',
                marker=dict(color=colors[sex]),
                name=sex if i == 0 else None,
                showlegend=i == 0
            ),
            row=1, col=i + 1
        )

# Update figure layout
fig.update_layout(
    title="Insurance Charges by Age, Region, and Sex",
    xaxis_title="Age",
    yaxis_title="Charges ($)",
    showlegend=True,
    height=500
)

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Insurance Data Visualization", style={'textAlign': 'center'}),
    dcc.Graph(id='example-plot', figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8090)
