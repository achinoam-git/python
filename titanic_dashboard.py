import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output

# Load Titanic dataset (will use seaborn for loading the classic version)
try:
    import seaborn as sns
    df = sns.load_dataset('titanic')
except:
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Handle differences in column naming between seaborn and Kaggle version
if 'survived' not in df.columns:
    df.rename(columns={'Survived': 'survived', 'Sex': 'sex', 'Age': 'age', 'Pclass': 'pclass'}, inplace=True)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Titanic Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Passenger Class:"),
        dcc.Dropdown(
            id='class-dropdown',
            options=[{'label': str(cls), 'value': cls} for cls in sorted(df['pclass'].dropna().unique())],
            value=1,
            clearable=False
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Select Sex:"),
        dcc.RadioItems(
            id='sex-radio',
            options=[{'label': sex.capitalize(), 'value': sex} for sex in df['sex'].dropna().unique()],
            value='male',
            inline=True
        ),
    ], style={'width': '30%', 'display': 'inline-block', 'marginLeft': '5%'}),

    html.Br(),

    dcc.Graph(id='survival-pie'),
    dcc.Graph(id='age-hist'),
])

@app.callback(
    [Output('survival-pie', 'figure'),
     Output('age-hist', 'figure')],
    [Input('class-dropdown', 'value'),
     Input('sex-radio', 'value')]
)
def update_graphs(selected_class, selected_sex):
    filtered_df = df[(df['pclass'] == selected_class) & (df['sex'] == selected_sex)]
    
    # Pie chart for survival
    pie_fig = px.pie(
        filtered_df,
        names='survived',
        title=f'Survival Distribution (Class {selected_class}, Sex: {selected_sex})',
        color='survived',
        category_orders={'survived': [0,1]},
        color_discrete_map={0: "firebrick", 1: "seagreen"},
        labels={'survived': {0: "Did Not Survive", 1: "Survived"}}
    )

    # Age distribution (histogram)
    hist_fig = px.histogram(
        filtered_df, x='age',
        nbins=20,
        title='Age Distribution',
        labels={'age': 'Age'}
    )

    return pie_fig, hist_fig

if __name__ == "__main__":
    app.run_server(debug=True)