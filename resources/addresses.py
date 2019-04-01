from flask_restful import Resource
from models.addresses import AddressModel


class Address(Resource):
    def get(self, address):
        address = AddressModel.find_by_address(address)
        if address:
            # return address.json()
            return {'asd': 'asd'}
        return {'message': 'Address not found'}, 404


class CountyAddressesList(Resource):
    def get(self, county):
        return {'county_addresses': list(map(lambda x: x.json(), AddressModel.query.all()))}
