#!/bin/python3
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Dragon Warrior',
        'title':'How you doing',
        'content':'First blog',
        'date_posted':'Feb 19, 2021'
    },
    {
        'author':'Axel Blaze',
        'title':'How you doing',
        'content':'Second blog',
        'date_posted':'Feb 20, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

if __name__=='__main__':
    app.run(debug=True)