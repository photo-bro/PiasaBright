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
    
    def __init__(self):
        self.FixManager = FixtureManager()
        
    def get(self, id):
        fixtures = self.FixManager.GetFixtures()
        s = {}
        for f in fixtures:
            s.append(f.ToDictionary())
        return {'fixtures' : s }
    
    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass