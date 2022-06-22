import os
import sys
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pagetitle = 'Home')

@app.route('/blog/')
def blog(): 
    return render_template('blog.html', pagetitle = 'Blog')

@app.route('/aboutus/')
def aboutUs(): 
    return render_template('aboutUs.html', pagetitle = 'About Me')

@app.route('/contact-us/')
def contactUs(): 
    return render_template('contactPage.html')

@app.route('/hobbies/')
def hobbies(): 
    return render_template('hobbies.html', pagetitle = 'Hobbies')

