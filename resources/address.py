from flask import session, Response, render_template, request
from flask_restful import Resource
from app import mongo



class Address(Resource):

    def get(self):

        ## Counties for the form
        counties = list(mongo.db.geocodes.distinct("county"))
        counties = sorted(counties)

        geo = ""
        warning = ""

        return Response(render_template('dashboard.html'))


    def post(self):

        ## Counties for the form
        counties = list(mongo.db.geocodes.distinct("county"))
        counties = sorted(counties)

        geo = ""
        warning = ""

        county = request.form['county']
        locality = request.form['locality']
        locality = locality.capitalize()
        locality = locality.strip()

        ## Find desired locality

        geo = mongo.db.geocodes.find_one({"$and": [{"county": county}, {"townland": locality}]})

        if not geo:
            warning = "Geocode not found"

            return Response (render_template("dashboard.html", geo=geo, counties=counties, warning=warning))

        return Response (render_template("dashboard.html", counties=counties, geo=geo))