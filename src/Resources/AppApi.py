'''
Created on Dec 3, 2015

@author: jharm
'''
from flask_restful import Resource
from AppLogic.Fixture import FixtureManager, Fixture, FixtureType

class ScheduleApi(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass
    
class PresetApi(Resource):
    def get(self, id):
       pass
    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass
    
class FixtureApi(Resource):
    
    def get(self, id):
        f = Fixture('IkeaLamp', 'downstairs', FixtureType.Light, 100)
        return {'fixtures' : f.ToDictionary() }
    
    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass