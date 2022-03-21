# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:08:31 2022

@author: yosis
"""

import dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = 'ASEAN Earthquake Information Center'
server = app.server