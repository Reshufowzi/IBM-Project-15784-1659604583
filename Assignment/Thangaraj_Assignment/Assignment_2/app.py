from flask import Flask,render_template,url_for

#app Instance
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html",title="Home")


@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.route("/register")
def register():
    return render_template("register.html",title="Register")

@app.route("/login")
def login():
    return render_template("login.html",title="Login")


#Main Method
if __name__=="__main__":
    app.run(debug=True)