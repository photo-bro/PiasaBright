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

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
auth = HTTPBasicAuth()


## URL Routes
# Add resources 
api.add_resource(Ping, '/' )
api.add_resource(Auth, '/auth')
api.add_resource(ScheduleApi, '/schedules/<int:id>')
api.add_resource(PresetApi, '/presets/<int:id>')
api.add_resource(FixtureApi, '/fixtures/<int:id>')

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True) # set debug to false eventually