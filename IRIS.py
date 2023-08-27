#http://localhost:5000/

from flask import Flask, g, render_template, jsonify, json
import psycopg2
from config import user, password, host, port, database 
import configparser

# Set up the app
app= Flask(__name__)

# Load configuration
app.config.from_mapping(
    DATABASE_HOST=host,
    DATABASE_PORT=port,
    DATABASE_NAME=database,
    DATABASE_USER=user,
    DATABASE_PASSWORD=password
)

# Reusable connection to PostgreSQL
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=app.config['DATABASE_HOST'],
            port=app.config['DATABASE_PORT'],
            database=app.config['DATABASE_NAME'],
            user=app.config['DATABASE_USER'],
            password=app.config['DATABASE_PASSWORD']
        )
        g.cursor = g.db.cursor()
    return g.db, g.cursor

@app.teardown_appcontext
def teardown_appcontext(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

## home - right now just displays state coords table 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/IrisTypes')
def IrisTypes():
    return render_template('IrisTypes.html')

@app.route('/Predictor')
def Predictor():
    return render_template('modelpredict.html')

@app.route('/Visuals')
def Visuals():
    return render_template('VisualsIris.html')

if __name__ == '__main__':
    app.run()