from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

#safe capitalize lower upper title trim striptags

def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong> text" #need to use safe for bold
    fav = ["cheese", "apple", 20]
    return render_template("index.html", 
                first_name = first_name,
                stuff=stuff,
                fav=fav)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500