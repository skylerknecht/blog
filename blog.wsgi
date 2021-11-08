import sys
sys.path.insert(0, '/var/www/html/rayke.dev/')

activate_this = '/home/skylerknecht/.local/share/virtualenvs/rayke.dev-8GFNc1XV/bin/activate_this.py'
with open(activate_this) as fd:
    exec(fd.read(), dict(__file__=activate_this))

from blog import app as application
