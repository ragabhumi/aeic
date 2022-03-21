# activate_this = '/home/seiscomp/radon-monitoring/venv/bin/activate_this.py'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

import sys

# add your project directory to the sys.path
project_home = u'/home/sysop/Downloads/aeic'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# need to pass the flask app as "application" for WSGI to work
# for a dash app, that is at app.server
# see https://plot.ly/dash/deployment
from app import app
application = app.server
