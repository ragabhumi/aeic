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
                            style = navbarcurrentpage
                            ),
                        dbc.NavItem(dbc.NavLink("Links", href='/apps/links')),
                    ]
                )
            ],
                className = 'col',
            style = {'background-color' : corporate_colors['dark-grey'],
                    'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
            )

def introduction():
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

                
                html.Div([html.B(['Introduction']),
                html.P(), html.P(['The ASEAN region is located at the intersection of three major tectonic plates namely Eurasian, Indo-Australian and the Pacific plates, and one minor plate, Philippine plate. This condition generates thousands of earthquake every year most of which are potentially destructive. In recent years, several big earthquakes occurred in some parts of ASEAN countries which caused considerable damage to buildings and other structures, landslides in mountainous regions, ground subsidence and ground rupture. These big earthquakes have also caused major fatalities. What makes an earthquake more devastating is the fact that it may generate tsunami with up to 10 meter high waves which add to the extent of the damage, especially in areas along the coast. ']),
                html.P(['To monitor earthquake activities, and to help mitigate the effects of earthquake disasters, most countries in ASEAN have established their National Seismological Centres (NSCs). While NSCs in some countries are quite modern, others are still in the process of upgrading. Ideally each of the upgraded NSC should have a real time monitoring system and other facilities for rapid dissemination of earthquake information.']),
                html.P(['ASEAN member countries have been striving to improve the capabilities of NSCs in their respective countries to enable NSCs to conduct various activities and research programme addressing earthquake prediction and monitoring, proper land use planning, seismic hazard and risk assessment with different levels of techniques and degrees of depth. These are all aimed at mitigating the risks of earthquakes to mankind. These efforts are, however, hampered by common problems relating to trained personnel and adequate seismic facilities. One way of overcoming these problems is to establish a regional seismic information center where the services and facilities already available could be shared by all ASEAN member countries.']) ], 
                className = 'col-12', style={'width': '80%', 'height': '100%', 'margin': "auto", "position": "relative", "text-align": "justify"}), 
                    
                ]),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page


def history():
    page = html.Div([dbc.Col([

        #####################
        #Row 1 : Header
        get_header(),
        
        #####################
        #Row 3
        get_emptyrow(),
        

        html.Div([ # External row

        navigation,

            dbc.Alert([            
                html.Div([html.B(['Brief History']),
                html.P(), html.P(['The concept of establishing the ASEAN Earthquake Information Centre (AIEC) was initially put forward by Directors of the National Meteorological Services of ASEAN countries during the 13th Meeting of the ASEAN Sub-Committee on Meteorology and Geophysics (SCMG) in August 1990. The AEIC was expected to be capable of disseminating information on big/strong earthquakes as early as possible occurring in the territories of ASEAN countries, and also to provide scientific and technical training of seismologists from members of ASEAN. The 13th Meeting of SCMG also endorsed that the Centre be co-located with the Meteorological and Geophysical Agency of Indonesia. The 40th Meeting of the Committee on Science and Technology held in October 2000 further endorsed the request of SCMG to obtain an approval from the ASC to  officially use the name "ASEAN Earthquake Information Centre (AEIC)".']),
                html.B(['Goals']),
                html.P(), html.P(['- To rapidly disseminate information on earthquakes and their associated events occurring in various parts of ASEAN countries to authorities and public.']),
                html.P(['- To provide communication tools for NSCs in ASEAN to exchange earthquake data.']),
                html.P(['- To build an earthquake data bank accessible to NSCs in ASEAN.']),
                html.P(['- To undertake research and training programs for improving the capability of the member countries to monitor and locate earthquakes, and to understand the earthquake mechanism and tectonic behaviour in the region']),
                html.P(['- To undertake collaborative work with other seismological centres in other regions with the aim of accelerating the transfer of knowledge and technology into the region.'])], 
                className = 'col-12', style={'width': '80%', 'height': '100%', 'margin': "auto", "position": "relative", "text-align": "justify"}),    
                ]),

        ],
        className = 'row sticky-top'),

        #####################
        #Row 5 : Footer
        get_footer(),

        ])
    ])

    return page

def activities():
    page = html.Div([dbc.Col([

        #####################
        #Row 1 : Header
        get_header(),
        
        #####################
        #Row 3
        get_emptyrow(),
        

        html.Div([ # External row

        navigation,

            dbc.Alert([            
                html.Div([html.B(['Past Activities']),
                html.P(), html.P(['In view of the need to rapidly disseminate earthquake information among ASEAN countries, the AEIC has started its activities since the name was first proposed by SCMG. With funding support from the MGA of Indonesia, the Centre issued regular earthquake bulletins which were available to all other ASEAN countries. The issuance of these bulletins were then discontinued due to some technical problems relating to the slowness of computer and communication facilities at the Indonesian NSC in processing earthquake data, and rapid dissemination of processed data to other NSCs in other countries.']),
                html.P(['Further improvement of facilities and human resources at the Centre was recently made with financial support from the Government of Indonesia allowing more facilities to be upgraded. As a result, near real time earthquake data could now be disseminated to other ASEAN NSCs and interested parties. The Centre also received a boost when it implemented a project on "ASEAN Network for Rapid Exchange of Strong Earthquake Data (ASNET-RESED)" with funding support from the Government of Japan. The project, completed in July 2000, was aimed at enhancing and interconnecting existing facilities of the NSCs of ASEAN countries via the internet to enable them to send and receive seismic data transmission as close to real-time as possible. To achieve the aim of the project, computer facilities were installed in each NSC in ASEAN, and relevant training was given to ASEAN seismologists and technicians.']),
                html.P(['nother significant achievement of the Centre is the establishment of a website of the AEIC (http://aeic.bmg.go.id) in April 2000. The website, hosted and managed by MGA of Indonesia, displays earthquake and related events and can be accessed by the general public. Further, two application systems for dissemination of earthquake information have been employed by the Centre. The first system allows automatic updating of earthquake information to be done in the web site. The second system allows earthquake data to be sent automatically to email addresses in the mailing list. Since August 2000, earthquake phase data and preliminary hypocenter have been sent automatically to all NSCs in ASEAN and other subscribed members. This information is also sent to the Tsunami alert system of the Japanese Meteorological Agency (JMA).']),
                html.B(['Current activities']),
                html.P(), html.P(['- Closely maintaining links with all NSCs in ASEAN countries.']),
                html.P(['- Continuously enhancing earthquake data exchange among NSCs in ASEAN.']),
                html.P(['- Maintaining and improving the Internet server (email, ftp and web server) at the Centre, and coordinating with other NSCs in upgrading their communication facilities.']),
                html.P(['- Continuously updating earthquake information in the Web allowing the public be informed of the latest earthquake events, and building data bank to enable scientists to carry out studies on earthquake-related subject in the region. ']),
                html.B(['Future activities']),
                html.P(), html.P(['With funding support from the MGA of Indonesia and also from external sources, the AEIC has identified the following activities in the future:']),
                html.P(['- To upgrade the email server and performance of the web page and the Centre and other NSCs, and to assist NSCs in some member countries to be linked through internet.']),
                html.P(['- To issue AEIC bulletin, electronic bulletin or/and printed materials for dissemination to registered members and the public.']),
                html.P(['- To promote public awareness through publication of earthquake manuals for distribution to schools and the general public.']),
                html.P(['- To conduct training programs and workshops on seismology-related areas such as hypocenter determination, focal mechanism, microzoning and regional tectonic activities.']),
                html.P(['- To collaborate with other advanced seismological centres in R&D in areas such as earthquake monitoring systems and earthquake prediction.']),
                html.P(['- To provide facilities for seismologists from member countries for research attachments. '])], 
                className = 'col-12', style={'width': '80%', 'margin': "auto", "position": "relative", "text-align": "justify"}),    
                ]),

        ],
        className = 'row sticky-top'),

        #####################
        #Row 5 : Footer
        get_footer(),

        ])
    ])

    return page

def facilities():
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

                
                html.Div([html.B(['Facilities']),
                html.P(), html.P(['A wide range of computer and information processing facilities are available at the Centre. For the purpose of rapid dissemination of earthquake information, the facilities are supported by IBM Unix and IBM PC machines with internet server facilities installed in each computer including the data server for collecting and compiling earthquake data using the Oracle data base management system. The AEIC computer network is connected to the Indonesian MGA computer network through Local Area etwork (LAN) and to the NSC of MGA. These networks are also connected to 5 Regional Seismological Centres (RSCs) of MGA through Wide Area Network (WAN) using VSAT communication.'])], 
                className = 'col-12', style={'width': '80%', 'height': '100%', 'margin': "auto", "position": "relative", "text-align": "justify"}), 
                    
                ]),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page

def financial():
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

                
                html.Div([html.B(['Financial support']),
                html.P(), html.P(['The MGA is prepared to financially support the operation and maintenance of the AEIC, which includes hardware and software maintenance, leased lines internet connection, leased telecom channel, electricity and staff salaries. Through the SCMG, the AEIC will seek, from time to time, external funding to support special programmes and activities, such as training and research.'])], 
                className = 'col-12', style={'width': '80%', 'height': '100%', 'margin': "auto", "position": "relative", "text-align": "justify"}), 
                    
                ]),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page