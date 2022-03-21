# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:08:50 2021

@author: yosis
"""

from dash.dependencies import Output, Input
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
import pandas as pd
import dash
from app import app
from random import random
import json
import urllib

####################################################################################################
# 003 - SHOW DATA
####################################################################################################
@app.callback(
    [dash.dependencies.Output('recap-table', 'data'), dash.dependencies.Output('recap-table', 'columns'), dash.dependencies.Output('recap-table', 'style_cell_conditional'), dash.dependencies.Output('recap-table', 'style_data'), dash.dependencies.Output('recap-table', 'style_data_conditional'), dash.dependencies.Output('recap-table', 'style_header')],
    [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_table(n):
    # Baca data json

    with urllib.request.urlopen("https://bmkg-content-inatews.storage.googleapis.com/aeicgempaQL.json") as url:
        data_eq = json.loads(url.read().decode())
        
    data_eq = pd.json_normalize(data_eq["features"])
    print(data_eq)
    data_eq['DATE'] = pd.to_datetime(data_eq['properties.time']).dt.date
    data_eq['TIME'] = pd.to_datetime(data_eq['properties.time']).dt.time

    data_eq[['LON','LAT', 'idx']] = pd.DataFrame(data_eq['geometry.coordinates'].tolist(), index= data_eq.index)

    
    data_eq.rename(columns={"properties.mag": "MAGNITUDE", "properties.place": "REGION", "properties.depth": "DEPTH (KM)"}, inplace=True)
    data_eq['NO'] = data_eq.index + 1
    data_eq = data_eq.drop(['type', 'properties.id', 'properties.time', 'properties.fase', 'properties.status', 'geometry.type', 'geometry.coordinates'], axis = 1)
    data_eq = data_eq[['NO', 'DATE', 'TIME', 'LAT', 'LON', 'MAGNITUDE', 'DEPTH (KM)', 'REGION']]
    data_eq['LAT'] = data_eq['LAT'].astype('float').round(decimals=2)
    data_eq['LON'] = data_eq['LON'].astype('float').round(decimals=2)
    data_eq['MAGNITUDE'] = data_eq['MAGNITUDE'].astype('float').round(decimals=1)
    data_eq['DEPTH (KM)'] = data_eq['DEPTH (KM)'].astype('float').round(decimals=0)

    data=data_eq.to_dict('records')
    
    columns=[{"name": i, "id": i} for i in data_eq.columns]

    style_cell_conditional=[
        {
            'if': {'column_id': i},
            'textAlign': 'left'
        } for i in ['NO', 'DATE']
    ],
    style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    }

    return data, columns, style_cell_conditional, style_data, style_data_conditional, style_header

####################################################################################################
# 008 - UPDATE EARTHQUAKE & LATEST EARTHQUAKE LOCATIONS
####################################################################################################
ns_eq = Namespace("myEq", "myMarkerEq")
ns_latest_eq = Namespace("myLatestEq", "myMarkerLatestEq")

@app.callback(Output("latest_earthquake", "children"), [Input('interval-component', 'n_intervals')])
def update_latest_eq(n):
    with urllib.request.urlopen("https://bmkg-content-inatews.storage.googleapis.com/aeicgempaQL.json") as url:
        data_eq = json.loads(url.read().decode())
    latest_eq = {'type': "FeatureCollection", 'features': [data_eq['features'][0]]}

    fig = dl.LayerGroup(id="latest_earthquake", children=[dl.GeoJSON(data=latest_eq, options=dict(pointToLayer=ns_latest_eq("pointToLayer"), onEachFeature=ns_latest_eq("bindPopup")))])
    return fig

@app.callback(Output("earthquake", "children"), [Input('interval-component', 'n_intervals')])
def update_eq(n):
    fig = dl.LayerGroup(id="earthquake", children=[dl.GeoJSON(url="https://bmkg-content-inatews.storage.googleapis.com/aeicgempaQL.json?a="+str(random()),  options=dict(pointToLayer=ns_eq("pointToLayer"), onEachFeature=ns_eq("bindPopup")))])
    return fig
