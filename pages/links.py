import dash_bootstrap_components as dbc
from dash import html
from function.structure import get_header, get_footer, get_emptyrow
from function.theme import corporate_colors, navbarcurrentpage, filterdiv_borderstyling, externalgraph_rowstyling, corporate_font_family

navigation = html.Div([
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href='/apps/home')),
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
                            nav=True,
                            ),
                        dbc.NavItem(dbc.NavLink("Links", active=True, href='/apps/links', style = navbarcurrentpage)),
                    ]
                )
            ],
            className = 'col',
            style = {'background-color' : corporate_colors['dark-grey'],
                    'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
            )

def links():
    page = html.Div([dbc.Col([

        #####################
        #Row 1 : Header
        get_header(),
        
        #####################
        #Row 3
        get_emptyrow(),
        
        html.Div([ # External row

        navigation,

            dbc.Alert([ # External row

                
                html.Div([
                    html.Table([
                        html.Tr([html.P(['1. ASEAN Members Country'], style={"font-weight":"bold", "text-align":"center"})]),
                        html.Tr([html.Td(['Brunei Darussalam']), html.Td(['Seismology web site in Brunei Darussalam'])]),
                        html.Tr([html.Td(['Cambodia']), html.Td(['Seismology web site in Cambodia'])]),
                        html.Tr([html.Td([html.A(['Indonesia'], href="https://inatews.bmkg.go.id/")]), html.Td(['InaTEWS (Indonesia tsunami Early Warning System)'])]),
                        html.Tr([html.Td(['LAO P.D.R']), html.Td(['Seismology web site in LAO P.D.R'])]),
                        html.Tr([html.Td([html.A(['Malaysia'], href="http://www.kjc.gov.my/")]), html.Td(['Seismology web site in Malaysia'])]),
                        html.Tr([html.Td(['Myanmar']), html.Td(['Seismology web site in Myanmar'])]),
                        html.Tr([html.Td([html.A(['Philippines'], href="http://www.phivolcs.dost.gov.ph/")]), html.Td(['Seismology web site in Philippines'])]),
                        html.Tr([html.Td([html.A(['Singapore'], href="http://app.nea.gov.sg/cms/htdocs/category_sub.asp?cid=53")]), html.Td(['Seismology web site in Singapore'])]),
                        html.Tr([html.Td(['Thailand']), html.Td(['Seismology web site in Thailand'])]),
                        html.Tr([html.Td(['Vietnam']), html.Td(['Seismology web site in Vietnam'])]),

                        html.Tr([html.P(['2. Others Country'], style={"font-weight":"bold", "text-align":"center"})]),
                        html.Tr([html.Td([html.A(['United States Geological Survey (USGS)'], href="http://app.nea.gov.sg/cms/htdocs/category_sub.asp?cid=53")]), html.Td(['Seismology web site in Singapore'])]),
                        html.Tr([html.Td([html.A(['Singapore'], href="http://earthquake.usgs.gov/recenteqsww/Quakes/quakes_all.html")]), html.Td(['You can click on the location and it will give you a map of where these earthquakes have occured around the globe. Shows the earth depths and gives you the magnitude. Very good visual information'])]),
                        html.Tr([html.Td([html.A(['Prototype International Data Center (PIDC)'], href="http://www.rdss.info/index_ie.html")]), html.Td(['PIDC Data Product (Global Earthquake)'])]),
                        html.Tr([html.Td([html.A(['C S E M'], href="http://www-csem.bruyeres.cea.fr/")]), html.Td(['Centre Sismologique Euro-Mediterraneen'])]),
                        html.Tr([html.Td([html.A(['I S C'], href="http://www.isc.ac.uk/")]), html.Td(['http://www.isc.ac.uk/'])]),
                        html.Tr([html.Td([html.A(['Recent World Earthquakes (Institude Of Geophysics)'], href="http://www.gphs.vuw.ac.nz/seismology/quakes_recent.html")]), html.Td(['RECENT WORLD EARTHQUAKES Victoria University of Wellington'])]),
                        html.Tr([html.Td([html.A(['Earthquake Research Institute - Univ. of Tokyo'], href="http://www.eri.u-tokyo.ac.jp/index.html")]), html.Td(['Earthquake Information'])]),
                        html.Tr([html.Td([html.A(['EARTHWORKS'], href="http://www.earthworks-jobs.com/")]), html.Td(['A world leading on-line database of  career opportunities for seismologists, geoscientists, geotechnical engineers, oceanographers, marine scientists, remote sensing/GIS staff, climate/atmospheric scientists and many others more.'])]),
                        html.Tr([html.Td([html.A(['Last two week Earthquake Maps'], href="http://www.eas.slu.edu/Earthquake_Center/quakemaps.html")]), html.Td(['Other locations in the rest of the world. Pick your area of interest. Updated every 6 hours.'])]),
                        html.Tr([html.Td([html.A(['Earthquake maps on the Web'], href="http://cires.colorado.edu/people/jones.craig/Web_EQs.html#globe")]), html.Td([' 	More maps for everywhere'])]),
                        html.Tr([html.Td([html.A(['ABAG Earthquake Maps And Information'], href="http://www.abag.ca.gov/bayarea/eqmaps/eqmaps.html")]), html.Td(['Seismology web site in Singapore'])]),
                        html.Tr([html.Td([html.A(['Plate Tectonics'], href="http://www.seismo.unr.edu/ftp/pub/louie/class/100/plate-tectonics.html")]), html.Td(['The cause of earthquakes'])]),
                        html.Tr([html.Td([html.A(['Earth s Interior'], href="http://www.seismo.unr.edu/ftp/pub/louie/class/100/interior.html")]), html.Td(['From the inside out on why we have earthquakes.'])]),
                        html.Tr([html.Td([html.A(['Susan Rosenberg s Quaking Home Page'], href="http://www.earthwaves.com/")]), html.Td(['Dedicated to the Art of Seismosurfing. Susan has put a lot of work into her pages and she has some excellent data.'])]),
                        html.Tr([html.Td([html.A(['Seismic Resources on the Web'], href="Seismic Resources on the Web ")]), html.Td(['Developed for high school teachers'])]),
                        html.Tr([html.Td([html.A(['The Richter Magnitude'], href="http://www.seismo.unr.edu/ftp/pub/louie/class/100/magnitude.html")]), html.Td(['A short answer'])]),
                        html.Tr([html.Td([html.A(['The Modified Mercalli Scale'], href="http://www.seismo.unr.edu/ftp/pub/louie/class/100/mercalli.html")]), html.Td(['From the University of Utah'])]),
                        html.Tr([html.Td([html.A(['Seismograph Stations'], href="http://www.seis.utah.edu/Welcome.html")]), html.Td(['Seismology web site in Singapore'])]),
                        html.Tr([html.Td([html.A(['Saint Louis Earthquake Center'], href="http://www.eas.slu.edu/Earthquake_Center/earthquakecenter.html")]), html.Td(['For your New Madrid earthquake information'])]),
                        html.Tr([html.Td([html.A(['Make your own seismogram'], href="http://www.geo.arizona.edu/tools/seismo")]), html.Td(['Has instructions'])]),
                        html.Tr([html.Td([html.A(['Carnegie Institution'], href="http://www.carnegieinstitution.org/")]), html.Td(['Has many earthquake related links'])]),
                        html.Tr([html.Td([html.A(['Earthquakes'], href="http://www.pcez.com/~richard/earthquake.htm")]), html.Td(['links page'])]),
                        html.Tr([html.Td([html.A(['The great 1906 Earthquake'], href="http://www.sfmuseum.org/1906/06.html")]), html.Td(['From the Museum of the City of San Francisco'])]),
                        html.Tr([html.Td([html.A(['Surfing the Internet for Earthquake Data'], href="http://www.geophys.washington.edu/seismosurfing.html")]), html.Td(['Lots of earthquake information from all over'])]),
                        html.Tr([html.Td([html.A(['Earthquake Information'], href="http://www-geology.ucdavis.edu/eqmandr.html")]), html.Td(['Lots more earthquake info plus links to discussion groups'])]),
                        html.Tr([html.Td([html.A(['The US Geological Survey'], href="http://quake.wr.usgs.gov/")]), html.Td(['Some good folks helping you to reduce earthquake hazards'])]),
                        html.Tr([html.Td([html.A(['Strong Motion Data Catalog Search'], href="http://www.ngdc.noaa.gov/mgg/gdas/gd_cri.Html")]), html.Td(['From the National Geophysical Data Center'])]),
                        html.Tr([html.Td([html.A(['Earthquake Geodesy'], href="http://earth.agu.org/revgeophys/hudnut01/hudnut01.html")]), html.Td(['And hazard monitoring'])]),
                        html.Tr([html.Td([html.A(['EarthQuake Data Explorer'], href="http://www.ldeo.columbia.edu/res/pi/EV/GEO/geo_main.html")]), html.Td(['Find your area of interest'])]),
                        html.Tr([html.Td([html.A(['Risk Prediction Initiative'], href="http://www.bbsr.edu/agcihome/sitelinks/quakes.html")]), html.Td(['Earthquake related links'])]),
                        html.Tr([html.Td([html.A(['Global Earthquake Response Center'], href="http://www.earthquake.com/")]), html.Td(['UCLA'])]),
                        html.Tr([html.Td([html.A(['Southern California Earthquake Center'], href="http://minotaur.ess.ucla.edu/")]), html.Td(['Seismology web site in Singapore'])]),
                        html.Tr([html.Td([html.A(['Understanding Earthquakes'], href="http://www.crustal.ucsb.edu/ics/understanding/")]), html.Td(['Excellent for students'])]),
                        html.Tr([html.Td([html.A(['Finding an earthquakes location with modern seismic networks'], href="http://quake.wr.usgs.gov/more/eqlocation")]), html.Td(['where was it'])]),
                        html.Tr([html.Td([html.A(['Earthquake'], href="http://www.teleport.com/~tacing/")]), html.Td(['Research breakthrough'])]),
                        html.Tr([html.Td([html.A(['Emergency Management Australia'], href="http://www.ema.gov.au/ema-eq.htm")]), html.Td(['From EMA'])]),
                        html.Tr([html.Td([html.A(['Insurance News Network'], href="http://www.insure.com/home/quake.html")]), html.Td(['Gives you information on earthquake insurance.'])]),
                        html.Tr([html.Td([html.A(['SAFE-T-PROOF'], href="http://www.safe-t-proof.com/")]), html.Td(['Earthquake Preparedness Specialists. You can check out their survival kits and the mobile earthquake simulator'])]),
                        html.Tr([html.Td([html.A(['QUAKES'], href="http://shake2.earthsciences.uq.edu.au/index.html")]), html.Td(['from our Australian friends'])]),
                        html.Tr([html.Td([html.A(['Damage Statistics '], href="http://www.dis-inc.com/quakecov.htm")]), html.Td(['for recent earthquakes through out the world'])]),
                        html.Tr([html.Td([html.A(['30 Year Probabilities'], href="http://www.freddiemac.com/function/fm-news/smm/0296/eqtable2.htm")]), html.Td(['of Major Earthquakes by Region'])]),
                        html.Tr([html.Td([html.A(['Deadliest Earthquakes on Record'], href="http://www.disasterrelief.org/Library/WorldDis/wde1_txt.html")]), html.Td(['Locations and Magnitudes'])]),
                        html.Tr([html.Td([html.A(['Earthquakes'], href="http://www.scholastic.com/bookclubs/arrow/arrow3.htm")]), html.Td(['more study for students'])]),
                        html.Tr([html.Td([html.A(['Earthquake Engineering'], href="http://www.takenaka.co.jp/takenaka_e/index.html")]), html.Td(['Cities harbour a great weakness when it comes to earthquakes'])]),
                        html.Tr([html.Td([html.A(['Planning for Earthquakes'], href="http://www.geophys.washington.edu/")]), html.Td(['measures for natural hazard prevention'])])
                    ])
                ], 
                className = 'col-12', style={'width': '80%', 'margin': "auto", "position": "relative", "text-align": "justify"}), 
                    
                ], style={"width":"100vw"}),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page
