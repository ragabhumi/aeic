# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:09:01 2021

@author: yosis
"""

from dash import dcc
from dash import html
import dash
from app import app
from app import server
from layouts import home_page, data_page, links, introduction_page, history_page, activity_page, facilities_page, financial_page, indonesia_page, malaysia_page, philippines_page, thailand_page, singapore_page, brunei_page, vietnam_page, laos_page, myanmar_page, links_page
from pages.about import introduction, history, activities, facilities, financial
import callbacks
from flask_caching import Cache


cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache',
    'CACHE_THRESHOLD': 1000
})
app.config.suppress_callback_exceptions = True

timeout = 20


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
@cache.memoize(timeout=timeout)
def display_page(pathname):
    if pathname == '/apps/home':
         return home_page
    elif pathname == '/apps/data':
         return data_page
    elif pathname == '/apps/indonesia':
         return indonesia_page
    elif pathname == '/apps/malaysia':
         return malaysia_page
    elif pathname == '/apps/philippines':
         return philippines_page
    elif pathname == '/apps/thailand':
         return thailand_page
    elif pathname == '/apps/singapore':
         return singapore_page
    elif pathname == '/apps/brunei':
         return brunei_page
    elif pathname == '/apps/vietnam':
         return vietnam_page
    elif pathname == '/apps/laos':
         return laos_page
    elif pathname == '/apps/myanmar':
         return myanmar_page
    elif pathname == '/apps/introduction':
         return introduction_page
    elif pathname == '/apps/history':
         return history_page
    elif pathname == '/apps/activities':
         return activity_page
    elif pathname == '/apps/facilities':
         return facilities_page
    elif pathname == '/apps/financial':
         return financial_page
    elif pathname == '/apps/links':
         return links_page
    else:
        return home_page # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=False, host = host, port = 8080)
