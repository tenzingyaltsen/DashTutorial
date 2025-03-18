import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# Create a Dash app
app = dash.Dash(__name__)

# Define a figure
fig = go.Figure()

# Add a scatter plot to the figure
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines+markers', name='Sample Line'))

# Layout for the figure
fig.update_layout(title="Sample Plot", xaxis_title="X Axis", yaxis_title="Y Axis")

# Define the layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='example-plot', figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8090)
