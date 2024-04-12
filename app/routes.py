
from flask import render_template, redirect, url_for
from app import app, db, bcrypt

## CODE MIGHT NEED THIS TO RUN
# app.app_context().push()

@app.route('/')
def layout():
    return render_template('layout.html')