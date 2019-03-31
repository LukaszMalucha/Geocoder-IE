import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy



################################################################## APP SETTINGS ########################################################


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") 
Bootstrap(app)


### Mongo DB

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") 
mongo = PyMongo(app)

### SQLite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///addresses.db'
db = SQLAlchemy(app)


##################################################################### SQLITE DB ###################################################

## For uploading geocoded addresses to sqlite db
class Addresses(db.Model):
    __tablename__ = 'addresses'
    id = db.Column('id', db.Integer, primary_key=True)
    county = db.Column('county', db.Unicode)
    address = db.Column('address', db.Unicode)
    longitude = db.Column('longitude', db.Float)
    latitude = db.Column('latitude', db.Float)
    


################################################################# VIEWS #######################################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/geocoder', methods=['GET', 'POST'])
def geocoder():

    ## Counties for the form
    counties = list(mongo.db.geocodes.distinct("county"))
    counties = sorted(counties)
    
    geo = ""
    warning = ""
    
    
    if request.method == 'POST':
        county = request.form['county']
        locality = request.form['locality']
        locality = locality.capitalize()
        locality = locality.strip()

        ## Find desired locality
        
        geo = mongo.db.geocodes.find_one({"$and": [{"county": county},  {"townland": locality }]})
        
        if not geo:
            warning = "Geocode not found"
        
        
        return render_template("geocoder.html" , geo = geo, counties = counties, warning = warning)
    
    return render_template("geocoder.html", counties = counties, geo = geo)
    
    

@app.route('/addresses')    
def addresses():
    
    ## All the geocoded addresses
    
    addresses = Addresses.query.all()
    
    
    return render_template("addresses.html", addresses=addresses)
    
    

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500    
    
    
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port, debug=False)
    app.run()
