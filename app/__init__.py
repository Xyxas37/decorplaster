from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'popap13popap13'

from app import routes