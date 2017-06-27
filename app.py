from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

from models import *

@app.route("/", methods=['GET'])
def index():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def save():
    if request.form['name'] and request.form['color'] and request.form['pet']:
        pet = Pets(
            request.form['name'],
            request.form['color'],
            request.form['pet']
        )
        db.session.add(pet)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flash('Error before save data')
        finally:
            db.session.close()
    pets = pet.query.all()
    return render_template('form.html', data=pets)

if __name__ == '__main__':
    app.run()
