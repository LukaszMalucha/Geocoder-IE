from flask_restful import Resource
from models.addresses import AddressModel


class Address(Resource):
    def get(self, address):
        address = str.capitalize(address)
        match_addresses = AddressModel.find_by_address(address)
        addresses = list(map(lambda x: x.json(), match_addresses))
        if len(addresses):
            return {'address': addresses}
        else:
            return {'message': 'Address not found'}, 404


class CountyAddressesList(Resource):
    def get(self, county):
        return {'county_addresses': list(map(lambda x: x.json(), AddressModel.find_by_county(county)))}
