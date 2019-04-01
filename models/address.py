from db import db


class AddressModel(db.Model):
    __tablename__ = 'addresses'
    id = db.Column('id', db.Integer, primary_key=True)
    county = db.Column('county', db.Unicode)
    address = db.Column('address', db.Unicode)
    longitude = db.Column('longitude', db.Float)
    latitude = db.Column('latitude', db.Float)


    def __init__(self, county, address, longitude, latitude):
        self.county = county
        self.address = address
        self.longitude = longitude
        self.latitude = latitude

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()