from dash import html
from app import app
from function.theme import corporate_colors


#####################
# Header with logo
def get_header():

    header = html.Div([

        html.Div([
            html.Img(
                    src = app.get_asset_url('aeic.png'),
                    height = '100 px',
                    width = 'auto')
            ],
            className = 'col-2',
            style = {
                    'align-items': 'center',
                    'padding-top' : '0.5%',
                    'padding-bottom' : '0.5%',
                    'height' : 'auto'}),

        html.Div([
            html.H1(children='ASEAN EARTHQUAKE INFORMATION CENTER',
                    style = {'textAlign' : 'center'}
            )],
            className='col-8',
            style = {'padding-top' : '0.5%'}
        ),


        html.Div([], className = 'col-2') #Same as img width, allowing to have the title centrally aligned

        ],
        className = 'row',
        style = {'height' : '4%',
                'background-color' : corporate_colors['darkest-grey']}
        )

    return header

#####################
# Footer
def get_footer():
    footer = html.Div([
        html.Div([ # External row
        get_emptyrow(),
        html.H5(children='Copyright \u00A9 AEIC 2022',
                    style = {'textAlign' : 'center'}
            )
    ],
        style = {'position': 'fixed', 'bottom' : '0', 'width' : '100vw',
                'background-color' : corporate_colors['darkest-grey']}, className = 'col-12')
        ], className = 'row')
    
    return footer

#####################
# Empty row

def get_emptyrow(h='3px'):
    """This returns an empty row of a defined height"""

    emptyrow = html.Div([
        html.Div([
            html.Br()
        ], className = 'col-12')
    ],
    className = 'row',
    style = {'height' : h, 'background-color' : corporate_colors['green']})

    return emptyrow