from flask import Flask, render_template, url_for
app = Flask(__name__)

list_of_blogs = [
{ 'title': '> The First One','file_name':'thefirstone.html'}
]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/blogs/")
def blogs():
    return render_template('blogs.html',list_of_blogs=list_of_blogs)

@app.route("/blog/<string:file_name>")
def blog(file_name):
    return render_template(file_name)

@app.route("/about")
def about():
    return "Nope"

if __name__ == '__main__':
    app.run(host='0.0.0.0') 
