from flask import render_template, url_for
from application import app

blogData = [
    {  
        "name": {"first":"John", "last":"Doe"},
        "title":"First Post",
        "content":"This is some blog data for Flask lectures"
    },
    {   
        "name": {"first":"Jane", "last":"Doe"},
        "title":"Second Post",
        "content":"This is even more blog data for Flask lectures"
    }
]




@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home', posts=blogData)

@app.route('/about')
def about():
    return render_template('about.html', title='About', desc='This is about blods')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')


