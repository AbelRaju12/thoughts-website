from flask import Flask, render_template, redirect, flash, url_for
from forms import loginform, registerform

app = Flask(__name__, template_folder='views') #__name__ name of the module, to specify a template folder other than 'templates
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = registerform()
    return render_template('register.html', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = loginform()
    return render_template('login.html', form = form)


if __name__ == "__main__":
    app.run(port = 3000, debug = "True")