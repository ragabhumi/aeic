# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:09:17 2021

@author: yosis
"""

from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
from pages.members import *
from pages.home import home
from pages.about import introduction, history, activities, facilities, financial
from pages.members import indonesia, malaysia, philippines, thailand, singapore, brunei, vietnam, laos, myanmar
from pages.links import links
from function.structure import get_header, get_footer, get_emptyrow
from function.theme import corporate_colors, navbarcurrentpage, filterdiv_borderstyling, externalgraph_rowstyling, corporate_font_family

def datapage():
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
                        dbc.NavItem(dbc.NavLink("Home", href='/apps/home')),
                        dbc.NavItem(dbc.NavLink("Data", active=True, href='/apps/data', style = navbarcurrentpage)),
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
                            nav=True,
                            ),
                        
                        dbc.DropdownMenu(
                            [dbc.DropdownMenuItem("Introduction", href='/apps/introduction'),
                            dbc.DropdownMenuItem("History and Goals", href='/apps/history'),
                            dbc.DropdownMenuItem("Activities", href='/apps/activities'),
                            dbc.DropdownMenuItem("Facilities", href='/apps/facilities'),
                            dbc.DropdownMenuItem("Financial Support", href='/apps/financial')],
                            label="About",
                            nav=True,
                            ),
                        dbc.NavItem(dbc.NavLink("Links", href='/apps/links')),
                    ]
                )
            ],
                className = 'col',
            style = {'background-color' : corporate_colors['dark-grey'],
                    'box-shadow': '2px 5px 5px 1px rgba(0, 255, 0, .5)'}
            ),

            html.Div([ # External row

            html.Div([
            ],
            className = 'col-1'), # Blank 1 column

            html.Div([
                dash_table.DataTable(
                    id='recap-table',
                    cell_selectable = True,
                    column_selectable = False,
                    page_current=0,
                    page_size=1440
                )
            ], style = {'margin-bottom' : '5%'},
            className = 'col-10'),

            html.Div([
            ],
            className = 'col-1'), # Blank 1 column
            dcc.Interval(
            id='interval-component',
            interval=600*1000, # in milliseconds
            n_intervals=0
        ),

        ],
        className = 'row',
        style={'width': '100%'}
        ),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page


home_page = home()

data_page = datapage()

introduction_page = introduction()

history_page = history()

activity_page = activities()

facilities_page = facilities()

financial_page = financial()

indonesia_page = indonesia()
malaysia_page = malaysia()
philippines_page = philippines()
thailand_page = thailand()
singapore_page = singapore()
brunei_page = brunei()
vietnam_page = vietnam()
laos_page = laos()
myanmar_page = myanmar()

links_page = links()
