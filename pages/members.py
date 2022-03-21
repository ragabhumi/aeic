import dash_bootstrap_components as dbc
from dash import html
from app import app
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
                            nav=True,
                            style = navbarcurrentpage
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
                    'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
            )

def indonesia():
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

                
                html.Div([html.P(['Tectonic Earthquake Monitoring in Indonesia'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Introduction']), 
                html.P(), html.P(['Indonesia  is one of the most earthquakes-prone countries of the world. Because of Indonesia is at the convergence of three active tectonic plates which are generating the earthquake. A study of historical earthquakes recorded throughout the world shows that most of the epicenters of major earthquake events are concentrated in this mobile area. Some of the destructive earthquake in Indonesia that occurred in this area, including the Aceh earthquake(2004), Nias earthquake (2005), Pangandaran earthquake (2006) and Mentawai Earthquake (2010). Not a bit of loss of life and property caused by the earthquake. Therefore, monitoring of seismic activity in Indonesia is an important part in order to reduce the risk of earthquakes.']),
                html.P(['After the Aceh tsunami earthquake December 2004, Indonesia strengthening earthquake monitoring network to support the establishment of the tsunami early warning system in Indonesia. Reinforcement in the form of increasing the number and type of sensors used in monitoring earthquakes. Currently 162 broadband seismometers and 237 accelerometer has installed spread all over Indonesia to monitor seismic activity in the region. With this development, Indonesia is able to inform the parameters of earthquakes in less than 5 minutes after the earthquake. ']),
                html.P(), html.P(), html.B(['Tectonic Setting and Seismicity of Indonesia']), 
                html.P(), html.P(['Indonesia lies on the boundaries of three tectonic plates, which slide past each other. These three tectonic plates are: The continental-oceanic Indo-Australian Plate to the south, the oceanic Pacific Plate to the east, the Eurasian Plate to the north(where most of Indonesia area lies), and the Philippine Plate. The Indo-Australian Plate moves north, colliding the Eurasian Plate. The Pacific Plate moves west, whereas the Eurasian Plate in relation to the other plate is not moving.']),
                html.P(['The relative movement between these four tectonic plates causes an accumulation  of pressure and mechanical stress where they collide. When the material’s elasticity is no longer able to withstand this stress, the rock will break and spring back to something close to its original shape. This rebound, which generates strong seismic waves that radiate in all directions along the tectonic plate, is called a tectonic earthquake.']),
                html.P(['Millions of these earthquakes have occurred over thousands and millions of years on the geological time scale. Evidence of these past earthquakes is recorded in natural geological phenomena (paleo-seismology). Today earthquake can be recorded using seismometer networks, which calculate an earthquake location and focal depth (hypocenter) and measure its magnitude. Approximately 4000 earthquakes happened in Indonesia per year, whereas earthquake of magnitude greater than 5.5, or earthquake that can be physically felt on land, average around 70 – 100 per years, and destructive earthquakes around one to two times a year. Between 1991 – 2011, 186 significant earthquakes were recorded in Indonesia seismic network.']),
                html.P(), html.P(), html.B(['Indonesian Seismic Network']), 
                html.P(), html.P(['Post the Aceh earthquake December 26, 2004, the government of Indonesia, decided to develop a network of digital seismic for the monitoring of regional seismic station for monitoring of regional seismicity and to collect data for tsunami early warning system. In order to monitor seismic activity in Indonesia and surrounding areas, Indonesia has developed an earthquake monitoring network consisting of Broadband Seismometers and Accelerometers spread in the region of Indonesia.  By using these new seismic networks and new seismic data analysis, Seiscomp3, Indonesia has been able to provide earthquake information to the interface institution and public less than 5 minutes after the earthquake occurred.']),
                html.Img(src = app.get_asset_url('ina_seismic.gif')),
                html.P(), html.P(['Figure-1: Indonesian seismic network consist of national center and 10 regional centers.'], style={"text-align":"center"}),
                html.P(['Indonesia is currently operating and maintaining 162 broadband seismometers and 237 accelerometers. Some of the accelerometer placed collocated with broadband seismometers location. Using telemetry equipment and VSat lines, these digital recordings are transmitted on  real-time mode to the central processing system at BMKG. The data are processed and issued as earthquake bulletin or tsunami warning by the central office.']),
                html.P(), html.P(), html.B(['Institution that monitor the tectonic earthquakes in Indonesia']),
                html.P(['Monitoring of tectonic earthquakes and tsunami activities in Indonesia are doing by Agency for Meteorology, Climatology, and Geophysics (BMKG) which is conducted in deputy of geophysics. Accordance with Director General of BMKG’s regulation Number: KEP 03 in 2009, about the organization and work procedure of BMKG that the deputy of geophysics is executive element of some tasks and functions of BMKG in geophysics section who is responsible to Director General of BMKG.']),
                html.P(['Deputy of geophysics has tasks on formulating, executing, and controlling the implementation of technical policies, and implementing on data and information service in geophysics section. The organizational structure in deputy of geophysics is as follows :']),
                html.P(['Deputy of geophysics consists of :']),
                html.Ul([html.Li(['Center of Earthquake and Tsunami']), html.Li(['Center of Seismology  Engineering, Geophysical Potential and Time Signal'])]),
                html.P(), html.P(), html.B(['A. Center of Earthquake and Tsunami']),
                html.P(['Center of earthquake and tsunami has tasks on implementing the technical policies formulation, provisioning of technical assistance, technical guidance, and controlling of technical policies, coordination of functional activities and cooperation, management, and services of data and information, as well as early warning in earthquake and tsunami division.']),
                html.P(['CEarthquake and Tsunami Center consists of 3 divisions, there are:']),
                html.Ol([html.Li(['Division of Earthquake and Tsunami Early  Information.']), html.Li(['Division of Earthquake and Tsunami Mitigation.']), html.Li(['Division of Earthquake and Tsunami Mitigation.'])]),
                html.B(['1. Division of Earthquake and Tsunami Early Information']),
                html.P(['has tasks on implementing the disseminating of earthquake information and tsunami early warning. In performing its duties, early information division conduct the function of the implementation on monitoring, processing and data analyzing as well as dissemination of earthquake information; and implementation on monitoring, processing and data analyzing as well as dissemination of tsunami early warning.']),
                html.P(['Division of Earthquake and Tsunami Early Information consists of :']),
                html.P(['a. Earthquake Information Sub-Division; and ']),
                html.P(['b. Tsunami Information Sub-Division']),
                html.P(['Earthquake Information Sub-Division has tasks on data monitoring, processing, and analysing as well as dissemination of earthquake information.']),
                html.P(['Tsunami Early Warning Sub-Division has tasks on data monitoring, processing, and analysing as well as dissemination of tsunami early warning.']),
                html.B(['2. Division of Earthquake and Tsunami Mitigation']),
                html.P(['has tasks on implementing the services of data and information in division of earthquake and tsunami mitigation. In performing its duties, Division of Earthquake and Tsunami Mitigation conduct the function of the implementation on services of data and information for earthquake disaster mitigation and services of data and information for tsunami disaster mitigation.']),
                html.P(['Division of Earthquake and Tsunami Mitigation consists of :']),
                html.P(['a. Earthquake Mitigation Sub-Division; and']),
                html.P(['b. Tsunami Mitigation Sub-Division ']),
                html.P(['Earthquake Mitigation Sub-Division has duty to perform services in earthquake disaster mitigation.']),
                html.P(['Tsunami Mitigation Subdivision has duty to perform services in tsunami disaster mitigation.']),
                html.B(['3. Division of Earthquake and Tsunami Operation Development']),
                html.P(['has tasks of preparing materials for formulation of technical policies, provisioning of technical assistance, preparation of development’s materials as well as controlling of technical policies, coordination of functional activities and cooperation in earthquake and tsunami operation development division.']),
                html.P(['In performing its duties, Division of Earthquake and Tsunami Operation Development conduct the function of preparing materials for formulation of technical policies in earthquake and tsunami operation development division, provisioning of technical assistance, preparation of development’s materials as well as controlling of technical policies in earthquake and tsunami operation development division, and implementation for coordination of functional activities and cooperation in earthquake and tsunami operation development division.']),
                html.P(['Division of Earthquake and Tsunami Operation Development consists of :']),
                html.P(['a. Earthquake Operation Development Sub-Division; and']),
                html.P(['b. Tsunami Operation Development Sub-Division']),
                html.P(['Earthquake Operation Development Sub-Division has tasks on preparing materials for technical policies formulation, provisioning technical assistance, preparation of development’s materials as well as controlling of technical policies, coordination of functional activities and cooperation in earthquake operation development sub-division.']),
                html.P(['Tsunami Operation Development Sub-Division has tasks on preparing materials for technical policies formulation, provisioning technical assistance, preparation of development’s materials as well as controlling of technical policies, coordination of functional activities and cooperation in tsunami operation development sub-division.']),
                
                html.P(), html.P(), html.B(['B. Center of Engineering Seismology, Potential Geophysics and Time Signal']),
                html.P(['Center of Engineering Seismology, Potential Geophysics and Time Signal has tasks on implementing the technical policies formulation, provisioning of technical assistance, technical guidance, and controlling of technical policies, coordination of functional activities and cooperation, management, and services of data and information in division of engineering seismology, potential geophysics and time signal.Center of Engineering Seismology, Potential Geophysics and Time Signal consists of :']),
                html.Ol([html.Li(['Division of Engineering Seismology']), html.Li(['Division of Potential Geophysics and Time Signal']), html.Li(['Division of Operation Development for Engineering Seismology, Potential Geophysics, and Time Signal.'])]),
                html.B(['1. Division of Engineering Seismology ']),
                html.P(['has tasks on implementing the services of data and information in division of engineering seismology. In performing its duties, Division of Engineering Seismology conduct the function of the implementation on monitoring, collecting, processing, and analyzing data in seismology engineering division, preparing materials for information services in engineering seismology division, and performing information services in engineering seismology division.']),
                html.P(['Division of Engineering Seismology consists of :']),
                html.P(['a. Engineering Seismology Data Sub-Division; and']),
                html.P(['b. Engineering Seismology Information Sub-Division']),
                html.P(['Engineering Seismology Data Sub-Division has tasks on monitoring preparation, collecting, processing and analyzing in division of engineering seismology data.']),
                html.P(['Engineering Seismology Information Sub-Division has tasks on preparing materials for services in division of engineering seismology information.']),
                html.B(['2. Division of Potential Geophysics and Time Signal']),
                html.P(['has tasks on implementing the services of data and information in division of earth’s magnetic, air electrical, gravity, and time signal. In performing its duties, Division of Potential Geophysics and Time Signal conduct the function of the implementation on data and information services in division of earth’s magnetic, air electrical, and performing data and information services in division of gravity and time signal. ']),
                html.P(['Division of Potential Geophysics consists of :']),
                html.P(['a. Earth’s Magnetic and Air Electrical Sub-Division; and']),
                html.P(['b. Gravity and Time Signal Sub-Division']),
                html.P(['Earth’s Magnetic and Air Electrical Sub-Division has tasks on implementing the services of data and information in division of earth’s magnetic and air electrical.']),
                html.P(['Gravity and Time Signal Sub Division has tasks on implementing the services of data and information in division of gravity and time signal.']),
                html.B(['3. Division of Operation Development for Engineering Seismology, Potential Geophysics, and Time Signal']),
                html.P(['has tasks of preparing materials for formulation of technical policies, provisioning of technical assistance, preparation of development’s materials as well as controlling of technical policies, coordination of functional activities and cooperation in division of operation development for engineering seismology, potential geophysics, and time signal.']),
                html.P(['In performing its duties, Division of Operation Development for Engineering Seismology, Potential Geophysics, and Time Signal conduct the function of preparing materials for formulation of technical policies, provisioning of technical assistance and development, controlling of technical policies, and implementation for coordination of functional activities and cooperation in division of operation development of engineering seismology, and  preparing materials for formulation of technical policies, provisioning of technical assistance and development, controlling of technical policies, and implementation for coordination of functional activities and cooperation in division of operation development of potential geophysics and time signal.']),
                html.P(['Division of Operation Development for Engineering Seismology, Potential Geophysics, and Time Signal consists of :']),
                html.P(['a. Operation Development for Engineering Seismology Sub-Division; and']),
                html.P(['b. Operation Development for Potential Geophysics and Time Signal Sub-Division.']),
                html.P(['Operation Development for Engineering Seismology Sub-Division has tasks on preparing materials for technical policies formulation, provisioning technical assistance and development, controlling of technical policies, implementation for coordination of functional activities and cooperation in division of operation development for engineering seismology.']),
                html.P(['Operation Development for Potential Geophysics and Time Signal Sub-Division has tasks on preparing materials for technical policies formulation, provisioning technical assistance and development, controlling of technical policies, implementation for coordination of functional activities and cooperation in division of operation development for potential geophysics and time signal. '])                
                ], 
                className = 'col-12', style={'width': '80%', 'height': '100%', 'margin': "auto", "position": "relative", "text-align": "justify"}), 
                    
                ], style={'height': '100%'}),

        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ], style={'padding-bottom': '0'})
    ])

    return page

def malaysia():
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

                
                html.Div([html.P(['Earthquake Monitoring System In Malaysia'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Introduction']), 
                html.P(), html.P(['Malaysia is situated on the southern edge of the Eurasian. It is closed to the most two seismically active plate boundaries, the inter plate boundary between the indo-Australian and Eurasian plates on the west and the inter-plate boundary between the Eurasian and Philippines plates on the east. Major Earthquake originating from these plate boundaries have been felt in Malaysia. Several possible active faults have been delineated and local earthquakes in east Malaysia appear to be related to some of them. ']),
                html.P(['Peninsular Malaysia is classified as a seismically stable area. There has been no known record of local earthquakes so for, except some reservoir-included events over the Kenyir Dam area in Terengganu (Fig.2) between 1984 to 19986. However, the west coast of peninsular Malaysia is affected by tremors originating from large Sumatran earthquakes on the average of 1.5 t 2 tremors a years [1]. The maximum intensity observed so far was V on the modified Mercalli (MM) scale.']),
                html.P(['According to the study based on earthquakes with body wave magnitude 4 and above located within a radius of 450 km of the Penang island during the period 1976 to 1990, the return periods for different magnitudes were found to be as follows[2]: ']),
                html.Table([
                    html.Tr([html.Td([html.B(['Magnitude'])]), html.Td(['4.0']), html.Td(['5.0']), html.Td(['5.5']), html.Td(['6.0']), html.Td(['6.5']), html.Td(['7.0'])]),
                    html.Tr([html.Td([html.B(['Return Period (year)'])]), html.Td(['0.3']), html.Td(['1.01']), html.Td(['2.07']), html.Td(['3.95']), html.Td(['7.52']), html.Td(['14.30'])])]),
                html.P(), html.P(['East Malaysia, on the other hand, is classified as moderately active in Seismicity mainly Sabah. It has experienced earthquakes of local origin (Fig.3) with magnitudes of up to 5.8 on the Richter scale. Some of these resulted in some damages on properties [3]. The maximum intensity observed so far was VII on the MM scale. In addition to the local earthquakes, east Malaysia is also affected by tremors originating from large earthquakes located over southern Philippines and in the Straits of Macassar, Sulu Sea and Celebes Sea.']),
                html.P(['It is important to be noted that earthquakes do not need to be of large magnitude to produce severe damage, because the degree of damage depends not only on the physical size of an earthquake but also on other factors such as where and when an earthquakes occurred, the population density in the area concerned and secondary events such as fire.']),
                html.P(), html.P(), html.B(['Seismic network ']), 
                html.P(['In the late sixties, the government of Malaysia decided to monitor seismic actives in and around the country systematically to meet increasing demand for seismological information. In order to achieve this purpose., the seismological division was established in 1974 at Malaysian Meteorological Services MMS) ']),
                html.P(['Instrumental recording of seismic event in Malaysia began only 1975 with the establishment of the first seismological station at Petaling Jaya (KLM) under the seismological programs for South East Asia sponsored by UNESCO. At the moment , MMS operates a total of ten seismological station throughout the country. Five in peninsular Malaysia, namely Petaling Jaya (KLM) , Kuala Lumpur (FRM), Ipoh (IPM), Kluang (KGM), and Kuala Terengganu (KTM), and five in East Malaysia, namely Kota Kinabalu (KKM), Kudat (KDM), Tawau (TSM), Bintulu (BTM), and Kuching (KGM). ']),
                html.P(['Two station (Ipoh and Kota Kinabalu) are equipped with the short period three component seismographs. One station (Bintulu) is equipped with the short period three component seismographs and also three component strong -motion accelerographs. Another seven stations are equipped with the standar short period veritical component seismographs. By end of 1998, MMS would install two more seismological stations in east Malaysia as a continuing effoert to further upgrade its national monitoring network.']), 
                html.P(['Digital recorders were first introduce in the department in November 1993. At the same time, MMS installed a PC-based Seismic Data Acquisition System SDAS) centered at the headquarter KLM, to link up all the stations by telephone lines. The system would enable seismic data at the seismological stations to be retrieved at pre-programmed times or whenever necessary. ']), 
                html.P(['MMS server as the national information center for seismology in the country. Apart from MMS, other agencies also installed seismograph and accelerographs at the dam sites and others facilities. However reports on their performance are not available.']),
                html.P(['See the Web site ', html.Br(), html.A(['Seismology on Malaysia'], href="http://www.kjc.gov.my")])], 
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

def philippines():
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
                html.Div([html.P(['Earthquake and Volcano Monitoring Network in the Philippines'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Summary']), 
                html.P(), html.P(['The Philippines is considered to be one of the most earthquakes-prone countries of the world. There are a number of earthquake generators in the country. The archipelago is bounded by oppositely-dipping subduction zones. As well as transected by a number of fault, where movement are periodically detected through the recordings of tectonic earthquakes.']),
                html.P(['At least five imperceptible to perceptible earthquakes occurs per day. However, there are some regions of the country, which are considered more earthquake prone than others, such as east tern Mindanao, Leyte and Samara which host an average of 16 felt earthquakes per year. The most recent destructive earthquakes were the 16 august 1976 Moro gulf earthquakes (Ms=7.9), which triggered a tsunami, the 16 July 1990 Luzon earthquakes (Ms=7.8) , which was generated by movement along the northern segment of the Philippine fault zone and the 15 November 1994 Mindoro earthquakes (ms=7.1) which like wise triggered a tsunami.']),
                html.P(['Seismological observation in the Philippines could be traced as early as 1884. but it was only after 1986 that the Philippine institute of volcano logy and seismology Come in to being , which took on the responsibility of seismic monitoring in the country.']),
                html.P(['PHIVOLCS is currently operating and maintaining 29 manned seismic observatories, 6 volcanological observatories and 3 telemetered station. Each manned station is equipped with short period seismographs operating on a 24-hours basis. Daily transmissions of seismic data to the central office in question city are done through single side band radios or through telephone lines. The data are processed and issued as earthquake bulletin by the crisis by central office. During occurrence of destructive earthquakes, PHIVOLCS respond to the crisis by sending a quick response team. QRT, which conduct seismic monitoring of aftershock, geological investigation, impact assessment and information dissemination. Like wise PHIVOLCS also conduct public awareness program on the earthquake hazards in the Philippine and how they can be mitigated on a regular basis.']),
                html.P(['By improving the earthquakes monitoring and prediction capability of the institute we may be able to minimize, if not totally eliminate disaster whish may arise from the occurrences of large-magnitude earthquakes in the Philippines.']),
                html.P(), html.P(), html.B(['Introduction']),
                html.P(["The Philippines archipelago is one of the world's most tectonically active areas inasmuch as it is situated along the circum-pacific belt of fire. As an offshoot of this geographic, geologic and tectonic setting, the country is highly vulnerable to such natural disaster as volcanic eruption , occurrences of destructive earthquake and other relative phenomena. A study of historical earthquakes recorded throughout the world shows that most of the epicenters of major earthquake events are concentrated in this mobile belt."]),
                html.P(["There are two major tectonic plate movement influencing the tectonic activity in the Philippines. The north westward moving pacific plate is currently pushing the Philippine sea plate toward the eastern side of the archipelago. The rate of movement is about seven centimeter per year. On the other hand , the oceanic region of the slower moving Eurasian plate are being sub ducted along the western side of Luzon and MINDORO. At the rate of three centimeter per year. The movement of the northeastward component of the Eurasian plate is sustaining the active collision of the continental block of Palawan with MINDORO and that of the northern sections of the Zamboanga peninsula with western MINDORO."]),
                html.P(["There are eight major and several minor earthquakes generator in the Philippines. These major tectonic structures are zones where differential movement of solid material are likely to occur and consequently generating earthquakes. The Philippines is bounded by several trenches: on the west by east dipping manila trench, Negros trench and sulu trench; on the east by west dipping Philippine trench. And on the south by east dipping Cotabato trench and west dipping Davao trench. Thus, the Philippines can be described as a wedge caught between two oppositely -dipping subduction zones. The archipelago is likewise transected by numerous faults of normal, wrench, Tran current and thrust fault types that form lineament in the Philippine landscape. Foremost among these zones of weakness is the Philippine fault zone, which extends from northern Luzon to eastern Visayas too as far south as eastern Mindanao. The distribution of earthquake occurrences in the country is greatly influenced by these tectonic process."]),
                html.P(), html.P(), html.B(['Seismicity in Philippines']),
                html.P(["The Philippines hosts at least five imperceptible to perceptible earthquake per day. However, not all parts of the country are equally vulnerable to destructive earthquakes. Based on spatial distribution of earthquake events, the most seismically active region are eastern Mindanao, Leyte , Samara with and average of 16 perceptible tremors per year. The seismic activity in these regions can be directly be attribute to movement along the Philippine trench and the Philippine fault zones. Other relatively active regions are found at the eastern sector of northern Luzon and areas in the vicinity of Lubang island and MINDORO. Needed to adequately cover the Philippine archipelago and be able to locate earthquakes more accurately."]),
                html.P(["The seismic station if PHIVOLCS are equipped with short period seismographs and are manned by well-trained personal on a 24-hour basis. Seismic data from each of the seismic station SRE relayed every morning to the central office in question city using single side band SSB radio transceiver or via telephone for processing, interpretation and dissemination. The filed personal are also required to report to the central office seismic data of felt events or those with magnitude 4 and above immediately after their occurrence. Earthquake parameter are determined with the use of computerized hypo central determination program utilizing a dapped least squared algorithm and a velocity model adapted from Jeffrey and Bullen. It required a minimum of five P- arrival data and if possible one good S-arrival. Accuracy of epicenter location is determined by the root mean square rms, with minimal number of iteration every 1km and less than 1.0 rms. Implying greater degree of confidence in determination. Accuracy of plotting are in the order of +/- 5-15 kms. For magnitude calculation, a quick basic program maggal2 utilizes formula developed by Uy and Punzalan.1985. for the Philippine earthquakes. The data required are time duration and distance of the epicenter to the recording stations. Results are displayed in local magnitude, surface magnitude and body magnitude. Magnitude calculations are based on data from calibrated PHIVOLCS seismograph already located in predetermined seismic stations."]),
                html.P(["A sts1 and sts2 broad band seismic observation system is in operation at out Tagaytay and Baguio seismic station respectively. The equipment are being maintained in cooperation with DPRI, Kyoto university. Data are stored in mo-disk and are also available in analogue record. A program of global alliance of regional network (garnet) has been conceived by scientist at several research institution in Japan and funded by Japanese science and technology. Agency. The primary goal of garnet project is to enhance international cooperation, coordination and communication in observational seismology through a program of tele seismic waveform data exchange among regional and national seismic networks for selected earthquakes worldwide to study the earth deep structure. Hardware were provided by the project and digital record were sent to Japan for analysis and interpretation."]),
                html.P(["At the rate , the cities are growing, and with the current government efforts to accelerate industrial development by putting up more building , road, power plant and other infrastructures, the need for a wider database becomes apparent since seismic risk is relatively greater in populated areas. Photographic strong motion accelerograph in metro manila. With the help of the USGS donated spare art, Kinematrics SMA aut of operation for a long time were repaired and calibrated. Likewise Kyoto University donated 3 analogue strong motion accelographs and where installed in Mindanao. For the 1998 , in cooperation with Tokyo institute of technology , 8 strong motion digital accerlograph will be operational in metro manila."]),
                html.P(["To keep the public and authorizes informed, an earthquakes bulletin is issued for each major earthquakes, which contain all the details of events. During times of earthquakes crisis. PHIVOLCS send a quick response team QRT to conduct immediate impact assessment and install and operate temporary seismic stations to monitor aftershock in the area. PHIVOLCS likewise coordinates with various disaster management agencies such as the disaster coordinating council. Office of civil defense, Philippine national red cross, also conduct public awareness programs through periodic tours of schools and communities, giving lectures//seminar and exhibits on earthquakes hazards and safety measures before, during and after earthquakes occurrences."]),
                html.P(), html.P(), html.B(['Future Plan']),
                html.P(["Modernization of seismic instrument system is also desired with the uses of telemetred and digital instrument. A JICA project to improve the earthquakes and volcano monitoring capability of PHIVOLCS is being worked out between the Philippine and the Japanese government. Thirty three 33 sites for earthquakes and volcano monitoring station were identified for improvement by telemetered to on central recording station and three sub center. These station will de equipped the minimum required number of monitoring equipment and facilities to ensure continuous and reliable generation and collection of seismic data. Considering the number and distribution of active earthquakes generator in the Philippine, at least sixty strategically, distributed seismic station are needed to enable PHIVOLCS to effectively and accurately document the seism city of the country. In dong so seismic hazard and risk assessment could be better addressed. Proper land use planning with due consideration of the identified seismic hazard could be minimize if not totally eliminate disasters arising from earthquakes."]),    html.P(['See the Web site ', html.Br(), html.A(['Seismology on Philippines'], href="www.phivolcs.dost.gov.ph")])],
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

def thailand():
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

                
                html.Div([html.P(['Seismic Monitoring Network in Thailand'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(['Burin WECHBUNTHUNG'], style={"text-align":"center"}),
                html.P(), html.P(), html.B(['1. Introduction']),
                html.P(), html.P(['Generally in the past it has been believed that Thailand locates in low seismicity area, no earthquake effect to the people. Severe seismic intensity caused by major earthquake have never occurred inside Thai territory areas except one events in history was recording that describing the collapse of a town in the northern part by a big earthquake more than thousand years ago. By the time passed, many important events that panicked to people have been forgotten. However, in the past 3 decades several moderate earthquakes occurred more frequently and caused a great panic to the public with slight to moderate damages to the vulnerable development, create enormous construction with crowded community are expanded into seismic risk zones. Some locations of moderate earthquakes that have never harmed to people in the past record initially cause some damage to vulnerable construction.']),
                html.P(['Several agencies concerned establish their own seismic network or improve their instruments to monitor these phenomena on the purpose of obtaining the basic information of location, occurring time and magnitude which are necessary for Thai scientist and engineers to study the nature of earthquakes.']),
                html.P(['Looking back into the historic records of seismicity in neighboring countries such a Burma, China, Andaman Sea, earthquakes of magnitude greater than 7 Richter and some potentially seismic sources of long faults in the northern and western part, cause the worrying of dangerous situation that may be occur in the future to Thai scientist and engineers. To realized this problem, several efforts have been done in the past decades, installing analog seismic monitoring system, established National Earthquake committee of Thailand, extends seismic section in Meteorological Department to Division level i.e. Office of Seismology, cooperated with experts from China, USA, Japan etc. Thus, at present new digital seismic monitoring are installed in order to operate, analyze, determine, and compile seismic information automatically in real time or near real time. Moreover seismic activities for prevention and mitigation will be directly implemented by several agencies related.']),
                html.P(), html.P(), html.B(['2. Seismicity']),
                html.P(), html.P(), html.B(['2.1 Seismic Source Zones']),
                html.P(['The most interested area for consideration is in the area of latitude 5-26 N and longitude 90-110 E which can be characterized into 12 seismic source zones A, B, C, D, E, F, G, H , I, J, K and L based on active fault zones and historical records as shown in Figure 1. Tables 1. Gives the zone names, number of events, and maximum magnitude in each zone.']),
                html.P(['From the seismicity map of the world, Thailand is located at the eastern part of the Alpine-Himalayan earthquake belt, where the Indo-Australian plate moves and pushes northeastward to Eurasian plate. The pressure from the movement of the plates is the main causes of earthquakes along the belt.']),
                html.P(['Basically fault system in Thailand can be grouped into 3 different categories (1) N-S normal fault (2) NW-SE strike slip fault (3) NE-SW strike slip fault. Shrestha(1) identified 9 active fault zones as shown in Figure 2 and some description are the following. ']),
                html.P(['1. Chaingrai Fault. This fault trends east-northeasterly and its approximately 130 km, long. The largest earthquake recorded along this fault is magnitude 4.9 Mb on September 1, 1978. Earthquake of smaller magnitude were frequent, three of these are above 4.5 Mb. The maximum focal depth is 10 km.']),
                html.P(['2. Mae Tha Fault. The arc shaped concave toward Chiangmai. It is about 100 km, long. The fault plane dips 50-55 degree toward northwest. A cluster of shallow depth small earthquake occurs in northwestern part of Mae Tha Fault.']),
                html.P(['3. Phrae Fault. This fault bounds the eastern rim of Phrae basin. Its length is about 115 km. During the past 10 years, more than 20 earthquakes of magnitude 3-4 occurred along this fault.']),
                html.P(['4. Thoen fault. This fault is roughly parallel to Pharae fault. Its length is about 100 km. A few earthquakes of low magnitude were recorded along the fault. The latest one was recorded on December 23, 1980 with magnitude 3.7.']),
                html.P(['5. Moei Uthai Thani fault. The northwestern trending Moei Utahi Thani Fault is one of the major fault systems in Thailand. The fault is about 250 km, long. Several splay faults were mapped branching off from this fault. An earthquake of magnitude 5.6 occurred on February 17, 1975. A focal plane solution shows a component of right lateral movement.']),
                html.P(['6. Sri Sawat Fault. This fault lies to the west of Moei Uthai Thani Fault with the most parallel trend. It occupies the Quae Yai and Mae Klong River channels and extends northwesterly into Burma. The total is more than 500 km. Several earthquakes were reported along this fault, the largest of which occurred on April 22, 1983 with magnitude 5.9 on Richter scale. All earthquakes are of shallow depths. Ground crack and landslides were reported in the epicenter area. The focal plane solution of the April 22, 1983 earthquakes shows a right lateral strike slip along this fault.']),
                html.P(['7. Three Pagoda Fault. This fault lies in the channel of Quae Noi River; its northwestern extension joins the Sagiang Fault of Burma. Its length in Thai portion is more than 250 km. Two large earthquakes of magnitude 7.6 and 5.8 occurred along this fault on January 7, 1937 and January 11, 1960. Several hundreds of small earthquakes have been registered since 1984.']),
                html.P(['8. Ranong Fault. The ranong fault lies in the channel of Kra Buri River; its total length is about 270 km. One earthquake of magnitude 5.6 occurred along this fault on September 30, 1978.']),
                html.P(['9. Klong Marui Fault. This fault cut across the Phangnga Bay and the Ban Don Bay. It is about 150 km, long. A few earthquakes were recorded in Phangnga Province and south of Phuket Province.']),
                html.P(), html.P(), html.B(['2.2 Historical Earthquakes']),
                html.P(['Historical earthquakes were scattering along the seismic source zone of faulting system. There were 2 kinds of earthquakes that effected to people in Thai territory. Firstly, earthquakes locate outside country in neighboring areas such as Burma, China, Laos, Vietnam, and Andaman Sea. Secondly, earthquakes locate inside country nearby active faults mainly in northern and western part. Most of historical earthquake records in Thailand and adjacent area were mainly compiled from 624 B.C. to 1989 by Nutalaya and Prachaub (SEASEE project). These seismic data reports contain two catalogs. First are the historical data compiled from historical text, annual, stone inscription and astrological documents. Second is the instrumental data recorded from 1900-present compiled from various sources such as USGS, ISC and Meteorological Department. The seismicity map of Thailand and adjacent area from 624 B.C. and 1983-1989 are shown in Figure 3 and Figure 4 respectively. Normally minor to moderate earthquakes could be found in northern part and western part, but in southern, northeastern, eastern part are rare.']),
                html.P(), html.P(), html.B(['2.3 Recent Seismicity']),
                html.P(['After the first installing of Chiangmai station in the year 1963, epicenter information is continuously compiled by Office of Seismology, coincident with establishment of new analog seismic monitoring instrument and then existing analog network extended until 1995. The firs exciting earthquake was on February 17, 1975 of magnitude 5.6 in northwestern Thailand. This event frightened people almost thought country. The second was earthquake occurring along Sri-Sawat Fault zone on 22 April 1983, are believed that caused by the reservoir induced seismicity, causing the maximum magnitude of 5.9 ever recorded by Meteorological Department seismographs. The wide spread panic ran throughout country and slight damages to the vulnerable buildings including created long ground crack on surface and landslides near epicenter vicinity. Other important event was an earthquake of magnitude 5.1 occurred at Pan District, Chiangrai Province northern Thailand on September 11, 1994 caused moderate damages to one of hospital building at Pan District 20-25 km. Away from epicenter, schools and temples nearby. The other two panic events were reported of earthquakes at Phrae Province on December 9, 1995 of magnitude 5.1 and earthquake at Chiangmai on December 21, 1995 of Magnitude 5.2. Both events caused slightly damages to Schools buildings and ancient pagodas as shown in Figure 5.']),
                html.P(), html.P(), html.B(['3. Seismic Network in Thailand']),
                html.P(['There are 3 agencies that operate and monitor the earthquakes, Thai Meteorological Department, Hydrographic Department and Electricity Generating Authority of Thailand. Each agencies has it own seismic network to meet their purposes, study the regional and local earthquakes, to study micro earthquakes nearby the dam site and under ground nuclear test detection']),
                html.P(), html.P(), html.B(["3.1 TMD's Seismic Monitoring Network"]),
                html.P(["TMD seismic monitoring network system composed of 3 kinds of seismic stations which are analog seismic stations, digital seismic stations and accelerograph stations, digital seismic stations and accelerograph stations."]),
                html.P(['3.1.1 Analog Seismic Stations']),
                html.P(['3.1.2 Digital Seismic Network']),
                html.P(['3.1.2.1 Instrument at each regional station :', html.Br(),
                '3.1.2.1.1 Short Period Seismometer, L-4-D (Mark Product) or broadband seismometer CMGT-40 T (Guralp Instrument), Accelerograph FBA 23', html.Br(),
                '3.1.2.1.2 GPS 11 A (Ref.Tek)', html.Br(),
                '3.1.2.1.3 Personal Computer Pentium 166 MHz.', html.Br(),
                '3.1.2.1.4 Data acquisition system 72A-08 ref tek 24 bit', html.Br(),
                '3.1.2.1.5 Backup system 72 A-05 Disk RefTek 1 GB, Charger and Batteries', html.Br(),
                '3.1.2.1.6 Stabilizers etc.']),
                html.P(['3.1.2.2 Instrument at center :', html.Br(),
                '3.1.2.2.1 2 sets of SUN SPARC Workstations', html.Br(),
                '3.1.2.2.1 2 sets of SUN SPARC Workstations', html.Br(),
                '3.1.2.2.3 5 microcomputers', html.Br(),
                '3.1.2.2.4 peripherals ie. Plotter, printer, scanner, UPS, Modems etc.', html.Br(),
                'The detail of instrument can be shown in Table 3.']),
                html.P(['3.1.2.3 Software utilized to process and analyze seismic information', html.Br(),
                '3.1.2.3.1 On line software from Suds utility software run in DOS mode', html.Br(),
                '3.1.2.3.1.1 Process.bat, merge.bat, pachub.bat, dialup server, command server, data server', html.Br(),
                '3.1.2.3.1.2 Locate.bat, hypo71PC, hypomap.', html.Br(),
                '3.1.2.3.2 Offline software about waveform analysis', html.Br(),
                '3.1.2.3.2.1 Format conversion software, suds utility for simulate seismogram recording in each day, filtering, multiple waveform plotting etc.', html.Br(),
                '3.1.2.3.3 Offline software for epicenter analysis and database', html.Br(),
                '3.1.2.3.3.1 Hypo71PC, Hypocenter 3.2, Seisan, Pitsa, Winquake 2.4, Focus, Focmec, datascope etc.', html.Br(),
                '3.1.3 Accelerograph station']),
                html.P(["In addition, about 16 strong motion accelrograph (SMA-1) were installed at the dam sites by EGAT and some are installed on highrise building in Bangkok under the National Earthquake Committee of Thailand's project which study about the site amplification and Dynamic response of structures in Bangkok area and western portion for studying the site response and seismic ground motion as shown in Table 4."]),
                html.P(), html.P(), html.B(["3.2 EGAT's seismic network "]),
                html.P(["There are 2 types of seismic stations installed under EGAT. First is permanent short period seismograph. Second is portable short period seismograph. Three small network are locate at northern part, western part at the Khao Laem & Srinagarin dam sites and Rachaprapa dam in the southern part. In addition network in western part has been modified to monitor automatically for the micro earthquakes nearby the dam site."]),
                html.P(), html.P(), html.B(["3.3 Hydrographic Department's Seismic Array network "]),
                html.P(["Seismic Array has been established in 1962 by US and Thai Government. First was operate by US Air force Detachment 415 since 1976 it transferred to Hydrographic Department. The center of array is located at Chiangmai with 18 short period sensors and 6 long period sensors were located in neighboring province around Chiangmai. Seismic data were transferred by Cable, radio link and Microwave as shown in Figure 11. This array now is one of station in Group of Scientific Expert (GSE) which is dealing with nuclear testing detection. The entire seismic monitoring in Thailand are shown in Figure 12."]),
                ], 
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

def singapore():
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

                
                html.Div([html.P(['Earthquake Monitoring System in Singapore'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Introduction']),
                html.P(), html.P(['In September 1996, the Meteorological Services Singapore (MMS) established a network of digital seismic for the monitoring of regional seismic station for monitoring of regional seismicity and to collect scientific data for the study of extend and intensity of tremors experienced in various parts of Singapore.']),
                html.P(), html.P(), html.B(['Overview of Earthquake Monitoring System']),
                html.P(['This system is built upon a network of digital station that are located at various remote sites in Singapore. At these stations, data acquisition and storage equipment is employed to digitally record and store seismic measurement. Using telemetry equipment and leased telephone lines, these digital recordings are transmitted on a near real-time mode to the central processing system at mms, change airport, for further processing and dissemination.']),
                html.P(), html.P(), html.B(['Seismic Sensor and Stations']),
                html.P(['The network of digital seismic station consists of five classical high gain three component seismograph stations, one of them being a VBB Global Seismographic Station (GSN) , and two strong motion down -hole stations. The down hole stations are established primarily for engineering seismology and earthquake engineering purposes. The equipment at these down hole packages which are installed at various depths below the ground. The seismometers and accelerometers convert vertical and horizontal ground motions into electrical signals that are proportional to velocities. This electrical signal are recorded as digital data by a computerized recorder.']),
                html.P(), html.P(), html.B(['Data telemetry']),
                html.P(['At each of the seismic stations, the computerized recorder digitize the earth motion signal and telemeter the recording in near real time to the cps via dedicated leased lines. In the event when the signal exceed predetermined threshold values, in addition to the continuous digital recordings, the recorder can also activate warning via dial up telephone line. A typical seismograph station is shown in figure 1.']),
                html.P(), html.P(), html.B(['Central Processing System']),
                html.P(['The CPS consist of a Central Recording System (CRS), a Seismic Data Analysis System (SDAS) and Warning System (WS). A photograph of the CPS is shown in figure 2.']),
                html.P(['The CRS receives the digital seismic recording from the seismic stations via leased and telephone lines. The SRS is also the file server. Raw and processed waveform and parametric files are stored on the file server where they are accessible by users.']),
                html.P(['The SDAS provides the software for the analysis of the seismic recordings. This software uses standard seismological tools. There are software features for the selection of wave arrivals to perform various analysis and the display of displacement spectra, perform attenuation analysis, earthquakes location, as well as the interactive analysis of seismic time series using fundamental display and processing operations and digital seismic processing. The SDAS is also able to perform real time data acquisition and has the facility to allow the exchange of data with the international seismological research community. The cps also comes with a WS that provides warning signals to interested parties via facsimile or electronic mail.']),
                html.P(), html.P(), html.B(['Role and Current Development Efforts ']),
                html.P(['With the establishment of earthquakes monitoring system. Mss is now able to perform the ole of monitoring regional seismic activities. The procedures for the detection and location of earthquakes events have been develop and implemented on an operational mode. For earthquakes that generate earth motions and affect the populace of Singapore , mms will furnish the relevant earthquakes information such as the location and magnitude of the earthquakes on a dial a phone system for access y the general public. This information is provided to assure and to help allay the fears of the public when they are affected by earth tremors that emanated from earthquakes. Figure 3 depicts the locations of earthquakes events, magnitude greater than 4.0 on Richter scale, that were detected by the system from September 1996 to December 1997. This system also enabled the provision of invaluable seismic data to the geotechnical, civil and structural engineers in the study of local ground motion characteristics. For the study of ground motion characteristics, mss has initiated joint research efforts with a number of civil and structural institutions and the tertiary institutions in Singapore . formal arrangement have also been made with the incorporated research institutions for seismology iris USGS for the exchange of seismic observations for research purposes.']),
                html.P(), html.P(), html.B(['Conclusion']),
                html.P(["Although Singapore is outside the major earthquakes zones and has no history of near-field earthquakes, with the establishment of its earthquakes monitoring network, mms hopes to contribute to the regional earthquakes monitoring programs in ASEAN. In view of the closely knitted socio-economic fabric amongst the ASEAN countries and the reality of devastating seismic risk in the region, it is beneficial for ASEAN members to develop collaborative seismic programs and activities. The current economic crisis serves as an additional impetus for the ASEAN members to exploit the synergies an the optimal utilization of scarce seismic know-how and resources in the region. Regional collaborative efforts in earthquakes monitoring will no doubt enhance the region's capability and ability to response in a timely manner to earthquakes disasters. In this regard, the ASNET RESED project is very relevant effort that will certainly contribute to the well being of the ASEAN region."]),
                html.P(['See the Web site ', html.Br(), html.A(['Seismology on Singapore'], href="app.nea.gov.sg/cms/htdocs/category_sub.asp?cid=53")])], 
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

def brunei():
    page = html.Div([dbc.Col([

        #####################
        #Row 1 : Header
        get_header(),
        
        #####################
        #Row 3
        get_emptyrow(),
        
        html.Div([ # External row

        navigation,


        ],
        className = 'row sticky-top'), # External row

        #####################
        #Row 5 : Footer
        get_footer(),
        ])
    ])

    return page

def vietnam():
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

                
                html.Div([html.P(['Seismic Activity and Seismological Network in Vietnam'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Seismic Activity']),
                html.P(), html.P(['In figure 1. shown the location of Vietnam in the regional tectonic setting. The collision of Indian and Eurasian plates deformed all the east Asian continent and divided it into the sub plates moving to the different directions mainly to the east and southeast. We can see in this figure the red river fault as one of the boundaries of these sub plates. Beside, Vietnam is situated between two greatest dynamic belt of the planet: the Mediterranean-Himalayan and pacific ones. It is suffering strongly the influence of these belts.']),
                html.P(['In figure 1. shown the location of Vietnam in the regional tectonic setting. The collision of Indian and Eurasian plates deformed all the east Asian continent and divided it into the sub plates moving to the different directions mainly to the east and southeast. We can see in this figure the red river fault as one of the boundaries of these sub plates. Beside, Vietnam is situated between two greatest dynamic belt of the planet: the Mediterranean-Himalayan and pacific ones. It is suffering strongly the influence of these belts.']),
                html.P(['The regions were divided into some units by the deep fault. Most of main faults in Vietnam are strike-slip fault. The NW-SE deep strike-slip fault system in the north is more active than the longitudinal or NE-SW fault system.']),
                html.P(['Relating to the tectonic characteristics. Vietnam is a country with moderate seismicity. The seismic hazard is not so height but it is also necessary to take care. The strong earthquake with magnitude ms>=5 from 1900 to 1995 are listed in the table 1 and epicenter of the earthquakes with magnitude Ms>4 in Vietnam of this period are shown in the epicenter map figure3. It is clear that Vietnam is not quiet in seismic activity and earthquakes must frequently occur in the north rather than in the south. The largest events are earthquakes of ms=6.7-6.8 occurred in the Northwest of Vietnam in Dienbien 11/1935 and Tuan Giao 24/6/1993. They caused destructions of building and construction in the area of thousand square kilometers. In the another regions, there were not an earthquake of magnitude larger than 5.5.']),
                html.P(), html.P(), html.B(['Seismological network']),
                html.P(['Digital instrument , from which data can be stored electronically and easily processed ., were replacing the older analog instruments where data are stored in the form of photographic image in papers.']),
                html.P(['At present, in Vietnam there are 14 seismic station . the fundamental parameters of the network are shown I the table 2. the figure 4 present the distribution of seismological network in Vietnam, the concentration of earthquakes in the north of Vietnam causes the most of stations are installed in it. There are 11 stations in the north and only 3 once I the south. Depending upon the seismic equipment Vietnam seismological network divided into 2 different observation system 1. telemetry seismic array 2. individual stations.']),
                html.P(), html.P(), html.B(['1. Telemetry Seismic Array']),
                html.P(['This array consist 6 stations being around Hanoi, Chua Tram Bavi (Ha Tay), Doan Hung (Tuyen Quang) Bac Giang, Tam Dao and Phu lien. The principle of work of telemetry seismic array shown in fig 5. the seismic signal from receiver will be amplified and converted to the digital signal and thought generator in the filed of frequency modulated FM transmitted to the recording centre for interpretation']),
                html.P(['The technical parameters of this array are presented as following: ']),
                html.Ul([html.Li(['Seismograph: Mark Product model l-4c , Eignfrequency :1 Hz, 3 components (2 station,), 1 vertical component (4 station)']), html.Li(['Transmission frequency 475 MHz']), html.Li(['Sampling rate 75 sps ']), html.Li(['Acquisition equipment geotras-95 made in France with 1 set of IBM pc 586 ( hard driver:850 mb)'])]),
                html.P(["Software ACQUI (Strasbourg institute of geophysics permit to store continuously seismic signal on hard drive automatically. The seismic event will be analyzed for locating earthquakes epicenter by using the program written by Vietnamese seismologist. Figure 6 shown seismic traces recorded by the telemetry seismic array and result of the analysis. It's earthquakes occurred in Muong Luan. 35 km in the east-east south east to the Dienbien at 18h39 gmt June, 30 1996 with magnitude 5.0"]),
                html.P(), html.P(), html.B(['2. Individual Stations ']),
                html.P(["The rest 8 station work in individual regime. In figure 4 shown the principle of work of this system. The principle of work of these stations is used digital technology , storing continuously seismic signals on hard drive and to extract seismic event on floppy disk automatically."]), 
                html.P(["The technical parameter of individual stations are presented as following: "]),
                html.Ul([html.Li(['Seismograph Len arts electronic, model le-3d Eignfrequency 1 Hz, 3 component']), html.Li(['Sampling rae:75 sps']), html.Li(['Acquisition equipment Geostras -95 made in France with 1 set of IBM pc 586 (hard driver 850 mb)'])]),
                html.P(["The result of observation will be transmitted to the data processing center in Hanoi by two ways:1 quick transmission by telephone line using modem when occurred strong events and 2 sending by post the stored floppy disks every month. The software used for acquisition and interpretation is the same one which used for telemetry array. In figure 7 shown seismic traces recorded by one station of individual system. Finally , the Vietnam seismological network is monitoring all the seismic event of magnitude larger than 3.0 in the territory of Vietnam. And also the storing of seismic signal by digital instrument will give us a change to promote seismological observation in Vietnam and to exchange the seismic data with another countries easily and quickly , so that our participation into ASNET -RESED projects is real necessary. "])], 
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

def laos():
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

                
                html.Div([html.P(['Seismology on LAO P.D.R.'], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Introduction']),
                html.P(), html.P(["The Lao People's Democratic Republic is a landlocked country situated in the center of the indochinese peninsula with population of 4.6 million sharing border with China, Vietnam, Myanmar, Thailand, and Cambodia. The countries covers an of 236.800 km2. Elevation ranges from 81 m amsl in the Mekong river on the southern border with Cambodia to 2.819 m in the mountain Phoubia situated 130 km NNE of Vientiane, capital city. In the high ground of northern LAO and toward the SE along the Annamite mountain ridge whose watershed defines the Lao P.D.R.-Vietnam border many summit reach elevation between 1.200 m and 2000 m. The Mekong river which defines much of the western border of LAO, flows southwards from elevation of just under 600 m amsl on the border with Myanmar to less thane 100 m a further 1970 km downstream at the border with Cambodia. Most of the remaining major river within the country flow Westward or Southwards into the Mekong rivers."]),
                html.P(['The climate of the Lao is tropical. The general circulation over the region is dominated by two monsoons: the north-east and the south- west. The northeast affects from November to mid march, when atmospheric pressure are high. It is a dry period with low humidity and temperature. The southwest monsoon affects from mid may to mid October, short dry spell of about 2 week is normally experienced from cyclonic disturbance which are classified as depression, tropical storms or Typhoons.']),
                html.P(), html.P(), html.B(['Situation of earthquake disaster']),
                html.P(['Lao P.D.R. is lightly affected from the impacts of earthquakes. Even the epicenter is far, it can be felt throughout the country especially in the northern provinces but the magnitude is may be not high. So the damage to building or human life is nor severe.']),
                html.P(['Lao P.D.R. has not yet his seismological stations for earthquakes to prevention and monitoring system. In the past , no institution was responsible for this matter so in 1997 this responsibility of the seismological observation and monitoring was mentioned in the new role and function of the department of meteorology and hydrology. In this field until now, there is no station, no observation , no data and technicians or scientist on the seismology.']) ,
                html.P(['In the further , one or two station should be installed in particular in northern past of Lao also the seismological training should be done and the international and regional cooperation should be set up.']) ], 
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

def myanmar():
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

                
                html.Div([html.P(['Seismological Monitoring System Of Myanmar '], style={"font-weight":"bold", "text-align":"center"}),
                html.P(), html.P(), html.B(['Myanmar']),
                html.P(), html.P(["Myanmar covers an area of 678,528 km2. The country lies between about 10oN and 28o30 'N and 92o 30'E and 101o 30' E. The greatest north-south extent is about 2,200 km and the greatest east-west extent about 950 km. In the 800 km long part of southern Myanmar, the Taninthayi area, the east west extent is only 50 to 150 km. "]),
                html.P(["In the west, the Union of Myanmar is bordered by Bangladesh, in the north-west by India, in the north and north-east by the Peoples' Republic of China, in the east by Laos and in the south east by Thailand. The total length of the country's border is 4,000 km. The central and southern part of the country is bounded in the west by the 2,100 km long Rakhine and Taninthayi coastline of the Bay of Bengal and the Andaman Sea."]),
                html.P(["Myanmar is the homeland of the great number of different ethnic and linguistic groups. The Union of Myanmar includes 7 federal states, namely Kayin, Mon, Kayah, Rakhine, Chin, Shan and Kachin, and 7 divisions, namely Yangon, bago, Mandalay, Sagaing, Ayeyarwady, Taninthayi, and Magway. The locations of the state and divisions are shown in Figure 1."]),
                html.P(), html.P(), html.B(['Geological Aspect']),
                html.P(["Myanmar is part of the extra-peninsular region, which also comprises the young fold mountains of the Himalayan and hill ranges of Afghanistan and Baluchistan in the west. All this area forms part of a weak and flexible zone of the earth's crust which has not yet attains its final state of equilibrium. That those folding movements have not yet ceased is proved by the frequent occurrence of earthquakes. Indeed, minor quakes are felt not infrequently in Yangon, the capital city of Myanmar. These may be associated with the most continuous folding of the ridge on the southern end of which stand the Shwedagon pagoda, golden gigantic religious edifice of Buddhism."]),
                html.P(["Volcanoes tend to act as safety values and to relieve the strain and pressure; it is to be noted that a number of extinct volcanoes, Mount Popa which situates in the central part of the country is the tourist's attraction for its scenic beauty and a panoramic view of the surrounding countryside."]),
                html.P(), html.P(), html.B(['Seismicity']),
                html.P(['As Myanmar is situated on the boundary of Alpide-Himalayan Earthquake belt where devastating earthquakes had occurred from time to time, there is obviously the seismic risk in and near the country. The earthquakes in this Alpide-Himalayan region have resulted in massive loss of life and untold suffering. The Alpide-Himalayan zone, extending from the Mediterranean Sea to the Andaman Sea, is characterized by a widely diffused continental region encompassing young mountain ranges. These mountains owe their existence to large compressive forces resulting from collision of Indian plate and Eurasia Plate and are mostly associated with shallow earthquakes.']),
                html.P(['A geological collision between Indian sub continental plate and the rest of Eurasia Continental plate on which Myanmar stands and the collision is still in progress. The world highest mountains, Himalayas rise abruptly from the flat, densely populate Ganges Plain in the northern India and shield the Tibatan plateau from the seasonally shifting monsoon winds of southern Asia. ']),
                html.P(['As an example of its currents effects of collision, we believed the great earthquake that occurred in the region was the result of forces originated in the collision area. Even in Myanmar, the moderate seismically active country, the Bago earthquake of 5 May 1980 caused the loss of about 500 lives at Bago and 50 lives at Yangon with major destruction at Bago and some destruction at Yangon. The Sagaing earthquake of 16 July 1956 caused damages to religious edifices and buildings at Sagaing and about 40 lives were lost. The Pagan earthquake of 8 July 1975 caused destruction too many historical monuments at Pagan Pagan earthquake of July 1975 caused destruction to many historical monuments at Pagan and 2 lives were lost. It was really the untold religious heritage losses to its people. The Tagaung earthquake of 5 January 1991 caused moderate destruction to the surrounding area. A list of some of the strong earthquakes that occurred in Myanmar is given in Table 1.']),
                html.P(), html.P(), html.B(['Structural Feature']),
                html.P(['Due to the collision of the continental and oceanic plates, the country falls naturally into the following four divisions, each of which runs from north to south, through the length of the land.']),
                html.Ol([html.Li(['The Shan Plateau in the east. ']), html.Li(['The central belt of Myanmar, covering roughly the basins of the lower Ayeyerwady and its tributary, the Chindwinn, and the basin of the Sittoung River.']), html.Li(['The central belt of Myanmar, covering roughly the basins of the lower Ayeyerwady and its tributary, the Chindwinn, and the basin of the Sittoung River. ']), html.Li(['The narrow coastal strip of Rakhine.'])]),
                
                html.Table([
                    html.Tr([html.Td(['No']), html.Td(['Date']), html.Td(['Latitude']), html.Td(['Longitude']), html.Td(['Magnitude']), html.Td(['Remarks'])]), 
                    html.Tr([html.Td(['1']), html.Td(['23-05-1912']), html.Td(['21.00']), html.Td(['97.00']), html.Td(['8.0']), html.Td(['North of Taunggyi serious landslide'])]), 
                    html.Tr([html.Td(['2']), html.Td(['06-03-1913']), html.Td(['17.00']), html.Td(['96.50']), html.Td(['7.0']), html.Td(['"Hti" of Shwe-maw-daw Pagoda grounded'])]), 
                    html.Tr([html.Td(['3']), html.Td(['05-07-1917']), html.Td(['17.00']), html.Td(['96.50']), html.Td(['7.0']), html.Td(['"Hti" of Shwe-maw-daw Pagoda grounded'])]), 
                    html.Tr([html.Td(['4']), html.Td(['19-01-1929']), html.Td(['25.90']), html.Td(['98.50']), html.Td(['7.0']), html.Td(['Brick buildings destroyed at Htaw-Gaw'])]), 
                    html.Tr([html.Td(['5']), html.Td(['08-08-1929']), html.Td(['19.25']), html.Td(['96.25']), html.Td(['7.0']), html.Td(['Railway lines destroyed at Swa'])]), 
                    html.Tr([html.Td(['6']), html.Td(['16-12-1929']), html.Td(['25.90']), html.Td(['98.50']), html.Td(['7.0']), html.Td(['Landslides'])]), 
                    html.Tr([html.Td(['7']), html.Td(['05-05-1930']), html.Td(['17.00']), html.Td(['96.50']), html.Td(['7.3']), html.Td(['Many houses destroyed, 500 killed in Bago. Some houses deftoryed, 50 killed in Yangon.'])]), 
                    html.Tr([html.Td(['8']), html.Td(['03-12-1930']), html.Td(['18.00']), html.Td(['96.50']), html.Td(['7.3']), html.Td(['Some houses destroyed, about 30 killed'])]), 
                    html.Tr([html.Td(['9']), html.Td(['27-01-1931']), html.Td(['25.60']), html.Td(['96.80']), html.Td(['7.3']), html.Td(['Brick buildings collapse, landslide'])]), 
                    html.Tr([html.Td(['10']), html.Td(['12-09-1946']), html.Td(['23.50']), html.Td(['96.00']), html.Td(['7.5']), html.Td(['Pagoda collapse'])]), 
                    html.Tr([html.Td(['11']), html.Td(['15-08-1950']), html.Td(['28.50']), html.Td(['96.50']), html.Td(['8.6']), html.Td(['Under the influence of Assam earthquake, Chindwinn river at Mawlaik and Kalewa, Ayeyarwady at Aunglan flow upstream.'])]), 
                    html.Tr([html.Td(['12']), html.Td(['16-07-1956']), html.Td(['22.00']), html.Td(['96.00']), html.Td(['7.0']), html.Td(['Pagodas & Buildings at Sagaing destroyed, about 40 killed. Sagaing bridge moved slighty.'])]), 
                    html.Tr([html.Td(['13']), html.Td(['08-07-1975']), html.Td(['21.50']), html.Td(['94.70']), html.Td(['6.8']), html.Td(['Many historical pagodas destroyed, 2 killed'])]),
                    html.Tr([html.Td(['14']), html.Td(['05-01-1991']), html.Td(['23.48']), html.Td(['95.98']), html.Td(['7.1']), html.Td(['Landslide & some buildings destroyed at tagaung and surrounding area 2 killed.'])])
                ]),
                
                html.P(), html.P(), html.B(['DMH']),
                html.P(['The Department of Meteorology and Hydrology (DMH) is a state organization under the Ministry of Communications, Post and Telegraph of the Government of the Union of Myanmar responsible for undertaking measurements, data management, computations, studies and provisions of services on all aspects of meteorology, hydrology, seismology and agro meteorology to meet the requirements of the nation and its people.']),
                html.P(), html.P(), html.B(['Seismological Division ']),
                html.P(['A full-fledge seismological division was establish in 1986 under the control and management of the Department of Meteorology and Hydrology in accordance with the UNESCO / UNDP Regional project RAS/79/116: Regional Seismological Network of Himalayan Range which unfortunately failed to come up to its implementation stage. Nowadays, the department has four seismological stations and the seismological division is manned by twenty-five staff including three officered. The recording of earthquakes, analysis, processing and compilation of seismic data were systematically carried by the division. Seismicity of different regions in the country have also been studied and prepared. All major construction groups in the country had now sought for earthquake information at their construction sites for the purposes of taking earthquake resistant measures. Seismic data for that purposes are also provided and supplied by the department. ']),
                html.P(), html.P(), html.B(['Network']),
                html.P(['The threat of earthquake in Myanmar ha been long recognized by the government and its people and efforts, therefore, were being made to establish a seismological network to deal with all works pertaining to seismicity ever since the early sixties. Earthquake recording was undertaken at Yangon as early as 1962 and at Mandalay in 1966, using only then the electromagnetic seismographs with photographic recordings. ']),
                html.P(['In September 1970, a moderate earthquake with its epicenter near Yangon, there were many buildings suffered cracks and minor damage. A team of Japanese seismological experts was invited by the government to find out what could be done with the threat of earthquakes in Myanmar. The team, in addition to its recommendation for seismic resistant measures in construction and the formulation of earthquake resistant regulations, also recommended the seismological network consisting of 8 stations to provide a full coverage of earthquakes in and near Myanmar, whenever only earthquakes of 5.0 and above on Richter scale occurred. Those stations should be located at Yangon, Mandalay, Sittway, Dawei, Myitkyina, Kalemyo, Magway and Taunggyi. ']),
                html.P(['Another moderate earthquake jolted central Myanmar in 1975 with its epicenter near Pagan - Nyaung Oo and produced slight to moderate damages to many religious edifices and brick buildings. This Pagan earthquake had awakened the country to the fact that earthquake threat to the country is very dangerous to its people and properties. In 1976, two sets of Japanese visual velocity type seismograph were purchased and each set was installed at Yangon and Mandalay in 1977. In 1984, two sets of solar powered visual velocity type seismograph were obtained through the assistance was installed at Sittway in 1984 and another was installed at Dawei in 1985. ']),
                html.P(['A digitized seismograph, manufactured in USA was obtained though the assistance of the regional UNESCO office in New Delhi, India in 1995. The relevant software and training on interpretation of seismic are being request to the UNESCO. ']),
                html.P(), html.P(), html.B(['Monitoring']),
                html.P(['There are only four seismological stations for monitoring earthquakes in and near the country. Out of four stations, three stations at Mandalay, Dawei and Sittway are equipped with Japanese Katsujima short-period seismographs. Only in Yangon, capital city of Myanmar, one Japanese Katsujima short-period seismograph, one Japanese Katsujima long-period seismograph and one US K2 Digitized Seismograph, altogether three seismograph are installed. Locations of the existing and planned seismological stations are shown in Figure 2.']),
                html.P(['Whenever an earthquake occurred in the country, seismic data were collected from the out-stations simultaneously by using telephones, single side band (S.S.B) etc. Then the locations of epicenter with body wave magnitude and origin time was analyzed and determined at Yangon, main seismological office. After thoroughly analyzing the seismic data, earthquake information was disseminated to the people and the users through radio, television and news papers.']),
                html.P(['Since our network is not completed yet, in case of emergency to locate the epicenters of earthquake which had occurred in the country, we have to make, sometimes, request the neighboring ASEAN countries for the earthquake information by using fax.']),
                html.P(['Altough our Japanese analog seismographs are old and still in urgent need of calibration, repair and replacement, the seismological division is doing its best to run all the existing stations smoothly and to provide the country with seismological data for national projects and construction work.']),
                html.P(['As engineers require modern design technology and basic seismic information, preferably for long period, to construct earthquake resistant buildings and infrastructure, seismic zoning of the country for designing is necessary for safety and efficiency. For this purpose, the department provide the seismicity index map which will in some way serve as zoning map for earthquake risk. The seismicity index map is illustrated in Figure 3.']),
                html.P(), html.P(), html.B(['Conclusion']),
                html.P(['Myanmar tries its best to upgrade the monitoring system with the intention to lessen and mitigate the disastrous effects of earthquakes. It is envisaged that when the complete seismological network recommended by the Japanese seismological experts could be established and well-equipped with modernized instrument, disasters due to earthquakes in this part of the world could be thoroughly understood and more efficient steps be taken to combat against their disastrous effects.'])], 
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