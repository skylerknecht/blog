from flask import Flask, render_template, url_for
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

list_of_blogs = [
{ 'title': '> Kerberos within Active Directory','file_name':'kerberoswithinactivedirectory.html'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/blogs/")
def blogs():
    return render_template('blogs.html',list_of_blogs=list_of_blogs)

@app.route("/blog/<string:file_name>")
def blog(file_name):
    return render_template(f'/blogs/{file_name}')

@app.route("/about")
def about():
    return render_template('about.html')

@app.errorhandler(HTTPException)
def handle_excpetion(e):
    return render_template('home.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0')
