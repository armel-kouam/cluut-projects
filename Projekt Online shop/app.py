import time
import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, State
from queries_dynamodb import*
import plotly.express as px
from datetime import datetime

# colors = {
#     'background': 'pink',
#     'text': '#A52A2A'
# }
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')


plant_bestellung = get_productorders_timerange('plant')
vis_plant_bestellung = px.area(plant_bestellung, x="orderID", y="quantity", color_discrete_sequence =['#ff008b']*len(plant_bestellung))

# vis_plant_bestellung.update_layout(
#         plot_bgcolor=colors['background'],
#         font_color=colors['text']
#         )
        
#Neue Bestellung anlegen
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    [
        html.H1("Neue Bestellung anlegen"),
        html.H6("Bestellinformationen im Format : <customerID>,<firstname>,<lastname>,<country>,<product>,<quantity>"),                                                                                                                 
        html.Div(
            dbc.Input(id="zone",  type = 'text')
        ),
            html.Br(),
            dbc.Button(
            "Submit", id="button", color="success", className="me-2", n_clicks=0),
        html.Div(id="output", children=[]),
        
        html.Br(),
        html.H1(children='Verkäufe für das Produkt Plant',
        style={'textAlign': 'recht'}
        ),

        dcc.Graph(
            id='plant_bestellung',
            figure=vis_plant_bestellung
        ),
        html.Br(),
        html.H1(children='Übersicht Produktbestellungen weltweit',
        style={'textAlign': 'recht'}
        ),
        html.Div([
        dbc.Row([
            dbc.Col(
                dbc.Card([ 
                    dbc.CardHeader("Book", style={'textAlign': 'center'}),
                    
                    dbc.CardBody([
                        dbc.CardImg(src = app.get_asset_url('book.png'), top=True),
                        
                    ]),
                    
                    dbc.CardFooter([
                        html.P (id = "sum_book", style={'textAlign': 'center'}),
                        dcc.Interval(
                            id='interval-book', 
                            interval=1*1000, # in millisecond 
                            n_intervals=0
                        )
                        
                    ])
                ]),
            ),
            
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardHeader("Shoes", style={'textAlign': 'center'}),
                    
                    dbc.CardBody([
                        dbc.CardImg(src= app.get_asset_url('sneakers.png'), top=True)
                        
                    ]),
                        
                    dbc.CardFooter([
                        html.P (id = "sum_shoes", style={'textAlign': 'center'}),
                        dcc.Interval(
                            id='interval-shoes', 
                            interval=1*1000, # in millisecond 
                            n_intervals=0
                        )
                    ])
            
                ])
            ),
            
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardHeader("Plant", style={'textAlign': 'center'}),
                    
                    dbc.CardBody([
                        
                        dbc.CardImg(src= app.get_asset_url('spider-plant.png'),  top=True)
                        
                        
                    ]),
                    
                    dbc.CardFooter([
                        html.P (id = "sum_plant", style={'textAlign': 'center'}), 
                        dcc.Interval(
                            id='interval-plant', 
                            interval=1*1000, # in millisecond 
                            n_intervals=0
                        )
                    ])
                ])
            )
        ])
        ])
    ]
)
# Callback funktion für eine neue Bestellung
@app.callback(
    [Output("output", "children"), Output("zone", "value") ], Input("button", "n_clicks"), State("zone", "value")
)
def new_order(n_clicks, values):
   
    if n_clicks > 0 or values is not None:
        row = values.split(",")
        
        if '@'  not in row[0] or len(row) < 6:
            return 'Sie müssen richtige Informationen eingeben', ''
            
        else:
            content = {
                "customerID": row[0],
                "orderID": datetime.now().strftime("%Y%m%d"),
                "lastname": row[2],
                "country": row[3],
                "product": row[4],
                "quantity": row[5]
            }
        
        response = table.put_item(Item=content)
    
# um HTTP statut code zu bekommen, werde ich mit print(response) von dynamodb arbeiten : 
# {'Items': [], 'ResponseMetadata': {'RequestId': 'UGPL8B97NND16STSGROFN4D547VV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sun, 12 Mar 2023 09:29:55 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '12', 'connection': 'keep-alive', 'x-amzn-requestid': 'UGPL8B97NND16STSGROFN4D547VV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2770214093'}, 'RetryAttempts': 0}}
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return f'Sie haben {row[5]} {row[4]} bestellt!!!',""
            
        else:
            return 'Sie haben falsche Information(en) eingegeben, Bitte überprüfen Sie noch mal.',""
    # elif n_clicks > 0 or values is None:
    #     return 'Sie müssen Informationen eingeben'
    return 'Bitte Bestellinformationen eingeben.', ""

# Callback Funktion für book
@app.callback(
    Output("output", "children"),  Input("button", "n_clicks")
)
def empty_zone(n_clicks):
    time.sleep(5)
    return 'hallo'
@app.callback(
    Output("sum_book", "children"), Input("interval-book", "n_intervals")
 )   
def update_books(product):
    return get_total_orders("book")

# Callback Funktion für shoes
@app.callback(
    Output("sum_shoes", "children"), Input("interval-shoes", "n_intervals")
 )   
def update_shoes(product):
    return get_total_orders("shoes")

# Callback Funktion für plant
@app.callback(
    Output("sum_plant", "children"), Input("interval-plant", "n_intervals")
 )   
def update_plant(product):
    return get_total_orders("plant")

# #Verkäufe für das Produkt plant
# Erstelle in deinem Layout einen Header für die Verkaufsgrafik.
# Benutze deine Funktion get_productorders_timerange, um eine Abbildung für die Verkäufe für unser neues Produkt “plant” anzuzeigen.
# Hole dir hierfür gerne Inspiration aus dem Assignment für RDS.



if __name__ == "__main__":
    app.run_server(debug=True)

