import sys
sys.path.insert(0, '/var/www/html/rayke.dev/')

activate_this = ''
with open(activate_this) as fd:
    exec(fd.read(), dict(__file__=activate_this))

from blog import app as application
