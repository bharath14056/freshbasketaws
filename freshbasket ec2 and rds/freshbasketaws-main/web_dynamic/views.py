# app/views.py (example)
from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html')  # This will look in the 'templates' folder
