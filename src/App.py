'''
Created on Dec 2, 2015

@author: Josh Harmon

Flask inspiration and help:
https://github.com/miguelgrinberg/REST-tutorial/
'''
# packages
from flask import Flask, jsonify, make_response
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

# local
from Resources.BaseApi import Ping, Auth
from Resources.AppApi import ScheduleApi, PresetApi, FixtureApi
from DB import Database

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
auth = HTTPBasicAuth()
db = Database()

db.OpenDb()
#db.GenerateDb()

## URL Routes
# Add resources 
api.add_resource(Ping, '/' )
api.add_resource(Auth, '/auth')
api.add_resource(ScheduleApi, '/schedules/<int:id>')
api.add_resource(PresetApi, '/presets/<int:id>')
api.add_resource(FixtureApi, '/fixtures/<int:id>')



if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True) # set debug to false eventually