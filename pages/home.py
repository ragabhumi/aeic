from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
from random import random
from function.structure import get_header, get_footer, get_emptyrow
from function.theme import corporate_colors, navbarcurrentpage


# Map Source
attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://ig.utexas.edu/marine-and-tectonics/plates-project/">UTIG Plate Project, Esri &mdash; National Geographic</a>'

ns_icon = Namespace("myNamespace", "myIcon")
ns_marker = Namespace("myNamespace", "myMarker")
ns_eq = Namespace("myEq", "myMarkerEq")
ns_latest_eq = Namespace("myLatestEq", "myMarkerLatestEq")
ns_trench = Namespace("myTectonic", "myTrench")
ns_transform = Namespace("myTectonic", "myTransform")
ns_ridge = Namespace("myTectonic", "myRidge")
ns_fault = Namespace("myTectonic", "myFault")
ns_slab = Namespace("myTectonic", "mySlab")

# Legenda
def legend(feature=None):
    return [html.B(["Recent EarthQuakes for ASEAN Countries"], style={"font-size":"large"})] + [html.Br()] \
        + [html.B(["(Magnitude >= 6.5)"], style={"font-size":"large"})] + [html.Br()] + [html.Br()] \
        + [html.B("Depth in km")] + [html.Br()] + [html.Br()] + [html.Table([html.Tr(\
        [html.Td([html.I(className="box", style={"background":"#FF0000", "vertical-align":"middle"})], style={"border":"none"})] + [html.Td([html.I("<=50 ", style={"font-size":"medium", "margin-left":"6%", "vertical-align":"middle"})], style={"border":"none"})]\
        + [html.Td([html.I(className="box", style={"background":"#FFA500", "vertical-align":"middle"})], style={"border":"none"})] + [html.Td([html.I("<=100 ", style={"font-size":"medium", "margin-left":"6%", "vertical-align":"middle"})], style={"border":"none"})]\
        + [html.Td([html.I(className="box", style={"background":"#FFFF00", "vertical-align":"middle"})], style={"border":"none"})] + [html.Td([html.I("<=250 ", style={"font-size":"medium", "margin-left":"6%", "vertical-align":"middle"})], style={"border":"none"})]\
        + [html.Td([html.I(className="box", style={"background":"#008000", "vertical-align":"middle"})], style={"border":"none"})] + [html.Td([html.I("<=600 ", style={"font-size":"medium", "margin-left":"6%", "vertical-align":"middle"})], style={"border":"none"})]\
        + [html.Td([html.I(className="box", style={"background":"#0000FF", "vertical-align":"middle"})], style={"border":"none"})] + [html.Td([html.I(">600 ", style={"font-size":"medium", "margin-left":"6%", "vertical-align":"middle"})], style={"border":"none"})]\
        )], style={"width":"100%", "border":"none"})]

legenda = dl.LayerGroup(id="info_delay", children=[html.Div(children=legend(), className="info", style={"position": "absolute", "bottom": "10px", "left": "10px", "z-index": "1000", "width":"22%", "text-align":"center"})])

def home():
    page = html.Div([dbc.Col([

        #####################
        #Row 1 : Header
        get_header(),
        
        #####################
        #Row 3
        get_emptyrow(),
        

        html.Div([ # External row

        html.Div([
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", active=True, href='/apps/home', style = navbarcurrentpage)),
                        dbc.NavItem(dbc.NavLink("Data", href='/apps/data')),
                        dbc.DropdownMenu(
                            [dbc.DropdownMenuItem("Indonesia", href='/apps/indonesia'),
                            dbc.DropdownMenuItem("Malaysia", href='/apps/malaysia'),
                            dbc.DropdownMenuItem("Philippines", href='/apps/philippines'),
                            dbc.DropdownMenuItem("Thailand", href='/apps/thailand'),
                            dbc.DropdownMenuItem("Singapore", href='/apps/singapore'),
                            dbc.DropdownMenuItem("Brunei DS", href='/apps/brunei'),
                            dbc.DropdownMenuItem("Vietnam", href='/apps/vietnam'),
                            dbc.DropdownMenuItem("Laos", href='/apps/laos'),
                            dbc.DropdownMenuItem("Myanmar", href='/apps/myanmar')],
                            label="Members",
                            nav=True
                            ),
                        
                        dbc.DropdownMenu(
                            [dbc.DropdownMenuItem("Introduction", href='/apps/introduction'),
                            dbc.DropdownMenuItem("History and Goals", href='/apps/history'),
                            dbc.DropdownMenuItem("Activities", href='/apps/activities'),
                            dbc.DropdownMenuItem("Facilities", href='/apps/facilities'),
                            dbc.DropdownMenuItem("Financial Support", href='/apps/financial')],
                            label="About",
                            nav=True
                            ),
                        dbc.NavItem(dbc.NavLink("Links", href='/apps/links')),
                    ]
                )
            ],
                className = 'col',
            style = {'background-color' : corporate_colors['dark-grey'],
                    'box-shadow': '2px 5px 5px 1px rgba(0, 100, 0, .5)'}
            ),

        html.Div([
            dl.Map(center=[6.0, 114.77], zoom=4, children=[
                
                dl.LayersControl(
                    [dl.BaseLayer(dl.TileLayer(url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', maxZoom=20, attribution=attribution), name="OpenStreetMap", checked= "Esri NatGeo World Map"),
                        dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri World Imagery", checked= "Esri NatGeo World Map"),
                        dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri World Topo Map", checked= "Esri NatGeo World Map"),
                        dl.BaseLayer(dl.TileLayer(url='https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', maxZoom=20, attribution=attribution), name="Esri NatGeo World Map", checked= "Esri NatGeo World Map")
                        ] + 
                [
                
                dl.Overlay(dl.GeoJSON(url="/assets/trench.geojson", id="trench", options=dict(style=ns_trench("style"), onEachFeature=ns_trench("bindPopup"))), name="Trench", checked=False),
                dl.Overlay(dl.GeoJSON(url="/assets/transform.geojson", id="transform", options=dict(style=ns_transform("style"), onEachFeature=ns_transform("bindPopup"))), name="Transform", checked=False),
                dl.Overlay(dl.GeoJSON(url="/assets/ridge.geojson", id="ridge", options=dict(style=ns_ridge("style"), onEachFeature=ns_ridge("bindPopup"))), name="Ridge", checked=False),
                dl.Overlay(dl.GeoJSON(url="/assets/slab.pbf", format="geobuf", id="slab", options=dict(style=ns_slab("style"), onEachFeature=ns_slab("bindPopup"))), name="Slab", checked=False)]),
                
                dl.LayerGroup(id="earthquake", children=[dl.GeoJSON(url="https://bmkg-content-inatews.storage.googleapis.com/aeicgempaQL.json?a="+str(random()), options=dict(pointToLayer=ns_eq("pointToLayer"), onEachFeature=ns_eq("bindPopup")))]),
                
                dl.LayerGroup(id="latest_earthquake", children=[dl.GeoJSON(url="/assets/latest_eq.json?a="+str(random()), options=dict(pointToLayer=ns_latest_eq("pointToLayer"), onEachFeature=ns_latest_eq("bindPopup")))]),
                
                dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="sqmeters", secondaryAreaUnit="hectares",
                                activeColor="#214097", completedColor="#972158"), legenda])
        ], style={'width': '100vw', 'height': 'calc(100vh - 193px)', 'margin': "auto", "position": "relative"}), 
            dcc.Interval(
                id='interval-component',
                interval=600*1000, # in milliseconds
                n_intervals=0
            ),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),

        ])
    ])

    return page