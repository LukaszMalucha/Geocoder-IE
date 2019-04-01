## App Utilities
import os
import env
from db import db
from flask_pymongo import PyMongo

from flask import Flask, render_template, request
from flask_restful import Api
from flask_bootstrap import Bootstrap

from models.addresses import AddressModel
from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.addresses import Address, CountyAddressesList
from resources.utils import sql_loader

## App Settings

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

mongo = PyMongo(app)
app.config['DEBUG'] = True
api = Api(app)

Bootstrap(app)
login_manager.init_app(app)

## Register Resources

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Address, '/api/address/<string:address>')
api.add_resource(CountyAddressesList, '/api/county/<string:county>')


## Main View
@app.route('/', methods=['GET', 'POST'])
def dashboard():
    ## Counties for the form
    counties = list(mongo.db.geocodes.distinct("county"))
    counties = sorted(counties)
    geo = None

    if request.method == 'POST':
        county = request.form['county']
        locality = request.form['locality']
        locality = locality.capitalize()
        locality = locality.strip()

        ## Find desired locality

        geo = mongo.db.geocodes.find_one({"$and": [{"county": county}, {"townland": locality}]})

        if not geo:
            warning = "Geocode not found"
            return render_template("dashboard.html", counties=counties, warning=warning, geo=geo)

    return render_template("dashboard.html", counties=counties, geo=geo)


@app.route('/addresses')
def addresses():
    """All the geocoded addresses"""

    address_list = AddressModel.query.limit(10000).all()

    return render_template("addresses.html", addresses=address_list)


@app.route('/api')
def api():
    return render_template("api.html")


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(debug=True)
